---
name: oracle-skill-78334d2522895b26dbe8
description: "Audite definição de conversão, tracking, atribuição e qualidade dos dados antes de otimizar mídia. Produz plano de teste sem instalar tags ou enviar listas automaticamente."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-08"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Mensuração e qualidade de dados

## Entrada
Objetivo econômico, eventos, exports ou leituras autorizadas e dados agregados de qualidade de leads/vendas.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Mapeie objetivo de negócio para evento observável e diferencie conversão da plataforma e resultado confirmado.
2. Inventarie eventos, nomes, timezone, moeda, valor e janela de atribuição; marque não disponíveis.
3. Compare amostras agregadas e reconcilie divergências sem enviar dados pessoais a terceiros.
4. Desenhe teste com eventos sintéticos e ambiente apropriado; instalar tags ou enviar conversões exige autorização própria.
5. Verifique duplicação, exclusões, atraso, consentimento e falhas de captura; separar problema técnico de baixa performance.
6. Defina baseline e limites para interpretar experimentos. Não atribua causalidade a diferenças brutas de ROAS.
7. Entregue mapa, evidências, falhas e plano de correção não executado ou recibo específico quando houve teste autorizado.

## Perguntas por lacunas
Qual evento importa? Está duplicado ou atrasado? Qual janela e origem dos dados? Há autorização para investigar o tracking?

## Saída
Mapa evento→negócio, fontes, qualidade de dados, limitações e plano de teste mensurável.

## Erro crítico
Otimizar com conversões inventadas ou tratar soma de atribuições de plataformas como receita única.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [Automation Layering — painel de 2022](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
