---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# No Secrets In Git

Never commit:

- API keys or OAuth tokens
- service-role keys
- private keys
- payment card data
- raw exported customer data
- `.env` files
- screenshots containing credentials

Use dashboard-managed environment variables or local ignored files. If a secret is found in Git, rotate it before continuing work.

## Private Engagement Vault

`engagements/` is ignored/private and may contain owner-provided context that is
not safe for public repo scans or public proof. The public repo secret scan
excludes that private vault path so private client artifacts do not leak into
tracked validation output.

Before promoting any engagement material into tracked docs, consulting proof,
templates, fixtures, or case studies:

- remove secrets and tokens,
- run the relevant redaction check,
- record permission and reviewer status,
- keep raw private source pointers out of public artifacts.
