---
title: "AIsa no Codex: pesquisa de GTM com dados de SEO, tráfego e clientes"
slug: aisa-gtm-no-codex
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/gengdaJ/status/2098293186292765046
source_author: "逸尘 (@gengdaJ)"
source_published_at: "2026-09-11T06:10:54Z"
source_thread: https://x.com/gengdaJ/status/2098252168625332263
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
repository: https://github.com/AIsa-team/agent-skills
repository_commit: bb70b34de56aff23cc3fcc4a8b30ea5e9da78821
official_sources:
  - https://aisa.one/solutions/go-to-market
  - https://aisa.one/docs/agent-quickstart.md
  - https://aisa.one/docs/guides/pricing.md
  - https://aisa.one/TOS
  - https://aisa.one/privacy
  - https://developers.openai.com/codex/skills
  - https://docs.dataforseo.com/v3/dataforseo_labs-google-keyword_overview-live/
  - https://developers.similarweb.com/docs/similarweb-web-traffic-api
tags:
  - aisa
  - codex
  - gtm
  - seo
  - pesquisa-de-mercado
  - inteligencia-competitiva
---

# AIsa no Codex: pesquisa de GTM com dados de SEO, tráfego e clientes

Este tutorial transforma a [publicação de 逸尘](https://x.com/gengdaJ/status/2098293186292765046) e a [thread original com a demonstração](https://x.com/gengdaJ/status/2098252168625332263) em um processo controlado para pesquisar go-to-market no Codex.

A proposta é combinar dados de tráfego, pesquisa orgânica, resultados de busca, avaliações e conversas públicas para responder três perguntas:

1. de onde vem a demanda de cada concorrente;
2. quais problemas aproximam ou afastam clientes;
3. quais oportunidades de aquisição e posicionamento merecem teste.

A AIsa funciona como uma camada de acesso a vários provedores. O site do produto lista Similarweb, Ahrefs, Semrush, DataForSEO, Reddit, X, YouTube, Instagram, Pinterest, WaveInflu, Oxylabs, Apollo e outros. Uma credencial e uma interface comum reduzem integrações separadas, mas não tornam os dados gratuitos, completos, exatos ou equivalentes entre si.

## Limites da fonte

A publicação e as páginas da AIsa têm caráter promocional. A AIsa afirma oferecer acesso oficial a diferentes provedores e se apresenta como parceira autorizada da Similarweb. Nesta verificação, a afirmação foi encontrada no site da AIsa; não foi localizada uma confirmação nominal da AIsa nas páginas públicas da Similarweb consultadas.

Há também duas descrições comerciais atuais que precisam ser conferidas no checkout:

- a página de GTM anuncia um plano Builder de US$ 39 por 30 dias com US$ 50 em créditos incluídos;
- a visão geral de preços afirma que não há tarifa mensal fixa para a plataforma e descreve cobrança por uso.

Essas ofertas podem representar modalidades distintas, mas as páginas consultadas não eliminam a ambiguidade. Confira plano, multiplicador, créditos, validade, impostos e preço por endpoint antes de contratar ou executar uma pesquisa.

As métricas dos provedores têm naturezas diferentes:

- tráfego de concorrentes é geralmente uma estimativa, não o Analytics interno da empresa;
- volume de busca é aproximado e depende de país, idioma, período e base de dados;
- comentários públicos são uma amostra enviesada de pessoas que decidiram publicar;
- sentimento gerado por modelo é uma classificação sujeita a erro;
- correlação entre canal de aquisição e reclamação não comprova causa.

O resultado correto é um relatório com rastreabilidade e limites, não uma tabela de números sem origem.

## O que você vai construir

Ao final, você terá:

1. a skill oficial `aisa` disponível no Codex;
2. autenticação local sem expor a chave em prompts;
3. um plano de chamadas com custo máximo antes de gastar;
4. uma análise comparativa de tráfego e SEO;
5. uma análise amostral de avaliações e conversas públicas;
6. um relatório HTML com fatos, inferências e recomendações separados;
7. arquivos de evidência para repetir ou auditar a pesquisa.

## 1. Defina a decisão de GTM

Não comece pela lista de APIs. Comece pela decisão que o relatório precisa apoiar.

Use este briefing:

```markdown
# Briefing de GTM

## Produto
- nome:
- URL oficial:
- categoria:
- mercado atual:

## Decisão
[Ex.: escolher o primeiro canal de aquisição nos Estados Unidos]

## Público
- segmento:
- problema:
- idioma:
- país ou região:

## Concorrentes iniciais
1. [nome] — [domínio que ainda será verificado]
2. [nome] — [domínio que ainda será verificado]
3. [nome] — [domínio que ainda será verificado]

## Perguntas
1. Qual concorrente tem maior alcance estimado e melhor qualidade de visita?
2. Quem depende mais de busca, social, referência ou acesso direto?
3. Quais demandas não relacionadas à marca possuem sinais de busca?
4. Quais elogios e reclamações aparecem de forma recorrente?
5. Quais hipóteses podemos testar sem confundir correlação com causa?

## Comparabilidade
- período:
- país:
- idioma:
- dispositivo:
- limite de resultados por fonte:

## Orçamento
- teto total em USD:
- chamadas proibidas sem nova aprovação:

## Saídas
- relatório HTML:
- evidências JSON/CSV:
- data de corte:
```

Limite o primeiro estudo a três concorrentes. Cinco empresas, como no exemplo do post, aumentam rapidamente o número de domínios, palavras-chave, resultados de busca e comentários.

## 2. Escolha a menor combinação de fontes

Cada pergunta deve ter uma fonte principal. Acrescente outra somente quando ela responder algo que a primeira não cobre.

| Pergunta | Fonte inicial | Saída esperada |
|---|---|---|
| tamanho e qualidade estimada da visita | Similarweb | visitas, duração, páginas, rejeição e período |
| canais de aquisição | Similarweb | busca, direto, social, referência e outros |
| palavras e demanda de busca | DataForSEO | volume, intenção, dificuldade e SERP |
| força de backlinks | Ahrefs ou Semrush | domínios de referência e métricas próprias |
| avaliações de lojas | DataForSEO | avaliações com data, nota e origem |
| conversas públicas | Reddit, X, YouTube | posts ou comentários com URL e data |
| descoberta de criadores | WaveInflu | perfis e dados disponibilizados pelo provedor |
| visibilidade em respostas de IA | Oxylabs ou DataForSEO | menções e fontes citadas por mecanismo |
| prospecção B2B | Apollo | empresas ou contatos dentro do uso permitido |

Não misture métricas homônimas de Ahrefs, Semrush, DataForSEO e Similarweb como se usassem a mesma base. Registre o provedor em cada coluna.

Para um estudo inicial, use:

1. **DataForSEO** para palavras-chave e SERP;
2. **Similarweb** apenas para tráfego e canais que o DataForSEO não responde;
3. **uma ou duas fontes de voz do cliente**, escolhidas conforme o produto.

## 3. Instale a skill oficial no Codex

A [documentação oficial de skills do Codex](https://developers.openai.com/codex/skills) explica que uma skill é uma pasta com `SKILL.md` e recursos opcionais. Skills pessoais ficam em `~/.agents/skills`; o Codex detecta mudanças automaticamente e pode exigir reinício se a skill não aparecer.

A [documentação atual da AIsa](https://aisa.one/docs/agent-quickstart.md) publica este instalador para uso global no Codex. Ele exige Node.js 22.20.0 ou superior no momento desta verificação:

```bash
node --version
npx skills add AIsa-team/agent-skills --skill aisa --agent codex --global
```

O comando deve instalar somente a skill `aisa`. Não use `--all` se o objetivo é este tutorial.

Confirme a presença dos arquivos:

```bash
find "$HOME/.agents/skills/aisa" -maxdepth 2 -type f -print
```

O conjunto oficial atual contém `SKILL.md`, `LICENSE` e `agents/openai.yaml`. Abra o `SKILL.md` e revise instruções, comandos e ações permitidas antes de fornecer uma credencial.

Se a skill não aparecer no seletor do Codex após a instalação, reinicie o aplicativo. No Codex, você pode invocá-la explicitamente com `$aisa` ou selecioná-la em `/skills`. O `/aisa` mostrado na publicação pode pertencer a outra interface e não deve ser assumido como comando universal.

## 4. Instale e autentique a CLI

A skill usa a CLI para descobrir ferramentas, ler schemas, calcular preço e executar chamadas. A documentação atual pede `@aisa-one/cli` 0.5.0 ou posterior e informa Node.js 18 ou posterior para a CLI:

```bash
npm install -g @aisa-one/cli
aisa --version
aisa login --help
aisa login
aisa balance
```

O login pelo navegador é o caminho preferido. `aisa balance` comprova que a CLI conseguiu usar a autenticação e consultar a conta. `aisa whoami` é somente uma leitura local e não compro prova acesso protegido.

Regras para a chave:

- não cole a chave em uma conversa;
- não grave a chave em `AGENTS.md`, `SKILL.md`, scripts ou relatórios;
- não inclua a chave em repositórios;
- use o armazenamento criado pelo login ou `AISA_API_KEY` em um gerenciador de segredos;
- se a variável e a credencial armazenada forem diferentes, descubra qual fonte está ativa antes de alterar qualquer uma;
- crie quota e saldo compatíveis com o teto do estudo.

Uma alternativa é conectar o MCP remoto `tools.aisa.one/mcp` com OAuth. Segundo o quickstart da AIsa, a conexão só está operacional quando a autorização terminou e as quatro ferramentas de busca, schema, cotação e uso aparecem. Ver metadados do servidor ou um desafio HTTP 401 não comprova conexão utilizável.

## 5. Entenda o fluxo `search → schema → quote → call`

A skill oficial organiza o uso em quatro estágios:

```text
search → schema → quote → call
```

- **search:** encontra ferramentas que podem responder à tarefa;
- **schema:** retorna parâmetros e limites completos quando o resultado da busca não basta;
- **quote:** calcula o custo para chamadas e argumentos definidos;
- **call:** executa exatamente o lote cotado e autorizado.

Exemplo de descoberta, sem chamada de dados:

```bash
aisa search --input '{"query":"compare organic search demand for three SaaS domains"}' --json
```

Quando a busca informar que o schema completo é necessário, use o identificador retornado pela própria CLI. Não invente nome de ferramenta, endpoint ou argumento.

Modelo de cotação:

```bash
aisa quote --input '{
  "calls": [
    {
      "call_id": "c1",
      "tool": "<tool retornada pela busca>",
      "arguments": {"<campo>": "<valor>"}
    }
  ]
}' --json
```

A cotação não coleta os dados e não autoriza a execução. Se ela falhar, vier parcial ou não trouxer limite máximo documentado, não assuma custo zero.

## 6. Crie o plano de custo antes da pesquisa

O plano precisa expor a multiplicação completa. Por exemplo:

```text
3 domínios × 1 mês × 1 chamada de tráfego = 3 chamadas
3 domínios × 10 palavras-chave = até 30 linhas
5 palavras comuns × 1 SERP sem paginação = 5 chamadas
2 fontes sociais × 25 itens = até 50 itens
```

Exija esta tabela antes de executar:

| ID | Provedor | Ferramenta/endpoint | Escopo | Unidade cobrada | Quantidade máxima | Preço | Máximo USD |
|---|---|---|---|---|---:|---:|---:|
| c1 | DataForSEO | retornado pela CLI | 3 domínios, US/en | chamada ou linha | X | US$ Y | US$ Z |

O [guia de preços da AIsa](https://aisa.one/docs/guides/pricing.md) diz que alguns endpoints têm preço fixo por chamada e outros usam fórmulas baseadas em dimensões ou linhas. Similarweb é citado como caso de custo dinâmico. Leia o contrato do endpoint, incluindo os metadados de preço, antes de executar.

Defina estes limites:

- número de domínios;
- país e idioma;
- mês ou intervalo;
- granularidade;
- dispositivo;
- métricas solicitadas;
- limite de palavras ou comentários;
- número de páginas;
- número de tentativas;
- custo máximo total.

Não autorize paginação automática, repetição silenciosa nem expansão do período. Uma mudança de ferramenta, parâmetro ou escopo exige nova cotação.

## 7. Prompt para planejar e cotar a análise

Use este prompt primeiro. Ele deve terminar antes de qualquer chamada paga:

```text
Use a skill $aisa para planejar uma pesquisa de GTM sobre [MEU PRODUTO] e os
concorrentes [A, B, C]. A decisão é [DECISÃO].

Não execute chamadas pagas nesta etapa.

1. Verifique os domínios oficiais e registre como chegou a cada domínio.
2. Fixe Google Estados Unidos, inglês, desktop + mobile e o último mês completo
   disponível como base comparável. Se alguma fonte não suportar esses mesmos
   parâmetros, sinalize a diferença.
3. Use DataForSEO como fonte principal de palavras-chave e SERP.
4. Use Similarweb somente para visitas, qualidade e canais que a primeira fonte
   não responde.
5. Para cada domínio, limite a 10 palavras não relacionadas à marca.
6. Após deduplicar, limite a 5 palavras comuns para conferir a primeira página
   da SERP, sem paginação.
7. Descubra as ferramentas com `aisa search`, leia o schema completo quando
   necessário e não invente IDs ou preços.
8. Gere uma cotação com ferramenta, endpoint, argumentos, chamadas ou linhas,
   unidade de cobrança, preço e exposição máxima em USD.
9. Não repita chamadas, não pagine e não amplie o escopo.

Entregue apenas:
- domínios verificados;
- perguntas que cada fonte responderá;
- plano de chamadas;
- tabela de custo máximo;
- campos que serão salvos como evidência;
- limitações previstas.

Pare e aguarde uma autorização explícita para o lote e o teto apresentados.
```

Após revisar a cotação, autorize somente o que deseja executar. Exemplo:

```text
Autorizo apenas o lote cotado [IDENTIFICADOR OU RESUMO EXATO], com os mesmos
endpoints, argumentos, limites e exposição máxima total de US$ [VALOR].
Não autorizei paginação, repetição, troca de ferramenta nem expansão de escopo.
Salve respostas brutas e o custo realizado de cada chamada.
```

## 8. Produza a análise de tráfego e busca

Após a autorização, a execução deve preservar a resposta bruta de cada chamada. Não deixe o modelo gerar apenas uma síntese.

Estrutura recomendada:

```text
gtm-report/
├── README.md
├── scope.json
├── quotes/
│   └── approved-quote.json
├── raw/
│   ├── dataforseo/
│   └── similarweb/
├── normalized/
│   ├── domains.csv
│   ├── traffic.csv
│   ├── keywords.csv
│   └── serp.csv
├── costs.csv
└── report.html
```

Cada linha normalizada deve conter:

```text
provider, tool, endpoint, retrieved_at, period, country, language, device,
domain, metric, value, unit, source_file, estimated_or_observed, notes
```

### Leitura correta das métricas

O volume de busca do DataForSEO é aproximado e depende da combinação de localização e idioma. A [documentação do Keyword Overview](https://docs.dataforseo.com/v3/dataforseo_labs-google-keyword_overview-live/) informa que a base deriva de Google Ads, recebe atualização mensal e pode ser revisada pela própria fonte.

Os números de concorrentes do Similarweb devem ser chamados de **estimativas de tráfego**. Use o mesmo país, período, dispositivo e granularidade para comparar. Consulte a [documentação da API de tráfego da Similarweb](https://developers.similarweb.com/docs/similarweb-web-traffic-api) para conferir cobertura, período, granularidade e campos de cada endpoint.

Evite estas conclusões:

- “direto” significa necessariamente força de marca;
- maior volume estimado significa maior receita;
- dificuldade baixa garante classificação;
- CPC alto comprova disposição de compra;
- uma posição atual da SERP é estável;
- duas métricas de provedores diferentes são diretamente intercambiáveis.

## 9. Pesquise elogios e reclamações com amostragem explícita

Escolha as fontes conforme o produto:

- SaaS web: Reddit, X, YouTube, Trustpilot e Product Hunt;
- aplicativo móvel: Apple App Store, Google Play, Reddit e YouTube;
- produto visual: Instagram, TikTok, YouTube e comunidades específicas;
- B2B: fóruns do setor, avaliações, YouTube e conversas públicas relevantes.

Não use todas por padrão. Uma amostra pequena e comparável é mais auditável que centenas de itens sem critério.

Defina:

- janela de 90 ou 180 dias;
- quantidade máxima por empresa e fonte;
- idioma e mercado;
- consultas relacionadas à marca;
- regra de deduplicação;
- regra para spam, repost e conteúdo patrocinado;
- campos mínimos: data, URL, autor público, texto, fonte e produto;
- tratamento de dados pessoais e termos da plataforma.

## 10. Prompt para planejar a voz do cliente

```text
Use a skill $aisa para planejar uma comparação de feedback público recente sobre
[EMPRESAS]. O objetivo é identificar benefícios percebidos, reclamações
recorrentes e problemas que podem contribuir para cancelamento, reembolso ou
recomendação.

Não execute chamadas pagas nesta etapa.

1. Proponha no máximo duas fontes adequadas ao tipo de produto.
2. Use uma janela de [90] dias e limite de [25] itens por empresa por fonte.
3. Exija URL original, data, fonte e trecho representativo para cada item.
4. Defina deduplicação, remoção de spam e identificação de conteúdo patrocinado.
5. Preserve o texto original e crie uma tradução separada quando necessário.
6. Não infira sentimento, intenção, churn ou causa apenas pela nota.
7. Descubra ferramentas e schemas pela CLI e apresente uma cotação completa.
8. Não pagine, não repita e não amplie o escopo.

Entregue o plano amostral, as ferramentas, os argumentos, o máximo de itens, a
unidade de cobrança, o custo máximo em USD, os campos de evidência e os limites.
Pare antes da execução e aguarde autorização explícita.
```

Após autorizar o lote exato, use este contrato para a síntese:

```text
Analise apenas os registros coletados e salvos na pasta de evidências.

Para cada empresa, apresente:
- quantidade de itens por fonte e período;
- temas positivos e negativos, com contagem;
- no máximo três exemplos por tema, com data e URL;
- casos contraditórios;
- possíveis problemas de produto;
- hipóteses para pesquisa adicional.

Separe cada conclusão em:
1. EVIDÊNCIA: o que os registros mostram diretamente;
2. INFERÊNCIA: interpretação apoiada pela amostra;
3. HIPÓTESE: explicação que ainda precisa de teste.

Não trate frequência na amostra como prevalência em toda a base de clientes.
Não associe comentário a tráfego, receita, churn ou conversão sem outra fonte.
```

## 11. Cruze aquisição e voz do cliente

O cruzamento serve para criar hipóteses. Exemplo:

| Observação | Evidência | Inferência possível | Próximo teste |
|---|---|---|---|
| concorrente recebe busca por “sem marca d'água” | SERP e palavras-chave | remoção de marca pode orientar escolha | landing page e entrevista |
| reclamações citam exportação lenta | amostra de avaliações | desempenho pode prejudicar satisfação | medir tempo e entrevistar usuários |
| tráfego social estimado cresceu | Similarweb | campanha ou conteúdo pode ter contribuído | procurar campanhas no período |

Não escreva “as reclamações causaram queda de tráfego” apenas porque os dois fatos aparecem no mesmo mês.

## 12. Gere o relatório HTML

Peça um arquivo único que possa ser aberto localmente, sem carregar bibliotecas externas:

```text
Gere `gtm-report/report.html` como um único arquivo HTML, CSS e JavaScript.
Não use CDN, pixels, fontes remotas ou chamadas de rede.

Inclua:
1. escopo, data de corte e decisão;
2. cobertura por empresa, fonte e período;
3. tabela de tráfego estimado e qualidade de visita;
4. composição estimada de canais;
5. palavras não relacionadas à marca e intenção;
6. presença na primeira página da SERP;
7. temas positivos e negativos com tamanho da amostra;
8. evidências com links originais;
9. fatos, inferências e hipóteses em estilos visuais diferentes;
10. oportunidades priorizadas por impacto, confiança e esforço;
11. metodologia, custo realizado e limitações.

Toda métrica deve mostrar provedor, período, país, dispositivo, data de coleta e
arquivo de origem. Use “estimativa” no rótulo quando aplicável. Não invente dados
ausentes. Se um valor não estiver disponível, exiba “não coletado”.
```

O HTML é uma visualização. Os arquivos JSON e CSV continuam sendo a evidência que permite auditar o relatório.

## 13. Valide o resultado

### Instalação e autenticação

- [ ] A skill veio do repositório `AIsa-team/agent-skills`.
- [ ] A pasta possui `SKILL.md`, licença e metadados esperados.
- [ ] A chave não aparece em arquivos, histórico ou saída do Terminal.
- [ ] `aisa balance` confirmou autenticação sem expor o segredo.
- [ ] Versões da skill, CLI e commit foram registradas.

### Escopo e custo

- [ ] Domínios oficiais foram verificados.
- [ ] País, idioma, período, dispositivo e granularidade estão fixados.
- [ ] Cada endpoint e argumento veio de busca/schema atual.
- [ ] A cotação inclui todas as chamadas ou linhas possíveis.
- [ ] O máximo total cabe no teto aprovado.
- [ ] Não houve paginação, repetição ou expansão silenciosa.
- [ ] O custo realizado foi salvo por chamada.

### Evidência

- [ ] Respostas brutas foram preservadas.
- [ ] Cada métrica aponta para provedor e arquivo de origem.
- [ ] Estimativas estão rotuladas como estimativas.
- [ ] Comentários mantêm data e URL original.
- [ ] Tradução não substituiu o texto original.
- [ ] Tamanho e viés da amostra estão descritos.
- [ ] Fatos, inferências e hipóteses estão separados.

### Relatório

- [ ] O HTML abre sem internet.
- [ ] Não há bibliotecas ou pixels remotos.
- [ ] Empresas têm cobertura comparável ou diferenças explícitas.
- [ ] Ausência de dados aparece como “não coletado”.
- [ ] Recomendações apontam para evidência e próximo teste.
- [ ] Nenhuma correlação foi apresentada como causa.

## 14. Expanda somente depois do primeiro relatório

Depois de concluir um estudo pequeno, decida o próximo módulo pela lacuna encontrada:

- adicione Ahrefs ou Semrush se backlinks ou histórico de ranking forem decisivos;
- adicione WaveInflu se a estratégia aprovada incluir criadores;
- adicione Oxylabs ou DataForSEO para uma pergunta específica de visibilidade em respostas de IA;
- adicione Apollo somente quando houver finalidade legítima, campos necessários e processo de prospecção definido;
- crie monitoramento recorrente apenas depois de medir custo e utilidade de uma execução.

Mais fontes aumentam custo, diferenças metodológicas, obrigações de uso e trabalho de normalização. A vantagem da camada unificada aparece quando o estudo mantém pergunta, escopo e evidência sob controle.

## Fontes

Fonte de origem, recuperada pelo Agent Reach em 12 de setembro de 2026:

- [逸尘 — publicação sobre a AIsa como interface de dados para GTM](https://x.com/gengdaJ/status/2098293186292765046)
- [逸尘 — demonstração e prompts de tráfego, SEO e feedback](https://x.com/gengdaJ/status/2098252168625332263)

Documentação consultada:

- [AIsa — solução de go-to-market](https://aisa.one/solutions/go-to-market)
- [AIsa — quickstart para agentes](https://aisa.one/docs/agent-quickstart.md)
- [AIsa — preços e modelos de cobrança](https://aisa.one/docs/guides/pricing.md)
- [AIsa — termos de serviço](https://aisa.one/TOS)
- [AIsa — política de privacidade](https://aisa.one/privacy)
- [OpenAI Docs — criação, descoberta e instalação de skills no Codex](https://developers.openai.com/codex/skills)
- [DataForSEO — Keyword Overview](https://docs.dataforseo.com/v3/dataforseo_labs-google-keyword_overview-live/)
- [Similarweb — documentação da API de tráfego](https://developers.similarweb.com/docs/similarweb-web-traffic-api)
- [AIsa Team — repositório oficial de agent skills](https://github.com/AIsa-team/agent-skills), commit `bb70b34de56aff23cc3fcc4a8b30ea5e9da78821`

Os catálogos, preços, versões, endpoints e termos podem mudar. Refaça `search`, `schema` e `quote` no momento da pesquisa e trate a documentação do endpoint como contrato da chamada.
