---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Diagram: Operator Flow

```mermaid
flowchart LR
  A["Diagnose\nWhat is actually stuck?"]
  B["Plan\nWhat should happen first?"]
  C["Translate\nWhat does the operator need to understand?"]
  D["Build\nInstall the useful system"]
  E["Hand Off\nRunbook + walkthrough + safe-change rules"]
  F["Stay Close\nReview rhythm + lessons"]

  A --> B --> C --> D --> E --> F
  F -->|"lesson candidates"| B
```

## Notes

- Use the plain six-step method for operator-facing work.
- The shorter public phrase can be "Diagnose, Install, Operate" when simplicity
  matters.
- Handoff is not a final document; it is the proof that the system works.
