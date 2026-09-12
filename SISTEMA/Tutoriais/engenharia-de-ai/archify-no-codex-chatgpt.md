---
title: "Archify no Codex/ChatGPT: instalação e uso avançado"
slug: archify-no-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://github.com/tt-a1i/archify
source_commit: 18911058008f17dc065af23a2cdc9bfeff6d3f7a
source_version: v2.17.0-dev.1
captured_at: 2026-09-10
---

# Archify no Codex/ChatGPT: instalação e uso avançado

O Archify é uma Skill que transforma uma descrição de sistema ou um repositório em um mapa interativo de arquitetura, workflow, sequência, fluxo de dados ou ciclo de vida. O agente escreve uma especificação JSON tipada; o Archify valida essa especificação e gera um HTML/SVG autocontido, com exportação para PNG, JPEG, WebP, SVG, WebM e cartão de compartilhamento 1200×630.

Fonte do pacote: [tt-a1i/archify](https://github.com/tt-a1i/archify), commit `18911058008f17dc065af23a2cdc9bfeff6d3f7a`. A versão consultada do repositório é `v2.17.0-dev.1`; comandos e caminhos podem mudar em versões futuras.

## O que a Skill faz

O Archify é indicado quando você precisa visualizar:

- componentes, serviços, bancos, filas, fronteiras de segurança e dependências externas;
- processos, aprovações, chamadas de ferramentas, CI/CD e runbooks;
- sequências de chamadas API, autenticação, cache, retornos e operações assíncronas;
- pipelines, ETL/ELT, linhagem, PII, armazenamentos e consumidores;
- estados, esperas, retries, cancelamentos e resultados terminais;
- um `flowchart`, `sequenceDiagram` ou `stateDiagram` do Mermaid convertido para uma especificação Archify nova.

Ele não é um editor WYSIWYG, um serviço hospedado de compartilhamento, um auto-layout genérico nem um tema do Mermaid. O resultado é um artefato de comunicação fundamentado nos fatos que você forneceu ou que o agente conseguiu verificar no repositório.

## Antes de instalar

Você precisa de:

- Codex Desktop/Codex CLI com acesso às Skills locais;
- Node.js 18 ou superior (`node --version`);
- `npx` disponível para o instalador de Skills;
- acesso ao GitHub para baixar o pacote.

O pacote do Archify não exige `npm install` para executar os comandos da Skill. Depois da instalação, o diagnóstico oficial é feito com `node bin/archify.mjs doctor`.

## Instalação no Codex

### Método recomendado: instalador `skills`

No Terminal, execute:

```bash
npx -y skills add tt-a1i/archify --skill archify --agent codex --global --copy --yes
```

O comando instala a Skill globalmente para o agente `codex` e copia os arquivos em vez de criar um link simbólico. O README do projeto também oferece a forma curta:

```bash
npx skills add tt-a1i/archify -g
```

A forma explícita é preferível quando você tem mais de um agente instalado, porque deixa claro que o destino é o Codex e que a instalação é global.

Feche e abra novamente o app do Codex para que o catálogo local de Skills seja recarregado. Verifique se existe um destes arquivos, conforme a configuração da sua instalação:

```bash
ls ~/.codex/skills/archify/SKILL.md
ls ~/.agents/skills/archify/SKILL.md
```

O diretório precisa conter `SKILL.md`, `bin/`, `schemas/`, `examples/`, `references/` e os demais arquivos do pacote. Ter apenas o README ou apenas o `SKILL.md` não instala o renderer e os validadores completos.

### Fallback manual para o app do Codex

Se o instalador informar que copiou a Skill para outro agente, baixe o repositório e copie a subpasta `archify` para o diretório global de Skills usado pelo seu Codex:

```bash
git clone --depth 1 https://github.com/tt-a1i/archify /tmp/archify
mkdir -p ~/.codex/skills/archify
cp -R /tmp/archify/archify/. ~/.codex/skills/archify/
```

Depois, reinicie o Codex e confira:

```bash
node ~/.codex/skills/archify/bin/archify.mjs doctor
```

Se a sua instalação usa `~/.agents/skills` como diretório global, aplique os mesmos comandos trocando apenas o prefixo do destino. Não misture cópias de versões diferentes: mantenha uma única pasta `archify` visível para o agente que você usa.

### Uso sem instalar

Para gerar um prompt de uso sem copiar a Skill, o pacote `skills` oferece:

```bash
npx skills use tt-a1i/archify@archify --agent codex
```

Isso é útil para experimentar a instrução em uma sessão; os binários e os exemplos locais continuam indisponíveis quando a Skill não está instalada.

## E no ChatGPT?

O pacote documenta instalação completa para Codex CLI, Claude Code, OpenCode e Raven. Para uma interface ChatGPT que esteja executando o Codex localmente, use a instalação global acima: a Skill é carregada pelo runtime do Codex, não como um app separado do catálogo de conectores.

No ChatGPT sem runtime local de Node.js, a alternativa é anexar `archify.zip` ao contexto ou ao conhecimento do projeto e pedir uma especificação/diagrama. Isso oferece um fallback orientado por prompt, mas não garante que `doctor`, `validate`, `deliver`, exportações ou `visual-check` possam ser executados no sandbox. Não trate um HTML produzido pelo modelo sem validação como um artefato aprovado.

O repositório menciona upload em **Settings → Capabilities → Skills** para Claude.ai; essa instrução não deve ser apresentada como uma tela existente em todas as contas ChatGPT. Se a sua conta expuser uma área equivalente para Skills, envie o `archify.zip` completo e confirme no ambiente se o Node.js está disponível.

## Como chamar a Skill

Você pode ser explícito no primeiro pedido:

```text
Use a Skill Archify. Crie um diagrama de arquitetura em português para este sistema.
```

A descrição da Skill também permite ativação por intenção. Ainda assim, escrever “use Archify” reduz ambiguidades e deixa claro que você quer um artefato verificável, não somente uma explicação textual.

## Escolha o tipo certo

| Tipo | Use quando | Informe no pedido |
|---|---|---|
| `architecture` | Componentes, serviços, armazenamento, cloud e fronteiras | escopo, componentes centrais e caminho principal |
| `workflow` | Processos, aprovações, tool calls, CI/CD e runbooks | participantes, ordem, ramificações e exceções |
| `sequence` | Chamadas API, cache, autenticação e async | chamadores, chamados, retornos e tempo |
| `dataflow` | Pipelines, ETL/ELT, linhagem e sensibilidade | fontes, transformações, stores e fronteiras |
| `lifecycle` | Estados, retries, esperas e encerramento | estados, eventos, retries e cancelamentos |

Quando houver dúvida, peça ao CLI uma classificação estrutural:

```bash
node bin/archify.mjs guide "Mostrar uma requisição API com cache Redis e fallback"
node bin/archify.mjs guide "Mapear tópicos Kafka, consumer groups, replay e DLQ" --json
```

O `guide` orienta o tipo e a forma da especificação; os exemplos retornados são referências de estrutura, não fatos para copiar.

## Primeiro diagrama sem repositório

Comece com uma descrição curta, um caminho principal e poucas ramificações:

```text
Use Archify para desenhar este fluxo de arquitetura:
Browser -> API -> cache Redis -> fallback PostgreSQL.

Tipo: architecture.
Idioma do conteúdo: pt-BR.
Mostre os quatro componentes, o caminho principal, a fronteira externa e o que acontece quando o cache falha.
Use visual_preset classic e qualidade showcase.
```

O agente deve criar a especificação JSON antes de inspecionar internals do renderer. Para uma primeira versão, mantenha no máximo 12 nós primários, rótulos curtos, uma hierarquia evidente e rotas automáticas. Não peça coordenadas exatas no prompt.

## Diagrama baseado em código real

Abra o projeto no Codex e peça evidência somente quando o mapa precisar refletir o código:

```text
Analise este repositório e use Archify para criar um diagrama de arquitetura de runtime.
Mostre 8–12 componentes centrais, um caminho primário, dependências externas e fronteiras de confiança.
Coloque detalhes de suporte em cards em vez de adicionar mais arestas.
Marque a origem apenas nos nós que realmente puder verificar no commit atual.
```

A Skill deve preservar nomes de produtos, identificadores, comandos, protocolos e rotas de API. A evidência de repositório é opcional: não invente arquivos, linhas, impacto em produção ou topologia de infraestrutura viva.

Quando uma fonte for solicitada, o Archify pode marcar nós de arquitetura como `SRC n` e abrir arquivos e linhas verificados em um commit público. Isso comprova a origem do trecho mapeado; não comprova que o sistema está funcionando em produção.

## O ciclo correto: gerar, validar, entregar e revisar

O fluxo confiável separa quatro etapas:

1. **Gerar:** o agente cria JSON IR tipado a partir do pedido.
2. **Validar:** schemas, layout, HTML/SVG, rotas e folgas de rótulos são verificados.
3. **Entregar:** somente uma especificação aprovada substitui atomicamente o HTML anterior.
4. **Revisar no navegador:** `visual-check` coleta evidência automatizada do HTML entregue, sem rerenderizá-lo.

Exemplo para uma arquitetura:

```bash
cd ~/.codex/skills/archify
node bin/archify.mjs validate architecture /caminho/candidato.json --quality showcase --json
node bin/archify.mjs deliver architecture /caminho/candidato.json /caminho/arquitetura.html --quality showcase --json
node bin/archify.mjs visual-check /caminho/arquitetura.html --json
```

Para `workflow`, `sequence`, `dataflow` ou `lifecycle`, substitua o tipo no comando. Um passe `showcase` deve apresentar os nove checks de artefato, zero erros de composição e zero avisos. Um recibo com somente quatro checks é validação básica, não aceitação showcase.

Depois de um `deliver` bem-sucedido, o recibo traz hashes SHA-256 e bytes da especificação e do HTML. Guarde esse JSON junto do artefato. `deliver` demonstra integridade determinística; `visual-check` demonstra comportamento limitado no navegador; nenhum dos dois substitui uma revisão visual humana.

Para uma sessão de edição ao vivo, use `preview` apenas quando fizer sentido:

```bash
node bin/archify.mjs preview workflow /caminho/candidato.json /caminho/workflow.html --quality showcase --no-open
```

O modo `preview` observa um JSON em loopback (`127.0.0.1`), mantém o último resultado válido quando uma gravação falha e termina com `Ctrl-C`. Ele não é necessário para uma entrega única.

## Como corrigir uma falha sem degradar o mapa

Após cada edição, rode `validate`. Se houver diagnóstico:

1. leia o `code`, `subject` e `evidence` exatos em `diagnostics[]`;
2. aplique somente os `supportedFixes` indicados para aquele sujeito;
3. corrija uma causa por vez e valide novamente;
4. preserve o significado das relações e dos rótulos;
5. pare se duas rodadas consecutivas não reduzirem o melhor número de erros e relate o diagnóstico pendente.

Não adicione `via`, `channelX`, `channelY` ou `labelAt` preventivamente. Comece pelas rotas automáticas; use no máximo um controle geométrico diagnosticado por reparo. Não remova um rótulo semanticamente importante apenas para fazer a geometria passar.

Quando a validação final passar, considere a especificação congelada. Edite uma cópia e repita o ciclo se precisar alterar conteúdo depois do passe final.

## Mermaid: preserve significado, refaça a autoria

Ao receber Mermaid, use a topologia e o significado como entrada:

- `flowchart` ou `graph` → `workflow`, ou `architecture` se for um mapa de componentes;
- `sequenceDiagram` → `sequence`;
- `stateDiagram` → `lifecycle`.

Peça ao agente para criar JSON Archify novo. Não converta cegamente estilos, cores ou coordenadas do Mermaid. O Archify valida sua própria geometria, cria rotas semânticas e mantém o artefato explorável.

## Use o viewer ao máximo

Depois de abrir o HTML entregue, o viewer oferece:

| Ação | Atalho |
|---|---|
| Abrir o guia de diagramas | `?` |
| Buscar e focar um nó | `/` |
| Ver alcance autorado upstream/downstream | foco no nó → `Upstream` / `Downstream` |
| Investigar uma rota direcionada | `R` ou `PATH` |
| Comparar papéis semânticos | `L` ou `LENS` |
| Abrir o radar geral | `M` ou `MAP` |
| Reproduzir uma história ou trocar capítulo | `P`, `[` e `]` |
| Entrar no modo apresentação | `F` |
| Alternar preset visual, tema e Export | `S`, `T` e `E` |
| Aproximar, afastar e redefinir zoom | `+`, `-` e `0` |

O viewer também aceita links estáveis com `#focus=<id>`, `#focus=<id>&reach=upstream|downstream`, `#relation=<id>`, `#route=<source>~<target>`, `#lens=<kind>~<kind>` e `#view=<view-id>`. A animação é finita, respeita `prefers-reduced-motion` e não entra nos exports canônicos.

O menu **Export** gera PNG, JPEG, WebP, SVG e WebM. Use **Copy Share Card** para o cartão 1200×630 de README, release ou post. Use **Route Share Card** e **Reach Share Card** somente depois de uma rota ou alcance autorado estar selecionado; esses cartões não afirmam impacto em runtime.

## Qualidade visual e idioma

Para uma entrega de apresentação, use:

```json
{
  "meta": {
    "quality_profile": "showcase",
    "animation": "trace",
    "visual_preset": "signal-flow"
  }
}
```

`animation: "trace"` é opcional e deve ser usado quando uma demonstração ou apresentação pedir movimento. O preset padrão é `classic`; `signal-flow`, `blueprint` e `editorial` devem ser escolhas conscientes. Tema claro/escuro e preset visual são controles separados.

O conteúdo autorado pode ficar em pt-BR. O renderer traduz somente superfícies próprias do viewer para `en` ou `zh-CN`; `meta.locale` não traduz seus nós, arestas ou cards. Para pt-BR, omita `meta.locale` e informe que a UI fixa do viewer pode permanecer em inglês.

## Identidade de marcas

Se um nó representa um produto real, use um ID de marca embutido quando existir. Se não existir e você recebeu a URL oficial do produto, capture a marca com digest fixo antes de autorar:

```bash
node bin/archify.mjs brands "Nome do produto" --json
node bin/archify.mjs brands capture "https://produto.example" --json
```

Nunca infira uma marca a partir de um papel genérico como “database”, nem use um selo para substituir o tipo semântico, o rótulo ou os fatos das relações.

## Diagnóstico e manutenção

Após instalar:

```bash
node bin/archify.mjs doctor
node bin/archify.mjs demo /tmp/archify-demo
```

Depois que o primeiro candidato existir, o pacote recomenda executar uma vez o verificador de atualização:

```bash
node scripts/check-update.mjs
```

Esse verificador apenas informa o estado; ele não baixa nem instala atualização. Se você precisa de operação sem rede, use a configuração documentada:

```bash
ARCHIFY_UPDATE_CHECK_DISABLED=1 node bin/archify.mjs doctor
```

O servidor do manifesto recebe metadados HTTP normais quando o check está ativo, mas não recebe versão, prompts, dados de projeto, conta ou dispositivo. A decisão de atualizar permanece sua.

## Prompts prontos para obter bons resultados

### Arquitetura de runtime

```text
Use Archify, tipo architecture, para mapear o runtime deste repositório.
Mostre o caminho Browser → API → serviços internos → banco principal.
Inclua dependências externas e fronteiras de confiança.
Use 8–12 nós primários, rótulos curtos e cards para detalhes.
Não invente conexões que não aparecem no código.
Valide com quality_profile showcase e entregue o HTML.
```

### Workflow de deploy

```text
Use Archify, tipo workflow, para representar o deploy.
Mostre commit, checks, aprovação, deploy, smoke test, rollback e os pontos de bloqueio.
Separe o caminho feliz das exceções e identifique quem executa cada etapa.
Mantenha uma única rota principal e valide antes de entregar.
```

### Sequência de cache

```text
Use Archify, tipo sequence, para uma requisição com cache.
Mostre Browser, API, Redis e PostgreSQL; inclua hit, miss, retorno e timeout.
Não transforme cards em novas mensagens e não suponha latência que não foi fornecida.
```

### Fluxo de dados com sensibilidade

```text
Use Archify, tipo dataflow, para mapear a origem dos eventos até o warehouse.
Marque PII, transformações, armazenamentos e consumidores.
Mostre as fronteiras de confiança e diferencie dado observado de dado inferido.
```

### Ciclo de vida de um job

```text
Use Archify, tipo lifecycle, para o job de processamento.
Inclua queued, running, waiting, retry, failed e completed, com eventos e cancelamento.
Use failure somente quando existir uma transição real de retorno ou encerramento.
```

## Checklist final

- [ ] Node.js 18+ e `SKILL.md` estão acessíveis no runtime do Codex.
- [ ] O tipo do diagrama corresponde à pergunta.
- [ ] O conteúdo tem idioma e nomes solicitados, sem traduzir identificadores.
- [ ] Existe um caminho principal claro e no máximo 12 nós primários.
- [ ] `meta.quality_profile` está exatamente como `showcase` quando a entrega exige qualidade de apresentação.
- [ ] `validate --quality showcase --json` passou com nove checks, zero erros de composição e zero avisos.
- [ ] `deliver --json` passou e o HTML foi gravado no caminho informado.
- [ ] `visual-check` foi executado no HTML entregue, quando evidência de navegador era necessária.
- [ ] A revisão visual humana foi registrada separadamente da validação automatizada.
- [ ] Nenhum resultado afirma runtime, impacto, topologia viva ou segurança que não esteja autorado e evidenciado.

Referências técnicas: [`archify/SKILL.md`](https://github.com/tt-a1i/archify/blob/18911058008f17dc065af23a2cdc9bfeff6d3f7a/archify/SKILL.md), [`README.md`](https://github.com/tt-a1i/archify/blob/18911058008f17dc065af23a2cdc9bfeff6d3f7a/README.md), [`schemas/README.md`](https://github.com/tt-a1i/archify/blob/18911058008f17dc065af23a2cdc9bfeff6d3f7a/archify/schemas/README.md) e [`references/delivery-contract.md`](https://github.com/tt-a1i/archify/blob/18911058008f17dc065af23a2cdc9bfeff6d3f7a/archify/references/delivery-contract.md).
