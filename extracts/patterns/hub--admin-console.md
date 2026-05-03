---
repo: hub
signal: admin-surface
pattern_slug: admin-console
detected_at: '2026-04-29T02:10:05Z'
model: claude-sonnet-4-6
files_read:
- api/console/dashboard.ts
- api/console/outreach.ts
- api/console/roadmap.ts
- api/console/todos.ts
- apps/web/src/pages/Console.tsx
- apps/web/src/pages/Dashboard.tsx
- api/_lib/console-store.ts
- api/intake.ts
- apps/server/src/console-data.ts
- apps/web/src/api.ts
- apps/web/src/App.tsx
- apps/web/src/pages/Ask.tsx
confidence: medium
truncated: true
promoted: false
private_review_required: true
---

# Admin Console

## What this is

`hub` exposes a `admin-surface` pattern evidenced by Admin, console, or dashboard surface. This detector only used the indexed files listed below, so the pattern is a grounded extraction candidate rather than a full architectural claim.

## Where it lives

- `api/console/dashboard.ts`
- `api/console/outreach.ts`
- `api/console/roadmap.ts`
- `api/console/todos.ts`
- `apps/web/src/pages/Console.tsx`
- `apps/web/src/pages/Dashboard.tsx`
- `api/_lib/console-store.ts`
- `api/intake.ts`
- `apps/server/src/console-data.ts`
- `apps/web/src/api.ts`
- `apps/web/src/App.tsx`
- `apps/web/src/pages/Ask.tsx`

## Reusable shape

Public proof or entry surfaces should route into a private operating room. Reusable pieces include intake status, command links, triage state, work orders, health checks, and handoff/runbook boundaries. Client-specific pieces should vary by domain language, record schema, auth requirements, and privacy rules.

## Review notes

- `promoted` starts false until Toni confirms this pattern helped real work.
- `private_review_required` starts true so private details are checked before reuse.
- Treat this as a pattern candidate; use citations before carrying it into a SOW.

## Citations

- api/console/dashboard.ts:2-2
- api/console/dashboard.ts:69-69
- api/console/dashboard.ts:4-4
- api/console/dashboard.ts:16-16
- api/console/outreach.ts:4-4
- api/console/roadmap.ts:12-12
- api/console/todos.ts:4-4
- apps/web/src/pages/Console.tsx:5-5
- apps/web/src/pages/Console.tsx:63-63
- apps/web/src/pages/Console.tsx:6-6
- apps/web/src/pages/Console.tsx:66-66
- apps/web/src/pages/Dashboard.tsx:4-4
- api/_lib/console-store.ts:8-8
- api/_lib/console-store.ts:1-1
- api/_lib/console-store.ts:6-6
- api/intake.ts:1-1
- apps/server/src/console-data.ts:38-38
- apps/web/src/api.ts:163-163
- apps/web/src/api.ts:195-195
- apps/web/src/App.tsx:9-9
- apps/web/src/App.tsx:2-2
- apps/web/src/pages/Ask.tsx:3-3

## Constrained Prompt

```text
Describe the pattern present in these files. Cite specific file paths and line ranges for every claim. If you cannot tell from the files what the pattern is, say so. Do not extrapolate from filenames or imports to functionality you did not see. The agent gets no filesystem tools; only this embedded content is in scope.

Signal: admin-surface
Evidence: Admin, console, or dashboard surface

## File: api/console/dashboard.ts
Included ranges: ((1, 104),)

1: import { requireHubAuth } from '../_lib/auth'
2: import { countOutreachThisWeek, loadOperationalData } from '../_lib/console-store'
3: import { json } from '../_lib/http'
4: import { loadPlaybookDashboardBase } from '../_lib/playbook'
5: 
6: export async function GET(request: Request): Promise<Response> {
7:   const authError = requireHubAuth(request)
8:   if (authError) return authError
9: 
10:   try {
11:     const [base, ops] = await Promise.all([loadPlaybookDashboardBase(), loadOperationalData()])
12:     const sentThisWeek = ops.configured
13:       ? countOutreachThisWeek(ops.outreach, base.weekly.weekOf)
14:       : base.legacyOutreach.sentThisWeek
15:     const openTodos = ops.todos.filter((todo) => todo.status === 'open').length
16:     const inboundNew = ops.intake.filter((submission) => submission.status === 'new').length
17: 
18:     return json({
19:       source: {
20:         ...base.source,
21:         warnings: [...base.source.warnings, ...ops.warnings],
22:       },
23:       stats: [
24:         {
25:           label: 'open todos',
26:           value: String(openTodos),
27:           subtext:
28:             openTodos === 0
29:               ? 'clear board - choose the next business action'
30:               : 'live actions from Supabase',
31:           tone: openTodos === 0 ? 'empty' : 'warn',
32:         },
33:         {
34:           label: 'weekly dms',
35:           value: `${sentThisWeek} / 3`,
36:           subtext: sentThisWeek >= 3 ? 'weekly outreach target hit' : 'send the three referral DMs',
37:           tone: sentThisWeek >= 3 ? 'ok' : 'warn',
38:         },
39:         {
40:           label: 'inbound',
41:           value: String(inboundNew),
42:           subtext: inboundNew === 0 ? 'no inbound yet - send the dms' : 'new intake submissions',
43:           tone: inboundNew === 0 ? 'empty' : 'ok',
44:         },
45:         {
46:           label: 'capacity',
47:           value: `${base.pipeline.activeEngagements} / 5`,
48:           subtext:
49:             base.pipeline.activeEngagements === 0
50:               ? 'no active engagements - first audit lands here'
51:               : 'active engagement points',
52:           tone:
53:             base.pipeline.activeEngagements === 0
54:               ? 'empty'
55:               : base.pipeline.activeEngagements >= 5
56:                 ? 'warn'
57:                 : 'ok',
58:         },
59:       ],
60:       weekly: base.weekly,
61:       todos: {
62:         rows: ops.todos,
63:         openCount: openTodos,
64:         completedThisWeek: ops.todos.filter((todo) => todo.status === 'done').length,
65:         configured: ops.configured,
66:         emptyMessage: ops.configured
67:           ? 'no todos yet - add the next concrete business action'
68:           : 'configure Supabase to manage todos from the console',
69:         sourcePath: 'supabase.admin_todos',
70:       },
71:       outreach: {
72:         rows: ops.configured ? ops.outreach : base.legacyOutreach.rows,
73:         sentThisWeek,
74:         target: 3,
75:         configured: ops.configured,
76:         emptyMessage: ops.configured
77:           ? 'no outreach logged yet - send the three referral DMs'
78:           : 'configure Supabase to log outreach from the console',
79:         sourcePath: ops.configured ? 'supabase.outreach_events' : base.legacyOutreach.sourcePath,
80:       },
81:       intake: {
82:         rows: ops.intake,
83:         newCount: inboundNew,
84:         configured: ops.configured,
85:         emptyMessage: ops.configured
86:           ? 'no inbound yet - send the dms'
87:           : 'configure Supabase to capture consulting intake submissions',
88:         sourcePath: 'supabase.intake_submissions',
89:       },
90:       pipeline: base.pipeline,
91:       proofArtifacts: base.proofArtifacts,
92:       roadmap: base.roadmap,
93:     })
94:   } catch (error) {
95:     return json(
96:       { error: 'console_dashboard_failed', message: errorMessage(error) },
97:       { status: 500 },
98:     )
99:   }
100: }
101: 
102: function errorMessage(error: unknown): string {
103:   return error instanceof Error ? error.message : String(error)
104: }

## File: api/console/outreach.ts
Included ranges: ((1, 90),)

1: import { requireHubAuth } from '../_lib/auth'
2: import {
3:   archiveOutreachEvent,
4:   ConsoleStoreError,
5:   createOutreachEvent,
6:   listOutreachEvents,
7:   parseOutreachCreateInput,
8:   parseOutreachPatchInput,
9:   updateOutreachEvent,
10: } from '../_lib/console-store'
11: import { badRequest, json, methodNotAllowed, readRequestObject } from '../_lib/http'
12: import { isSupabaseConfigured } from '../_lib/supabase'
13: 
14: export async function GET(request: Request): Promise<Response> {
15:   const authError = requireHubAuth(request)
16:   if (authError) return authError
17:   if (!isSupabaseConfigured()) return supabaseNotConfigured()
18: 
19:   const limit = Number(new URL(request.url).searchParams.get('limit') ?? '50')
20:   return json({
21:     rows: await listOutreachEvents(Number.isFinite(limit) ? Math.min(limit, 100) : 50),
22:   })
23: }
24: 
25: export async function POST(request: Request): Promise<Response> {
26:   const authError = requireHubAuth(request)
27:   if (authError) return authError
28:   if (!isSupabaseConfigured()) return supabaseNotConfigured()
29: 
30:   const parsed = parseOutreachCreateInput(await readRequestObject(request))
31:   if (!parsed.ok) return badRequest(parsed.error)
32: 
33:   try {
34:     return json({ row: await createOutreachEvent(parsed.value) }, { status: 201 })
35:   } catch (error) {
36:     return storeError(error)
37:   }
38: }
39: 
40: export async function PATCH(request: Request): Promise<Response> {
41:   const authError = requireHubAuth(request)
42:   if (authError) return authError
43:   if (!isSupabaseConfigured()) return supabaseNotConfigured()
44: 
45:   const parsed = parseOutreachPatchInput(await readRequestObject(request))
46:   if (!parsed.ok) return badRequest(parsed.error)
47: 
48:   try {
49:     return json({ row: await updateOutreachEvent(parsed.value) })
50:   } catch (error) {
51:     return storeError(error)
52:   }
53: }
54: 
55: export async function DELETE(request: Request): Promise<Response> {
56:   const authError = requireHubAuth(request)
57:   if (authError) return authError
58:   if (!isSupabaseConfigured()) return supabaseNotConfigured()
59: 
60:   const body = await readRequestObject(request)
61:   const id = new URL(request.url).searchParams.get('id') ?? (body['id'] as string | undefined)
62:   if (!id) return badRequest('Outreach id is required.')
63: 
64:   try {
65:     return json({ row: await archiveOutreachEvent(id) })
66:   } catch (error) {
67:     return storeError(error)
68:   }
69: }
70: 
71: export function OPTIONS(): Response {
72:   return methodNotAllowed('OPTIONS', ['GET', 'POST', 'PATCH', 'DELETE'])
73: }
74: 
75: function supabaseNotConfigured(): Response {
76:   return json({ error: 'supabase_not_configured' }, { status: 503 })
77: }
78: 
79: function storeError(error: unknown): Response {
80:   if (error instanceof ConsoleStoreError) {
81:     return json({ error: 'console_store_error', message: error.message }, { status: error.status })
82:   }
83:   return json(
84:     {
85:       error: 'console_store_error',
86:       message: error instanceof Error ? error.message : String(error),
87:     },
88:     { status: 500 },
89:   )
90: }

## File: api/console/roadmap.ts
Included ranges: ((1, 18),)

1: import { 
```
