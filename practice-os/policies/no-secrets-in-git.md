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
