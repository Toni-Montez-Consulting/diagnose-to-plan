---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Opportunity OS V0

Status: design spec, no live private relationship ledger yet

Owner method repo: `diagnose-to-plan`

Active relationship data: not started

## Thesis

Toni's consulting growth should be relationship-led, trust-led, and
capacity-aware.

The goal is not a generic CRM and not cold outbound machinery. The goal is a
lightweight operating system for noticing high-trust, high-leverage business
relationships over time, understanding what those operators may need, and
choosing the right follow-up without overcommitting.

Opportunity OS should help answer:

- Who do I know?
- Who knows whom?
- Which operators or businesses have real leverage?
- What business pain or system gap might exist?
- What is the timing/readiness?
- What is the trust path?
- What would be useful, not pushy?
- What should I avoid because of bandwidth, fit, COI, or low-quality demand?

## Why This Exists

The best early consulting opportunities are likely to come through warm
relationships:

- friends and referrals;
- CrossFit/community connections;
- business owners and operators;
- founders;
- professional service operators;
- local service and real estate operators;
- operators connected to larger ownership groups.

The value is not "AI tools" as a standalone pitch. The value is helping
operators identify leverage points, build practical systems, improve workflows,
use AI thoughtfully, and leave with assets they can actually run.

## Source-Of-Truth Split

The word "source of truth" needs a split by record type:

Storage boundary decision: `decisions/0010-opportunity-os-private-store-boundary.md`.

| Surface | Owns | Does Not Own |
|---|---|---|
| DTP | Opportunity OS method, data contract, scoring rules, approval gates, steward receipts | raw relationship database if it includes private personal details |
| consulting repo | public-safe methodology pointer and potential future launcher/admin surface | raw relationship records, private notes, source authority |
| Notion | sanitized cockpit and mobile capture mirror | final authority, private notes, sensitive relationship details |
| Future private store | durable relationship/opportunity records if/when justified | public proof, unmanaged automation |

Recommendation:

- Keep the methodology in DTP.
- Keep public-safe pointers in consulting.
- Use Notion as capture/mirror only.
- Do not store the real relationship ledger in the public/deploy-adjacent
  consulting repo.
- For V0, if real records are needed, start in an internal-only DTP/private
  ledger or ignored local file until a private store is selected.

## V0 Loop

```text
capture signal -> classify relationship -> score opportunity -> choose next touch
-> protect capacity -> review weekly -> mirror sanitized status
```

V0 should be manual.

Do not automate outreach, follow-up, or relationship scoring until the manual
system proves useful.

## Core Objects

### Person

- name;
- relationship path;
- contact channel;
- trust level;
- notes sensitivity;
- last touch;
- next touch;
- connected companies;
- connected people;
- off-limits notes.

### Company / Operator Context

- company name;
- industry;
- size/maturity;
- operator type;
- suspected pain points;
- existing systems;
- technology appetite;
- budget/readiness signal;
- possible fit lane.

### Opportunity

- title;
- source person;
- company/operator;
- opportunity type;
- problem hypothesis;
- likely offer lane;
- readiness;
- timing;
- value/leverage;
- risk;
- next action.

### Referral Path

- introducer;
- target person/company;
- relationship strength;
- appropriate ask;
- timing;
- sensitivity.

## Opportunity Types

Use simple tags:

- clarity / blueprint;
- website / public presence;
- app / product build;
- workflow / internal system;
- AI enablement;
- reporting / visibility;
- operational cleanup;
- launch readiness;
- proof / case-study candidate;
- future relationship only.

## Fit Scoring

Score lightly. This is advisory, not a boss.

| Factor | 1 | 3 | 5 |
|---|---|---|---|
| Trust path | cold or weak | warm but indirect | direct high-trust relationship |
| Business seriousness | unclear | operating but fuzzy | committed operator with real stakes |
| Leverage | low impact task | useful workflow | meaningful revenue, profit, time, or decision leverage |
| Budget/readiness | likely no budget | maybe | likely able and willing |
| Timing | too early/too busy | medium-term | timely and actionable |
| Fit with Toni | random task | adjacent | builder/advisor sweet spot |
| Capacity risk | high | manageable | low |
| COI/privacy risk | high | manageable | low |

Suggested decision:

- 32+ total: active nurture or Diagnostic Call candidate.
- 24-31: stay warm and learn more.
- 16-23: park with reminder.
- below 16: ignore or no active follow-up.

Do not let the score override judgment.

## Bad-Fit Filters

Avoid:

- cheap website requests;
- random automations with no business owner buy-in;
- chatbot-only requests for novelty;
- unclear or unserious business ideas;
- people who want free strategic labor indefinitely;
- work that creates COI concerns;
- work that needs production support Toni cannot responsibly own;
- relationships where outreach would feel extractive or forced.

## Capacity Guard

Every opportunity needs a capacity label:

- `now`: worth immediate attention;
- `soon`: worth a light touch within 30-60 days;
- `later`: stay warm;
- `parked`: do not pursue unless signal changes;
- `no_fit`: do not pursue.

Rule:

Do not accept a major new engagement unless one of these is true:

- current commitments are closed or stable;
- the work is small and bounded;
- the client is high-fit/high-leverage enough to justify reshuffling;
- the engagement starts with a paid Blueprint or clearly scoped diagnostic.

## Notion Mirror Fields

Safe mirror fields:

- opportunity name;
- company/operator category;
- relationship path summary;
- status;
- next touch;
- fit score band, not private score notes;
- sensitivity;
- DTP source path.

Do not mirror:

- raw private relationship notes;
- sensitive personal details;
- private finances;
- private introductions;
- COI-sensitive context;
- anything that would feel bad if screenshotted.

## Consulting Repo Boundary

The consulting repo can later expose:

- public-safe methodology language;
- internal admin launcher;
- sanitized offer lane references;
- a pointer to DTP's Opportunity OS method.

It should not hold the raw relationship ledger.

## Research Arm Relationship

Research Arm feeds external market intelligence.

Opportunity OS feeds business-development intelligence.

They meet when a research signal improves:

- a discovery question;
- a client explanation;
- an offer lane;
- an opportunity score factor;
- a relationship follow-up reason;
- a future content seed.

## First Manual Pilot

Do not enter all named relationships yet.

First pilot should create 3-5 sanitized test records using generic labels:

- established operator with app/system need;
- local services operator with workflow bottlenecks;
- professional services / marketing operator with internal systems need;
- real estate operator with pipeline/workflow opportunity;
- future relationship only.

After the schema feels right, decide where private records should live.

Private storage decision:

- use `decisions/0010-opportunity-os-private-store-boundary.md` before creating
  raw opportunity records, a CRM, a Notion source-of-truth database, Hub/Supabase
  tables, or a private relationship ledger;
- for now, keep DTP limited to method, sanitized records, mirror contracts, and
  steward receipts;
- private client truth belongs in the private `engagements` lane after an
  opportunity becomes an active engagement.

First sanitized pilot:

- `practice-os/opportunities/sanitized-test-records-2026-05-09.md`

Pilot readout:

- the schema helps separate relationship warmth from actual opportunity quality;
- capacity risk needs to stay visible before enthusiasm turns into scope;
- scores are useful only as advisory signal;
- real names should wait for an approved private storage boundary.

## Acceptance Criteria

V0 works if:

- Toni can see warm opportunities without feeling pulled into everything;
- follow-ups feel thoughtful rather than salesy;
- high-trust paths are visible;
- low-fit work is filtered earlier;
- capacity protection is built into the system;
- Notion can show safe reminders without holding raw private notes;
- future robust persistence has a clean data contract.

## Non-Goals

- No cold-outreach engine.
- No automated lead scoring.
- No automatic emails or follow-ups.
- No raw private relationship database in the public consulting repo.
- No Notion source-of-truth shift.
- No CRM SaaS decision yet.
- No public proof or named relationship use.
