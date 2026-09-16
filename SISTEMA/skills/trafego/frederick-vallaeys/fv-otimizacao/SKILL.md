---
name: fv-otimizacao
description: "Transforme dados confiáveis em hipóteses e experimentos de mídia, com limites, diff e aprovação antes de executar alterações."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-09"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
# Otimização supervisionada e experimentos

## Entrada
Brief, dados com definição/janela, baseline, orçamento e histórico de alterações.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Verifique qualidade e comparabilidade dos dados antes de concluir que há ganho ou perda.
2. Identifique o principal gargalo com evidência; separe observação, hipótese e ação proposta.
3. Escolha mudança mínima que teste a hipótese e preserve variáveis importantes. Evite muitas mudanças simultâneas sem justificativa.
4. Defina métrica primária, guardrails, janela, atraso esperado, capacidade de amostra e condição de parada.
5. Prepare diff e limite para execução; reutilize autorização válida somente dentro do escopo já aprovado.
6. Encaminhe escrita à skill da plataforma e verifique o resultado. Um relatório que sugere pausa não pode dizer que pausou.
7. Leia o experimento com incerteza e registre aprendizados. Não invente significância ou um vencedor quando a amostra não resolve a pergunta.

## Perguntas por lacunas
Que hipótese estamos testando? Qual evidência a refutaria? Quais custos, duração e mudanças são autorizados?

## Saída
Hipótese, plano de experimento, diff e decisão fundamentada com resultados reais ou status não executado.

## Erro crítico
Aplicar recomendações automáticas em massa ou prometer retorno garantido por uma regra de orçamento.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Automation Layering — painel de 2022](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [MutateGoogleAdsRequest v25](https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
