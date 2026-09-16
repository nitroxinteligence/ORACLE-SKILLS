---
title: "Como configurar as skills de engenharia de Matt Pocock em um repositório"
slug: configurar-skills-matt-pocock-em-um-repositorio
language: pt-BR
type: tutorial
category: engenharia-de-ai
subcategory: skills-de-agentes
source: https://www.aihero.dev/skills-setup-matt-pocock-skills
source_title: "The /setup-matt-pocock-skills Skill"
source_author: "Matt Pocock (AI Hero)"
source_updated_at: 2026-08-24
source_repository: https://github.com/mattpocock/skills
source_skill: skills/engineering/setup-matt-pocock-skills
captured_at: 2026-09-16
capture_method: web-reader+github-source
related_skill: "../../../skills/codigo/matt-pocock/01-getting-started/setup-matt-pocock-skills/SKILL.md"
tags:
  - matt-pocock
  - skills
  - agentes-de-codigo
  - codex
  - engenharia-de-software
  - issue-tracker
  - triagem
  - documentacao-de-dominio
---

# Como configurar as skills de engenharia de Matt Pocock em um repositório

A skill `setup-matt-pocock-skills` prepara um repositório para que as outras
skills de engenharia saibam como trabalhar nele. Ela registra três decisões:

1. onde os tickets do projeto são mantidos;
2. quais nomes representam os cinco estados de triagem;
3. onde ficam o contexto de domínio e os registros de decisão.

Essas respostas são gravadas como Markdown dentro do próprio repositório. As
outras skills consultam esses arquivos durante a execução, evitando adivinhar
como o projeto organiza trabalho, documentação e decisões.

```text
repositório ainda não configurado
→ inspeção da estrutura atual
→ escolha do sistema de tickets
→ definição dos rótulos de triagem
→ definição da documentação de domínio
→ revisão do plano
→ gravação em docs/agents/ e AGENTS.md ou CLAUDE.md
```

## Quando usar

Execute a configuração uma vez em cada repositório, antes de usar skills como:

- `triage`;
- `to-spec`;
- `to-tickets`;
- `wayfinder`;
- `domain-modeling`.

Também vale executá-la em projetos existentes. A skill primeiro lê o que já
está presente e deve preservar instruções, documentos e convenções anteriores.

No conjunto original, essa é uma skill de acionamento explícito. Inicie o fluxo
quando quiser configurar o repositório; não dependa de outra skill para chamá-la
automaticamente.

## O que será criado

| Arquivo | Função |
|---|---|
| `docs/agents/issue-tracker.md` | descreve onde os tickets vivem e como o agente deve operá-los |
| `docs/agents/domain.md` | define onde ficam `CONTEXT.md`, mapas de contexto e ADRs |
| `docs/agents/triage-labels.md` | relaciona os cinco papéis de triagem aos rótulos reais do projeto |
| bloco `## Agent skills` | aponta o agente para os arquivos acima |

O arquivo de rótulos só é necessário quando a skill `triage` está instalada.

## 1. Instale ou localize a skill

No Obsidian OS, a skill está em:

```text
SISTEMA/skills/codigo/matt-pocock/01-getting-started/setup-matt-pocock-skills/SKILL.md
```

Em outro ambiente compatível com o instalador do skills.sh, a instalação
individual apresentada pela página é:

```bash
npx skills@latest add mattpocock/skills --skill=setup-matt-pocock-skills
```

Para instalar todo o conjunto do autor:

```bash
npx skills@latest add mattpocock/skills
```

Instalar a skill disponibiliza o procedimento. Isso ainda não configura um
projeto específico; a configuração acontece quando a skill é executada dentro
do repositório desejado.

## 2. Inspecione o repositório

Antes de escrever, a skill deve verificar:

- os remotos do Git e o arquivo `.git/config`;
- `AGENTS.md` e `CLAUDE.md`;
- `CONTEXT.md` e `CONTEXT-MAP.md`;
- `docs/adr/` e diretórios de ADR dentro de pacotes;
- `docs/agents/`, caso uma configuração anterior já exista;
- `.scratch/`, que pode indicar tickets locais em Markdown;
- se a skill `triage` está disponível;
- sinais reais de monorepo, como workspaces ou vários pacotes independentes.

Essa leitura evita criar uma segunda convenção paralela ou substituir arquivos
que o projeto já usa.

## 3. Escolha onde os tickets vivem

A escolha deve refletir o fluxo real do repositório.

| Opção | Onde os tickets ficam | Dependência |
|---|---|---|
| GitHub | GitHub Issues do próprio repositório | CLI `gh` autenticada |
| GitLab | GitLab Issues | CLI `glab` autenticada |
| Markdown local | `.scratch/<feature>/` | nenhuma integração externa |
| Outro | Jira, Linear, Azure DevOps, Beads ou sistema próprio | descrição operacional e ferramenta correspondente |

Se o remoto aponta para o GitHub, GitHub Issues costuma ser a recomendação. Se
o projeto não possui remoto ou é estritamente pessoal, Markdown local pode ser
mais simples.

Não misture GitHub Issues e `.scratch/` como duas fontes oficiais para o mesmo
trabalho. Escolha uma fonte principal para que as skills encontrem o mesmo
estado.

## 4. Defina os rótulos de triagem

Quando `triage` está instalada, o padrão usa cinco papéis:

| Papel | Rótulo padrão | Significado |
|---|---|---|
| entrada | `needs-triage` | item ainda não analisado |
| informação | `needs-info` | faltam dados para continuar |
| agente | `ready-for-agent` | pode ser executado por agente |
| pessoa | `ready-for-human` | requer decisão ou trabalho humano |
| encerramento | `wontfix` | não será implementado |

O arquivo `triage-labels.md` é um mapeamento. Ele não cria esses rótulos no
GitHub ou em outro sistema. Confirme que os rótulos realmente existem antes da
primeira execução de `triage` ou `wayfinder`.

Se o projeto já usa nomes diferentes, preserve-os e apenas relacione cada nome
ao papel correspondente. Isso evita duplicar rótulos com o mesmo significado.

## 5. Escolha a estrutura de domínio

Para a maioria dos repositórios, use **contexto único** com esta estrutura:

```text
repositorio/
├── CONTEXT.md
└── docs/
    └── adr/
```

Use **múltiplos contextos** somente quando o projeto for de fato um monorepo
com domínios ou produtos independentes. Nesse caso, um `CONTEXT-MAP.md` na raiz
aponta para os arquivos `CONTEXT.md` de cada área.

Não crie documentos vazios apenas para completar a árvore. A configuração
registra onde eles devem ficar; skills como `domain-modeling` podem criá-los
quando um conceito ou uma decisão for realmente resolvido.

## 6. Revise antes de gravar

Antes da escrita, confira a proposta completa:

- sistema de tickets escolhido;
- comandos que serão usados para consultar e criar tickets;
- rótulos de triagem e seus nomes reais;
- estrutura de contexto único ou múltiplo;
- arquivo de instruções que receberá o bloco `## Agent skills`;
- conteúdo dos arquivos em `docs/agents/`.

A skill é conduzida por prompts. Ela deve apresentar o que encontrou e pedir a
confirmação das decisões que alteram o resultado antes de editar os arquivos.

## Atenção ao usar com Codex

A regra original prefere `CLAUDE.md` quando ele existe e usa `AGENTS.md` apenas
quando não encontra o primeiro. Isso pode colocar as instruções em um arquivo
que o Codex não lê.

Em um projeto operado pelo Codex:

1. identifique qual arquivo de instruções está efetivamente ativo;
2. mantenha `AGENTS.md` como referência principal quando essa for a convenção do
   projeto;
3. se `CLAUDE.md` também existir, use-o como ponte para o arquivo canônico ou
   replique somente o bloco necessário de maneira deliberada;
4. confirme que não foram criados dois blocos `## Agent skills` contraditórios.

## Como verificar o resultado

A configuração está pronta quando:

- `docs/agents/issue-tracker.md` existe e descreve o sistema usado de verdade;
- `docs/agents/domain.md` corresponde à estrutura atual do repositório;
- `docs/agents/triage-labels.md` existe quando `triage` está instalada;
- o arquivo de instruções lido pelo agente contém um único bloco
  `## Agent skills`;
- os rótulos mencionados existem no sistema de tickets;
- `to-tickets` sabe onde publicar sem perguntar novamente;
- `triage` usa rótulos existentes em vez de inventar nomes;
- nenhum arquivo `SKILL.md` foi modificado pela configuração.

Use uma revisão de Git antes do commit para confirmar que somente os arquivos
esperados foram adicionados ou alterados.

## Quando executar novamente

Execute novamente quando:

- o projeto trocar de sistema de tickets;
- a estrutura de domínio mudar de contexto único para múltiplo, ou o contrário;
- os arquivos de configuração ficarem incompatíveis com uma versão nova das
  skills;
- você quiser reconstruir deliberadamente a configuração.

Pequenas mudanças podem ser feitas diretamente nos arquivos Markdown de
`docs/agents/`.

## Como essa skill se encaixa no fluxo

```text
setup-matt-pocock-skills
        ↓
define tracker, triagem e domínio
        ↓
to-spec / to-tickets / triage / wayfinder
        ↓
domain-modeling registra contexto e decisões conforme necessário
```

Ela é uma pré-condição do fluxo de engenharia, não uma etapa repetida em cada
tarefa. Para decidir qual skill usar depois, consulte `ask-matt` quando ela
estiver disponível.

## Fontes

- [Tutorial original no AI Hero](https://www.aihero.dev/skills-setup-matt-pocock-skills)
- [Repositório mattpocock/skills](https://github.com/mattpocock/skills)
- [Skill no skills.sh](https://www.skills.sh/mattpocock/skills/setup-matt-pocock-skills)
