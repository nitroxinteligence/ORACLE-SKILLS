---
id: "fv-indice-conectado"
type: "index"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: "2026-10-16"
---
# Tráfego conectado — biblioteca adicional

Comece pela orquestração quando houver várias etapas ou pela skill específica quando o pedido já estiver definido. A biblioteca contém procedimentos; instalar arquivos no vault não registra MCP nem concede acesso ao host.

- [fv-trafego-orquestracao](./fv-trafego-orquestracao/SKILL.md) — [guia](./fv-trafego-orquestracao/references/guia.md)
- [fv-trafego-entrevista](./fv-trafego-entrevista/SKILL.md) — [guia](./fv-trafego-entrevista/references/guia.md)
- [fv-meta-conectar](./fv-meta-conectar/SKILL.md) — [guia](./fv-meta-conectar/references/guia.md)
- [fv-meta-operar](./fv-meta-operar/SKILL.md) — [guia](./fv-meta-operar/references/guia.md)
- [fv-google-conectar](./fv-google-conectar/SKILL.md) — [guia](./fv-google-conectar/references/guia.md)
- [fv-google-operar](./fv-google-operar/SKILL.md) — [guia](./fv-google-operar/references/guia.md)
- [fv-conector-terceiros](./fv-conector-terceiros/SKILL.md) — [guia](./fv-conector-terceiros/references/guia.md)
- [fv-mensuracao](./fv-mensuracao/SKILL.md) — [guia](./fv-mensuracao/references/guia.md)
- [fv-otimizacao](./fv-otimizacao/SKILL.md) — [guia](./fv-otimizacao/references/guia.md)
- [fv-criativos-handoff](./fv-criativos-handoff/SKILL.md) — [guia](./fv-criativos-handoff/references/guia.md)
- [fv-auditoria-relatorios](./fv-auditoria-relatorios/SKILL.md) — [guia](./fv-auditoria-relatorios/references/guia.md)
- [fv-acessos-revogacao](./fv-acessos-revogacao/SKILL.md) — [guia](./fv-acessos-revogacao/references/guia.md)

## Recursos compartilhados
[Operação segura](references/operacao-segura.md) · [Entrevista](references/entrevista.md) · [Fontes e limites](references/fontes.md) · [Papéis](agents/indice.md) · [Configuração proposta](templates/mcp-proposta.toml)

## Estado de implementação
Criadas skills e recursos no OS. Não foram instalados editores, CLIs ou servidores; não houve OAuth, leitura de contas, alteração de campanhas, render ou publicação. O host precisa de descoberta real e um teste autorizado antes da operação. Os auxiliares de teste avaliam dados sintéticos, não impõem controles às ferramentas externas.

[Matriz de integração](docs/matriz-integracoes.md) · [Uso e validação](docs/uso-e-validacao.md)

As três skills anteriores (`ad-creative`, `ads-plan`, `ads-test`) foram preservadas. [Índice anterior](indice.md).
