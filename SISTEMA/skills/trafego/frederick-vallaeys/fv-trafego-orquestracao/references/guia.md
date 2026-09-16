---
id: "fv-trafego-orquestracao-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://pypi.org/project/meta-ads/", "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://learn.chatgpt.com/docs/extend/mcp?surface=cli", "https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/"]
confidence: "medium"
review_after: "2026-10-16"
---
# Gestão de tráfego — iniciar e coordenar — guia

## Árvore operacional
Comece perguntando a plataforma apenas quando não estiver definida. “Meta Ads” é o destino; “Codex no Mac” é o executor; “CLI oficial” é o mecanismo. São escolhas diferentes. Para duas plataformas, mantenha contas, credenciais e autorização separadas.

Se há apenas necessidade de planejamento, não instale nada. Se há exports, registre cobertura e data sem presumir acesso vivo. Se é necessária leitura contínua, apresente os pré-requisitos da rota correspondente. Uma conta não autorizada permanece bloqueada; prossiga com trabalho independente que não precisa dela.

## Roteamento
- Contexto faltante: `fv-trafego-entrevista`.
- Meta: `fv-meta-conectar`, depois `fv-meta-operar`.
- Google: `fv-google-conectar`; `fv-google-operar` só com executor de escrita comprovado.
- Fornecedor remoto: `fv-conector-terceiros`, sem pressupor que sua arquitetura está em conformidade.
- Qualidade de dados: `fv-mensuracao`; decisão de mudança: `fv-otimizacao`.
- Produção de anúncios: `fv-criativos-handoff`; prestação de contas: `fv-auditoria-relatorios`.

## Exemplo de abertura
“Vou usar o contexto já autorizado para entender objetivo e capacidade. Você pretende Meta Ads, Google Ads, ambos ou somente analisar arquivos? E vai operar no ChatGPT web, Desktop/Work ou Codex local?” Não repita alternativas que o usuário já escolheu.

## Critério de passagem
O plano precisa dizer o que pode ser feito agora, o que exige autorização humana e o que ainda não está tecnicamente disponível. A limitação do MCP oficial Google não deve aparecer só no fim: deve mudar o roteamento desde o início.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Automation Layering — painel de 2022](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
