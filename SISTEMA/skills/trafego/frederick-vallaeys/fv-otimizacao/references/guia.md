---
id: "fv-otimizacao-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/", "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://pypi.org/project/meta-ads/", "https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest"]
confidence: "medium"
review_after: "2026-10-16"
---
# Otimização supervisionada e experimentos — guia

## Método operacional
Automação de plataforma, supervisão do operador e hipótese de experimento são camadas diferentes. Use ferramentas para detectar onde investigar, não para autorizar toda recomendação de um fornecedor. O painel de Vallaeys fundamenta essa orientação conceitual; os critérios deste pacote são autorais.

## Escolha do teste
Compare grupos/períodos razoavelmente equivalentes e registre limitações de sazonalidade, mudanças simultâneas e composição do público. Testar uma variável não elimina todos os fatores de confusão. Se um teste formal não for viável, relatar a observação como exploratória em vez de fabricar um p-valor.

## Orçamento e parada
Fixar no plano a unidade de orçamento, período e limite autorizado. Mudanças acima desse limite exigem revisão. Uma regra de emergência pode permitir pausa apenas se explicitamente preautorizada para conta/condição determinadas. Não criar um daemon ou agenda de monitoramento por um pedido pontual.

## Memória de aprendizado
Salvar hipótese, evidência, ação, resultado e limites num output derivado. Não reintroduzir esse output como prova independente do fato original. Uma falha isolada não vira lei universal nem justificativa para mudar todas as campanhas.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Automation Layering — painel de 2022](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [MutateGoogleAdsRequest v25](https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
