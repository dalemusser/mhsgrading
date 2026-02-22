# Unit 1 Point 1 Grading

**Activity:** Getting Your Space Legs

**Trigger Event:** `DialogueNodeEvent:31:29`

---

## Grading Rule

Completion-only check. If the trigger event exists for the player, the point is green.

| Outcome | Condition |
|---------|-----------|
| **Green** | Trigger event exists |

> No yellow pathway exists for this point.

---

## Event Keys

| Role | Event Key |
|------|-----------|
| Trigger | `DialogueNodeEvent:31:29` |

---

## Reason Codes

> No reason codes — this point is always green when the trigger event exists.

---

## Analytics Script

```js
// Unit 1, Point 1 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:31:29"

const color = "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 1, Point 1 — Attempt-based standalone production script (latest attempt)
// Trigger eventKey: "DialogueNodeEvent:31:29"

const color = "green";
color;
```

> Because the rule has no evidence keys, attempt-based semantics don't change the outcome — the trigger existing is sufficient.
