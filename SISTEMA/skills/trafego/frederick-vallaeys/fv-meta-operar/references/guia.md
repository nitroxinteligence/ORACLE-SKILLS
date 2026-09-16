---
id: "fv-meta-operar-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://pypi.org/project/meta-ads/", "https://github.com/facebook/facebook-python-business-sdk", "https://learn.chatgpt.com/docs/extend/mcp?surface=cli"]
confidence: "medium"
review_after: "2026-10-16"
---
# Meta Ads — operar campanhas sob aprovação — guia

## Cobertura não é onipotência
O catálogo da CLI contém grupos para campanhas, conjuntos, anúncios, criativos, catálogos, datasets e insights. A disponibilidade real depende de conta, escopos, versão e campos. Não prometa “toda a Meta” como uma operação universal. Um objeto não suportado deve permanecer plano, ou ser tratado por API/interface oficial em tarefa específica.

## Plano antes da escrita
O template `../../templates/diff-campanha.json` guarda IDs, valores, datas e aprovação. Para uma criação, liste dependências na ordem correta e o que acontecerá se uma etapa falhar. Para uma edição, capture o valor atual; diferenças posteriores indicam alteração concorrente e invalidam a suposição do plano.

O exemplo público de criação da CLI não informa um status pausado. Não o execute como tutorial de conexão. Descubra o parâmetro de status em `meta ads campaign create --help` e equivalentes dos níveis seguintes. Se não houver forma demonstrada de criar de maneira segura, pare no plano ou escolha a API documentada; não invente uma flag.

## Ativação e recuperação
Inspecione campanha, conjunto e anúncio; um nível ativo com outro pausado não equivale à intenção aprovada. Antes de ativar, confirme limites totais/diários, período, moeda, público, destino e evento. Uma alteração no plano exige nova aprovação do diff, não repetir todas as perguntas do onboarding.

Se o retorno for incerto, use a consulta pelo ID já retornado ou por identificador inequívoco do plano. Nunca assumir sucesso pelo HTTP sozinho. Pausar recursos é uma ação externa: use autorização específica ou regra de emergência explicitamente preautorizada. Gasto já ocorrido não pode ser desfeito por um rollback técnico.

## Teste recomendado para futura conexão
Em conta de teste ou escopo autorizado, listar campanhas e preparar uma criação pausada sem executá-la; conferir unidades e parâmetros. A criação pausada e leitura posterior são uma segunda etapa autorizada. Registrar qual caminho foi realmente exercitado.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

A consulta pública aos padrões de anúncios Meta retornou erro 429. Antes de lançar uma campanha, confira a política Meta vigente e aplicável ao anúncio; este guia não certifica sua conformidade. As regras do Google não substituem as da Meta.

- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [SDK oficial Meta](https://github.com/facebook/facebook-python-business-sdk)
- [MCP no ChatGPT/Codex — configuração e aprovação](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
