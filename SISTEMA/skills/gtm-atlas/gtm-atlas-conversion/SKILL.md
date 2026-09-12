---
name: oracle-skill-ae65c3eca0040b1e6238
description: Design conversion motions that combine AI agents with human sales judgment. Use when deciding what an agent should own, defining agent playbooks and knowledge, detecting user attachment, mapping champions and decision-makers, or routing accounts by conversion potential.
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->

# GTM Atlas Conversion

Use AI to own bounded parts of the motion end to end when it has the playbook, knowledge, and data to act reliably. Route human attention through attachment, urgency, and buying-role evidence.

## Workflow

1. Define the conversion outcome and every decision required to reach it.
2. Classify each decision as agent-owned, human-owned, or approval-gated based on ambiguity, relationship depth, risk, and available context.
3. Give the agent three foundations: a natural-language playbook with goals and boundaries; current product, pricing, and competitive knowledge; and bidirectional access to the relevant research and CRM context.
4. Define handoff conditions before deployment. Preserve conversation context and record actions so the human does not rebuild the relationship.
5. Identify attachment signals: repeated use, workflow dependency, collaboration, qualitative advocacy, and urgency. Prefer a few interpretable signals over a dense score.
6. Map the champion, economic buyer, technical evaluator, procurement roles, and potential blockers. Do not assume the most active user controls the decision.
7. Allocate effort by attachment, urgency, revenue potential, and account complexity. A small deeply attached team may deserve more attention than a large shallow deployment.
8. Review old metrics after automation. If the agent changes the process, redesign measurement around customer outcomes and clean escalations.

## Guardrails

- Do not automate relationship-heavy discovery merely because generation is possible.
- Ground claims in approved knowledge and expose uncertainty.
- Keep a human path for exceptions, commitments, sensitive topics, and high-value decisions.
- Measure conversion quality, retention, and customer trust alongside speed or containment.

## Output

Return: ownership matrix, agent brief, knowledge requirements, data flows, handoff rules, attachment signals, buying committee map, routing logic, metrics, and failure controls.

Source basis: [Let AI own, not assist](https://atlas.attio.com/let-ai-own-not-assist) and [Attachment is the signal](https://atlas.attio.com/attachment-is-the-signal).
