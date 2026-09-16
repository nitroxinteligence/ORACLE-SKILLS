---
id: especialista-codigo-matt-pocock
type: index
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
source: https://github.com/mattpocock/skills
source_commit: 959a8e9f1edc3adbe2f7e3054bb6fbefa6696260
---

# Matt Pocock

Especialista digital do departamento **Código**.

Coleção oficial completa com 25 skills para engenharia de software assistida por agentes.

## Começando

- [[01-getting-started/setup-matt-pocock-skills/SKILL|setup-matt-pocock-skills]] — Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.
- [[01-getting-started/ask-matt/SKILL|ask-matt]] — Ask which skill or flow fits your situation. A router over the skills in this repo.

## Fluxo principal

- [[02-main-flow/grill-with-docs/SKILL|grill-with-docs]] — A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
- [[02-main-flow/to-spec/SKILL|to-spec]] — Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed.
- [[02-main-flow/to-tickets/SKILL|to-tickets]] — Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker).
- [[02-main-flow/implement/SKILL|implement]] — Implement a piece of work based on a spec or set of tickets.
- [[02-main-flow/code-review/SKILL|code-review]] — Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\".

## Definição e exploração

- [[03-shaping/wayfinder/SKILL|wayfinder]] — Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear.
- [[03-shaping/prototype/SKILL|prototype]] — Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like.
- [[03-shaping/research/SKILL|research]] — Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.

## Manutenção

- [[04-upkeep/improve-codebase-architecture/SKILL|improve-codebase-architecture]] — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- [[04-upkeep/diagnosing-bugs/SKILL|diagnosing-bugs]] — Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
- [[04-upkeep/resolving-merge-conflicts/SKILL|resolving-merge-conflicts]] — Use when you need to resolve an in-progress git merge/rebase conflict.
- [[04-upkeep/triage/SKILL|triage]] — Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs.
- [[04-upkeep/wizard/SKILL|wizard]] — Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover. Don't invoke this for steps the agent can perform itself.

## Produtividade

- [[05-productivity/grill-me/SKILL|grill-me]] — A relentless interview to sharpen a plan or design.
- [[05-productivity/handoff/SKILL|handoff]] — Compact the current conversation into a handoff document for another agent to pick up.
- [[05-productivity/to-questionnaire/SKILL|to-questionnaire]] — Turn a decision you can't fully answer into a questionnaire for someone else to fill in.
- [[05-productivity/teach/SKILL|teach]] — Teach the user a new skill or concept, within this workspace.
- [[05-productivity/wait-what/SKILL|wait-what]] — Stop. That last message did not land: re-pitch it.
- [[05-productivity/writing-for-agents/SKILL|writing-for-agents]] — Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.

## Referências

- [[06-reference/codebase-design/SKILL|codebase-design]] — Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary.
- [[06-reference/domain-modeling/SKILL|domain-modeling]] — Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.
- [[06-reference/grilling/SKILL|grilling]] — Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
- [[06-reference/tdd/SKILL|tdd]] — Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.

## Documentação de origem

- [[README-ORIGEM|README oficial]]
- [[CHANGELOG-ORIGEM|Changelog oficial]]
- [AI Hero Skills](https://www.aihero.dev/skills)
- [GitHub](https://github.com/mattpocock/skills)
- Commit instalado: 959a8e9f1edc3adbe2f7e3054bb6fbefa6696260

## Escopo

- Incluídas: 25 skills oficiais exibidas no catálogo AI Hero.
- Não incluídas: pastas experimentais in-progress e utilitários misc, que não pertencem ao catálogo oficial.
- Compatibilidade Oracle/Codex: os campos upstream disable-model-invocation e argument-hint foram removidos das skills que os utilizavam; todas as demais instruções e arquivos foram preservados.
