# Custom Interface Craft Standard

Status: hard practice-wide standard for broad UI work on new sites, apps, admin portals, proof surfaces, and assistant-facing interfaces.

This standard captures Toni's preference that every new interface should feel authored, custom, expressive, and specific to its audience. It does not mean every project should be plain. It means every project should have its own designed point of view across visual direction, HTML structure, CSS system, components, copy, assets, interactions, accessibility, public/private boundaries, and verification.

Custom is the default. Plain is only a deliberate audience-specific style choice, not the practice baseline. Generic is never the baseline.

## Intent

Every broad UI implementation should start from a custom interface craft brief before significant design or frontend work begins. A narrow hotfix may skip the brief only when the implementer records that it is a hotfix exception and does not expand the UI surface.

`architected-strength` and `consulting` are the intended gold-standard reference tracks, but they are not yet complete. Until each reaches production-level operational quality, future agents may use them for ambition, taste, direction, and style cues, but not as finished templates to copy. They start as in-progress north-star candidates and can become operational or gold-standard references only after the promotion gate below is satisfied.

The expression should change by audience: CCAAP can be warm, civic, readable, and older-audience friendly; consulting can be precise and operator-grade; DeMario can feel local, trustworthy, and booking-focused; Omnexus can feel native, polished, and high-trust. None of those should feel like a default template.

## Research Basis

Use official platform and framework guidance as the floor:

- Astro components support HTML-first, reusable page and UI building blocks with no client JavaScript by default, which fits custom static/public sites and low-maintenance owner projects: https://docs.astro.build/en/basics/astro-components/
- Astro styling supports component-scoped CSS and global CSS through layouts, which lets each repo own a custom visual system without forcing a generic theme: https://docs.astro.build/en/guides/styling/
- MDN documents CSS custom properties as reusable semantic values, which should be used for project-specific tokens instead of scattered hard-coded style values: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties
- MDN documents container queries for component-level responsive behavior, which should be considered when a component needs to adapt to its own space rather than only the viewport: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries
- W3C/WAI page-structure guidance anchors custom design in semantic regions, landmarks, headings, and labels so authored interfaces stay navigable and understandable: https://www.w3.org/WAI/tutorials/page-structure/regions/
- web.dev's responsive design material reinforces that responsive interfaces should work across screen sizes and input contexts, not merely pass a desktop screenshot check: https://web.dev/learn/design

## Core Rules

1. Start with audience and job.
   - Name who the interface serves first.
   - Name the top 3-5 tasks the interface must make obvious.
   - Name what should feel familiar, premium, civic, technical, playful, quiet, energetic, editorial, cinematic, operational, or expressive.

2. Author the HTML.
   - Use real document structure: `header`, `nav`, `main`, `section`, `article`, `aside`, and `footer` where appropriate.
   - Give headings real information hierarchy.
   - Use buttons for actions, links for navigation, lists for lists, tables only for tabular data, and forms with labels.
   - Avoid div soup and anonymous card grids that only look organized visually.

3. Author the CSS.
   - Define project-specific tokens for color, type, spacing, radius, borders, shadows, focus, motion, and surfaces.
   - Name CSS primitives around the project language, not generic template concepts.
   - Keep responsive rules close to the component or layout they govern.
   - Use container queries when a component's container matters more than global viewport width.
   - Keep CSS readable enough that future agents can understand the design system without reverse engineering screenshots.

4. Author the components.
   - Create custom layout primitives, page sections, action modules, proof modules, owner guidance blocks, content cards, nav, footer, and form states that fit the project.
   - Do not treat imported component libraries as the design. Libraries may provide plumbing, but the product should own the interface language.
   - Stable dimensions should prevent hover states, labels, icons, counters, or dynamic text from shifting the layout.

5. Author the copy.
   - Use domain language, owner language, and audience language.
   - Avoid generic SaaS, AI consultancy, nonprofit, fitness, portfolio, or marketplace filler.
   - Every public page should answer: what is this, who is it for, what can I do next, what proof or trust signal exists, and how do I get help?

6. Author the assets.
   - Prefer authentic photos, screenshots, diagrams, documents, logos, and product states.
   - Use placeholders only when they are honest and explicitly waiting on owner approval.
   - Avoid stock-like mood imagery when users need to inspect the real organization, product, person, venue, or workflow.

7. Keep public/private boundaries visible.
   - Public surfaces may show method, redacted proof, source discipline, and public-safe examples.
   - Admin surfaces must protect private records, unpublished proof, client details, credentials, and raw traces.
   - Assistant/chatbot experiences must follow the cross-site assistant architecture before implementation.

8. Verify visually and structurally.
   - Check desktop and mobile.
   - Check text fit, no horizontal overflow, focus states, navigation clarity, and form states.
   - Run repo-local hard gates before handoff.
   - For public/proof/client work, run privacy, secret, evidence, and claim checks.

## Reference Maturity Model

Use this maturity model before citing any project as a reusable design reference.

- North-star candidate: useful for direction, ambition, taste, or style cues, but unfinished. Do not copy as a completed pattern.
- Operational reference: production-level enough to learn selected patterns from. The reusable lessons are named, reviewed, and bounded.
- Gold-standard reference: reviewed, verified, accepted by Toni, and documented as reusable. Future agents may treat it as a canonical example for the specific pattern it earned.

Reference promotion requires:

- Core routes or screens are complete.
- Build, check, route, and visual gates pass.
- Desktop and mobile QA are reviewed.
- Toni accepts the design direction and content voice.
- No generic template sections or placeholder copy remain.
- Public, private, admin, proof, and assistant boundaries are clean.
- A DTP note explains what future agents should learn from the project.
- The project is explicitly marked as an operational or gold-standard reference.

## Project-Specific Application

- `architected-strength`: in-progress north-star candidate for an expressive personal-brand OS, content hub, networking engine, proof lab, and fully authored craft. Do not treat it as canonical until promoted.
- `consulting`: in-progress north-star candidate for precise operator/proof surfaces, Steel Ledger style, high-trust copy, clear services, proof loops, and Hub-first intake. Do not treat it as canonical until promoted.
- `ccaap-site`: warm civic nonprofit surface for an older/community audience. The site should stay easy and familiar, but every element should be custom, readable, warm, trustworthy, and owner-guided.
- `demario-pickleball-1`: client-first booking clarity, venue rules, admin support, and local-business trust. Customization should reduce booking confusion before adding visual flair.
- `fitness-app` / Omnexus: mobile trust, App Store proof, onboarding clarity, billing/auth safety, and launch evidence. Custom craft includes native feel and support flows, not only marketing screens.
- Future client sites/apps: start with the craft brief, then decide whether the project needs a simple handoff site, command room, public proof page, admin portal, assistant, or mobile app.

## Minimum Craft Brief

Before broad UI implementation, create or fill `practice-os/templates/custom-interface-craft-brief.md` in the owning repo or DTP lane. If the work is a small hotfix, record why the brief is deferred and avoid expanding the UI scope.

The brief should answer:

- What is the audience and emotional tone?
- What are the primary actions?
- What should feel custom, memorable, and project-specific?
- What HTML regions and page types are needed?
- What CSS primitives and tokens are project-specific?
- What components must be authored rather than copied from a template?
- What content voice and words are not allowed?
- What real assets are needed?
- What public/private/admin boundaries apply?
- What verification proves the interface is usable, custom, and safe?
- Which reference maturity level applies to any inspiration sources?
- What must not be copied from an unfinished or generic reference?

## Done Gate

A new site/app/admin surface meets this standard when:

- A custom interface craft brief exists or is intentionally deferred for a narrow hotfix.
- The implementation uses project-specific HTML, CSS, layout primitives, content, and asset rules.
- It has no obvious generic template sections, unsupported public claims, private leaks, or stock-like trust theater.
- Desktop and mobile manual review pass.
- Repo-local build/check/test gates pass or blockers are named.
- Any public proof, private/admin data, or assistant behavior passes the relevant DTP gates before launch.
