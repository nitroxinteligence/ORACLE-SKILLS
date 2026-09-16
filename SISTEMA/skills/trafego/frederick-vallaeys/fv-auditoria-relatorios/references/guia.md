---
id: "fv-auditoria-relatorios-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://pypi.org/project/meta-ads/", "https://support.google.com/adspolicy/answer/6169371?hl=en"]
confidence: "medium"
review_after: "2026-10-16"
---
# Auditoria e relatórios de campanhas — guia

## Protocolo de cobertura
Registre conta e filtros, paginação, período, campos, falhas e número de recursos examinados. Um relatório de sete dias não inspecionou todo o histórico. Quando API retorna erro ou linha não aplicável, mantenha o campo indisponível em vez de preenchê-lo com zero.

## Cálculos e interpretação
Calcule taxas somente com denominador definido e não nulo; explicite unidade. Não comparar CPC de cliques diferentes sem dizer a definição. Preserve dados da plataforma separados de conversões confirmadas por outra fonte. Para dados com atraso, relatar a data real da extração.

## Estrutura sugerida
Pergunta/escopo → saúde dos dados → observações → hipóteses → decisões sugeridas → lacunas. Uma tabela deve informar período, moeda e origem. Fatos de conta privada não devem entrar numa biblioteca pública reutilizável. O output do usuário fica no projeto autorizado, não dentro da skill compartilhada.

## Auditoria versus operação
Concluir que uma campanha merece revisão não dá autorização para pausar. O operador receberá um diff numa tarefa de mudança. Um pedido de relatório semanal não cria por si só uma rotina permanente neste pacote; se o usuário pedir agenda, usar a ferramenta disponível com consentimento apropriado.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
