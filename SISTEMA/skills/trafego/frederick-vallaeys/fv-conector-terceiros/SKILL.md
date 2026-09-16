---
name: fv-conector-terceiros
description: "Compare um MCP hospedado de terceiros com acesso oficial/local; avalie fornecedor, dados, permissões, custos e política antes de conectar."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-07"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
# Conectores de tráfego — avaliação e conexão opcional

## Entrada
Plataforma, host, proposta de fornecedor e autorização de avaliação; acesso à documentação pública.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Compare a necessidade real com a rota oficial. Uma ferramenta remota simples pode acrescentar custos e destinatário de dados.
2. Leia domínio, responsável, transportes, OAuth, política de dados, termos e integração anunciada. Distinga repositório de plugin e backend hospedado.
3. Para Google, verifique projeto por entidade, autenticação direta e restrições a proxies. Não declare um fornecedor aprovado pelo Google sem evidência.
4. Apresente limitações e alternativas ao usuário; conecte somente o fornecedor escolhido e autorizado. Não execute scripts de instalação remotos cegamente.
5. Conclua OAuth pelo humano e selecione contas permitidas. Primeiro descubra ferramentas e faça uma consulta mínima sem mutações.
6. Restrinja recursos à tarefa e exija diffs para escrita. Hints de segurança declarados pelo servidor não provam comportamento.
7. Registre dados compartilhados, custo do serviço versus mídia, estado, limites e revogação. Se diligência falhar, mantenha rota local/oficial ou análise offline.

## Perguntas por lacunas
Você aceita compartilhar dados com um fornecedor adicional? Ele comprova a rota de acesso exigida pela plataforma? Qual custo e escopo aceitáveis?

## Saída
Matriz de decisão, evidências de fornecedor, consentimento de dados e recibo opcional de leitura.

## Erro crítico
Vender um MCP comunitário como oficial ou usar um proxy para evitar acesso próprio exigido pela plataforma.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Adspirer — fornecedor terceiro](https://github.com/amekala/ads-mcp)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
