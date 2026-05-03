---
repo: consulting
signal: admin-surface
pattern_slug: admin-command-room
detected_at: '2026-04-29T02:28:46Z'
model: claude-sonnet-4-6
files_read:
- src/pages/admin.astro
- README.md
confidence: medium
truncated: true
promoted: false
private_review_required: true
---

# Admin Command Room

## What this is

`consulting` exposes a `admin-surface` pattern evidenced by Admin, console, or dashboard surface. This detector only used the indexed files listed below, so the pattern is a grounded extraction candidate rather than a full architectural claim.

## Where it lives

- `src/pages/admin.astro`
- `README.md`

## Reusable shape

Public proof or entry surfaces should route into a private operating room. Reusable pieces include intake status, command links, triage state, work orders, health checks, and handoff/runbook boundaries. Client-specific pieces should vary by domain language, record schema, auth requirements, and privacy rules.

## Review notes

- `promoted` starts false until Toni confirms this pattern helped real work.
- `private_review_required` starts true so private details are checked before reuse.
- Treat this as a pattern candidate; use citations before carrying it into a SOW.

## Citations

- src/pages/admin.astro:6-6
- src/pages/admin.astro:112-112
- src/pages/admin.astro:9-9
- src/pages/admin.astro:90-90
- src/pages/admin.astro:36-36
- src/pages/admin.astro:13-13
- src/pages/admin.astro:63-63
- src/pages/admin.astro:94-94
- README.md:37-37
- README.md:3-3
- README.md:35-35
- README.md:52-52

## Constrained Prompt

```text
Describe the pattern present in these files. Cite specific file paths and line ranges for every claim. If you cannot tell from the files what the pattern is, say so. Do not extrapolate from filenames or imports to functionality you did not see. The agent gets no filesystem tools; only this embedded content is in scope.

Signal: admin-surface
Evidence: Admin, console, or dashboard surface

## File: src/pages/admin.astro
Included ranges: ((1, 200), (488, 537))

1: ---
2: import Base from "@/layouts/Base.astro";
3: import ArtifactFrame from "@/components/ArtifactFrame.astro";
4: import WorkOrderLedger from "@/components/WorkOrderLedger.astro";
5: 
6: const hubAdminUrl = import.meta.env.PUBLIC_HUB_ADMIN_URL || "https://onhand.dev/console";
7: const hubHealthUrl =
8:   import.meta.env.PUBLIC_HUB_HEALTH_URL || new URL("/health", hubAdminUrl).toString();
9: const consultingIntakeEndpoint = import.meta.env.PUBLIC_CONSULTING_INTAKE_ENDPOINT || "";
10: const formspreeEndpoint = import.meta.env.PUBLIC_FORMSPREE_ENDPOINT || "";
11: const launchChecklistUrl = "https://github.com/toniomon96/consulting/blob/main/docs/LAUNCH_CHECKLIST.md";
12: 
13: const commandLinks = [
14:   {
15:     label: "Hub console",
16:     href: hubAdminUrl,
17:     detail: "Open the protected operating room where private intake and workflow state belong."
18:   },
19:   {
20:     label: "Health route",
21:     href: hubHealthUrl,
22:     detail: "Check whether the live Hub runtime is reachable before trusting the intake path."
23:   },
24:   {
25:     label: "Public intake",
26:     href: "/start",
27:     detail: "Review the prospect-facing diagnostic path and field shape."
28:   },
29:   {
30:     label: "Launch checklist",
31:     href: launchChecklistUrl,
32:     detail: "Source checklist in the repo for the manual release pass."
33:   }
34: ];
35: 
36: const statusRows = [
37:   {
38:     label: "consulting site",
39:     value: "static Astro",
40:     state: "live surface",
41:     detail: "Public proof, diagnostic intake, case records, and this admin command room."
42:   },
43:   {
44:     label: "primary intake",
45:     value: consultingIntakeEndpoint ? "Hub endpoint" : "not set locally",
46:     state: consultingIntakeEndpoint ? "configured" : "needs env",
47:     detail: consultingIntakeEndpoint || "Set PUBLIC_CONSULTING_INTAKE_ENDPOINT in Vercel."
48:   },
49:   {
50:     label: "fallback intake",
51:     value: formspreeEndpoint ? "Formspree" : "email only",
52:     state: formspreeEndpoint ? "available" : "last resort",
53:     detail: formspreeEndpoint || "The public contact component will render the email fallback when no endpoint exists."
54:   },
55:   {
56:     label: "private data",
57:     value: "Hub only",
58:     state: "guardrail",
59:     detail: "This route does not render private submissions, service-role keys, client notes, or workflow rows."
60:   }
61: ];
62: 
63: const triageRows = [
64:   {
65:     stage: "01",
66:     title: "New diagnostic",
67:     owner: "Toni",
68:     signal: "messy context, 30-day target, already tried",
69:     next: "read for owner bottleneck and source-material gaps"
70:   },
71:   {
72:     stage: "02",
73:     title: "Qualified fit",
74:     owner: "Toni",
75:     signal: "clear route pressure, real business consequence",
76:     next: "send call link and define first useful packet"
77:   },
78:   {
79:     stage: "03",
80:     title: "Install candidate",
81:     owner: "Toni + client",
82:     signal: "intake, console, assistant, launch repair, or handoff system",
83:     next: "scope the smallest shippable operating layer"
84:   },
85:   {
86:     stage: "04",
87:     title: "Handoff record",
88:     owner: "Toni",
89:     signal: "access, decisions, risks, next-pass queue",
90:     next: "leave a runbook the owner can operate"
91:   }
92: ];
93: 
94: const workOrders = [
95:   {
96:     code: "P0",
97:     meta: "live intake",
98:     title: "Submit one real test intake.",
99:     copy: "Use the public form, confirm it lands in Hub, then delete or archive the test record from the private console.",
100:     emphasis: true
101:   },
102:   {
103:     code: "P0",
104:     meta: "ops proof",
105:     title: "Keep private rows out of the public site.",
106:     copy: "Use this route as the command surface. Keep actual prospects, client notes, service-role data, and workflow rows in Hub."
107:   },
108:   {
109:     code: "P1",
110:     meta: "spec leverage",
111:     title: "Turn admin work into a reusable pattern.",
112:     copy: "Feed this dashboard, the Hub console, and future client admin rooms into the extract spec as the canonical admin-surface pattern."
113:   },
114:   {
115:     code: "P1",
116:     meta: "next upgrade",
117:     title: "Add true auth only when there is private work here.",
118:     copy: "If this page starts managing records directly, move from static command room to protected server-rendered admin."
119:   }
120: ];
121: 
122: const runbookItems = [
123:   "Check Hub health before changing intake copy.",
124:   "Review new records in Hub, not in public markup.",
125:   "Capture decisions in the repo or Hub before memory decays.",
126:   "Promote repeated admin moves into reusable patterns.",
127:   "Ship public proof only after redaction is clear."
128: ];
129: ---
130: 
131: <Base
132:   title="Admin Command Room | Toni Montez"
133:   description="Private-ops command room for the Toni Montez consulting site: intake status, Hub routing, triage, runbook, and admin work orders."
134:   section="admin"
135:   status="ops room"
136:   robots="noindex,nofollow"
137: >
138:   <main id="main-content">
139:     <section class="admin-hero page-shell">
140:       <div class="admin-hero__copy">
141:         <p class="section-kicker">Admin / command room</p>
142:         <h1 class="admin-title">Run the consulting site like an operating room.</h1>
143:         <p class="admin-lead">
144:           Public site outside. Private Hub console inside. This page keeps the live intake route, triage logic, handoff runbook, and admin work queue in one place without exposing private records.
145:         </p>
146:         <div class="admin-actions" aria-label="Admin command links">
147:           <a class="command-button" href={hubAdminUrl} target="_blank" rel="noreferrer" data-cursor="open">Open Hub</a>
148:           <a class="text-link" href="#queue" data-cursor="proof">Review queue</a>
149:         </div>
150:       </div>
151: 
152:       <ArtifactFrame
153:         variant="terminal"
154:         title="admin command"
155:         kicker="ops surface"
156:         tone="blue"
157:         lines={[
158:           "check hub health",
159:           "review new intake",
160:           "triage fit",
161:           "write handoff note",
162:           "promote pattern"
163:         ]}
164:         caption="admin route / no private rows rendered"
165:       />
166:     </section>
167: 
168:     <section class="admin-board page-shell" aria-label="Admin dashboard">
169:       <div class="admin-board__header">
170:         <div>
171:           <p class="section-kicker">Live routing</p>
172:           <h2>Control plane.</h2>
173:         </div>
174:         <a class="health-chip" href={hubHealthUrl} target="_blank" rel="noreferrer" data-state="linked" data-cursor="open">
175:           <span></span>
176:           <p>open Hub health</p>
177:         </a>
178:       </div>
179: 
180:       <div class="status-ledger">
181:         {statusRows.map((row) => (
182:           <article class="status-row" data-cursor="proof">
183:             <p class="chrome-text">{row.label}</p>
184:             <strong>{row.value}</strong>
185:             <span>{row.state}</span>
186:             <small>{row.detail}</small>
187:           </article>
188:         ))}
189:       </div>
190: 
191:       <div class="command-grid" aria-label="Command links">
192:         {commandLinks.map((link) => (
193:           <a class="command-card" href={link.h
```
