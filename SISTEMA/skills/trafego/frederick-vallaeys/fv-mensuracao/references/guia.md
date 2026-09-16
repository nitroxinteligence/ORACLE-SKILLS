---
id: "fv-mensuracao-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://pypi.org/project/meta-ads/", "https://support.google.com/adspolicy/answer/6169371?hl=en", "https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/"]
confidence: "medium"
review_after: "2026-10-16"
---
# Mensuração e qualidade de dados — guia

## Diagnóstico em camadas
Primeiro confirmar o que foi medido; depois como foi atribuído; só então decidir orçamento. Use conta e período exatos e documente moeda/fuso. Não confundir view, clique, lead bruto, lead qualificado, venda e receita líquida. Ausência de coluna ou erro de API é desconhecido, não zero.

## Reconciliação
Compare fontes em nível compatível e preserve a origem de cada métrica. Reconciliar não significa forçar os totais a coincidir: há janelas diferentes, consentimento, modelagem e atraso. Dados Ads e dados CRM podem responder perguntas distintas. Não remover discrepância do relatório só porque prejudica uma tese.

## Teste técnico proposto
Definir evento sintético, pré-condições, número limitado de tentativas, destino de teste e critério de sucesso. Identificar qualquer chamada externa ou alteração de tag. Pedir aprovação antes de implementar. Evitar produzir conversões artificiais em produção para demonstrar performance. Verificar que testes não serão confundidos com resultados comerciais.

## Saída e decisão
Uma hipótese de tracking quebrado não justifica automaticamente pausar toda a conta. Especificar quais decisões dependem da correção e quais análises permanecem válidas. Conectar uma fonte agregada pode bastar; não exigir CRM completo, dados financeiros individuais ou export irrestrito para responder uma pergunta pequena.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [Automation Layering — painel de 2022](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
