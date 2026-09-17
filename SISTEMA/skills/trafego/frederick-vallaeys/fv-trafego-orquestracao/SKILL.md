---
name: oracle-skill-fc19921017708275598b
description: "Inicie a gestão supervisionada de Meta Ads ou Google Ads: resolva contexto, escolha de canal e host, conexão opcional e sequência de análise e execução."
metadata:
  departamento: "trafego"
  especialista: "frederick-vallaeys"
  skill-id: "TRF-FV-CON-01"
  versao: "1.0.0"
  autoria: "engenharia original; inspiração conceitual atribuída"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Gestão de tráfego — iniciar e coordenar

## Entrada
Pedido, contexto autorizado, plataformas de interesse, host e estado atual das integrações.

## Leitura obrigatória
Leia [operação segura](../references/operacao-segura.md) e [guia específico](references/guia.md). Consulte [entrevista](../references/entrevista.md) para lacunas e [autoria](../references/autoria.md) para atribuição. Não carregue referências sem pertinência nem afirme leitura integral quando usou um trecho.

## Procedimento
1. Identifique o objetivo e a entrega; leia o contexto disponível e marque cobertura e conflitos antes de entrevistar.
2. Separe escolha da plataforma de anúncios da escolha do host. Uma conta no ChatGPT não substitui uma conta Meta/Google nem aprova um servidor externo.
3. Use entrevista para resolver somente lacunas de negócio, tracking, conta, verba, período e aprovação. Sem conexão, aceite exports e indique suas datas.
4. Encaminhe Meta à conexão oficial CLI ou à verificação do MCP disponível na conta; Google à leitura pelo MCP oficial e escrita por rota comprovada separada.
5. Após consulta mínima, confirme identidade da conta, moeda, fuso e acesso. Classifique o restante como análise, plano, rascunho ou mutação.
6. Peça aprovação do diff concreto antes de alterar a plataforma. Aplique só o que foi aprovado e encaminhe a mensuração/relatório para fechar o ciclo.
7. Entregue mapa de etapas, arquivos, testes reais, limites e pendências. Não crie automação recorrente nem nova assinatura por padrão.

## Perguntas por lacunas
Qual plataforma: Meta, Google, ambas ou arquivos? Qual host? Quer diagnóstico, plano ou operação aprovada?

## Saída
Brief, plataforma/host escolhidos, rota de integração, estado verificável e próximos passos executáveis ou bloqueados.

## Erro crítico
Tratar “gerir campanhas” como aprovação genérica de gastos ou afirmar conexão por existir um arquivo.

## Aceitação
O entregável deve resolver o escopo pedido e registrar fatos/fontes, estado, ações realmente executadas, incertezas e autorizações. O guia contém casos e recuperação. Um checklist preenchido não prova eficácia, conformidade ou conexão. Não há publicação nem gasto implícitos.

## Referências
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Automation Layering — painel de 2022](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)

Procedimento original com orientação conceitual de supervisão, não método técnico oficial de Frederick Vallaeys. Fontes externas podem mudar; verifique versão, identidade e schema antes da ação.
