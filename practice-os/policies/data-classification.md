---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Data Classification

| Class | Meaning | Examples | Reuse |
|---|---|---|---|
| P0 | Public | site copy, public repo notes, public screenshots | allowed |
| P1 | Redacted | anonymous case-study claims, pattern notes | allowed after review |
| P2 | Client-private | client context, internal workflow notes, screenshots | keep in `engagements/` |
| P3 | Sensitive regulated/confidential | health, legal, account-level financial, HR decisions | avoid in v1 |
| P4 | Prohibited | credentials, payment cards, Microsoft confidential info | never store |

Default for new engagement artifacts is P2. Default for reusable practice artifacts is P0 or P1.
