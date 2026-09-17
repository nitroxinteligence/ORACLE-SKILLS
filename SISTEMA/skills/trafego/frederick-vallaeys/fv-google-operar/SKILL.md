---
name: oracle-skill-1f5e70b1d968c7cbbddb
description: "Prepare e execute mutações Google Ads por API oficial ou executor explicitamente aprovado. Não tenta escrever pelo MCP oficial somente leitura."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-06"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Google Ads — alterações pela API sob aprovação

## Entrada
Conta/projeto verificados, leitura atual, executor de escrita, objetivo e diff a aprovar.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Use os dados da leitura oficial para identificar conta, versão da API, moeda, fuso e recursos afetados.
2. Confirme executor de escrita e seu uso permitido. Se só houver o MCP oficial, entregue o plano e declare a escrita indisponível.
3. Prepare mutate_operations compatíveis, máscaras de atualização, dependências e valores em unidades documentadas. Crie novos recursos pausados quando suportado.
4. Monte diff e rollback com pré-condições e aprovação versionada. Valide quando suportado com validate_only=true, sem interpretar validação como execução.
5. Após aprovação para escrita, confirme estado anterior ainda atual e execute lote mínimo; escolha conscientemente transação ou partial_failure.
6. Leia recursos de volta, registre request ID e resultados por operação. Em falha parcial ou timeout, reconciliar estado antes de qualquer nova escrita.
7. Aplique ativação/gasto somente se incluídos no escopo aprovado; entregue relatório de mudanças e limites, preservando campanhas fora do plano.

## Perguntas por lacunas
Qual mudança exata? Qual ferramenta comprovada pode executá-la? A autorização cobre teste, criação pausada ou ativação?

## Saída
Plano, validação quando realmente executada, aprovação, resultados individuais, leitura de confirmação e recuperação.

## Erro crítico
Afirmar que validate_only alterou recursos ou que um lote partial_failure é atômico.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [MutateGoogleAdsRequest v25](https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest)
- [SDK oficial Google Ads Python](https://github.com/googleads/google-ads-python)
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
