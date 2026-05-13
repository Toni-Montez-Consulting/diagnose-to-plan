---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# CMS And Editor Tooling Decision Ladder

Status: planning lane only. This does not authorize implementing a CMS,
connecting accounts, inviting editors, changing DNS, migrating content, or
moving repo source of truth.

Owner repo: `diagnose-to-plan`

Primary trigger: a site, app, client project, or internal workspace needs
non-technical editing for public content, images, resources, updates, field
notes, or marketing pages.

## Why This Exists

The CCAAP Sanity work surfaced a reusable pattern: some projects need a real
editor experience, but not every repo needs the same kind of CMS, admin panel,
or visual page builder.

This ladder keeps future decisions intentional:

- Git stays best for developer-owned source, configuration, launch gates, and
  sensitive boundaries.
- Sanity fits public content editing where owners need a simple `/admin`
  surface for updates and photos.
- Supabase fits application data, auth, private records, operational state, and
  workflows.
- Payload, Directus, Strapi, or custom admin surfaces fit app-like data models
  when the CMS is really becoming product infrastructure.
- Tina or Decap can fit Git-backed editorial workflows when the repo should
  remain the content store but non-technical editors need a lighter editing
  surface.
- Builder.io, Webflow, Framer, or similar visual tools fit marketing-page
  ownership only when layout editing is a real requirement and brand drift is
  acceptable.
- Contentful or Hygraph fit larger multichannel/editorial programs where
  enterprise workflow, localization, or content API governance is more
  important than speed.
- Notion fits capture, cockpit, and mirror workflows. It should not become the
  source of truth for private client records, proof gates, repo validation, or
  launch configuration.

## Planning Boundary

This lane is on the backburner until a repo has a repeated, specific editing
workflow. A future implementation still needs:

- a real owner/editor persona;
- content types that are stable enough to model;
- public/private data boundaries;
- hosting and environment-variable plan;
- role and approval model;
- cost or paid-tier decision;
- migration plan for existing content/assets;
- launch validation and rollback path;
- source-of-truth decision between Git, CMS, app database, and mirror tools.

Do not implement a CMS just because a tool is interesting.

## Decision Ladder

1. Use Git and static content when Toni or a developer is the editor, content
   changes are infrequent, or launch safety matters more than self-service.
2. Use Sanity when non-technical owners need structured public content editing,
   image uploads, previewable content, and a reasonable embedded Studio/admin
   experience.
3. Use Supabase when the data is application state, user/member/payment-related
   records, private submissions, auth, permissions, or workflow state.
4. Use Payload, Directus, Strapi, or a custom admin when the project needs a
   deeper product back office, relational data management, or custom workflow
   logic.
5. Use Tina or Decap when Git should remain the content source but editors need
   a simpler writing/media workflow and the repo can handle the authentication
   and editorial setup safely.
6. Use Builder.io, Webflow, Framer, or a similar visual builder only when the
   owner truly needs page-layout editing and the project can tolerate stricter
   brand/design governance.
7. Use Contentful, Hygraph, or similar headless enterprise CMS tools when the
   client has larger editorial teams, localization, multichannel content, or
   enterprise governance requirements.
8. Use Notion only as capture/mirror/cockpit unless a separate source-of-truth
   decision accepts it for the specific workflow.

## Workspace Fit

| Repo / lane | Fit | Planning decision |
|---|---|---|
| `ccaap-site` | strong Sanity pilot | V1 editor is updates/photos only; board, meetings, payments, contact, resources, and proof stay repo/approval managed for now |
| `consulting` | possible later | Consider CMS only for approved public-safe case studies, articles, resources, or proof cards after proof gates mature |
| `architected-strength` | possible later | Candidate for field notes, content hub, media, and public writing if the repo becomes actively published |
| `demario-pickleball-1` | possible narrow use | Public updates/photos/testimonials may fit later; bookings, payments, students, and admin records stay app/backend managed |
| `FamilyTrips` | optional/private only | Could help family posts/photos if desired; itinerary/private coordination should remain app data or private records |
| `fitness-app` / Omnexus | marketing-only | Product education/blog/landing content could fit later; app state, subscriptions, training data, and user records stay outside CMS |
| `hub` | weak fit | Runtime records, prompts, runs, captures, and console state stay Hub/Supabase owned; CMS only for public docs/help if needed |
| `diagnose-to-plan` | no for core source of truth | DTP markdown/private hosted records remain canonical; a CMS could only publish a sanitized public mirror later |
| `dse-content` | blocked by default | Microsoft/COI/private-source boundaries make CMS reuse inappropriate unless separately selected and cleared |
| `tm-skills` | no implementation fit | Skills stay Git/version-controlled; a future skill can advise CMS decisions, but the repo should not use a CMS |
| `hub-prompts` / `hub-registry` | no implementation fit | Prompt/target registries stay validated Git artifacts unless a future runtime governance model is accepted |

## Tool Selection Scorecard

Score each candidate from 0 to 3 before choosing a tool.

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Owner editing need | developer-only | occasional owner request | recurring content editing | owner editing is launch-critical |
| Data boundary fit | unclear or sensitive | mixed public/private | mostly public with clear gates | public-only and well-modeled |
| Workflow fit | tool creates process | partial fit | supports current workflow | removes real repeated friction |
| Design control | likely brand drift | needs heavy guardrails | manageable templates | strong design system control |
| Hosting/build fit | unknown | manual setup | normal env/build setup | proven in current hosting path |
| Role/cost fit | unknown or expensive | paid tier likely | acceptable if approved | free/low-cost and role model fits |
| Migration burden | high | moderate | low | content already structured |
| Verification | unknown | manual smoke only | local plus preview smoke | repeatable launch validation |

Recommended decision labels:

- `git_static`
- `sanity_structured_public_content`
- `supabase_app_data`
- `custom_or_open_source_admin`
- `git_backed_editor`
- `visual_page_builder`
- `enterprise_headless_cms`
- `notion_mirror_only`
- `park`
- `blocked`

## Agent And Skill Routing

Use this ladder with:

- Tooling Steward for tool fit, cost, auth, data, and source-of-truth review.
- Software Architecture for data boundaries, schemas, hosting, and integration
  shape.
- Product Strategy for whether owner editing is actually part of the V1 value
  proposition.
- UX / Design for editor workflow, preview behavior, content-model usability,
  and visual brand drift.
- QA / Audit for publish gates, role boundaries, draft/review visibility,
  accessibility, and launch validation.
- DevOps / Infrastructure for environment variables, deployment previews,
  DNS, rollback, and auth/CORS setup.
- External Communications when owners need a plain-language ask explaining
  access, approvals, editor invites, and what is still blocked.
- `tm-skills/backend-design` when the decision touches persistence, auth,
  private data, API boundaries, or product back-office logic.
- A future `cms-editor-fit` skill only if this pattern repeats across at least
  two non-CCAAP projects and the triggers/evals can stay tool-agnostic.

## Backburner Skill Candidate

Do not create this skill now.

Candidate name: `cms-editor-fit`

Use only if repeated future sessions need a reusable skill for:

- choosing between Git, Sanity, Supabase, Payload, Directus, Strapi, Tina,
  Decap, Builder.io, Contentful, Hygraph, Webflow, Framer, Notion, or custom
  admin;
- defining public/private content boundaries;
- writing a CMS fit assessment;
- planning editor roles, review states, and publish gates;
- drafting owner handoff instructions for content updates.

Promotion gates:

- at least two real projects use this ladder;
- trigger examples and anti-triggers are clear;
- output eval covers tool choice, privacy boundary, source-of-truth decision,
  owner workflow, and no-implementation posture;
- DTP activation map and `tm-skills` readiness docs are updated;
- no tool-specific implementation instructions become default authority.

## Backburner Roadmap Items

- Add a reusable CMS/editor fit assessment template after CCAAP produces one
  more real editor handoff or another project has the same need.
- Compare Sanity, Payload, Directus, Strapi, Tina/Decap, Builder.io,
  Contentful, Hygraph, Webflow, Framer, and Notion with current docs before any
  client recommendation.
- Decide whether consulting should ever expose public-safe articles/resources
  through a CMS, or whether Git is still the right editorial control.
- Decide whether Architected Strength needs content publishing workflow beyond
  Git once the personal-brand lane is active.
- Turn the CCAAP `/admin` handoff into a generalized owner-editor handoff only
  after Leah/Tony use it and the review/publish gate proves workable.

## No-Touch Rules

- Do not store secrets, tokens, API keys, project IDs that should remain
  private, raw email/transcript text, payment/member/form records, or private
  client material in public repos.
- Do not move proof claims, board content, payment routing, contact routing,
  resources, meeting links, or DNS into an owner editor without an explicit
  source-of-truth decision.
- Do not invite client editors, change roles, enable paid tiers, or connect
  production domains without Toni's approval.
- Do not treat CMS draft content as public. Public rendering must filter for
  the accepted review/publish state.
- Do not turn a CMS decision into a CRM, member database, billing system, or
  private client portal by accident.
