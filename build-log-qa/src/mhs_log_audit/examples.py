"""Representative raw-record examples per event type (Step 18).

Exported to event_examples.json so automated interpretations can always be
validated against the underlying JSON. Records are exported verbatim.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from .profiling import EventProfile
from .temporal import get_path

ACTION_FIELD_CANDIDATES = (
    "actionType", "questEventType", "dialogueEventType", "actionKey",
    "Soil Key Puzzle Status",
)


def _action_field(prof: EventProfile) -> Optional[str]:
    for name in ACTION_FIELD_CANDIDATES:
        if f"data.{name}" in prof.fields:
            return name
    return None


def build_examples(profiles: Dict[str, EventProfile]) -> dict:
    out = {}
    for et in sorted(profiles):
        p = profiles[et]
        entry: dict = {
            "record_count": p.count,
            "first_occurrence": p.records[0].raw,
            "last_occurrence": p.records[-1].raw,
        }
        # typical = a record with the most common data key-set
        if p.key_sets:
            common_keys = p.key_sets.most_common(1)[0][0]
            for r in p.records:
                if isinstance(r.data, dict) and tuple(
                        sorted(k if k != "" else "<empty>" for k in r.data)) == common_keys:
                    entry["typical_record"] = r.raw
                    break
            # rarest key-set variant, if different from the common one
            rare_keys = min(p.key_sets.items(), key=lambda kv: (kv[1], kv[0]))[0]
            if rare_keys != common_keys:
                for r in p.records:
                    if isinstance(r.data, dict) and tuple(
                            sorted(k if k != "" else "<empty>" for k in r.data)) == rare_keys:
                        entry["rare_schema_variant"] = r.raw
                        break
        # one example per action-like value
        action = _action_field(p)
        if action:
            by_action = {}
            for r in p.records:
                v = get_path(r.data, action)
                if isinstance(v, str) and v not in by_action and len(by_action) < 25:
                    by_action[v] = r.raw
            if by_action:
                entry["action_field"] = action
                entry["by_action_value"] = dict(sorted(by_action.items()))
        out[et] = entry
    return out
