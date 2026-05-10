# Decision 0021: DevOps / Infrastructure Source Pack

Date: 2026-05-10

Status: Accepted

## Context

QA / Audit now defines how to match evidence to claims. The next source-pack
promotion needed to define how deployment, runtime, environment, observability,
rollback, and operational-risk evidence should be gathered without granting
live mutation authority.

## Decision

Promote DevOps / Infrastructure into
`practice-os/research/source-packs/agent-source-packs.v0.json`.

The role's source posture is:

- repo-local CI/CD files, deployment configs, environment docs, package scripts,
  logs, monitoring notes, release notes, and handoff receipts first;
- Software Architecture evidence for runtime boundaries and ownership;
- Software Engineering evidence for implementation scope and verification;
- QA / Audit evidence for go/no-go posture, missing evidence, manual gates, and
  residual risk;
- official platform, cloud, database, CI, hosting, security, identity, and IaC
  docs for current behavior;
- broad web search for source discovery only;
- human-gated approval before any deploy, live config, DNS, billing, database,
  secret, OAuth, CI/CD permission, or cloud mutation.

## Consequences

- Future agents can distinguish local, CI, preview, and production evidence.
- Deployment readiness can include rollback, observability, cost, quota, and
  maintenance instead of only build status.
- Live infrastructure authority remains gated.
- The source-pack chain now covers Architecture, Engineering, QA, and DevOps.

## Non-Goals

- No deploys.
- No cloud resource mutation.
- No DNS changes.
- No billing changes.
- No secret, token, key, OAuth, webhook, or integration mutation.
- No production database migration or data write.
- No production readiness claim.
- No public proof or client communication.
- No autonomous workflow promotion.

## Follow-Up

Decide whether the next source-pack move should be structured JSON schema
validation, a source-pack dashboard/freshness view, or another role pilot such
as Product Strategy, UX / Design, Web Experience, General Counsel, Compliance,
Data Architecture, or Controller.
