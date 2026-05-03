---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Diagram: Business Brain System Architecture

```mermaid
flowchart LR
  Storefront["consulting site\npublic storefront + /start + noindex /admin"]
  Hub["Hub\nprivate intake/runtime records"]
  DTP["DTP\nsource-of-truth Practice OS"]
  Brain["Business Brain\nskills + commands + agents + fixtures + comms"]
  Notion["Notion\nmobile mirror + inbox"]
  Client["Client context\noperating kit + handoff"]

  Storefront -->|"public intake"| Hub
  Storefront -->|"launcher/status only"| DTP
  Hub -->|"runtime summaries / approved exports"| DTP
  DTP --> Brain
  Brain -->|"repo-authored artifacts"| DTP
  DTP -->|"selected mirror items"| Notion
  Brain -->|"customized install pattern"| Client
  Client -->|"reviewed lessons only"| Brain
```

## Notes

- DTP is source of truth.
- Hub is runtime support.
- Notion is a mirror and phone inbox.
- Client installs do not become multi-tenant SaaS.
- Lessons flow back only after review and redaction.
