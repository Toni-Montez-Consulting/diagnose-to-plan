---
data_class: P0
confidential: false
permission_level: internal_only
review_status: recorded
---

# Starter DMARC Receipt - 2026-05-06

Status: recorded.

## Scope

Record the approved Google Workspace email-auth follow-up for
`tonimontez.co`. This receipt is DNS/admin-state evidence only; it does not
include mailbox contents, Google Admin screenshots, account secrets, client
records, or private calendar data.

## Action

- Verified `google._domainkey.tonimontez.co` has a Google DKIM TXT record.
- Verified `_dmarc.tonimontez.co` did not have a TXT record before the change.
- Added starter DMARC through Vercel DNS:
  `_dmarc.tonimontez.co TXT "v=DMARC1; p=none; pct=100"`.
- Verified DNS resolution after the change.

## Receipt

| Check | Result |
|---|---|
| Domain DNS host | Vercel DNS |
| DKIM TXT | present at `google._domainkey.tonimontez.co` |
| DMARC TXT before change | not observed |
| DMARC TXT after change | `v=DMARC1; p=none; pct=100` |
| Mutation command | `vercel dns add tonimontez.co _dmarc TXT "v=DMARC1; p=none; pct=100"` |
| Verification command | `Resolve-DnsName -Type TXT _dmarc.tonimontez.co` |

## Boundary

- Keep DMARC at `p=none` until normal send/receive behavior and any reports are
  reviewed.
- Do not tighten to quarantine or reject without a separate business-admin
  review.
- Google Admin DKIM status remains a manual dashboard check if Toni wants the
  Admin-console state captured in addition to DNS state.

## Next Action

Leave the starter policy in monitoring mode. Revisit only after email behavior
looks normal and there is a reason to tighten the policy.
