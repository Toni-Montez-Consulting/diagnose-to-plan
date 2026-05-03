---
created: 2026-04-28T07:12:05.3737441-05:00
command: manual
type: incident
severity: medium
status: resolved
---

# 0002 - Production intake outage (Supabase key)

## What happened

The production Hub intake endpoint at `https://onhand.dev/api/intake` was deployed with an invalid Supabase service-role key configuration, so real POST submissions could fail before reaching `intake_submissions`. The health route still returned a Vercel runtime response, which meant the outage was specific to the intake write path rather than the whole Hub deployment. After the key configuration was corrected and production was redeployed, a controlled intake submission returned `201 { ok: true }`, appeared in Supabase, and was deleted.

## Window

Unknown - not recoverable from logs available in this workspace. The latest known good state is after the GitHub-backed redeploy and controlled smoke test on April 28, 2026. The bug was likely live between the first production Hub deploy using Supabase-backed intake and the later correction of the production Supabase key, but this repo does not contain enough timestamped runtime logs to prove the exact start time.

## Root cause

The production Vercel environment had the wrong Supabase key value for Hub's server-side intake write path. The preview and production environment work happened across multiple repos and CLIs, and the original validation emphasized health/CORS checks before a real insert. That missed the credential mismatch because `OPTIONS /api/intake` does not exercise the Supabase insert path.

## How it was found

It was found during the portfolio ops Phase C controlled intake test. The test moved past CORS and submitted a real JSON payload to `https://onhand.dev/api/intake`, then verified whether the row landed in Supabase.

## Fix

The Hub Vercel Supabase service-role key was corrected for the deployed environments, then the latest clean GitHub-backed production deployment was redeployed and aliased to `https://onhand.dev`. Redeploying from GitHub instead of a local prebuilt kept unrelated dirty Hub draft work out of the production artifact and made the deployed code path match the pushed `main` state.

## Lead exposure

Potential exposure exists, but there is no evidence in this workspace that a real prospect submission was lost. The strongest evidence against confirmed lead loss is that the site was newly wired, the issue was found during the same portfolio ops pass that introduced the production smoke test, and no retained logs in this workspace show a real prospect POST failing. If a real prospect did submit during the unknown window, recovery options are limited to checking Vercel logs, email/Formspree fallback activity, referral conversations, and any browser-side analytics or contact attempts around the outage window.

## Prevention

The mechanism that would have caught this earlier is a production smoke test that performs one controlled insert, verifies the Supabase row, and deletes it. The portfolio ops wrapper should continue checking Vercel environment variable presence, but env-name parity alone is not enough because it cannot prove the value is correct. Stronger future controls are automated production-deploy smoke tests for `POST /api/intake`, 5xx/error-rate monitoring on the intake route, and a runbook that treats CORS-only success as insufficient for release verification.

## Follow-ups

- Completed: corrected the Hub Supabase service-role key in Vercel.
- Completed: redeployed production from the clean GitHub-backed Hub deployment instead of local dirty state.
- Completed: submitted one controlled intake test, verified the Supabase row, and deleted it.
- Completed: hardened the portfolio ops wrapper so it checks required Vercel env names and `npx supabase migration list` without printing secrets.
- Open: add automated production intake smoke coverage after deploy.
- Open: add route-level monitoring or alerting for intake failures.
