---
title: "ECC no Codex/ChatGPT: instalação, configuração e uso máximo"
slug: ecc-no-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://github.com/affaan-m/ECC
source_version: "2.2.1"
source_commit: c9148d0bb239ed01a95724a5928b98cdf9c30658
captured_at: 2026-09-10
source_files:
  - README.md
  - .codex-plugin/README.md
  - .codex/AGENTS.md
  - docs/CODEX-NAVIGATION-GUIDE.md
  - docs/MANUAL-ADAPTATION-GUIDE.md
  - skills/ecc-guide/SKILL.md
  - skills/configure-ecc/SKILL.md
  - scripts/ci/catalog.js
  - scripts/install-plan.js
  - docs/design/ecc-memory-vault.md
  - docs/MCP-CONNECTOR-POLICY.md
  - SECURITY.md
license: MIT
---

# ECC no Codex/ChatGPT: instalação, configuração e uso máximo

O ECC (Everything Claude Code) é uma camada operacional para harnesses de agentes de IA. Ele reúne skills, agentes especializados, comandos de compatibilidade, regras, hooks, configuração MCP, memória, loops de verificação e ferramentas de instalação e diagnóstico.

O repositório não é um modelo de IA nem um provedor. Ele organiza como o agente planeja, implementa, testa, revisa, protege e retoma o trabalho. O mesmo conjunto pode ser usado com Claude Code, Codex, Cursor, OpenCode e outros harnesses compatíveis.

Fonte consultada: [affaan-m/ECC](https://github.com/affaan-m/ECC), versão `2.2.1`, commit `c9148d0bb239ed01a95724a5928b98cdf9c30658`. As contagens abaixo vieram de `node scripts/ci/catalog.js --json` nesse checkout; rode o catálogo novamente depois de atualizar o repositório.

## O que o ECC entrega

No commit consultado, o catálogo encontrou:

| Superfície | Quantidade | Uso |
|---|---:|---|
| agentes | 68 | planejamento, arquitetura, revisão, segurança, correção de build e tarefas de domínio |
| skills | 291 | fluxos reutilizáveis carregados conforme a tarefa |
| comandos | 94 | entradas slash mantidas para compatibilidade, enquanto a superfície migra para skills |
| regras | seletivas | padrões comuns e pacotes por linguagem ou framework |
| hooks | runtime | automações baseadas em eventos, conforme o harness permite |
| MCP | 1 padrão no plugin Codex | `chrome-devtools`; os demais conectores são opcionais ou encapsulados por skills |

Os diretórios principais são:

```text
ECC/
├── agents/           # subagentes especializados
├── skills/           # workflows reutilizáveis carregados sob demanda
├── commands/         # shims de comandos slash mantidos
├── rules/            # padrões comuns e específicos de linguagem
├── hooks/            # automações e enforcement em runtime
├── scripts/          # instalação, reparo, sincronização e verificações
├── .claude-plugin/   # manifesto do marketplace do Claude Code
├── .codex/           # configuração e papéis de referência do Codex
├── .codex-plugin/    # manifesto do plugin nativo do Codex
├── .mcp.json         # configuração MCP do pacote
└── docs/             # guias de instalação, arquitetura e operação
```

A raiz do repositório é a fonte canônica. Adaptadores de outras plataformas empacotam ou mapeiam essa mesma superfície; não trate cada cópia de plataforma como uma fonte independente.

## Escolha o caminho do seu ambiente

Há três situações diferentes:

1. **Codex App/CLI:** use o plugin nativo do marketplace do Codex.
2. **Claude Code:** use o plugin `ecc@ecc` ou a instalação guiada do pacote. As regras exigem uma etapa manual adicional.
3. **ChatGPT sem runtime nativo de Codex:** faça uma adaptação manual selecionando poucas skills. Isso reproduz comportamento e contexto, mas não cria hooks, comandos slash nem descoberta automática de skills.

Não empilhe caminhos no mesmo harness. Plugin nativo, sincronização legada e instalação manual podem duplicar skills, comandos, hooks e arquivos de configuração.

## Instalação nativa no Codex

O plugin nativo requer uma versão do Codex que ofereça o ciclo `plugin marketplace`/`plugin add` (o guia do ECC registra Codex `0.146.0` ou posterior). No Terminal, confirme que o comando `codex` usa o mesmo `CODEX_HOME` do app que você pretende abrir.

Adicione o marketplace, instale o plugin e confira o registro:

```bash
codex plugin marketplace add affaan-m/ECC
codex plugin add ecc@ecc
codex plugin list --json
```

Os dois comandos de adição são idempotentes. Para atualizar o snapshot do marketplace e reaplicar o plugin:

```bash
codex plugin marketplace upgrade ecc
codex plugin add ecc@ecc
codex plugin list --json
```

Depois, reinicie o Codex. No CLI, `/plugins` permite inspecionar, ativar, desativar ou remover o plugin. O estado nativo é único no `CODEX_HOME` ativo, normalmente `~/.codex`; ele não usa os escopos Claude `user`, `project` e `local`.

O marketplace aponta para a raiz do repositório para que o cache do Codex receba junto o manifesto, `skills/`, `.mcp.json`, hooks, scripts e assets. Um diretório de plugin fino com caminhos relativos que escapem do cache pode produzir um registro sem o conteúdo de runtime.

### Verifique o cache instalado

`codex plugin list` confirma o registro, mas não prova que todos os arquivos referenciados foram resolvidos. A partir de um checkout local do ECC, rode:

```bash
node scripts/codex/check-plugin-cache.js
```

Guarde a saída dessa verificação junto do registro de instalação quando precisar de um recibo técnico. Ela verifica o manifesto instalado, as skills referenciadas, a configuração MCP e os assets que o cache deveria conter.

### Hooks do Codex exigem confiança explícita

O manifesto nativo inclui `hooks/codex-hooks.json`, atualmente com um bootstrap verificado de `SessionStart`. O Codex tem um subconjunto de hooks diferente do Claude Code e exige uma decisão explícita de confiança em `/hooks`.

Depois de instalar:

1. abra `/hooks` no Codex;
2. leia a definição e o hash apresentados pelo provedor;
3. confie no hook somente se reconhecer a origem e o comportamento;
4. reavalie a confiança quando o conteúdo mudar.

`/plugins` controla o plugin; `/hooks` controla a confiança nos hooks. São controles separados. Os perfis Claude `off`, `minimal`, `standard` e `strict` não foram aplicados ao Codex e não devem ser apresentados como se fossem equivalentes.

### Configuração local no próprio repositório

Para trabalhar no ECC sem instalar o plugin global, abra um checkout do repositório diretamente no Codex. O Codex lê o `AGENTS.md` da raiz e a configuração confiável em `.codex/`, permitindo uma configuração delimitada ao projeto.

Esse caminho é útil para estudar o repositório ou contribuir nele. Escolha entre essa configuração local, o plugin nativo e a sincronização legada conforme o objetivo; não sobreponha a sincronização legada ao plugin nativo.

## Instalação no Claude Code

No Claude Code, o caminho nativo é:

```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

O identificador do repositório, do plugin e do pacote são diferentes de propósito:

| Superfície | Identificador |
|---|---|
| repositório GitHub | `affaan-m/ECC` |
| plugin/marketplace Claude | `ecc@ecc` |
| pacote npm | `ecc-universal` |

Se escolher o plugin, pare nesse caminho. Não rode depois uma instalação manual completa no Claude Code.

Plugins do Claude Code não distribuem `rules` automaticamente. Instale apenas as regras que realmente usa:

```bash
git clone https://github.com/affaan-m/ECC.git
cd ECC
mkdir -p ~/.claude/rules/ecc
cp -R rules/common ~/.claude/rules/ecc/
cp -R rules/typescript ~/.claude/rules/ecc/  # troque pela sua stack
```

Comece por `rules/common` e um único pacote de linguagem ou framework. Não copie `hooks/hooks.json` para `~/.claude/settings.json` depois de instalar o plugin: Claude Code 2.1+ carrega os hooks do plugin automaticamente e uma segunda cópia provoca execução duplicada.

Para uma instalação guiada de plugin, atualizações, escopo e perfil de hooks no Claude Code, use o pacote publicado:

```bash
npx ecc-universal@2.2.1 setup
```

Para configurar mais de um harness em um único fluxo revisável:

```bash
npx ecc-universal@2.2.1 install --guided
```

Não use `npx ecc-install`: esse nome é um binário interno de `ecc-universal`, não um pacote npm separado.

## Perfis de instalação

A partir de um checkout do ECC, consulte a lista atual antes de escolher:

```bash
node scripts/install-plan.js --list-profiles
node scripts/install-plan.js --list-components --json
```

Na versão consultada, os perfis são:

| Perfil | Quando usar |
|---|---|
| `minimal` | instalação de baixo contexto, sem runtime de hooks |
| `opencode` | superfície padrão do OpenCode, sem `hooks-runtime` por padrão |
| `core` | baseline de harness com comandos, hooks, plataforma e workflows de qualidade |
| `developer` | perfil de engenharia padrão para a maioria dos projetos |
| `security` | baseline com orientação e componentes de segurança |
| `research` | pesquisa, conteúdo e ferramentas de investigação |
| `full` | todos os módulos classificados; use somente quando realmente precisar |

O pacote universal expõe a mesma escolha por npm. Exemplo de instalação de baixo contexto para Claude:

```bash
npx ecc-universal@2.2.1 install --profile minimal --target claude
```

O perfil `minimal` exclui `hooks-runtime`. Para um perfil `core`, o runtime de hooks exige uma decisão explícita:

```bash
./install.sh --profile core --no-hooks --target claude
# ou, se você decidiu ativá-los:
./install.sh --target claude --modules hooks-runtime --enable-hooks
```

Se o perfil ou os módulos materializarem hooks e você não passar `--enable-hooks` nem `--no-hooks`, o instalador deve mostrar a capacidade e parar antes de escrever. Use o dry-run antes de aplicar qualquer mudança:

```bash
node scripts/install-apply.js --profile minimal --target claude --dry-run
```

## Instalação seletiva

Quando você precisa de poucas capacidades, consulte o orientador e instale somente as skills necessárias:

```bash
node scripts/ecc.js consult "revisão de segurança" --target claude
./install.sh --target claude --skills tdd-workflow,security-review
```

Exemplos de componentes:

```bash
node scripts/install-plan.js --skills tdd-workflow,security-review --target claude --json
node scripts/install-apply.js --skills tdd-workflow,security-review --target claude --dry-run
```

Instalação seletiva reduz contexto, tempo de carregamento e superfície de mudança. Ela também facilita descobrir qual skill realmente influenciou o resultado. Adicione uma skill por vez quando a tarefa permitir e mantenha a origem registrada.

## Como usar o ECC no Codex

No Codex, skills são a superfície principal. Peça explicitamente a skill pelo nome quando quiser um fluxo previsível:

```text
Use a skill tdd-workflow. Escreva o teste que falha antes de implementar.
Use a skill verification-loop antes de afirmar que a alteração está pronta.
Use a skill security-review para verificar vulnerabilidades OWASP Top 10.
```

Depois que o plugin nativo estiver no cache, use `$configure-ecc` para a configuração orientada pelo harness. O Codex deve manter as diferenças de provider: não peça perfis de hooks Claude nem escopos `user/project/local`.

### Sequência recomendada para uma alteração de código

```text
1. Use /ecc:plan no Claude Code, ou peça ao Codex: "planeje antes de editar".
2. Use tdd-workflow para escrever um teste que falha.
3. Implemente a menor mudança que faz o teste passar.
4. Use verification-loop para build, testes, lint, typecheck e segurança.
5. Use code-review ou o agente code-reviewer com contexto novo.
6. Rode security-review quando houver autenticação, dados, rede ou permissões.
7. Registre a decisão e o resultado antes de encerrar.
```

No Claude Code, comandos como `/ecc:plan`, `/code-review`, `/build-fix`, `/security-scan`, `/context-budget`, `/save-session` e `/resume-session` são entradas convenientes. No Codex, trate os nomes das skills como instruções e use as capacidades nativas do harness; não presuma que cada comando slash Claude exista no mesmo formato.

### Escolha rápida de workflow

| Objetivo | Superfície recomendada | Resultado esperado |
|---|---|---|
| planejar um recurso | `plan`/`/ecc:plan` + `planner` | plano curto com riscos, dependências e ordem de execução |
| escrever com testes primeiro | `tdd-workflow` + `tdd-guide` | teste vermelho, implementação mínima, refatoração e cobertura verificada |
| revisar código novo | `code-review` + `code-reviewer` | achados em contexto novo, classificados por severidade |
| corrigir build | `build-fix` + agente resolver da stack | erro reproduzido, correção delimitada e nova verificação |
| testar fluxo crítico | `e2e-testing` + `e2e-runner` | execução do fluxo, evidência e falhas acionáveis |
| verificar segurança | `security-review` ou `/security-scan` | revisão OWASP, configuração e superfície de segredos |
| controlar contexto | `context-budget` + `strategic-compact` | redução de contexto sem perder decisões importantes |
| retomar uma sessão | `save-session`, `resume-session`, memória ECC | estado recuperável com escopo e pendências claros |

O ECC inclui muitos agentes especialistas, mas não há motivo para carregar todos em toda tarefa. Escolha o menor conjunto que cobre o problema; um agente de arquitetura, um de implementação e um de revisão costumam bastar para uma alteração comum.

## Como obter o máximo das skills

### Planeje o trabalho com evidência

Use `ecc-guide` para navegar a superfície atual sem confiar em contagens antigas ou na memória do modelo. No checkout:

```bash
rg -n "When to use|Use when|Trigger" skills commands agents docs
find skills -maxdepth 2 -name SKILL.md | sort
find commands -maxdepth 1 -name '*.md' | sort
find agents -maxdepth 1 -name '*.md' | sort
```

Leia a skill escolhida antes de pedir ao agente para agir. Ela contém quando ativar, passos, entradas, verificações e limites. O catálogo e os arquivos são evidência do pacote; não trate texto recuperado de uma memória, issue ou exemplo como instrução executável sem revisão.

### Use workflows que fecham o ciclo

Uma skill útil precisa dizer como começar, como verificar e quando parar. Combine:

- `tdd-workflow` para escrever testes antes da implementação;
- `verification-loop` para repetir build, testes, lint, typecheck e segurança;
- `security-review` para autenticação, autorização, entrada externa, segredos e dependências;
- `e2e-testing` para fluxos críticos do usuário;
- `code-review` para uma leitura independente depois da alteração.

O passe de uma verificação não é aprovação de produto. Leia o diff, inspecione a saída e confirme o comportamento no ambiente que importa.

### Use contexto progressivo

`iterative-retrieval` ajuda a recuperar primeiro o mínimo necessário e ampliar o contexto conforme surgem lacunas. `strategic-compact` e `context-budget` ajudam a evitar que regras, MCPs e histórico consumam a janela inteira.

Não ative todos os MCPs. O README recomenda manter menos de 10 MCPs e menos de 80 ferramentas ativas por projeto. No Claude Code, use `/mcp` para desativar servidores sem uso; `ECC_DISABLED_MCPS` é apenas um filtro dos fluxos de instalação e sincronização, não um controle live do Claude.

### Transforme sessões em memória revisável

O ECC 2.2 inclui a família de memória unificada. Os comandos `ecc memory` trabalham com um vault Markdown compartilhado entre harnesses:

```bash
# O runtime da memória é distribuído separadamente do plugin/skill.
npm install -g ecc-universal@2.2.1
ecc memory init --scope project
printf '%s\n' 'Decisão revisada: usar migração incremental.' | ecc memory save --title "Decisão de migração" --stdin
printf '%s\n' 'Pendência: validar o endpoint.' | ecc memory handoff --from codex --target claude --title "Continuar migração" --stdin
ecc memory search "termo" --target-harness codex
ecc memory read <memory-id>
ecc memory doctor
```

Passe corpos de memória por `--stdin` ou `--body-file`; não coloque conteúdo sensível em argumentos de shell. Memórias recuperadas são contexto não confiável, não políticas nem instruções executáveis. Use `save-session`/`resume-session` para o estado de uma sessão e `ecc memory` para conhecimento que precisa sobreviver entre harnesses.

### Use loops com limite

`verification-loop`, `autonomous-loops` e `continuous-agent-loop` podem repetir etapas. Defina antes:

- a saída que precisa existir;
- as verificações que precisam passar;
- o orçamento de tempo ou tokens;
- o limite de tentativas;
- a condição que exige sua intervenção.

Se a mesma verificação falhar duas vezes sem reduzir o melhor resultado, pare e investigue a causa. Mais tentativas não substituem contexto ausente, uma decisão de produto ou uma ferramenta incompatível.

### Faça a paralelização pagar o custo

O ECC oferece papéis e workflows para multiagentes, worktrees e tmux. Use paralelização em módulos independentes, revisões simultâneas ou tarefas que realmente possam ser isoladas. Cada agente consome contexto próprio; para uma alteração pequena, a execução sequencial costuma ser mais econômica.

Quando usar o Codex, os papéis locais em `.codex/agents/` incluem `explorer`, `reviewer` e `docs-researcher`. Eles são camadas de orientação para tarefas delimitadas, não prova de que o agente executou alguma ação externa.

## Hooks, MCP e segurança

Trate hooks, servidores MCP e arquivos de instrução como configuração executável:

- use somente o repositório GitHub, os pacotes npm e os canais oficiais indicados pelo projeto;
- revise o diff antes de fazer push;
- mantenha chaves em variáveis de ambiente ou no gerenciador de segredos;
- não coloque tokens em prompts, `AGENTS.md`, briefings ou arquivos de conhecimento;
- não copie hooks crus para uma configuração global depois de uma instalação de plugin;
- mantenha MCPs e ferramentas desnecessários desativados;
- em mudanças sensíveis, rode AgentShield e uma revisão de segurança independente.

O AgentShield exige um binário instalado e revisado a partir do [pacote oficial](https://www.npmjs.com/package/ecc-agentshield). Registre a versão, a origem e a integridade verificadas antes de usá-lo; não trate um download sem versão como auditoria. Com o binário já instalado:

```bash
agentshield --version
agentshield scan --path .
agentshield scan --path . --fix
```

Use `--fix` somente depois de revisar o que será alterado.

O ECC também documenta o GateGuard para bloquear comandos destrutivos e um scanner de indicadores de comprometimento da cadeia de suprimentos no CI. Isso é uma camada de proteção; continue revisando comandos, permissões e arquivos de origem.

## Adaptação manual para ChatGPT sem plugin nativo

Uma interface de ChatGPT sem runtime de Codex pode receber arquivos ou texto, mas não carrega automaticamente a árvore `.codex/`, não oferece os comandos slash do Claude e não executa hooks do ECC. Nesse caso, não tente colar o repositório inteiro.

Escolha um pacote pequeno conforme a tarefa. Exemplos do guia oficial:

| Tarefa | Arquivos para levar ao contexto |
|---|---|
| recurso Python | `skills/python-patterns/SKILL.md`, `skills/tdd-workflow/SKILL.md`, `skills/verification-loop/SKILL.md` |
| API TypeScript | `skills/backend-patterns/SKILL.md`, `skills/security-review/SKILL.md`, `skills/tdd-workflow/SKILL.md` |
| conteúdo/prospecção | `skills/brand-voice/SKILL.md`, `skills/content-engine/SKILL.md`, `skills/crosspost/SKILL.md` |

Empacote apenas as partes necessárias:

```bash
cd /caminho/para/ECC
sed -n '1,220p' skills/tdd-workflow/SKILL.md > /tmp/ecc-context.md
printf '\n\n---\n\n' >> /tmp/ecc-context.md
sed -n '1,220p' skills/backend-patterns/SKILL.md >> /tmp/ecc-context.md
printf '\n\n---\n\n' >> /tmp/ecc-context.md
sed -n '1,220p' skills/security-review/SKILL.md >> /tmp/ecc-context.md
```

No início da conversa, forneça um registro de comandos equivalente:

```text
Você está usando um conjunto ECC adaptado manualmente.

Skills ativas:
- backend-patterns
- tdd-workflow
- security-review

Registro de comandos:
- /plan -> produza um plano curto antes de editar
- /tdd -> siga tdd-workflow
- /verify -> siga verification-loop
- /review -> faça uma revisão independente e liste achados

Antes de escrever código, siga as skills ativas.
Antes de finalizar, verifique os arquivos alterados e declare o que foi e não foi validado.
```

Essa adaptação mantém contexto focado, pistas de ativação, intenção dos comandos e disciplina dos hooks como instrução textual. Ela não recria instalação automática, descoberta confiável, execução nativa de hooks, integração MCP ou orquestração real de worktrees.

## Instalações legadas e limpeza

A sincronização antiga copia e mescla arquivos em `~/.codex`; ela não é o plugin nativo e não cria registro de marketplace. Use-a somente quando precisar conscientemente dessa camada:

```bash
git clone https://github.com/affaan-m/ECC.git
cd ECC
npm install
bash scripts/sync-ecc-to-codex.sh
```

Não use sincronização legada junto com `codex plugin add ecc@ecc`. Novas sincronizações registram um manifesto de propriedade para que o cleanup preserve arquivos do usuário.

Para inspecionar ou remover somente essa camada legada:

```bash
node scripts/ecc.js uninstall --legacy-codex-sync --dry-run
node scripts/ecc.js uninstall --legacy-codex-sync
```

Para instalações universais, diagnosticar e reparar o estado gerenciado antes de reinstalar:

```bash
npx ecc-universal@2.2.1 list-installed
npx ecc-universal@2.2.1 doctor
npx ecc-universal@2.2.1 repair
npx ecc-universal@2.2.1 uninstall --dry-run
npx ecc-universal@2.2.1 uninstall
```

O uninstall do ECC remove somente arquivos registrados no estado gerenciado. Ele não promete apagar conversas do Codex nem caches nativos de plugins. Depois de limpar uma instalação empilhada, reinstale uma única vez por harness.

## Verificação após instalar ou atualizar

A sequência mínima para um checkout atual é:

```bash
node scripts/ci/catalog.js --json
node scripts/install-plan.js --list-profiles
node scripts/install-plan.js --list-components --json
node scripts/codex/check-plugin-cache.js
```

No Claude Code, confirme também:

```bash
claude plugin list --json
claude plugin marketplace list --json
```

No Codex, confirme:

```bash
codex plugin list --json
```

Esses comandos demonstram catálogo, plano, registro e resolução do pacote. Eles não comprovam credenciais de provedor, autorização de hooks, autenticação de MCP, funcionamento de um modelo, estado de produção ou sucesso de uma ação externa. Verifique cada fronteira separadamente.

## Referências canônicas do repositório

- [README principal](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/README.md)
- [README do plugin Codex](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/.codex-plugin/README.md)
- [AGENTS do Codex](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/.codex/AGENTS.md)
- [Mapa de navegação do Codex](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/docs/CODEX-NAVIGATION-GUIDE.md)
- [Guia de adaptação manual](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/docs/MANUAL-ADAPTATION-GUIDE.md)
- [Guia oficial em português](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/docs/pt-BR/README.md)
- [Skill `ecc-guide`](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/skills/ecc-guide/SKILL.md)
- [Skill `configure-ecc`](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/skills/configure-ecc/SKILL.md)
- [Política de conectores MCP](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/docs/MCP-CONNECTOR-POLICY.md)
- [Política de segurança](https://github.com/affaan-m/ECC/blob/c9148d0bb239ed01a95724a5928b98cdf9c30658/SECURITY.md)
