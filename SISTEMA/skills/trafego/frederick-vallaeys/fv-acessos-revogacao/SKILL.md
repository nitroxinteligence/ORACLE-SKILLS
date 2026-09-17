---
name: oracle-skill-201031e953170e95c799
description: "Revise permissões e ajude a desconectar integrações Meta/Google sem expor segredos, alterar campanhas ou sobrescrever configurações não relacionadas."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-12"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Acessos, manutenção e revogação

## Entrada
Inventário de integrações, aliases, responsáveis e pedido de manutenção/revogação.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Identifique fornecedor, host, conta e credencial por alias; não leia nem imprima valores.
2. Separe desabilitar ferramentas locais, interromper rotinas e revogar grants/tokens na origem.
3. Explique efeitos e dependências; cancelar acesso não pausa campanhas publicadas nem apaga dados remotos.
4. Com autorização, desabilite somente o bloco alvo no host, preservando demais servidores e projetos.
5. Oriente o humano a revogar OAuth/token/integração no painel oficial; confirme resultado por estado, não pela exposição da credencial.
6. Verifique chamadas futuras bloqueadas e jobs conhecidos reconciliados, sem provocar uma mutação de campanha como teste.
7. Entregue recibo de revogação, dados/retencão pendentes e plano de atualização futura; não reinstale ou reautorize automaticamente.

## Perguntas por lacunas
Qual conexão precisa parar? Existem jobs/rotinas dependentes? Deseja só desabilitar o host ou revogar também o acesso na origem?

## Saída
Inventário sanitizado, etapas autorizadas, estado de revogação e dependências não resolvidas.

## Erro crítico
Afirmar que apagar config local revogou token remoto ou que desconectar parou os anúncios.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Repositório oficial Google Ads MCP](https://github.com/googleads/google-ads-mcp)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
