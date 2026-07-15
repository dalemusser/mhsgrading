"""
Shared test harness for the MHS dashboard grading scripts.

Each `mhs-unitX-pointY-grading.md` file contains a "Production Script
(Attempt-Based)" written in MongoDB/JS that decides the dashboard color
(green / yellow) for one progress point. This module provides a small,
faithful, in-memory re-implementation of the MongoDB query primitives those
scripts rely on, so each production script can be transcribed 1:1 into Python
and run against the captured gameplay log (`tests/05-01-26/*.json`).

Supported query semantics (matching how the production scripts use them):

  * equality on any top-level field (`game`, `playerId`, `eventKey`,
    `eventType`, ...) and dotted paths (`data.toolName`).
  * `{"$in": [...]}` membership on `eventKey`.
  * `_id` range comparisons `$lt`/`$lte`/`$gt`/`$gte`. Mongo ObjectIds are
    compared by their byte order, which for the 24-char lowercase hex strings
    in this dump is identical to lexicographic string comparison. ObjectId
    generation order also tracks insertion/wall-clock time, so this windowing
    matches production.
  * `timestamp` range comparisons `$gte`/`$lte` (ISO-8601 strings compare
    lexicographically in chronological order) and the no-op `$type: "string"`.
  * `sort` by `_id` or `timestamp`, ascending (1) or descending (-1).
  * `find_one`, `find`, `count_documents`.

The query/result shapes are deliberately Mongo-like so the JS production
scripts read almost verbatim in the per-point test files.
"""

import json
import os

GAME = "mhs"

# ObjectId("000000000000000000000000") used as an exclusive lower bound in the
# production scripts when there is no previous trigger.
OID_MIN = "0" * 24

# Default log dump shipped with the repo.
DEFAULT_LOG = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "05-01-26",
    "wenyi050126-1.stratalog.logdata.json",
)


def ObjectId(hex_str):  # noqa: N802 - mirror the Mongo helper name
    """Mirror of the Mongo `ObjectId(hex)` helper. Ids are stored as the raw
    24-char hex string, so the value is its own comparison key."""
    return hex_str


def _oid(doc):
    """Return the 24-char hex id for a doc, regardless of how `_id` is stored
    (raw string, {"$oid": ...}, or {"$id": ...})."""
    v = doc.get("_id")
    if isinstance(v, dict):
        return v.get("$oid") or v.get("$id") or ""
    return v if v is not None else ""


def _field(doc, field):
    """Resolve a field path, supporting `_id` and dotted paths like
    `data.toolName`."""
    if field == "_id":
        return _oid(doc)
    if "." in field:
        cur = doc
        for part in field.split("."):
            if isinstance(cur, dict):
                cur = cur.get(part)
            else:
                return None
        return cur
    return doc.get(field)


def _matches(doc, query):
    for field, cond in query.items():
        val = _field(doc, field)
        if isinstance(cond, dict):
            for op, opv in cond.items():
                if op == "$in":
                    if val not in opv:
                        return False
                elif op == "$nin":
                    if val in opv:
                        return False
                elif op == "$lt":
                    if val is None or not (val < opv):
                        return False
                elif op == "$lte":
                    if val is None or not (val <= opv):
                        return False
                elif op == "$gt":
                    if val is None or not (val > opv):
                        return False
                elif op == "$gte":
                    if val is None or not (val >= opv):
                        return False
                elif op == "$ne":
                    if val == opv:
                        return False
                elif op == "$exists":
                    if (val is not None) != bool(opv):
                        return False
                elif op == "$type":
                    # Only "string" appears in the scripts; treat as a guard
                    # that the field is a present string.
                    if opv == "string" and not isinstance(val, str):
                        return False
                else:
                    raise ValueError(f"Unsupported query operator: {op}")
        else:
            if val != cond:
                return False
    return True


def _sort_key(sort):
    if isinstance(sort, dict):
        return list(sort.items())
    return list(sort)


class Collection:
    """Minimal Mongo-collection stand-in over a list of log documents."""

    def __init__(self, docs):
        self.docs = docs

    def _filtered(self, query):
        return [d for d in self.docs if _matches(d, query)]

    def find(self, query, sort=None):
        res = self._filtered(query)
        if sort:
            for field, direction in reversed(_sort_key(sort)):
                res = sorted(
                    res,
                    key=lambda d, f=field: (_field(d, f) is None, _field(d, f) or ""),
                    reverse=(direction == -1),
                )
        return res

    def find_one(self, query, sort=None):
        res = self.find(query, sort)
        return res[0] if res else None

    def count_documents(self, query):
        return len(self._filtered(query))


def load_collection(path=None):
    """Load the log dump and return a Collection. `_id` is normalized to its
    hex string in place so comparisons are plain string comparisons."""
    if path is None:
        path = DEFAULT_LOG
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    docs = []
    for d in raw:
        d = dict(d)
        d["_id"] = _oid(d)
        docs.append(d)
    return Collection(docs)


def latest_trigger_window(coll, pid, trigger_key):
    """The attempt window shared by most production scripts:

        Start: previous `trigger_key` (exclusive)
        End:   latest   `trigger_key` (inclusive)

    Returns ``(window_start_id, window_end_id)`` suitable for an
    ``_id: {"$gt": start, "$lte": end}`` filter, or ``None`` when no trigger
    exists for the player (in which case the production scripts yield the
    no-trigger color, usually "yellow").
    """
    latest = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": trigger_key}, sort={"_id": -1}
    )
    if latest is None:
        return None
    prev = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": trigger_key,
            "_id": {"$lt": latest["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = prev["_id"] if prev else OID_MIN
    window_end_id = latest["_id"]
    return window_start_id, window_end_id


def player_ids(coll):
    """Distinct playerIds present in the dump (newest-first dumps still yield
    the full set)."""
    seen = []
    for d in coll.docs:
        pid = d.get("playerId")
        if pid and pid not in seen:
            seen.append(pid)
    return seen


def default_player_id(coll):
    ids = player_ids(coll)
    if len(ids) != 1:
        # The shipped dump is a single-player capture; if that ever changes the
        # caller should pass an explicit playerId.
        pass
    return ids[0] if ids else None
