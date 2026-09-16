---
name: fv-meta-conectar
description: "Prepare conexão opcional do host com Meta Ads, preferindo a CLI oficial verificável e validando qualquer MCP escolhido. Não modifica campanhas."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-03"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
# Meta Ads — conexão oficial e permissões

## Entrada
Host/sistema, conta-alvo, autorização para preparação, versão do Python e escolha entre CLI e MCP.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Leia o guia e verifique pacote/fornecedor e compatibilidade real antes de instalar. A CLI documentada chama-se meta; um projeto com nome parecido não é o mesmo software.
2. Peça autorização para instalação isolada, quando necessária; mostre versão e efeitos. Não leia nem altere outras integrações.
3. Instrua o humano a configurar autenticação oficial e permissões necessárias à conta. Nunca receba senha/token; registre somente mecanismo e alias fora do vault.
4. Confira o executável e seu --help. Use ACCESS_TOKEN e AD_ACCOUNT_ID pelo mecanismo privado escolhido, sem imprimir env nem habilitar debug.
5. Faça somente consulta mínima de conta/campanhas. Confira conta pretendida, moeda, fuso e capacidades observadas antes de ampliar o acesso.
6. Para MCP, confirme URL, titular, autenticação, escopos e ferramentas a partir da documentação oficial acessível à conta. Não invente endpoint de configuração quando essa prova falta.
7. Registre recibo de leitura ou erro e a revogação. Encaminhe escrita à skill operacional com aprovação distinta.

## Perguntas por lacunas
A conta é própria ou de cliente autorizado? O host tem terminal local? Qual nível de acesso é necessário? Você consegue concluir o login em ambiente privado?

## Saída
Configuração proposta sem segredos, pré-requisitos, consulta somente leitura e recibo com estados separados.

## Erro crítico
Colar token no Obsidian/chat, instalar pacote homônimo ou criar campanha como teste de conexão.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [SDK oficial Meta](https://github.com/facebook/facebook-python-business-sdk)
- [Ajuda oficial Meta — acesso condicionado ao login](https://www.facebook.com/business/help/1456422242197840)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
