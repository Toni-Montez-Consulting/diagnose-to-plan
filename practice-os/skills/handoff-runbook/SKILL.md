---
name: handoff-runbook
description: Drafts an operator handoff manual or runbook that lets a client or non-technical operator run, change safe parts, report issues, disable, and recover the installed workflow.
risk_class: R1
version: 0.2.0
---

# Purpose

Make the client less dependent on Toni after the build.

Use this for client handoffs, family/operator admin transfers, Client Operating
Kits, and Mom/Mario-style non-technical operating manuals.

# Required Sections

- what is installed
- where it lives
- who owns accounts
- monthly cost
- how to run the workflow
- what can be safely changed
- what not to touch
- common failures
- disable and recovery path

# Plain-Language Operator Manual Sections

When the operator is non-technical, use these sections:

- what this system is for
- what to check every day
- what to update every week
- how to handle new students/leads/items
- how to fix or report common problems
- where to ask questions
- what not to touch

If screenshots are unavailable, insert placeholders rather than inventing
visuals.

# Acceptance Checks

The client should be able to demonstrate the main workflow with hands on keyboard.

The operator should know what not to touch and where to ask questions between
check-ins.

# Fixture

- Mom / Mario pickleball admin handoff:
  `practice-os/fixtures/business-brain/mom-mario-operator-handoff.md`
