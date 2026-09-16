---
id: "fv-google-conectar-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://github.com/googleads/google-ads-mcp", "https://developers.google.com/google-ads/api/docs/api-policy/developer-token", "https://learn.chatgpt.com/docs/extend/mcp?surface=cli", "https://support.google.com/adspolicy/answer/6169371?hl=en"]
confidence: "medium"
review_after: "2026-10-16"
---
# Google Ads — conectar leitura oficial — guia

## Mudança de acesso em setembro de 2026
O guia de migração informa sunset dos developer tokens em 09/09/2026; o anúncio publicado em 10/09 descreve o início do rollout. As datas são de fontes distintas, não devem ser fundidas. O corpo do guia atual associa o nível de acesso ao projeto dono das credenciais OAuth/conta de serviço e declara tokens antigos opcionais/ignorados. O resumo automático da própria página ainda contém instruções antigas. Use o corpo atual, confira a conta e registre divergências. A exceção documentada para App Conversion Tracking API não torna token obrigatório para esta integração Google Ads.

## Preparação pelo usuário
1. Abra Google Cloud Console, selecione o projeto que será dono das credenciais e confira Google Ads API Overview e o nível de acesso. Novo cadastro não depende de criar MCC só para obter token.
2. Habilite/solicite apenas o acesso adequado. Explorer/Basic/Standard e brand verification têm requisitos próprios; aprovação não é instantânea garantida para todo caso.
3. Configure cliente OAuth e consentimento apropriados ao uso. Guarde o JSON de cliente num diretório privado, fora do vault. A pessoa conclui o fluxo em navegador oficial.
4. Use ADC ou a forma suportada na versão do servidor. Escopo Ads é `https://www.googleapis.com/auth/adwords`; outros escopos somente quando o caminho escolhido realmente precisar deles. A conta autenticada precisa também de acesso à conta de anúncios.
5. Registre apenas project ID, customer ID e eventual login customer ID. O guia apresenta uma ambiguidade “Project ID / project number”; o README/config usa `GOOGLE_PROJECT_ID`. Confira o identificador aceito pela versão, sem substituir pelo customer ID.

## Configuração local proposta
Pin observado, não instalado: `7a40eae9655194a84d5291c63af817bb20d02ea8`.
```toml
[mcp_servers.google_ads_readonly]
command = "pipx"
args = ["run", "--spec", "git+https://github.com/googleads/google-ads-mcp.git@7a40eae9655194a84d5291c63af817bb20d02ea8", "google-ads-mcp"]
env_vars = ["GOOGLE_PROJECT_ID", "GOOGLE_APPLICATION_CREDENTIALS", "GOOGLE_ADS_LOGIN_CUSTOMER_ID"]
enabled = false
default_tools_approval_mode = "prompt"
```
O caminho de ADC pode ser dispensável quando sua resolução padrão já funciona; MCC só quando aplicável. A configuração é exemplo do host atual, não arquivo instalado. `pipx run` pode buscar dependências quando habilitado; aprove e revise esse efeito. Não rode instalação como efeito colateral de ler a skill. Remova campos desnecessários após verificar o caso.

## Teste e erros
Descobrir `list_accessible_customers`, `search`, `get_resource_metadata`, considerando prefixos configuráveis. Listagem de contas diretamente acessíveis não deve ser assumida como enumeração completa de todos os clientes MCC. Consulte a hierarquia apenas se necessário e autorizado. Comece com `customer.id`, `customer.currency_code` e `customer.time_zone`, conferindo campos por metadata.

`CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION`: conferir projeto/nível, não ampliar escopos a esmo. ADC ausente: humano reautoriza. Campo GAQL incompatível: use metadata da versão. Conta sem acesso: corrigir vínculo, não trocar silenciosamente para outra conta. O guia registra problemas temporários de rollout; não desative billing nem faça upgrade pago como “correção automática”.

## ChatGPT web
Um servidor stdio local não fica acessível ao ChatGPT web. Uma implantação própria remota precisa de arquitetura autorizada com OAuth, TLS, tokens protegidos e projeto/acesso apropriados. Ingress público não deve ser confundido com ferramenta sem autenticação; não copie `--allow-unauthenticated` ou segredos inline de exemplos sem entender o proxy OAuth. Esta tarefa entrega a documentação, não um servidor hospedado.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Guia oficial Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Repositório oficial Google Ads MCP](https://github.com/googleads/google-ads-mcp)
- [Migração do developer token](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
