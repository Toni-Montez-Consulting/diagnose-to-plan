---
data_class: P1
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Pattern: Customer Inquiry Bottleneck

## Signal

Inbound messages pile up, receive inconsistent replies, or wait on the owner for basic first response.

## Real Constraint

Owner attention, unclear service rules, and no standard intake-to-reply path.

## Non-AI Fix First

Define service categories, required intake fields, approval rules, and when to say no.

## Intervention

Client Operating Kit with inquiry workflow card, response-draft Skill, connector map, and weekly review metric.

## Eval

Primary: time from inquiry to owner-visible draft. Secondary: missed inquiries per week.

## When Not To Use This

Do not automate replies for legal, medical, financial, refund, safety, or conflict-heavy messages.
