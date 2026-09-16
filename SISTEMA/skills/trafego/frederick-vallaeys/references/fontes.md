---
id: "fv-fontes-conectadas"
type: "review"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://pypi.org/project/meta-ads/", "https://github.com/facebook/facebook-python-business-sdk", "https://www.facebook.com/business/news/meta-ads-ai-connectors", "https://www.facebook.com/business/help/1456422242197840", "https://github.com/TheMattBerman/meta-ads-kit", "https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server", "https://github.com/googleads/google-ads-mcp", "https://ads-developers.googleblog.com/", "https://developers.google.com/google-ads/api/docs/api-policy/developer-token", "https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest", "https://github.com/googleads/google-ads-python", "https://support.google.com/adspolicy/answer/6169371?hl=en", "https://github.com/amekala/ads-mcp", "https://learn.chatgpt.com/docs/extend/mcp?surface=cli", "https://learn.chatgpt.com/docs/computer-use", "https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/", "https://www.reddit.com/r/FacebookAds/comments/1szn2mx/meta_just_released_ads_mcp_this_is_where_facebook/", "https://www.reddit.com/r/davinciresolve/comments/1waf7ns/davinci_resolve_211_is_out_now/", "https://www.youtube.com/watch?v=C_m96-Tc3Fs", "https://www.youtube.com/watch?v=dA6DuxffnRo"]
confidence: "medium"
review_after: "2026-10-16"
---
# Fontes, alcance e limitações

Referências anotadas, não cópias integrais nem testemunhos independentes. A ficha informa exatamente o alcance da consulta. Declarações de fornecedor não foram convertidas em testes locais.

## m01 — Meta Ads CLI

Origem: `publisher-package`. [Abrir fonte](https://pypi.org/project/meta-ads/)

**Leitura:** Descrição, comandos, requisitos, licença, mantenedor e wheels.

**Uso:** CLI oficial publicada como meta-ads; executável meta; autenticação por variáveis documentadas.

**Limite:** Binário não instalado, código proprietário não auditado, conta não conectada. Compatibilidade depende do wheel e Python.

**Pin observado:** `1.1.0`. Não comprova instalação.

## m02 — Meta Python Business SDK

Origem: `official-repository`. [Abrir fonte](https://github.com/facebook/facebook-python-business-sdk)

**Leitura:** README e autenticação geral.

**Uso:** SDK oficial como alternativa programática da Marketing API.

**Limite:** Exemplos antigos no README não provam permissões/instaladores atuais. Nenhum request executado.

## m03 — Meta Ads AI connectors

Origem: `official-gated`. [Abrir fonte](https://www.facebook.com/business/news/meta-ads-ai-connectors)

**Leitura:** Acesso redirecionado para login; não lido integralmente.

**Uso:** Pista oficial de conectores; não fundamenta uma configuração completa de MCP.

**Limite:** Endpoint, escopos, região e elegibilidade da conta não confirmados.

## m04 — Ajuda Meta de conectores

Origem: `official-gated`. [Abrir fonte](https://www.facebook.com/business/help/1456422242197840)

**Leitura:** Página pública exigiu login.

**Uso:** O usuário precisa validar o procedimento oficial disponível à própria conta.

**Limite:** Não ultrapassar login nem transformar snippet em contrato técnico.

## m05 — Meta Ads Kit

Origem: `community-repository`. [Abrir fonte](https://github.com/TheMattBerman/meta-ads-kit)

**Leitura:** README com CLI oficial, mock e aprovação.

**Uso:** Exemplo de camada comunitária de planejamento sobre CLI, não software oficial Meta.

**Limite:** Não instalado, não copiado e não usado como prova de eficácia.

## g01 — Google Ads MCP — guia

Origem: `official-documentation`. [Abrir fonte](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)

**Leitura:** Modo, autenticação, instalação, três ferramentas e limites.

**Uso:** MCP atual somente leitura; não altera lances, não pausa campanhas, não cria assets.

**Limite:** Exemplos de deploy não foram executados; a documentação contém ambiguidade project ID/number.

## g02 — Google Ads MCP — código de origem

Origem: `official-repository`. [Abrir fonte](https://github.com/googleads/google-ads-mcp)

**Leitura:** README de configuração e autenticação; HEAD obtido por git ls-remote.

**Uso:** Configurações local/HTTP e prefixos de ferramentas dependem da versão.

**Limite:** HEAD observado não significa leitura integral do código, implantação ou teste do protocolo.

**Pin observado:** `7a40eae9655194a84d5291c63af817bb20d02ea8`. Não comprova instalação.

## g03 — Novo onboarding Google Ads API

Origem: `official-announcement`. [Abrir fonte](https://ads-developers.googleblog.com/)

**Leitura:** Texto do post de 10/09/2026 na página inicial, incluindo ação requerida.

**Uso:** Acesso associado ao projeto Cloud; cadastro migra do API Center.

**Limite:** Permalink bloqueado; corpo lido na página inicial. Data do anúncio não deve substituir a data de sunset do guia.

## g04 — Developer token — migração

Origem: `official-documentation`. [Abrir fonte](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)

**Leitura:** Corpo do guia, migração e problemas conhecidos.

**Uso:** Corpo informa sunset em 09/09; tokens opcionais/ignorados na transição, acesso pelo projeto das credenciais.

**Limite:** Resumo automático contradiz corpo; há exceção App Conversion Tracking API. Não alterar billing para contornar falhas.

## g05 — MutateGoogleAdsRequest v25

Origem: `official-api-reference`. [Abrir fonte](https://developers.google.com/google-ads/api/reference/rpc/v25/MutateGoogleAdsRequest)

**Leitura:** Campos customer_id, operations, partial_failure, validate_only.

**Uso:** Validação sem execução e semântica de transação/sucesso parcial são distintas.

**Limite:** Nenhuma mutação enviada; nem todo serviço utiliza esse mesmo contrato.

## g06 — Google Ads Python SDK

Origem: `official-repository`. [Abrir fonte](https://github.com/googleads/google-ads-python)

**Leitura:** README, requisito, instalação e vínculo com API.

**Uso:** Biblioteca oficial para implementar operações; não um servidor MCP pronto de escrita.

**Limite:** Não instalado, exemplos de criação não executados e versão do SDK não foi fixada.

## g07 — Google Ads Developer Policies

Origem: `official-policy`. [Abrir fonte](https://support.google.com/adspolicy/answer/6169371?hl=en)

**Leitura:** Uso aprovado, proxies, autenticação por entidade, proteção e saída.

**Uso:** Política restringe proxies programáticos e descreve acesso próprio e revisão de interfaces secundárias.

**Limite:** A pesquisa não certifica a conformidade de um fornecedor específico nem do Oracle.

## t01 — Adspirer Ads MCP

Origem: `vendor-repository`. [Abrir fonte](https://github.com/amekala/ads-mcp)

**Leitura:** README, endpoint, OAuth, plataformas, instalação e segurança declarada.

**Uso:** Candidato remoto de terceiro com gestão de anúncios; URL e OAuth documentados.

**Limite:** Claims do fornecedor não auditados; conector Google condicionado à política e à arquitetura real; não instalado.

## h01 — MCP — ChatGPT/Codex

Origem: `official-documentation`. [Abrir fonte](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

**Leitura:** Transportes, config, env_vars, OAuth e approval modes.

**Uso:** Host local e web têm mecanismos de acesso diferentes; config local não habilita conector web.

**Limite:** Menus e compatibilidade precisam ser verificados na instalação real.

## h02 — Computer Use — ChatGPT

Origem: `official-documentation`. [Abrir fonte](https://learn.chatgpt.com/docs/computer-use)

**Leitura:** Disponibilidade, setup, permissões, foreground Windows e limites.

**Uso:** Work/Codex Desktop pode operar GUI em sistemas/regiões suportados; permissões são humanas.

**Limite:** Não habilitado nem usado para editar vídeo nesta pesquisa. Capturas não provam revisão audiovisual completa.

## f01 — Automation Layering

Origem: `publisher-transcript`. [Abrir fonte](https://www.optmyzr.com/blog/ppc-town-hall-50-automation-layering/)

**Leitura:** Introdução, ferramentas, controle e dados do painel.

**Uso:** Supervisão e camadas de automação como orientação conceitual.

**Limite:** Painel de 2022 com vários autores; não especificação atual nem validação de resultado.

## r01 — Discussão Meta MCP

Origem: `community-discussion`. [Abrir fonte](https://www.reddit.com/r/FacebookAds/comments/1szn2mx/meta_just_released_ads_mcp_this_is_where_facebook/)

**Leitura:** Resultado indexado consultado como pista.

**Uso:** Discussão pública localizada.

**Limite:** Não usada como prova de autenticação ou eficácia, leitura integral não alegada.

## r02 — Discussão Resolve 21.1

Origem: `community-discussion`. [Abrir fonte](https://www.reddit.com/r/davinciresolve/comments/1waf7ns/davinci_resolve_211_is_out_now/)

**Leitura:** Página localizada/aberta; discussão como pista.

**Uso:** Pista sobre versões recentes e acesso a scripting.

**Limite:** Não substitui especificação técnica Blackmagic.

## yt01 — Vídeo Meta MCP

Origem: `video-discovery`. [Abrir fonte](https://www.youtube.com/watch?v=C_m96-Tc3Fs)

**Leitura:** Título/metadados de resultado.

**Uso:** Demonstração localizada para possível aprofundamento.

**Limite:** Não assistido integralmente, transcrição não analisada; nenhuma prova operacional derivada.

## yt02 — Vídeo Resolve 21.1

Origem: `video-discovery`. [Abrir fonte](https://www.youtube.com/watch?v=dA6DuxffnRo)

**Leitura:** Metadados/página com pouco texto.

**Uso:** Demonstração localizada.

**Limite:** Não assistido integralmente; não inferir suporte técnico de imagens não vistas.

[Operação segura](operacao-segura.md) · [Entrevista](entrevista.md)
