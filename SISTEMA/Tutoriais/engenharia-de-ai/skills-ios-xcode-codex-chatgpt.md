---
title: "Skills antes do Codex tocar seu projeto Xcode: tutorial para iOS"
slug: skills-ios-xcode-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/PaulSolt/status/2098517910960402552
source_quote: https://x.com/PaulSolt/status/2042716870512353294
source_article: https://x.com/i/article/2042696610484781056
source_title: "Install These Skills Before Codex Touches Your Xcode Project"
source_author: "Paul Solt"
source_published_at: "2026-04-10"
captured_at: 2026-09-12
official_sources:
  - https://learn.chatgpt.com/docs/plugins
  - https://learn.chatgpt.com/docs/skills-and-plugins
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
  - https://github.com/openai/plugins/tree/main/plugins/build-ios-apps
  - https://github.com/openai/plugins/tree/main/plugins/build-macos-apps
tags:
  - tutorial
  - codex
  - chatgpt
  - ios
  - swift
  - swiftui
  - xcode
  - skills
---

# Skills antes do Codex tocar seu projeto Xcode: tutorial para iOS

O [post de Paul Solt](https://x.com/PaulSolt/status/2098517910960402552)
propõe construir um aplicativo iOS em um fim de semana e instalar skills que
ensinem o agente a trabalhar melhor com Swift, SwiftUI e Xcode. O post cita o
artigo [Install These Skills Before Codex Touches Your Xcode
Project](https://x.com/i/article/2042696610484781056), publicado em 10 de abril
de 2026.

O endereço canônico do artigo pode responder com erro fora de uma sessão do X.
O [post original que contém a citação](https://x.com/PaulSolt/status/2042716870512353294)
permanece como a referência navegável para o conteúdo.

A ideia central continua válida: uma skill pode fornecer ao Codex um processo,
referências e critérios de qualidade específicos. A lista, porém, precisa ser
lida como um catálogo, não como uma ordem para instalar tudo. Os pacotes de Paul
Hudson e Antoine van der Lee cobrem vários dos mesmos temas. Empilhar duas ou
três skills de SwiftUI na mesma tarefa pode criar regras concorrentes e gastar
contexto sem melhorar o código.

Este tutorial adota uma configuração simples:

1. plugin oficial **Build iOS Apps** como base operacional;
2. no máximo uma skill comunitária por domínio quando houver uma necessidade
   específica;
3. um `AGENTS.md` curto com o contrato real do projeto;
4. build, execução no Simulator e verificação visual como critérios de término.

O objetivo do fim de semana é um **MVP vertical que compila e funciona no
Simulator**. Distribuição na App Store, assinatura para dispositivo físico,
backend de produção e acabamento completo são etapas separadas.

## O que é oficial, comunitário e comercial

| Recurso | Origem | Uso principal | Observação |
|---|---|---|---|
| Build iOS Apps | OpenAI | SwiftUI, Simulator, depuração, performance, App Intents | Plugin oficial e primeira escolha deste tutorial |
| SwiftUI Pro e pacote Swift de Paul Hudson | Comunidade | SwiftUI, concorrência, testes e SwiftData | Skills separadas, com instalação seletiva |
| Skills de Antoine van der Lee | Comunidade | SwiftUI, concorrência, testes, Core Data e tempo de build | Escolha somente o domínio necessário |
| Regras de Krzysztof Zabłocki | Comunidade e curso comercial | Padrões gerais e carregamento contextual de regras | Os dois arquivos públicos não equivalem ao conjunto completo do curso |
| AppCreator | Produto externo | Scaffold e comandos de build padronizados | Não é requisito do Codex e o código-fonte não estava público no artigo |

A [documentação oficial de skills e
plugins](https://learn.chatgpt.com/docs/skills-and-plugins) define uma skill como
um fluxo reutilizável com instruções e recursos de apoio. Um plugin é um pacote
instalável que também pode incluir MCP, hooks e outras capacidades. A presença de
uma skill não instala Xcode, não cria um simulador e não torna um projeto
compilável por si só.

## O que mudou desde o artigo

O artigo de abril lista sete áreas no plugin oficial de iOS. Na captura deste
tutorial, em 12 de setembro de 2026, o repositório oficial contém nove skills:

- `ios-debugger-agent`;
- `ios-simulator-browser`;
- `ios-ettrace-performance`;
- `ios-memgraph-leaks`;
- `ios-app-intents`;
- `swiftui-liquid-glass`;
- `swiftui-performance-audit`;
- `swiftui-ui-patterns`;
- `swiftui-view-refactor`.

Confira a lista atual no [plugin Build iOS Apps da
OpenAI](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps).
Existe também um [plugin oficial separado para
macOS](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps), com
fluxos próprios de AppKit, janelas, SwiftPM, assinatura, empacotamento e
notarização. Não use o pacote de macOS como substituto do fluxo de Simulator do
iOS.

O artigo afirma que os plugins oficiais atualizam automaticamente. A
documentação pública consultada confirma o diretório de plugins, a instalação e
a necessidade de abrir uma sessão nova, mas não estabelece que toda instalação
local estará sempre na versão mais recente. Verifique a versão mostrada pelo
cliente antes de depender de uma skill recém-adicionada.

## 1. Defina um MVP que caiba no fim de semana

Uma skill não corrige escopo excessivo. Antes de abrir o Codex, escreva uma
frase que descreva a ação principal do aplicativo:

> O usuário cria um temporizador, inicia a contagem e recebe uma confirmação
> visual quando o tempo termina.

Depois limite a primeira versão:

| Decisão | Exemplo de MVP |
|---|---|
| Usuário | Uma pessoa usando o próprio iPhone |
| Jornada | Abrir → configurar → executar → concluir |
| Telas | Lista, editor e execução |
| Dados | Armazenamento local |
| Integrações | Nenhuma na primeira versão |
| Critério visual | Estados vazio, preenchido, carregando, erro e concluído |
| Critério técnico | Compila, abre no Simulator e conclui a jornada |

Adie login, sincronização, pagamentos, notificações remotas e painel web, salvo
quando um deles for a proposta central do app. Cada integração adiciona uma
fonte de falha que a skill de SwiftUI não resolve.

### Prompt para fechar o escopo

```text
Quero construir um MVP iOS em SwiftUI durante um fim de semana.

Ideia: [descreva em duas ou três frases]
Usuário principal: [quem]
Ação principal: [o que precisa concluir]
Dados necessários: [locais, API ou nenhum]
Versão mínima do iOS: [versão]

Transforme isso em uma única jornada vertical com no máximo três telas.
Entregue:
1. escopo incluído;
2. escopo adiado;
3. estados de cada tela;
4. modelo de dados mínimo;
5. critérios observáveis de conclusão.

Não escreva código ainda. Aponte qualquer dependência que impeça build ou teste
local.
```

## 2. Prepare o ambiente antes de instalar skills

No Terminal, confirme as ferramentas básicas:

```bash
xcodebuild -version
xcrun simctl list devices available
swift --version
git --version
node --version
npx --version
```

`node` e `npx` só são necessários para o método de instalação documentado por
algumas skills comunitárias. O plugin oficial pode ser instalado pelo diretório
de plugins do ChatGPT/Codex.

Os estados abaixo são diferentes:

- **Xcode instalado:** `xcodebuild -version` responde.
- **projeto descoberto:** o workspace, projeto, scheme e target foram
  identificados.
- **build válido:** o comando real terminou com sucesso.
- **app executável:** o bundle abriu no Simulator.
- **jornada verificada:** a ação principal funcionou na interface.
- **distribuição pronta:** assinatura, entitlements, archive e canal de entrega
  foram testados separadamente.

Não chame o projeto de pronto após apenas um build.

## 3. Crie ou abra o projeto e obtenha um baseline

Para um app novo, crie no Xcode um projeto iOS com SwiftUI. Use um nome sem
espaços para o target e mantenha a primeira versão sem dependências externas.
Antes de permitir edições, registre a estrutura que já funciona.

Descubra projetos e workspaces:

```bash
find . -maxdepth 3 \( -name '*.xcworkspace' -o -name '*.xcodeproj' \) -print
```

Liste schemes do arquivo correto:

```bash
xcodebuild -list -project '<App>.xcodeproj'
```

Se houver um workspace real, use `-workspace '<App>.xcworkspace'` no lugar de
`-project`. Não escolha automaticamente o workspace interno de um
`.xcodeproj`.

Faça um primeiro build usando um dispositivo que aparece na lista local:

```bash
xcodebuild \
  -project '<App>.xcodeproj' \
  -scheme '<Scheme>' \
  -destination 'platform=iOS Simulator,name=<Simulador disponível>' \
  build
```

Guarde o comando que passou. Ele será o recibo básico para as próximas mudanças.
Se o projeto já falha antes do agente tocar no código, registre o erro como
baseline; não atribua essa falha à primeira edição do Codex.

## 4. Instale primeiro o plugin oficial Build iOS Apps

Na aplicação desktop:

1. abra **Plugins**;
2. procure **Build iOS Apps**;
3. revise a descrição e os componentes;
4. instale o plugin;
5. abra uma nova tarefa do Codex no projeto.

No Codex CLI, digite:

```text
/plugins
```

Use o navegador para localizar e instalar o plugin, depois inicie uma sessão
nova. Esse é o procedimento atual descrito na [documentação oficial de
plugins](https://learn.chatgpt.com/docs/plugins).

O plugin oficial inclui um servidor MCP baseado em `xcodebuildmcp` para fluxos
de Simulator, depuração, logs e automação de interface. Plugin instalado,
servidor iniciado e build validado continuam sendo evidências diferentes. Na
primeira tarefa, peça ao Codex para informar quais capacidades estão realmente
disponíveis antes de depender delas.

### Teste de descoberta

```text
Inspecione este projeto iOS sem editar arquivos.

Identifique:
- workspace ou project correto;
- schemes compartilhados;
- target principal e targets de teste;
- versão mínima do iOS;
- padrão atual de estado e dependências;
- comando de build para um Simulator disponível;
- skills e ferramentas de iOS carregadas nesta sessão.

Execute somente verificações de leitura e um build baseline. Entregue os
comandos e resultados. Não proponha refatoração ainda.
```

## 5. Escolha uma skill comunitária somente quando houver uma lacuna

Comece com o plugin oficial. Adicione uma skill comunitária quando a tarefa
pedir uma profundidade que a base não ofereceu. Para a mesma área, escolha uma
família e teste o comportamento antes de instalar outra.

### Família de Paul Hudson

O [diretório Swift Agent
Skills](https://github.com/twostraws/swift-agent-skills) reúne skills de Swift e
Apple Platforms e inclui um aviso para revisar e confiar no conteúdo de
terceiros antes da instalação.

As quatro skills destacadas no artigo continuam em repositórios separados:

| Skill | Quando usar | Instalação documentada pelo repositório |
|---|---|---|
| SwiftUI Pro | APIs modernas, composição, acessibilidade e performance | `npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro` |
| Swift Concurrency Pro | `async/await`, actors, `Sendable` e migração Swift 6 | `npx skills add https://github.com/twostraws/swift-concurrency-agent-skill --skill swift-concurrency-pro` |
| Swift Testing Pro | macros, testes parametrizados e migração de XCTest | `npx skills add https://github.com/twostraws/swift-testing-agent-skill --skill swift-testing-pro` |
| SwiftData Pro | modelos, queries, predicates, migrações e CloudKit | `npx skills add https://github.com/twostraws/swiftdata-agent-skill --skill swiftdata-pro` |

Links diretos: [SwiftUI
Pro](https://github.com/twostraws/SwiftUI-Agent-Skill), [Swift Concurrency
Pro](https://github.com/twostraws/Swift-Concurrency-Agent-Skill), [Swift Testing
Pro](https://github.com/twostraws/Swift-Testing-Agent-Skill) e [SwiftData
Pro](https://github.com/twostraws/SwiftData-Agent-Skill).

Para um app pequeno com UI e armazenamento local, comece apenas com
`swiftui-pro`. Adicione `swiftdata-pro` quando o modelo persistente estiver
definido. Não carregue concorrência e testes em toda tarefa por precaução; use-os
quando o escopo tocar esses domínios.

### Família de Antoine van der Lee

Os repositórios de Antoine usam referências que carregam sob demanda. A família
inclui:

| Skill | Quando usar | Comando atual do README |
|---|---|---|
| SwiftUI Expert | Estado, composição, performance, Swift Charts e Liquid Glass | `npx skills add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill` |
| Swift Concurrency | Segurança de dados e migração para Swift 6 | `npx skills add https://github.com/avdlee/swift-concurrency-agent-skill --skill swift-concurrency` |
| Swift Testing Expert | Migração, paralelização e testes assíncronos | `npx skills add https://github.com/avdlee/swift-testing-agent-skill --skill swift-testing-expert` |
| Core Data Expert | Stack, contexts, fetches e migrações | `npx skills add https://github.com/avdlee/core-data-agent-skill --skill core-data-expert` |
| Xcode Build Optimization | Medição e correção de builds lentos | `npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill` |

Links diretos: [SwiftUI
Expert](https://github.com/AvdLee/SwiftUI-Agent-Skill), [Swift
Concurrency](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill), [Swift
Testing Expert](https://github.com/AvdLee/Swift-Testing-Agent-Skill), [Core Data
Expert](https://github.com/AvdLee/Core-Data-Agent-Skill) e [Xcode Build
Optimization](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill).

O pacote de otimização contém um orquestrador e cinco skills especialistas. O
README atual orienta instalar as seis juntas quando o orquestrador for usado.
Esse pacote é adequado para medir regressão de build em um projeto existente;
é excesso para a primeira tela de um MVP novo.

### Não instale as duas famílias de SwiftUI ao mesmo tempo

As duas são válidas, mas possuem escolhas próprias de arquitetura, gatilhos e
referências. Faça um teste controlado:

1. escolha uma view real e um problema observável;
2. instale uma skill;
3. abra uma sessão nova;
4. peça uma análise sem edição;
5. confira as referências citadas e a proposta;
6. aplique uma mudança pequena;
7. faça build e inspeção visual;
8. mantenha a skill somente se o resultado for melhor e reproduzível.

## 6. Audite qualquer skill de terceiro antes de instalá-la

O comando `npx skills add` é recomendado pelos repositórios comunitários acima,
mas continua executando uma ferramenta e copiando conteúdo de terceiros. Revise
o repositório no commit que você pretende usar.

```bash
git clone --depth 1 '<URL-do-repositório>' /tmp/skill-audit
git -C /tmp/skill-audit rev-parse HEAD
find /tmp/skill-audit -type f -not -path '*/.git/*' -print | sort
rg -n -i \
  'curl|wget|sudo|rm -rf|keychain|token|secret|hook|mcp|postinstall|preinstall' \
  /tmp/skill-audit
```

Leia, no mínimo:

- `SKILL.md` e arquivos de referência chamados por ele;
- `package.json`, scripts de instalação e manifests de plugin;
- arquivos de MCP e hooks;
- licença e histórico recente;
- comandos que a skill pode executar;
- caminhos que ela pode editar ou apagar.

Não trate muitos stars, presença em uma lista ou nome conhecido como revisão de
segurança. A própria coleção de Paul Hudson diz que estar no diretório não é
endosso.

### Verifique o resultado da instalação

Depois de instalar:

```bash
find ~/.codex/skills -maxdepth 2 -name SKILL.md -print | sort
```

Abra uma sessão nova e peça:

```text
Liste as skills relevantes para SwiftUI disponíveis nesta sessão. Para cada uma,
informe o nome exato, o gatilho e o caminho do SKILL.md carregado. Não edite o
projeto.
```

Arquivos copiados no disco não provam que a sessão atual carregou a skill.

## 7. Use regras gerais de Krzysztof Zabłocki com escopo

O artigo cita a abordagem de regras contextuais de Krzysztof Zabłocki e dois
arquivos públicos:

- [`general.md`](https://merowing.info/assets/files/general.md): diretrizes
  gerais de implementação;
- [`rule-loading.md`](https://merowing.info/assets/files/rule-loading.md): seleção
  de regras por contexto.

O texto completo sobre a abordagem está em [Stop Getting Average Code from Your
LLM](https://merowing.info/posts/stop-getting-average-code-from-your-llm/).
O conjunto completo de regras citado no artigo faz parte do curso Swifty Stack;
os dois arquivos públicos não contêm todo esse material.

Leia cada regra antes de incorporá-la. Converta apenas decisões que o seu projeto
realmente adota para o `AGENTS.md`. Não cole um sistema genérico inteiro sobre
um repositório que já possui arquitetura e convenções.

O [Inject](https://github.com/krzysztofzablocki/Inject) pode acelerar a
visualização de mudanças SwiftUI por hot reload, mas adiciona uma dependência e
um fluxo próprio. Instale-o somente quando a redução do ciclo de feedback
justificar essa dependência. Ele não substitui build limpo, teste ou execução do
app sem injeção.

## 8. Trate AppCreator como uma opção externa

O artigo apresenta AppCreator como uma ferramenta de scaffold com Makefiles,
`xcbeautify`, pastas buildable e padrões favoráveis a agentes. O download é
oferecido em uma [página externa de
cadastro](https://super-easy-apps.kit.com/app-creator), e o próprio artigo
informa que o projeto não estava no GitHub.

Isso muda a forma de avaliar:

- confira origem, assinatura e conteúdo do download;
- não execute scripts antes de lê-los;
- não use em um projeto existente sem revisar o diff;
- preserve uma cópia recuperável antes de alterar arquivos de projeto;
- confirme licença, política de atualização e suporte;
- mantenha um comando de build nativo documentado, mesmo que haja Makefile.

AppCreator pode ajudar a criar um projeto novo padronizado. Não é pré-requisito
para o Codex, para o plugin Build iOS Apps ou para compilar um projeto Xcode.

## 9. Crie um `AGENTS.md` curto para o projeto iOS

As skills fornecem conhecimento de domínio. O `AGENTS.md` registra decisões do
seu repositório: target, versão mínima, comandos, arquitetura existente e
critério de conclusão. Segundo a [documentação oficial de
`AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md), o
Codex lê uma cadeia de instruções da raiz até o diretório atual; instruções mais
próximas têm precedência.

Adapte este modelo na raiz do projeto:

```markdown
# AGENTS.md

## Escopo

- Aplicativo iOS em SwiftUI.
- Versão mínima: iOS [VERSÃO].
- Target principal: `[TARGET]`.
- Scheme de validação: `[SCHEME]`.

## Arquitetura

- Preserve a organização e o padrão de estado já usados no projeto.
- Prefira APIs nativas do SwiftUI compatíveis com a versão mínima.
- Mantenha estado local na view quando não houver compartilhamento real.
- Não adicione dependências sem explicar a necessidade e o impacto.
- Não altere signing, bundle identifier ou entitlements fora de uma tarefa que
  peça isso explicitamente.

## Fluxo de trabalho

- Antes de editar, leia os arquivos envolvidos e confira `git status --short`.
- Preserve alterações não relacionadas.
- Implemente uma jornada vertical por vez.
- Depois de cada etapa compilável, execute o build do scheme principal.
- Para mudanças visuais, abra a tela afetada no Simulator e inspecione os estados
  pedidos.

## Validação

- Build:
  `xcodebuild -project '[APP].xcodeproj' -scheme '[SCHEME]' -destination
  'platform=iOS Simulator,name=[SIMULADOR]' build`
- Testes: `[COMANDO DE TESTE OU "não configurado"]`.
- Uma tarefa termina com arquivos alterados, build, testes pertinentes e
  evidência da jornada no Simulator.
```

Não mantenha placeholders depois de adotar o arquivo. Um comando genérico que
ninguém executou ensina o agente a repetir uma hipótese.

## 10. Entregue a primeira jornada vertical

Abra uma tarefa nova do Codex na raiz do projeto e invoque somente a skill
necessária. No Codex, skills podem ser chamadas com `$nome-da-skill`; no
ChatGPT, a sintaxe explícita é `@nome-da-skill` quando a skill estiver disponível
naquela superfície.

### Etapa A: inventário e plano

```text
Use $swiftui-ui-patterns para planejar a primeira jornada vertical deste app.

Objetivo do usuário: [ação principal]
Telas incluídas: [lista]
Versão mínima do iOS: [versão]

Antes de editar:
1. leia o AGENTS.md e os arquivos relevantes;
2. identifique o padrão atual de estado, navegação e dependências;
3. confirme project/workspace, scheme e comando de build;
4. proponha a menor alteração que entrega a jornada completa.

Entregue o plano por arquivos, estados da interface e critérios observáveis.
Não crie arquitetura paralela nem dependência nova.
```

Se a skill instalada tiver outro nome, use o identificador exato mostrado pelo
cliente, como `$swiftui-pro` ou `$swiftui-expert-skill`.

### Etapa B: implementação

```text
Implemente a jornada aprovada do início ao fim.

Requisitos:
- preserve a arquitetura e o estilo existentes;
- use estado SwiftUI no escopo mais estreito que funcione;
- represente estados vazio, conteúdo, carregamento e erro quando aplicáveis;
- extraia subviews somente quando houver responsabilidade ou reutilização clara;
- não altere signing, entitlements, bundle identifier ou dependências;
- faça build depois de cada etapa compilável e corrija erros antes de continuar;
- ao final, execute os testes pertinentes e abra a tela no Simulator.

Conclua somente quando a ação principal funcionar. Informe arquivos alterados,
comandos executados, resultados e qualquer limitação real.
```

### Etapa C: revisão visual

```text
Revise a jornada implementada no Simulator nos estados:
- vazio;
- preenchido;
- carregando;
- erro;
- sucesso;
- texto grande;
- modo escuro, se suportado.

Verifique hierarquia, alinhamento, espaçamento, contraste, truncamento, área de
toque, teclado, navegação e acessibilidade básica. Corrija somente problemas
observados. Preserve a composição aprovada e refaça o build após as correções.
```

## 11. Adicione persistência, concorrência e testes na hora certa

### Persistência

Escolha **SwiftData** ou **Core Data** conforme o projeto. Não instale skills de
ambos para decidir por votação. Se o repositório já usa Core Data, preserve essa
fundação salvo uma migração solicitada. Em um MVP novo, SwiftData pode ser
adequado quando a versão mínima e os requisitos de migração permitirem.

```text
Use $swiftdata-pro para adicionar persistência local ao modelo [MODELO].
Antes de editar, confirme a versão mínima do iOS e o schema atual. Defina
identidade, obrigatoriedade, relacionamentos e estratégia mínima de migração.
Não adicione CloudKit nesta etapa. Implemente, faça build, teste criação/leitura/
atualização/exclusão e registre os resultados.
```

### Concorrência

Use uma skill de concorrência quando houver chamadas assíncronas, isolamento de
estado ou migração para Swift 6. Não transforme funções síncronas simples em uma
rede de actors sem necessidade.

```text
Use $swift-concurrency-pro para revisar somente o fluxo [FLUXO]. Identifique
isolamento esperado, pontos de suspensão, cancelamento e acesso a estado de UI.
Faça a menor correção que elimine warnings ou riscos observados. Compile com as
configurações reais do projeto e não faça uma migração ampla fora deste fluxo.
```

### Testes

Primeiro teste regra de negócio e transformação de dados. Evite testes que apenas
repitam a implementação de uma view estática.

```text
Use $swift-testing-pro para adicionar testes significativos à regra [REGRA].
Cubra caminho principal, limite e falha. Use Swift Testing se ele já estiver
adotado e for compatível com o target; preserve XCTest onde a migração não faz
parte desta tarefa. Execute o target de teste e corrija qualquer flakiness
introduzida.
```

## 12. Use ChatGPT e Codex em papéis diferentes

O ChatGPT pode ajudar a fechar produto, revisar uma jornada, preparar textos,
comparar opções e usar skills disponíveis no diretório universal. O Codex local
é o ambiente adequado para ler o repositório, editar arquivos, executar
`xcodebuild` e trabalhar com o Simulator.

Instalar uma skill local via `npx` no Mac não prova que ela apareceu em um chat
web do ChatGPT. Plugins do diretório público são compartilhados entre
superfícies suportadas, mas uma skill de filesystem e uma skill instalada no
workspace possuem ciclos de vida distintos.

Um fluxo simples:

1. use ChatGPT para transformar a ideia em escopo e critérios;
2. registre as decisões no repositório;
3. use Codex local para implementar e validar;
4. volte ao ChatGPT apenas quando precisar revisar comunicação ou produto;
5. mantenha build e Simulator como recibos técnicos.

## 13. Diagnóstico de falhas comuns

### A skill não aparece

- confirme o nome da pasta e do `SKILL.md`;
- verifique o frontmatter da skill;
- abra uma sessão nova;
- use o nome exato após `$`;
- diferencie instalação local, plugin e skill de workspace.

### O agente escreve API indisponível

- confirme a versão mínima do iOS;
- peça a disponibilidade da API usada;
- use uma skill de SwiftUI por vez;
- compile imediatamente após a mudança;
- consulte documentação atual da Apple para a API específica.

### O build funciona no Terminal e falha no agente

- compare diretório atual, Xcode selecionado, scheme e destination;
- confira variáveis de ambiente e permissões;
- não presuma que MCP está ativo apenas porque o plugin está instalado;
- execute o mesmo comando em ambos os ambientes.

### O agente cria arquivos que o target não compila

- confirme se o projeto usa grupos sincronizados/buildable folders;
- verifique target membership;
- não regenere o projeto inteiro para corrigir um único arquivo;
- registre no `AGENTS.md` como novos arquivos entram no target.

### A interface parece genérica

- forneça finalidade, usuário, estados e conteúdo real da tela;
- peça uma composição antes de detalhes cosméticos;
- use dados plausíveis em previews;
- confira a tela no Simulator;
- corrija um problema visual por vez.

### As skills entram em conflito

- invoque explicitamente uma única skill;
- remova ou desabilite a duplicada;
- mova decisões permanentes do projeto para um `AGENTS.md` curto;
- reinicie a sessão e repita a mesma tarefa de avaliação.

## 14. Checklist de conclusão do fim de semana

### Produto

- [ ] A ação principal cabe em uma frase.
- [ ] O MVP tem no máximo três telas principais.
- [ ] O escopo adiado está escrito.
- [ ] Estados vazio, conteúdo, erro e sucesso foram definidos quando aplicáveis.

### Ambiente e instruções

- [ ] Xcode, Swift e Simulator foram identificados.
- [ ] O baseline foi executado antes das mudanças.
- [ ] Build iOS Apps foi instalado e descoberto em uma sessão nova.
- [ ] No máximo uma skill comunitária foi escolhida por domínio.
- [ ] Toda skill de terceiro foi revisada antes da instalação.
- [ ] O `AGENTS.md` contém comandos reais e não possui placeholders.

### Implementação

- [ ] A jornada principal foi implementada de ponta a ponta.
- [ ] O projeto compila no scheme e destination registrados.
- [ ] Os testes pertinentes passaram.
- [ ] O app abriu no Simulator.
- [ ] A ação principal foi exercitada na interface.
- [ ] Estados visuais relevantes foram inspecionados.
- [ ] O diff final não contém mudanças fora do escopo.

### Limites da entrega

- [ ] Build local não foi descrito como publicação.
- [ ] Simulator não foi descrito como teste em dispositivo físico.
- [ ] Assinatura e entitlements não foram alterados incidentalmente.
- [ ] Dependências externas e dados reais foram tratados como etapas próprias.
- [ ] Limitações restantes foram registradas sem fabricar sucesso.

## Catálogo verificado nesta captura

Os repositórios abaixo estavam ativos e tiveram atualização ou confirmação de
conteúdo verificada em 12 de setembro de 2026. Use os links para conferir o
estado atual antes de instalar:

- [Swift Agent Skills, de Paul Hudson](https://github.com/twostraws/swift-agent-skills);
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill);
- [Swift Concurrency Pro](https://github.com/twostraws/Swift-Concurrency-Agent-Skill);
- [Swift Testing Pro](https://github.com/twostraws/Swift-Testing-Agent-Skill);
- [SwiftData Pro](https://github.com/twostraws/SwiftData-Agent-Skill);
- [SwiftUI Expert](https://github.com/AvdLee/SwiftUI-Agent-Skill);
- [Swift Concurrency](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill);
- [Swift Testing Expert](https://github.com/AvdLee/Swift-Testing-Agent-Skill);
- [Core Data Expert](https://github.com/AvdLee/Core-Data-Agent-Skill);
- [Xcode Build Optimization](https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill);
- [plugins oficiais da OpenAI](https://github.com/openai/plugins);
- [Codex Monitor](https://github.com/Dimillian/CodexMonitor);
- [Inject](https://github.com/krzysztofzablocki/Inject).

Skills ajudam o agente a escolher processos e APIs melhores. O critério final
continua concreto: o código precisa compilar, o app precisa abrir e a jornada
precisa funcionar no ambiente que você declarou suportar.
