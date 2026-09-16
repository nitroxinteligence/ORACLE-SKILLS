---
name: fv-auditoria-relatorios
description: "Analise campanhas Meta/Google a partir de leituras ou exports autorizados, com cobertura, atribuição, limitações e recomendações não executadas."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-11"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
# Auditoria e relatórios de campanhas

## Entrada
Conta(s), período, perguntas de negócio, fontes e escopo de leitura.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Fixe conta, janela, moeda e timezone; descubra os campos disponíveis e controle paginação/cobertura.
2. Colete apenas dados necessários em leitura; exports antigos não representam estado atual sem qualificação.
3. Verifique totais, duplicatas, linhas ausentes, erros e limitação de granularidade antes de calcular taxas.
4. Separe Meta e Google e explique diferenças de definição/atribuição. Não somar receita como se fosse deduplicada.
5. Apresente observações sustentadas e hipóteses com incerteza; use baseline pertinente, não benchmarks inventados.
6. Priorize recomendações por evidência e esforço; escreva explicitamente que nenhuma foi executada quando o trabalho foi somente leitura.
7. Entregue relatório com fontes, cobertura, lacunas, timestamp e próximos testes. Recorrência só mediante solicitação e ferramenta real.

## Perguntas por lacunas
Qual decisão o relatório deve apoiar? Quais datas/fontes são comparáveis? Que detalhe realmente é necessário?

## Saída
Relatório rastreável com dados por fonte, comparações válidas, hipóteses e propostas distintas do realizado.

## Erro crítico
Apresentar snapshot parcial como auditoria integral ou erro de acesso como zero gasto/conversão.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
