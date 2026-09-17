---
name: oracle-skill-a33bde9baa0343bcfcf3
description: "Leia, planeje e execute alterações delimitadas em campanhas Meta Ads por uma integração previamente testada. Mantém criação pausada e aprovação de gasto separada."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-04"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Meta Ads — operar campanhas sob aprovação

## Entrada
Recibo de conexão, conta verificada, objetivo, mensuração, ativos e limites aprovados.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Confirme o recibo atual, conta e permissões reais; releia estado, moeda, fuso e objetos-alvo.
2. Valide objetivo, evento, página/identidade, materiais e políticas para o caso. Não fabrique prova ou resultado comercial.
3. Descubra comandos e campos no schema da versão instalada, incluindo unidade monetária e níveis de status. Não copie a sintaxe de outro CLI.
4. Prepare diff de campanha/conjunto/anúncio, antes/depois, custo, período, rollback e estados PAUSED para novos recursos. Solicite aprovação desta versão.
5. Execute uma operação pequena autorizada; capture IDs e retorno sanitizado. Verifique status efetivo na plataforma e pare diante de sucesso parcial inesperado.
6. Ative somente com autorização que inclua gasto e datas. Não transforme “copy aprovada” ou “conexão autorizada” em autorização de lançamento.
7. Em timeout, consulte os IDs/estado antes de repetir. Entregue recibo do realizado e pendências; não deixe recomendações descritas como executadas.

## Perguntas por lacunas
Qual recurso e mudança? Qual orçamento/moeda/período? A aprovação inclui criar pausado ou também ativar?

## Saída
Diff aprovado, IDs e estados verificados, alterações reais, custos conhecidos e registro de recuperação.

## Erro crítico
Executar create de exemplo sem status seguro ou repetir mutação incerta e duplicar campanhas.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [SDK oficial Meta](https://github.com/facebook/facebook-python-business-sdk)
- [MCP no ChatGPT/Codex — configuração e aprovação](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
