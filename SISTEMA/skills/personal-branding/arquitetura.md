---
id: "pb-00-sistema-skills-personal-branding-arquitetura"
type: "playbook"
status: "active"
area: "marca"
created: "2026-09-05"
updated: "2026-09-08"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: null
---
<!-- Modified for Oracle distribution; exact input/output digests and reasons are in the signed distribution manifest. -->
# Arquitetura e responsabilidades

| Camada | Responsável | Entrada → saída |
|---|---|---|
| Coordenação | personal-branding | Pedido/contexto → recomendação ou brief |
| Conhecimento | rory-vaden-personal-branding + Rory Vaden no OS | Pergunta → modelo, fontes, limites |
| Identidade | strategy + brand-voice | Provas/amostras → posicionamento proposto e voz |
| Editorial | mats-ia-media-company e módulos existentes | Brief → peças e revisão |
| Estado | Action Planner do projeto | Tarefa → estado verificável |

Papéis podem ser executados sequencialmente pela sessão ou delegados quando autorizado e útil. Não foram criados serviços autônomos, agendas nem um novo conjunto duplicado de agentes.

Acrescente ao handoff existente: `expert_consultation: {expert, corpus_version, model, source_ids, application, limits}`. A consulta deve influenciar uma decisão explícita, inclusive a decisão fundamentada de não aplicar o modelo.

[[SISTEMA/skills/personal-branding/README]] · WIKI/especialistas/rory-vaden/README (recurso externo: WIKI/especialistas/rory-vaden/README; não incluído nesta distribuição) · [[catalogo]]
