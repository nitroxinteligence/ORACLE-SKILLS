---
title: "NotFair no Codex e ChatGPT: 45 skills de marketing com dados reais"
slug: notfair-marketing-skills-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/robiartec/status/2098383879686271352
source_title: "NotFair: 45 skills de marketing para agentes de IA"
source_author: "RobiAR"
source_published_at: "2026-09-11"
repository: https://github.com/nowork-studio/notfair-plugin
repository_version: "0.27.7"
repository_commit: f5275f17ab17d0ee7afe30ed767a8fb503f8d3f4
captured_at: 2026-09-12
official_sources:
  - https://learn.chatgpt.com/docs/plugins
  - https://learn.chatgpt.com/docs/enterprise/apps-and-connectors
  - https://learn.chatgpt.com/docs/sandboxing
  - https://github.com/nowork-studio/notfair-plugin
  - https://notfair.co/privacy
  - https://notfair.co/terms
tags:
  - tutorial
  - codex
  - chatgpt
  - plugins
  - skills
  - mcp
  - marketing
  - seo
  - google-ads
  - meta-ads
  - analytics
---

# NotFair no Codex e ChatGPT: 45 skills de marketing com dados reais

O [post de RobiAR](https://x.com/robiartec/status/2098383879686271352)
apresenta o NotFair como um “departamento de marketing” para agentes de IA. A
descrição resume bem a variedade do pacote, mas esconde uma divisão que você
precisa entender antes de conectar qualquer conta:

- as **45 skills** são arquivos abertos que orientam o agente;
- o acesso ao Google Ads, Meta Ads, X Ads, LinkedIn Ads, GA4 e Search Console
  passa por um **servidor MCP hospedado pela NotFair**;
- instalar o plugin não autoriza nenhuma conta externa;
- autenticar uma conta não significa que toda ação de escrita está liberada;
- uma recomendação só vira alteração real depois de uma operação confirmada e
  de uma leitura do estado resultante.

Este tutorial mostra como revisar, instalar e testar o NotFair com o Codex ou o
ChatGPT. O primeiro piloto será somente leitura. Ações que mexem em orçamento,
campanhas, palavras-chave, eventos ou sitemaps ficam para uma etapa posterior,
com alvo e efeito explícitos.

## O que foi verificado

Em 12 de setembro de 2026, o repositório
[nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin)
estava na versão `0.27.7`, commit
`f5275f17ab17d0ee7afe30ed767a8fb503f8d3f4`. A inspeção local encontrou:

| Item | Estado verificado |
|---|---|
| Licença do repositório | MIT |
| Skills canônicas | 45 arquivos `SKILL.md` |
| Wrappers para Codex | 45 arquivos em `skills/` |
| Manifesto Claude | 45 entradas |
| Servidores MCP declarados | Um, chamado `NotFair` |
| Endpoint | `https://notfair.co/api/mcp/notfair` |
| Autenticação | OAuth 2.1 com Authorization Code + PKCE |
| Plataformas ao vivo declaradas | Google Ads, Meta Ads, X Ads, LinkedIn Ads, GA4, Search Console e GoHighLevel |
| TikTok, Amazon e ChatGPT Ads | Planejamento ou revisão de exportação, salvo se houver outro conector verificado |

O post falava em cerca de 3,7 mil estrelas. O GitHub mostrava 3,8 mil na captura
deste tutorial. Esse número muda e não é prova de segurança ou qualidade.

O endpoint respondeu `401` sem credencial e publicou o endereço de metadados
OAuth esperado. Isso prova que a proteção de autenticação estava ativa naquele
momento. Não prova que uma conta específica está conectada nem que uma operação
de anúncio funciona de ponta a ponta.

## O modelo correto: cinco camadas separadas

```text
Plugin instalado
  ↓
Skill encontrada pelo agente
  ↓
MCP NotFair autenticado
  ↓
Plataforma e conta corretas conectadas
  ↓
Leitura ou escrita executada e confirmada
```

Cada seta representa uma verificação própria. Se o agente reconhece
`google-ads-audit`, isso só comprova que recebeu as instruções da skill. Se
`codex mcp list` mostra o servidor, isso comprova configuração, não acesso a uma
conta. O recibo final precisa identificar a conta, o intervalo analisado e o
resultado retornado pela plataforma.

A [documentação oficial de plugins da
OpenAI](https://learn.chatgpt.com/docs/plugins) também separa skills e MCP:
skills são instruções reutilizáveis; servidores MCP fornecem ferramentas,
autenticação, dados e ações externas. Depois da instalação, abra uma conversa ou
sessão nova para carregar o pacote.

## Quando usar sem conectar contas

Várias skills funcionam com um site, repositório, arquivo ou exportação entregue
por você. Você pode começar sem OAuth para:

- auditar uma página ou estrutura de SEO;
- revisar metatags, links, imagens, schema e sitemap;
- criar um plano editorial;
- fazer pesquisa de palavras-chave com fontes disponíveis;
- elaborar briefs de criativos e anúncios;
- revisar um CSV exportado de uma plataforma;
- montar um plano de campanha ainda não publicado.

Esse modo é adequado para conhecer a qualidade das instruções antes de liberar
dados de clientes.

## Quando o MCP hospedado é necessário

Use a conexão NotFair quando você quiser consultar ou alterar o estado atual de
uma conta, por exemplo:

- buscar campanhas e termos de pesquisa no Google Ads;
- comparar aquisição e conversões no GA4;
- analisar consultas e páginas no Search Console;
- diagnosticar fadiga de criativo no Meta Ads;
- consultar campanhas no X Ads ou LinkedIn Ads;
- enviar ou remover um sitemap;
- alterar um orçamento, lance, palavra-chave ou configuração compatível.

As skills são abertas, mas o serviço hospedado tem seus próprios termos,
política de privacidade, autenticação, disponibilidade e limites. Avalie as duas
partes separadamente.

## 1. Revise o pacote antes de instalar

Crie uma cópia temporária e registre o commit que você analisou:

```bash
review_dir="$(mktemp -d /tmp/notfair-review.XXXXXX)"
git clone --depth 1 \
  https://github.com/nowork-studio/notfair-plugin.git \
  "$review_dir"

git -C "$review_dir" rev-parse HEAD
cat "$review_dir/VERSION"
```

Conte as skills canônicas:

```bash
find \
  "$review_dir/seo" \
  "$review_dir/google-ads" \
  "$review_dir/meta-ads" \
  "$review_dir/paid-ads" \
  "$review_dir/analytics" \
  "$review_dir/gemini" \
  "$review_dir/notfair-upgrade-skill" \
  -name SKILL.md -type f | wc -l
```

Leia primeiro estes arquivos:

```bash
sed -n '1,240p' "$review_dir/README.md"
sed -n '1,240p' "$review_dir/INSTALL_FOR_AGENTS.md"
cat "$review_dir/.codex-plugin/plugin.json"
cat "$review_dir/.mcp.json"
sed -n '1,240p' "$review_dir/docs/mcp-connection.md"
sed -n '1,240p' "$review_dir/paid-ads/shared/operating-contract.md"
```

Procure comandos, rede, atualizações e escrita:

```bash
rg -n \
  'curl|git fetch|git reset|rm -rf|OAuth|execute|mutation|write|approval' \
  "$review_dir"
```

Essa busca não decide se o pacote é seguro. Ela mostra onde a revisão humana
precisa se concentrar.

### Ponto de atenção: atualização automática nas instruções

O pacote inclui `bin/notfair-update-check`, que consulta o arquivo `VERSION` no
GitHub e grava estado em `~/.toprank/`. A skill de upgrade para Claude Code
instrui o agente a executar `git fetch`, `git reset --hard`, copiar uma nova
versão para o cache e remover versões antigas.

Esse fluxo não apareceu como hook no manifesto do Codex analisado. Ainda assim,
leia novamente a skill de upgrade quando a versão mudar. Um `SKILL.md` é texto
executável por intermédio do agente: ele pode orientar comandos com efeitos no
seu ambiente.

## 2. Escolha o primeiro caso de uso

Não conecte todas as plataformas para “ver o que acontece”. Escolha uma pergunta
real e uma única fonte de dados.

Um piloto seguro tem este formato:

| Campo | Exemplo |
|---|---|
| Objetivo | Entender por que o CPA subiu |
| Plataforma | Google Ads |
| Conta | ID e nome confirmados pelo usuário |
| Janela principal | Últimos 30 dias completos |
| Comparação | 30 dias anteriores |
| Ação permitida | Somente leitura |
| Saída | Evidências, hipóteses e propostas |
| Escrita | Proibida no piloto |

Para SEO sem conta conectada:

| Campo | Exemplo |
|---|---|
| Objetivo | Encontrar falhas técnicas prioritárias |
| Entrada | URL pública ou checkout local |
| Limite | Sem editar arquivos e sem publicar |
| Saída | Achado, evidência, impacto e correção sugerida |

## 3. Instale no Codex CLI

O caminho reproduzível documentado pelo projeto é adicionar o marketplace do
GitHub e instalar o plugin:

```bash
codex plugin marketplace add \
  nowork-studio/notfair-plugin \
  --json

codex plugin add notfair@nowork-studio --json
```

Confira o que o Codex passou a considerar:

```bash
codex plugin marketplace list --json
codex plugin list --json
codex mcp list --json
```

Os comandos acima instalam o pacote e registram a conexão. Eles não autorizam
Google, Meta, X ou LinkedIn.

Se o marketplace `nowork-studio` já existir, atualize a cópia local antes de
reinstalar:

```bash
codex plugin marketplace upgrade nowork-studio --json
codex plugin add notfair@nowork-studio --json
```

Abra uma sessão nova depois da instalação. A documentação oficial da OpenAI
indica que skills e ferramentas de um plugin são carregadas em novas conversas
ou sessões.

### Instalação pela interface do ChatGPT/Codex

No aplicativo desktop ou na web, abra **Plugins**, procure **NotFair**, revise a
ficha e use o botão de adicionar se o plugin estiver disponível para sua conta
ou workspace. Depois, inicie uma conversa nova.

Se ele não aparecer no diretório, não trate isso como erro da sua conta. A
visibilidade depende do catálogo e das políticas do workspace. Use o marketplace
Git do Codex CLI quando esse for o ambiente pretendido, ou peça ao administrador
para revisar a importação do marketplace.

Plugins não funcionam na extensão de IDE, segundo a documentação oficial da
OpenAI. Para o Codex, use o aplicativo desktop ou o navegador de plugins da CLI.

## 4. Autentique somente o MCP NotFair

No Codex CLI:

```bash
codex mcp login NotFair
```

O navegador abrirá o fluxo OAuth. Confira antes de aceitar:

1. o domínio é `notfair.co`;
2. o workspace selecionado é o correto;
3. a plataforma que você pretende testar está conectada;
4. a identidade possui somente os acessos necessários;
5. nenhuma conta de outro cliente aparece no mesmo escopo por engano.

Depois:

```bash
codex mcp list --json
```

O resultado precisa mostrar `NotFair` configurado e autenticado. Faça ainda uma
leitura inofensiva, como listar contas disponíveis. Essa leitura é o primeiro
recibo de que o OAuth chegou ao serviço externo.

### O que a política de privacidade declara

A [política da NotFair](https://notfair.co/privacy), efetiva em 7 de setembro de
2026, declara que o serviço armazena credenciais de acesso ou refresh, escopos,
IDs e metadados das contas conectadas em armazenamento restrito no servidor. Ela
também declara:

- `adwords` para Google Ads;
- `analytics.readonly` e `analytics.edit` para GA4;
- `webmasters` para Search Console;
- dados e acesso de escrita nas superfícies compatíveis de Meta, LinkedIn e X;
- escopos de escrita para contatos, oportunidades, eventos e tags no
  GoHighLevel;
- recebimento pelo MCP do nome da ferramenta e dos argumentos enviados pelo
  cliente;
- remoção dos argumentos de chamadas dos registros após 100 dias;
- exclusão dos registros de leitura após 365 dias;
- retenção dos recibos de escrita como histórico enquanto o workspace estiver
  ativo, sujeita ao processo de exclusão e a retenções legais ou de segurança.

A política também informa uma medição de produto via Meta Conversions API para
usuários atribuídos à Meta. Entre os marcos descritos está o primeiro pedido de
ferramenta MCP de escrita, acompanhado de identificadores com hash e do click ID
quando disponível. Leia o texto atual antes de conectar dados de clientes.

## 5. Confirme a identidade da conta

Use este prompt na primeira conversa com o plugin:

```text
Use o NotFair apenas para leitura.

Liste os workspaces, plataformas e contas ou propriedades que minha identidade
autenticada consegue acessar. Para cada item, mostre:
- plataforma;
- nome;
- ID exato, sem reformatação;
- moeda e fuso horário, quando existirem;
- se a capacidade atual é leitura ou também escrita.

Não faça auditoria, não altere configurações e não execute mutações.
Se a conexão não expuser alguma dessas informações, marque como não verificado.
```

Compare o ID retornado com a interface nativa da plataforma. O nome de uma conta
pode ser repetido; o ID é o identificador operacional.

Se nenhuma conta aparecer, revise três estados separados:

1. o MCP está autenticado no Codex;
2. a plataforma foi conectada dentro do workspace NotFair;
3. a identidade da plataforma tem acesso à conta desejada.

## 6. Execute um piloto somente leitura

### Google Ads

```text
Use a skill NotFair de auditoria do Google Ads e trabalhe somente em leitura.

Conta: [NOME E ID]
Período principal: [DATA INICIAL] a [DATA FINAL]
Comparação: [DATA INICIAL] a [DATA FINAL]
Objetivo de conversão: [DEFINIÇÃO]

Antes de analisar, confirme conta, moeda, fuso, janelas, atribuição e definição
de conversão. Verifique a integridade do tracking antes de tratar CPA ou ROAS
como acionáveis.

Para cada achado, mostre entidade, métrica, valor, denominador, período e fonte.
Separe fatos observados, hipóteses e recomendações. Não pause, habilite, crie,
remova ou altere nada. Termine com no máximo três propostas prontas para revisão.
```

### Meta Ads

```text
Use a skill NotFair de auditoria do Meta Ads em modo somente leitura.

Conta: [NOME E ID]
Período: [DATA INICIAL] a [DATA FINAL]
Conversão principal: [EVENTO]

Confirme Pixel, CAPI, janela de atribuição, moeda e fuso antes de concluir sobre
ROAS, CPA ou fadiga. Mostre campanha, conjunto ou anúncio afetado e os dados que
sustentam cada hipótese. Não altere orçamento, status, público ou criativo.
```

### GA4

```text
Use a skill NotFair de Google Analytics em modo somente leitura.

Propriedade: [NOME E ID]
Período: [DATA INICIAL] a [DATA FINAL]
Comparação: [DATA INICIAL] a [DATA FINAL]
Evento principal: [NOME EXATO]

Informe dimensões, métricas, filtros, timezone, frescor, amostragem e limites
relevantes. Separe aquisição, landing pages e eventos. Não crie ou arquive
dimensões e não altere key events.
```

### Search Console

```text
Use a skill NotFair de Search Console em modo somente leitura.

Propriedade: [URL OU ID EXATO]
Período: [DATA INICIAL] a [DATA FINAL]
Comparação: [DATA INICIAL] a [DATA FINAL]

Encontre os maiores ganhos e perdas por consulta e página. Mostre cliques,
impressões, CTR, posição, filtros e limites do relatório. Não envie nem remova
sitemaps e não altere o site.
```

### SEO sem conta conectada

```text
Use a skill NotFair de SEO para auditar esta URL: [URL].

Trabalhe somente com a página pública e as fontes que você conseguir abrir.
Não edite o site, o CMS ou arquivos locais. Para cada problema, mostre a
evidência observada, o impacto provável, a confiança e a correção sugerida.
Não invente dados do Search Console, volume de busca ou posição orgânica.
```

## 7. Julgue a qualidade da resposta

Uma resposta útil precisa conter:

- conta ou propriedade identificada;
- período e comparação completos;
- moeda e fuso quando relevantes;
- definição de conversão e atribuição;
- entidade afetada;
- numerador e denominador das métricas;
- tamanho da amostra;
- fonte de cada dado material;
- separação entre observação, hipótese e recomendação;
- limitações de tracking, frescor, amostragem ou linhas retornadas;
- nenhuma alegação de publicação sem recibo da plataforma.

Rejeite respostas como “o CPA está alto” sem referência de conta, período,
conversões, custo e comparação. Também rejeite benchmarks universais usados como
ordem automática para alterar campanhas.

## 8. Prepare uma alteração sem executá-la

Depois que o piloto estiver correto, peça uma proposta operacional:

```text
Com base apenas nos dados já verificados, prepare uma única mudança reversível.

Mostre:
1. plataforma, conta e entidade exata;
2. estado atual;
3. estado proposto;
4. evidência e cálculo que justificam a mudança;
5. exposição diária e mensal em moeda;
6. risco e efeito esperado;
7. janela de observação;
8. métrica de sucesso;
9. gatilho de reversão;
10. método de confirmação depois da operação.

Marque como ready_for_review. Não execute a mudança.
```

O próprio contrato de paid media do repositório usa estados claros:

| Estado | Significado |
|---|---|
| `draft` | Falta evidência ou decisão |
| `ready_for_review` | A proposta está especificada para revisão |
| `approved_to_publish` | O usuário aprovou o escopo exato |
| `published` | A plataforma confirmou a alteração |

`approved_to_publish` ainda não é `published`.

## 9. Execute uma mudança com recibo

Quando você decidir aprovar uma proposta concreta, cite o alvo e a mudança no
mesmo pedido:

```text
Aprovo somente esta alteração:
- plataforma: [PLATAFORMA]
- conta: [NOME E ID]
- entidade: [TIPO, NOME E ID]
- valor atual: [VALOR]
- valor novo: [VALOR]

Execute apenas essa operação. Depois, leia novamente a entidade e entregue o
antes, o depois, o ID da operação ou recibo disponível e qualquer falha parcial.
Se o estado lido não corresponder ao pedido, pare e reporte a divergência.
```

Para orçamento ou lance, inclua moeda, limite diário, impacto mensal e data de
revisão. Para habilitar campanha, confirme que criativos, tracking, público,
landing page e limite de gasto estão corretos.

Não agrupe dez mutações em uma aprovação vaga. Uma alteração por vez facilita
atribuição de impacto e reversão.

## 10. Preserve a separação entre plataformas

GA4, Google Ads, Meta Ads e CRM podem chamar coisas diferentes de conversão.
Antes de comparar ROAS ou CPA entre canais, registre:

| Campo | Pergunta |
|---|---|
| Evento | Qual ação conta como conversão? |
| Fonte | Qual sistema é a referência? |
| Janela | Quantos dias após o clique ou visualização? |
| Modelo | Last click, data driven ou outro? |
| Moeda | Todos os valores usam a mesma moeda? |
| Período | As janelas têm dias completos e o mesmo fuso? |
| Receita | Bruta, líquida, prevista ou confirmada? |

Não some ROAS de plataformas como se fossem observações independentes da mesma
receita. Deduplicação e definição de atribuição precisam vir antes do painel.

## 11. Use as skills por intenção

O catálogo atual se distribui assim:

| Área | Skills principais |
|---|---|
| SEO e GEO | `seo-analysis`, `seo-page`, `keyword-research`, `content-planner`, `geo-optimizer`, `sitemap-audit`, `seo-drift` |
| Paid media | `paid-ads`, `paid-ads-setup`, `paid-ads-review`, `paid-ads-optimize`, `paid-ads-creative` |
| Google Ads | `google-ads-audit`, `google-ads`, `google-ads-copy`, `google-ads-assets`, `google-ads-landing` |
| Meta Ads | `meta-ads-audit`, `meta-ads`, `meta-ads-creative` |
| Analytics | `google-analytics`, `search-console` |
| Outros canais | `paid-ads-x`, `paid-ads-linkedin`, `paid-ads-tiktok`, `paid-ads-amazon`, `paid-ads-chatgpt` |
| Apoio | `paid-ads-integrations`, `paid-ads-guide`, `gemini`, `upgrade` |

Use linguagem natural quando o host fizer o roteamento corretamente. Invoque a
skill pelo nome quando precisar remover ambiguidade:

```text
Use a skill NotFair `google-ads-audit` para esta análise.
```

O prefixo `/notfair:` aparece nos exemplos do repositório para hosts que expõem
comandos de plugin. Não confunda o nome do comando com garantia de que o MCP foi
autenticado.

## 12. Atualize com revisão

Veja o marketplace configurado e a versão instalada:

```bash
codex plugin marketplace list --json
codex plugin list --json
```

Antes de atualizar, leia o changelog remoto e confira o diff entre o commit já
aprovado e o novo:

```bash
git -C "$review_dir" fetch origin main
git -C "$review_dir" log --oneline HEAD..origin/main
git -C "$review_dir" diff --stat HEAD..origin/main
```

Depois da revisão:

```bash
codex plugin marketplace upgrade nowork-studio --json
codex plugin add notfair@nowork-studio --json
```

Abra uma sessão nova e repita a leitura inofensiva de identidade e contas. Uma
atualização pode mudar skills, manifestos, endpoint, escopos ou comportamento.

## 13. Desconecte e remova

Para retirar a autenticação do MCP no Codex:

```bash
codex mcp logout NotFair
```

Para remover o plugin:

```bash
codex plugin remove notfair@nowork-studio --json
```

Remover o plugin não garante que a conexão externa ou os dados do provedor
foram apagados. A documentação oficial da OpenAI informa que integrações MCP
conectadas podem continuar conectadas até serem desligadas separadamente. Faça a
revogação em três lugares quando aplicável:

1. cliente Codex ou ChatGPT;
2. workspace NotFair;
3. configurações de segurança do Google, Meta, X, LinkedIn ou outro provedor.

Consulte a política da NotFair para solicitar exclusão de dados armazenados.

## 14. Falhas comuns

### A skill não aparece

- confirme que `notfair@nowork-studio` está instalado;
- abra uma sessão nova;
- verifique se o plugin está habilitado;
- tente o nome exato da skill;
- não use a extensão de IDE como prova de disponibilidade de plugins.

### O MCP aparece, mas não há contas

- confirme o login OAuth;
- confira o workspace selecionado;
- conecte a plataforma dentro da NotFair;
- confira o acesso da identidade na plataforma original;
- liste contas novamente antes de auditar.

### O agente diz que alterou, mas nada mudou

- procure retorno de uma ferramenta de escrita;
- exija ID da entidade e recibo;
- faça uma leitura nova do estado;
- trate a resposta como proposta se não houver confirmação ao vivo.

### Os números não batem com a interface

- compare fuso e dias completos;
- confira moeda;
- confirme filtros e status das campanhas;
- alinhe evento de conversão e atribuição;
- verifique atraso, amostragem e limites de linhas;
- compare a mesma entidade e o mesmo período.

### O agente tenta agir cedo demais

Use este bloqueio explícito:

```text
Somente leitura. Qualquer criação, edição, pausa, ativação, remoção, envio ou
mudança de orçamento está fora do escopo. Entregue propostas como
ready_for_review e aguarde uma aprovação que nomeie a entidade e o novo valor.
```

## Checklist do piloto

### Revisão

- [ ] Repositório, versão e commit foram registrados.
- [ ] Manifestos, MCP, política de privacidade e termos foram lidos.
- [ ] Comandos e instruções de atualização foram revisados.
- [ ] O caso de uso inicial usa uma única plataforma.

### Instalação

- [ ] O marketplace correto foi adicionado.
- [ ] `notfair@nowork-studio` aparece instalado.
- [ ] Uma sessão nova foi aberta.
- [ ] O servidor `NotFair` aparece uma única vez.

### Autorização

- [ ] O domínio OAuth foi conferido.
- [ ] O workspace correto foi selecionado.
- [ ] Somente a plataforma necessária foi conectada.
- [ ] Conta, ID, moeda e fuso foram confirmados.
- [ ] A primeira operação foi somente leitura.

### Análise

- [ ] Períodos e comparação usam dias completos.
- [ ] Conversão e atribuição foram definidas.
- [ ] Achados citam entidade, métrica, valor e fonte.
- [ ] Fatos, hipóteses e recomendações estão separados.
- [ ] Limitações de dados foram registradas.

### Escrita futura

- [ ] A proposta está `ready_for_review`.
- [ ] O alvo e o valor novo estão explícitos.
- [ ] Exposição financeira e risco foram calculados.
- [ ] Existe janela de observação e gatilho de reversão.
- [ ] A operação será confirmada por leitura posterior.

## Fontes

- [Post original de RobiAR](https://x.com/robiartec/status/2098383879686271352)
- [Repositório NotFair Plugin](https://github.com/nowork-studio/notfair-plugin)
- [Guia de conexão MCP do repositório](https://github.com/nowork-studio/notfair-plugin/blob/main/docs/mcp-connection.md)
- [Plugins no ChatGPT e Codex — OpenAI](https://learn.chatgpt.com/docs/plugins)
- [Controles de plugins e conexões — OpenAI](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)
- [Sandbox e aprovações do Codex — OpenAI](https://learn.chatgpt.com/docs/sandboxing)
- [Política de privacidade da NotFair](https://notfair.co/privacy)
- [Termos de serviço da NotFair](https://notfair.co/terms)
- [Guia operacional da NotFair](https://notfair.co/guide)

O NotFair pode transformar tarefas vagas de marketing em procedimentos mais
estruturados. O ganho vem das instruções e do acesso a dados reais; o risco vem
do mesmo lugar. Comece com uma skill, uma conta e uma pergunta, mantenha o
primeiro ciclo somente leitura e só aceite `published` quando a plataforma
devolver um estado verificável.
