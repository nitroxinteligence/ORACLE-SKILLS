---
id: "video-fontes-conectadas"
type: "review"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://learn.chatgpt.com/docs/extend/mcp?surface=cli", "https://learn.chatgpt.com/docs/computer-use", "https://www.blackmagicdesign.com/", "https://github.com/samuelgursky/davinci-resolve-mcp", "https://developer.adobe.com/premiere-pro/uxp/", "https://github.com/leancoderkavy/premiere-pro-mcp", "https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP", "https://github.com/GuanYixuan/pyCapCut", "https://github.com/mrbuslov/capcut-ai-editor", "https://helpx.adobe.com/after-effects/desktop/automate-in-after-effects/automate-animation/scripts.html", "https://github.com/Dakkshin/after-effects-mcp", "https://docs.motion.so/guides/mcp", "https://docs.motion.so/guides/chatgpt-app", "https://hypit.ai/quickstart/", "https://github.com/hypit-ai/hypit", "https://github.com/hypit-ai/hypit/blob/main/LICENSE", "https://www.reddit.com/r/FacebookAds/comments/1szn2mx/meta_just_released_ads_mcp_this_is_where_facebook/", "https://www.reddit.com/r/davinciresolve/comments/1waf7ns/davinci_resolve_211_is_out_now/", "https://www.youtube.com/watch?v=C_m96-Tc3Fs", "https://www.youtube.com/watch?v=dA6DuxffnRo"]
confidence: "medium"
review_after: "2026-10-16"
---
# Fontes, alcance e limitações

Referências anotadas, não cópias integrais nem testemunhos independentes. A ficha informa exatamente o alcance da consulta. Declarações de fornecedor não foram convertidas em testes locais.

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

## d01 — Blackmagic Design

Origem: `official-announcement`. [Abrir fonte](https://www.blackmagicdesign.com/)

**Leitura:** Destaques públicos do DaVinci Resolve 21.1.

**Uso:** Homepage anuncia integração de assistentes de IA.

**Limite:** Contrato técnico MCP nativo, endpoint e permissões não recuperados em página completa.

## d02 — DaVinci Resolve MCP comunitário

Origem: `community-repository`. [Abrir fonte](https://github.com/samuelgursky/davinci-resolve-mcp)

**Leitura:** README, setup, edições, bridge e requisitos; HEAD remoto.

**Uso:** Alternativa comunitária e diferenças de acesso a scripting por edição/versão.

**Limite:** Não testado em Resolve; afirmações sobre edições são do autor e exigem conferir instalação.

**Pin observado:** `570b9eb0d8aea8e6daff23af53585318015146f2`. Não comprova instalação.

## p01 — Premiere UXP oficial

Origem: `official-documentation`. [Abrir fonte](https://developer.adobe.com/premiere-pro/uxp/)

**Leitura:** Introdução de extensibilidade e API.

**Uso:** Interface oficial de plugins; não prova que qualquer MCP comunitário seja oficial.

**Limite:** Nenhum plugin criado/instalado ou método executado.

## p02 — Premiere MCP — leancoderkavy

Origem: `community-repository`. [Abrir fonte](https://github.com/leancoderkavy/premiere-pro-mcp)

**Leitura:** README de setup, diagnóstico, CEP/UXP e versões.

**Uso:** Candidato CEP com pacote premiere-pro-mcp; versão observada 1.16.0.

**Limite:** Plugin Codex cita outro pin; pacote diferente adobe-premiere-pro-mcp compartilha executável. Não instalado.

**Pin observado:** `npm premiere-pro-mcp@1.16.0`. Não comprova instalação.

## p03 — Premiere MCP — hetpatel

Origem: `community-repository`. [Abrir fonte](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP)

**Leitura:** README de pacote, CEP, UXP experimental e instalação.

**Uso:** Alternativa distinta, não intercambiar comandos/variáveis com outro repositório.

**Limite:** Nenhum teste comparativo de editores; não escolhido como rota principal.

## c01 — pyCapCut

Origem: `community-repository`. [Abrir fonte](https://github.com/GuanYixuan/pyCapCut)

**Leitura:** README, geração de drafts, templates não encriptados e export.

**Uso:** Draft pode ser montado fora do Windows; export automatizado documentado usa CapCut Windows.

**Limite:** Não prova render Mac nem MCP oficial. Licença de redistribuição não estabelecida nesta leitura; não copiado.

## c02 — CapCut AI Editor

Origem: `community-repository`. [Abrir fonte](https://github.com/mrbuslov/capcut-ai-editor)

**Leitura:** Identificação/README consultado como alternativa.

**Uso:** Pista adicional para automação baseada em projetos.

**Limite:** Não adotado, nenhum draft/export foi testado; compatibilidade e licença devem ser verificadas antes de uso.

## a01 — Adobe — scripts After Effects

Origem: `official-documentation`. [Abrir fonte](https://helpx.adobe.com/after-effects/desktop/automate-in-after-effects/automate-animation/scripts.html)

**Leitura:** Scripts, painel e permissão de arquivos/rede.

**Uso:** Permissão de scripts é configuração separada e deve ser concedida conscientemente.

**Limite:** Não acionada; instruções antigas de ferramentas auxiliares não foram adotadas.

## a02 — After Effects MCP

Origem: `community-repository`. [Abrir fonte](https://github.com/Dakkshin/after-effects-mcp)

**Leitura:** README, bridge JSX, instalação e superfície de ferramentas; HEAD remoto.

**Uso:** MCP comunitário com ponte local de scripts.

**Limite:** Não instalado, arquivo JSX não executado, Node mínimo anunciado não substitui runtime suportado atual.

**Pin observado:** `88d5fbf08b7ae9f015ee98e5f8c4904095cf8202`. Não comprova instalação.

## v01 — Motion MCP

Origem: `official-documentation`. [Abrir fonte](https://docs.motion.so/guides/mcp)

**Leitura:** URL, OAuth, ferramentas e custos.

**Uso:** Endpoint https://mcp.motion.so/mcp; conexão padrão OAuth, créditos/render separados.

**Limite:** A conta, elegibilidade e tool schemas não foram testados ao vivo.

## v02 — Motion — ChatGPT app

Origem: `official-documentation`. [Abrir fonte](https://docs.motion.so/guides/chatgpt-app)

**Leitura:** Instruções de host e conexão.

**Uso:** Integração remota por interface de apps/plugins.

**Limite:** Menus do fornecedor divergem do guia OpenAI atual; conferir host real.

## y01 — Hypit quickstart

Origem: `official-project-documentation`. [Abrir fonte](https://hypit.ai/quickstart/)

**Leitura:** Instalação da skill, execução, runtime e produção.

**Uso:** Skill, executável, projeto, providers e outputs são camadas distintas.

**Limite:** Nenhum comando instalado/executado; custo e suporte dependem da rota escolhida.

## y02 — Hypit repositório

Origem: `project-repository`. [Abrir fonte](https://github.com/hypit-ai/hypit)

**Leitura:** README e revisão remota HEAD.

**Uso:** Workflow programável e adaptável, não garantia de viralização.

**Limite:** Código não auditado integralmente; não copiado.

**Pin observado:** `4d7f8f8e7f0ff40b674943c3a9a0d2a454b2af3e`. Não comprova instalação.

## y03 — Hypit licença

Origem: `project-license`. [Abrir fonte](https://github.com/hypit-ai/hypit/blob/main/LICENSE)

**Leitura:** Termos adicionais da licença modificada.

**Uso:** Apache modificada: uso interno não equivale à autorização de redistribuir/operar SaaS multi-tenant.

**Limite:** Não é parecer jurídico; revisar termos aplicáveis antes de distribuir runtime dentro do Oracle.

## l01 — Tutorial Hypit

Origem: `local-tutorial`. [Abrir fonte](../../../../tutoriais/criacao-de-videos/edicao-com-ia/hypit-clonar-videos-com-workflows-no-codex.md)

**Leitura:** Arquivo completo lido na conversa.

**Uso:** Pista e fluxo pedagógico usado na autoria, com verificação externa das integrações.

**Limite:** Tutorial não é teste da conta/host nem prova do conteúdo audiovisual vinculado.

## l02 — Tutorial Motion

Origem: `local-tutorial`. [Abrir fonte](../../../../tutoriais/criacao-de-videos/edicao-com-ia/motion-mcp-chatgpt-design-de-movimento.md)

**Leitura:** Arquivo completo lido na conversa.

**Uso:** Pista e fluxo pedagógico usado na autoria, com verificação externa das integrações.

**Limite:** Tutorial não é teste da conta/host nem prova do conteúdo audiovisual vinculado.

## l03 — Tutorial VibeEditing Resolve

Origem: `local-tutorial`. [Abrir fonte](../../../../tutoriais/criacao-de-videos/edicao-com-ia/vibe-editing-com-codex-e-davinci-resolve.md)

**Leitura:** Arquivo completo lido na conversa.

**Uso:** Pista e fluxo pedagógico usado na autoria, com verificação externa das integrações.

**Limite:** Tutorial não é teste da conta/host nem prova do conteúdo audiovisual vinculado.

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
