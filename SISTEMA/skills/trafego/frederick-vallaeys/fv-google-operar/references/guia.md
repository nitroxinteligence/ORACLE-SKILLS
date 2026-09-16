---
id: "fv-google-operar-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest", "https://github.com/googleads/google-ads-python", "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://support.google.com/adspolicy/answer/6169371?hl=en"]
confidence: "medium"
review_after: "2026-10-16"
---
# Google Ads — alterações pela API sob aprovação — guia

## Opções de executor
O SDK `google-ads` do repositório oficial fornece clientes da API; ele não é um MCP de escrita pronto. Uma implementação local precisa usar versão compatível, credenciais do próprio projeto e métodos oficiais. Não instalar uma biblioteca faz parte de uma consulta documental. Se o executor não existe, entregar payload/plano auditável e marcar operação não executada.

Um conector externo pode oferecer escrita, mas a política atual do Google restringe proxies programáticos e acesso compartilhado que contorna projeto/identidade de cada entidade. Não usar “funcionou com OAuth” como certificação de conformidade. Avalie o fluxo com `fv-conector-terceiros` antes de recomendar esse caminho para Google.

## Contrato da mutação
`customer_id` identifica a conta afetada; `mutate_operations` lista mudanças. No contrato v25 lido, `validate_only=true` valida sem executar. Com `partial_failure=false`, as operações daquele request são transacionais quando todas válidas; isto não torna uma sequência de vários requests atômica. Com `partial_failure=true`, sucessos podem ser gravados enquanto outras operações falham. Escolha com base nas dependências do plano, não numa suposta preferência universal.

## Exemplo de execução controlada
Caso sintético: atualizar o nome de uma campanha de teste pausada. Obter resource name e nome anterior; gerar operação e field mask somente para o nome; validar; apresentar diff; obter aprovação; executar; consultar novamente. Um teste de nome não comprova uma jornada completa de campanha Search/PMax/Shopping. Não generalize o resultado a todos os recursos.

## Orçamento e medição
Converter unidades explicitamente e rejeitar moeda/desenho de período ambíguos. Um orçamento diário não é um teto de gasto total da campanha. Verifique regras vigentes do produto e apresente os limites reais; não confunda limite interno do plano com enforcement técnico da plataforma. Para alterar campanha existente, examine orçamento compartilhado e recursos vinculados antes de calcular o impacto.

## Falhas
Não repetir erro de validação sem modificar a causa. Reconciliar resultados parciais por índice/ID. Se alguém alterou o mesmo objeto, renovar o diff; rollback antigo poderia sobrescrever o trabalho dessa pessoa. Revogar a autorização do plano cancela futuras ações, não desfaz gasto ou mutações anteriores.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [MutateGoogleAdsRequest v25](https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest)
- [SDK oficial Google Ads Python](https://github.com/googleads/google-ads-python)
- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
