---
name: fv-google-conectar
description: "Configure o MCP oficial Google Ads para consultas autorizadas, com projeto Cloud, OAuth e teste somente leitura. Distingue o acesso atual das instruções antigas de developer token."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-05"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
# Google Ads — conectar leitura oficial

## Entrada
Host, projeto Cloud apropriado, conta Google Ads e vínculo MCC quando houver; nenhum segredo no brief.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Verifique documentação atual e a versão escolhida do MCP. Confirme que a entrega inicial é somente leitura.
2. Instrua o humano a verificar o acesso Google Ads API no Google Cloud Console e a vinculação do projeto às credenciais OAuth. Não exigir um novo developer token como regra universal.
3. Conclua consentimento OAuth/ADC privadamente com o usuário. Confirme acesso à conta Ads; permissão no Cloud não concede automaticamente acesso publicitário.
4. Prepare configuração isolada do host. Local pode usar stdio; ChatGPT web requer rota remota suportada e autenticada, não o localhost do Mac.
5. Descubra ferramentas, seus prefixos e schema. Consulte contas acessíveis e selecione explicitamente a conta pretendida; MCC pode exigir login customer ID separado.
6. Execute uma consulta GAQL pequena de identificação/configuração e confirme moeda e timezone. Não usar mutate como teste.
7. Registre conexão de leitura, limites e revogação; encaminhe qualquer escrita para fv-google-operar sem atribuí-la ao MCP oficial.

## Perguntas por lacunas
Qual projeto gera suas credenciais OAuth? Qual conta Ads? Acesso direto ou via MCC? O host é local ou web?

## Saída
Guia e configuração sem segredos, identidade verificada e recibo com três ferramentas de leitura efetivamente descobertas.

## Erro crítico
Confundir projeto Cloud, customer ID e MCC; prometer criação de campanha no MCP oficial read-only.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Repositório oficial Google Ads MCP](https://github.com/googleads/google-ads-mcp)
- [Migração do developer token](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
