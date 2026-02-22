# Unit 1 Point 2 Grading

**Activity:** Info and Intros

**Trigger Event:** `DialogueNodeEvent:30:98`

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
| Trigger | `DialogueNodeEvent:30:98` |

---

## Analytics Script

```js
// Unit 1, Point 2 — Analytics-matching script
// Trigger eventKey: "DialogueNodeEvent:30:98"

const color = "green";
color;
```

## Production Script (Attempt-Based)

```js
// Unit 1, Point 2 — Attempt-based standalone production script
// Trigger eventKey: "DialogueNodeEvent:30:98"

const color = "green";
color;
```

> Because there are no evidence keys, attempt-based semantics don't change the outcome — the trigger existing is sufficient.

---

## Reason Codes

> No reason codes — this point is always green when the trigger event exists.
