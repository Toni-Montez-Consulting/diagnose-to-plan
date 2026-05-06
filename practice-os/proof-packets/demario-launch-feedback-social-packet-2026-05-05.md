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
- it supports lessons, venue routing, booking, payment guidance, admin
  workflow, availability, tasks, and launch operations;
- DFW pickleball students can check out `https://demariomontezpb.com`.

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

Shipping client work is fun. Shipping something for family hits different.

I just finished the new site and booking flow for my brother, DeMario Montez.

Mario is a Dallas-Fort Worth pickleball coach, and the goal was not just "make a
nice website." The goal was to build the small operating system around the
business.

Students need to understand what he offers, where lessons happen, how to book,
what happens with payment, and when they need to use a venue platform instead of
the site.

Mario needs the owner side to be clear too: bookings, inquiries, availability,
tasks, roadmap items, and the daily flow of running the business without every
detail living in texts.

That is the kind of build I like most. Not overbuilt. Not generic. Just enough
system to make a real small business easier to run.

If you are in DFW and want to get better at pickleball, check him out:
https://demariomontezpb.com

### Shorter LinkedIn Draft

I got to build this one for my brother.

DeMario Montez Pickleball Coaching is live: a public site, lesson flow, venue
routing, booking path, payment guidance, and admin workflow for his DFW coaching
business.

What I like about this project is that it is not trying to replace the human
part of the business. Mario still coaches, confirms courts, texts students, and
runs the relationships.

The site just removes confusion around the parts that should be clear:

- what lessons are available
- where students should book
- when a venue platform is required
- how payment works
- what Mario needs to manage after launch

That is the sweet spot for small-business software: make the path easier without
flattening the person behind it.

Live now: https://demariomontezpb.com

### Personal LinkedIn Draft

My brother is one of those people who can see the game before it happens.

He coaches pickleball with the kind of calm, specific feedback that makes people
feel like improvement is actually reachable.

I wanted his site to carry that same energy: clear, practical, local, and easy
to act on.

So this was not just a landing page. It became a working launch surface:
lessons, booking, venue routing, payment guidance, court-confirmation language,
admin tasks, availability, and a simple owner workflow behind the scenes.

I am proud of this one because it feels like what software should do for a small
business: take the messy operational pieces and turn them into a path people can
actually use.

DFW pickleball folks, go check out DeMario:
https://demariomontezpb.com

### Recommended Instagram Caption

Built this one for my brother.

DeMario Montez Pickleball Coaching is live at demariomontezpb.com.

The goal was not just a clean website. It was a clear path for a real coaching
business:

- lesson options
- booking
- venue routing
- payment guidance
- court confirmation
- admin workflow behind the scenes

Proud of this one. Simple public site on the outside, practical operating system
underneath.

DFW pickleball people, go check him out.

https://demariomontezpb.com

#pickleball #dfwpickleball #dallaspickleball #smallbusiness #webdesign

### Short Instagram Caption

New site is live for DeMario Montez Pickleball Coaching.

Built the public lesson flow, booking path, venue routing, payment guidance, and
admin workflow around Mario's coaching business.

Not just a website. A cleaner way for students to book and for Mario to run the
day-to-day.

DFW pickleball: demariomontezpb.com

#pickleball #dfwpickleball #smallbusiness

### Instagram Carousel Copy

1. Built this one for my brother.
2. DeMario Montez Pickleball Coaching is live.
3. The job was not just "make a website."
4. Students needed a clear path: lessons, locations, booking, payment.
5. Mario needed the owner side: bookings, inquiries, availability, tasks.
6. The best tech disappears into the way the business already works.
7. DFW pickleball: demariomontezpb.com

## Claims To Avoid Unless Separately Proven

- "Bookings increased."
- "Revenue grew."
- "Students love the site."
- "Automated the business" or anything that implies Mario is not still running
  the relationship side himself.
- Any student quote, review count, testimonial, booking row, payment proof, or
  private admin screenshot that Toni does not intentionally want to make public.

## Authenticity Review

- Canonical standard:
  `practice-os/policies/authentic-voice-and-anti-slop.md`
- Evidence named in the claim: site launch/readiness, booking route, payment
  handoff, admin handoff, roadmap/checklist.
- Caveat visible in the claim: no measured business impact or private proof is
  claimed.
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
