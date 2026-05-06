---
data_class: P0
confidential: false
permission_level: public_safe
review_status: approved_public_safe
---

# DeMario Launch-Feedback Social Proof Packet

Status: ready for Toni-selected public posting. Toni confirmed on 2026-05-06
that he is good to post about Mario's site and that the remaining Mario site
work has been finished.

## Proof Candidate

- Engagement/project: `demario-pickleball-1`
- Public-safe title: Live coaching site launch and booking handoff
- Claim: Toni helped move DeMario's pickleball coaching site toward a live,
  booking-ready operating surface with clearer venue routing, booking/payment
  handoff, admin workflow, and roadmap/tasks visibility.
- Audience: Toni's LinkedIn and Instagram channels.
- Reviewer: Toni has posting discretion; keep private admin/student/payment
  data out of assets unless separately redacted.

## Baseline

Before this candidate can become public proof, the baseline must be described
without private admin records or unsupported business impact claims.

Current internal baseline:

- The project needed a coaching site that did more than look polished.
- The launch path needed booking clarity, venue/platform routing, payment
  instructions, owner handoff, admin access, and a roadmap surface Mario could
  understand.
- Some proof signals are still private or owner-held, especially feedback,
  screenshots, booking/admin rows, and student/customer details.

## After-State

Current internal after-state:

- The site is live and positioned as a real coaching booking surface.
- The site includes public lesson, venue, payment, terms/privacy, and booking
  flows.
- Mario has admin/handoff docs and operating surfaces for bookings, tasks,
  roadmap, and launch follow-through.
- The repo-local code gate, Playwright smoke gate, GitHub CI, CodeQL, and basic
  live route smoke were refreshed on 2026-05-06 at DeMario commit `e92b1c0`.
- Toni reported that the remaining Mario site work is complete and that public
  posting can proceed.

## Evidence

- Source artifact:
  - `practice-os/efficiency/demario-pickleball-1-evidence-index.md`
  - `docs/PRACTICE_PROOF_QUEUE_INDEX.md`
  - `demario-pickleball-1/docs/ADMIN_HANDOFF.md`
  - `demario-pickleball-1/docs/APP_OVERVIEW.md`
  - `demario-pickleball-1/docs/MARIO_ACTION_PLAN.md`
  - `demario-pickleball-1/docs/RELEASE_CHECKLIST.md`
  - `demario-pickleball-1/docs/VENUE_RULES.md`
- Verification receipt:
  - DTP evidence index records `npm run ci` pass on 2026-05-06 at commit
    `e92b1c0`.
  - Local `npm run test:e2e` passed 20 Playwright smoke tests across desktop and
    mobile projects.
  - GitHub Actions CI run `25413691658` and CodeQL run `25413691307` passed.
  - Basic live smoke passed for `/`, `/pay`, `/privacy`, `/terms`,
    `/admin/login`, unauthenticated `/admin` redirect, and a public availability
    probe.
- Screenshot/walkthrough:
  - Public homepage, lesson, venue, booking, payment, and non-auth admin-login
    screenshots are usable.
  - Do not use private admin rows, booking records, student details, payments,
    emails, Supabase, Vercel, or private dashboard data.
- Metric:
  - None needed for the recommended posts.
  - Do not claim bookings, revenue, conversion, student count, lead volume, or
    review count unless Toni wants to attach separate source proof.
- Caveat:
  - Public proof is about launch/readiness and operating clarity, not measured
    business impact.

## Permission

- Permission level: public_safe
- Permission source: Toni confirmed posting freedom in chat on 2026-05-06.
- Reviewer: Toni for final channel selection and any asset choice.
- Review date: 2026-05-06

Public copy may say:

- the site is live;
- Toni built it for his brother;
- Toni has been using GitHub Copilot, Codex, and Claude as part of his current
  developer/creator workflow;
- it supports lessons, venue routing, booking, payment guidance, admin
  workflow, availability, tasks, and launch operations;
- DFW pickleball students can check out `https://demariomontezpb.com`.

## Voice Guardrail

Mario posts must stay plain, specific, practical, and human. Do not use
inspirational, gimmicky, motivational, or slogan-like phrasing for this lane.

Avoid sentiment-led openers, motivational slogans, grand metaphors, and claims
about what the work means beyond the actual site, booking flow, and owner
workflow.

Use concrete language instead: what was built, who it serves, what path it
clarifies, how Toni is building lately, and where people can find Mario.

Developer/creator journey framing is allowed when it stays specific:

- name the tools Toni is using;
- say what they helped him build;
- keep Toni as the builder, not the tools as the autonomous actor;
- connect the process back to a real shipped surface.

## Redaction

- Redaction status: public_copy_safe
- Redacted assets:
  - none needed for text-only posting or public-page screenshots
- Remaining private material:
  - booking/admin rows;
  - payment records or payment screenshots;
  - student names, photos, phone numbers, emails, or lesson notes;
  - private feedback texts unless Toni intentionally quotes them;
  - Supabase, Vercel, Resend, Google Calendar, and environment/config screens.

## Owner Approval Ask

No longer needed for this packet. Toni confirmed he can post about Mario's site.

Optional text if Toni still wants a courtesy heads-up:

> I am going to post about the site being live and about the booking/admin flow
> we put around it. I am keeping private student/admin/payment details out of the
> post.

## Public Claim Draft

### Recommended LinkedIn Draft

I have been having fun building lately and using GitHub Copilot, Codex, and
Claude as part of the process.

Using those tools, I built a website and booking flow for my brother's
pickleball business: DeMario Montez Pickleball Coaching.

Mario coaches pickleball in the Dallas-Fort Worth area. He is a 4.70 doubles
DUPR player, USTA certified, and a TeachMe.To SuperCoach. The site is built
around the practical questions students need answered before booking:

- what lessons are available;
- where lessons happen;
- when to book directly through the site;
- when a venue platform is required;
- what to expect around payment and court confirmation.

I also built the owner side around the way the business actually runs: bookings,
inquiries, availability, tasks, roadmap items, and launch handoff notes.

That has been the most interesting part of this developer/creator stretch for
me. The tools make it faster to move from idea to working product, but the real
work is still deciding what the business needs, shaping the flow, and checking
the details.

If you are in DFW and want to play pickleball or get better, hit up Mario:
https://demariomontezpb.com

### Shorter LinkedIn Draft

I have been having fun building lately with GitHub Copilot, Codex, and Claude.

One of the recent projects: a website and booking flow for my brother's DFW
pickleball coaching business, DeMario Montez Pickleball Coaching.

Mario is a 4.70 doubles DUPR player, USTA certified, and a TeachMe.To
SuperCoach. The site covers lesson options, venue-specific booking, payment
guidance, court-confirmation language, and an admin workflow for bookings,
inquiries, availability, tasks, and roadmap items.

DFW pickleball: hit up Mario.
https://demariomontezpb.com

### Personal LinkedIn Draft

I have been spending more time building with GitHub Copilot, Codex, and Claude,
and I am enjoying the developer/creator process more than I expected.

The latest thing I shipped is close to home: a website and booking flow for my
brother Mario's pickleball coaching business.

Mario coaches in the Dallas-Fort Worth area. He is a 4.70 doubles DUPR player,
USTA certified, and a TeachMe.To SuperCoach.

The site covers lesson options, venue routing, direct booking, payment guidance,
court confirmation, and the admin side for bookings, inquiries, availability,
tasks, and roadmap items.

If you are in DFW and want to play pickleball or get better, hit up Mario:
https://demariomontezpb.com

### Recommended Instagram Caption

I have been having fun building lately with GitHub Copilot, Codex, and Claude.

Recent project: a website and booking flow for my brother's DFW pickleball
business.

Mario is a 4.70 doubles DUPR player, USTA certified, and a TeachMe.To
SuperCoach.

- lesson options
- booking
- venue routing
- payment guidance
- court confirmation
- admin workflow behind the scenes

DFW pickleball: hit up Mario.

https://demariomontezpb.com

#pickleball #dfwpickleball #dallaspickleball #smallbusiness #webdesign

### Short Instagram Caption

Built a site and booking flow for my brother's DFW pickleball coaching business
using GitHub Copilot, Codex, and Claude as part of the process.

Lesson options, booking, venue routing, payment guidance, and admin workflow are
all in place.

DFW pickleball: hit up Mario.
demariomontezpb.com

#pickleball #dfwpickleball #smallbusiness

### Instagram Carousel Copy

1. I have been building more with GitHub Copilot, Codex, and Claude.
2. Recent project: my brother's pickleball coaching site.
3. DeMario Montez Pickleball Coaching is live.
4. Mario coaches pickleball in the DFW area.
5. The site covers lessons, booking, venues, and payment guidance.
6. The owner side covers bookings, inquiries, availability, tasks, and roadmap.
7. DFW pickleball: hit up Mario.

## Claims To Avoid Unless Separately Proven

- "Bookings increased."
- "Revenue grew."
- "Students love the site."
- "Automated the business" or anything that implies Mario is not still running
  the relationship side himself.
- "AI built this by itself" or any claim that removes Toni's role as builder.
- Inspirational, gimmicky, or slogan-like phrasing for Mario posts.
- Any student quote, review count, testimonial, booking row, payment proof, or
  private admin screenshot that Toni does not intentionally want to make public.

## Authenticity Review

- Canonical standard:
  `practice-os/policies/authentic-voice-and-anti-slop.md`
- Evidence named in the claim: site launch/readiness, booking route, payment
  handoff, admin handoff, roadmap/checklist, developer tool-assisted workflow.
- Caveat visible in the claim: no measured business impact or private proof is
  claimed.
- Voice test: human, plain, concrete; developer/creator journey is specific and
  does not overclaim what the tools did.
- Knowledgeable-reader test: ready for public text posting.

## What Stayed Manual On Purpose

- Mario still confirms exact court details when needed.
- Payment confirmation remains human-owned until a later payment processor path
  is approved.
- Refund/cancellation/payment adjustments remain manual.
- Public posting remains human-owned by Toni.
- Private admin screenshots remain redaction-gated.

## Publish Decision

- Status: approved_public_safe
- Recommended next action: use the recommended LinkedIn draft and recommended
  Instagram caption with a public homepage screenshot, a booking-flow screenshot,
  or a short public-page scroll recording.
- After posting, record the final LinkedIn/Instagram URL(s) back into this
  packet or the DTP proof queue.
