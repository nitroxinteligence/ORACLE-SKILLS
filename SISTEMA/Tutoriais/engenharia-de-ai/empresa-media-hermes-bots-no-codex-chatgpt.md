---
title: "Empresa de mídia de uma pessoa com bots Hermes no Codex/ChatGPT"
slug: empresa-media-hermes-bots-no-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/VibeMarketer_/status/2093330541177352217
source_article: https://x.com/i/article/2093330534495916032
source_title: "How to Build a One-Person Media Company With Hermes Bots"
source_published_at: "2026-08-28"
runtime_source: https://github.com/NousResearch/hermes-agent
runtime_source_commit: 6c3d4a4af70d76b7365bf19e9420ffdcbb9830ad
captured_at: 2026-09-10
source_files:
  - "X status 2093330541177352217 e artigo 2093330534495916032"
  - "NousResearch/hermes-agent README.md"
  - "website/docs/getting-started/quickstart.md"
  - "website/docs/user-guide/bot-mode.md"
  - "website/docs/user-guide/profiles.md"
  - "website/docs/user-guide/features/kanban.md"
  - "website/docs/user-guide/desktop.md"
license: MIT
---
<!-- Modified for Oracle distribution; exact input/output digests and reasons are in the signed distribution manifest. -->

# Empresa de mídia de uma pessoa com bots Hermes no Codex/ChatGPT

O tutorial da VibeMarketer descreve uma operação editorial para uma pessoa: seis bots especializados compartilham um cérebro de conteúdo no Obsidian, passam artefatos estruturados entre si e deixam a publicação sob aprovação humana. A ideia útil não é “gerar mais posts”; é fechar o ciclo **ideia → pesquisa → ângulo → peça principal → distribuição → revisão → desempenho → playbooks atualizados**.

Fonte consultada: [tutorial original no X](https://x.com/VibeMarketer_/status/2093330541177352217) e seu [artigo do X](https://x.com/i/article/2093330534495916032), publicado em 28 de agosto de 2026. A documentação de runtime foi conferida no [repositório oficial do Hermes Agent](https://github.com/NousResearch/hermes-agent), commit `6c3d4a4af70d76b7365bf19e9420ffdcbb9830ad`. Comandos, telas e nomes podem mudar depois desse commit.

O autor afirma ter gerado mais de 5,8 milhões de impressões no X em quatro semanas. Essa é uma declaração do artigo; não há, no tutorial, um recibo independente que a comprove. Use o texto como desenho de processo e valide os seus próprios resultados.

## O que está sendo construído

Uma empresa de mídia pequena precisa de uma cadeia editorial, não de seis cópias do mesmo chatbot. Cada etapa tem uma decisão, um artefato e um limite:

| Camada | Responsabilidade | Estado durável |
|---|---|---|
| **Bots** | tornam os papéis visíveis, conversáveis e especializados | perfil, conversa e rotina de cada bot |
| **Perfis** | isolam modelo, instruções, memória, skills e credenciais | diretório próprio em `~/.hermes/profiles/<nome>/` |
| **Obsidian** | guarda voz, público, ofertas, provas, hooks e playbooks aceitos | arquivos Markdown ligados por wikilinks |
| **Kanban** | move tarefas, dependências, comentários, retries e revisão | banco SQLite local e histórico de runs |

No Hermes, **Bot Mode é uma interface sobre perfis**. Um bot não é um subagente descartável nem um novo banco remoto. O perfil continua sendo dono de seus arquivos, credenciais, memória e histórico. O Bot Mode oferece roster, chats persistentes, grupos, menções e rotinas; o Kanban oferece uma fila de trabalho auditável. Consulte a [documentação oficial de Bot Mode](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/bot-mode.md), a [documentação de perfis](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md) e a [documentação de Kanban](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban.md) para a implementação atual.

## Limite do artigo

O artigo não entrega um repositório com os seis perfis, os arquivos do vault ou uma exportação do board. Ele fornece uma arquitetura editorial e exemplos de contratos. Portanto:

- os nomes de bots abaixo são uma implementação recomendada, não uma configuração capturada do autor;
- os prompts são modelos para adaptação, não instruções oficiais do Hermes;
- a existência de Bot Mode, perfis, rotinas e Kanban deve ser confirmada na versão do Hermes que você instalar;
- “publicado” só deve significar uma ação confirmada pelo provedor, com ID externo ou outro recibo verificável;
- a interface ChatGPT não cria, sozinha, seis perfis Hermes persistentes.

## Instalação do Hermes

O Hermes é um runtime separado do Codex e do ChatGPT. Para começar no macOS, a [documentação oficial de instalação](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/installation.md) recomenda o Hermes Desktop; para CLI sem Desktop, documenta o instalador abaixo:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.zshrc
```

O Desktop pode instalar o runtime na primeira execução. A documentação de [quickstart](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/quickstart.md) recomenda esta ordem:

1. instalar o runtime;
2. escolher um provedor e um modelo;
3. completar uma conversa normal;
4. confirmar que a sessão pode ser retomada;
5. só depois ativar bots, skills, gateways, rotinas ou Kanban.

Configuração inicial comum:

```bash
hermes setup
# ou, se você usa o provedor Nous Portal:
hermes setup --portal

# escolha ou troque o provedor de forma interativa
hermes model

# primeiro teste verificável
hermes --tui
```

O Hermes documenta também autenticação por assinatura ChatGPT/Codex via `hermes model` → **ChatGPT ou Codex Subscription**. Isso não transforma o Hermes em uma extensão do Codex: são runtimes distintos que podem usar o mesmo provedor, cada um com seu estado.

O estado normal fica separado dos segredos:

- `~/.hermes/config.yaml`: configurações não secretas;
- `~/.hermes/.env`: chaves e tokens, com permissão restrita;
- `~/.hermes/profiles/<nome>/`: estado de um perfil;
- `~/.hermes/kanban.db`: board padrão do Kanban.

Não coloque chaves em notas do Obsidian, em `SOUL.md` ou em prompts compartilhados. O Hermes exige, em geral, um modelo com pelo menos 64K tokens de contexto para fluxos longos de ferramentas; confirme o limite do provedor antes de criar uma frota de bots.

Teste a instalação antes de continuar:

```bash
hermes --tui
# peça algo que tenha uma resposta fácil de conferir:
# "Liste cinco arquivos deste projeto e indique o provável ponto de entrada."

hermes --continue
```

Uma resposta sem erro, uma ferramenta que realmente executa e uma retomada da sessão são o recibo mínimo. Uma tela instalada sem conversa funcional não é uma instalação pronta.

## Criar os seis perfis

Crie perfis com uma decisão editorial cada. A opção `--description` ajuda o roteador do Kanban a escolher um especialista. Os comandos abaixo são um esqueleto; ajuste as descrições ao seu negócio:

```bash
hermes profile create signal-scout \
  --description "Encontra sinais atuais, perguntas de clientes e fontes promissoras. Não escreve posts."

hermes profile create researcher \
  --description "Verifica fontes primárias, claims, números, contexto, contradições e limites da evidência."

hermes profile create content-strategist \
  --description "Escolhe leitor, resultado, tensão, tese, formato e ângulo a partir da pesquisa aprovada."

hermes profile create long-form-writer \
  --description "Transforma um angle brief e um source packet em uma peça principal reutilizável."

hermes profile create distribution-bot \
  --description "Reconstrói a ideia para X, LinkedIn, newsletter, vídeo e carrossel sem duplicar o hook."

hermes profile create editor \
  --description "Revisa o pacote inteiro, compara claims e hooks e prepara a fila de aprovação humana."
```

Confira o roster e cada perfil:

```bash
hermes profile list
hermes profile show signal-scout
```

Cada perfil tem memória, sessões, skills, credenciais e configuração próprias. `--clone` copia configuração e skills para começar com uma base comum, mas deixa sessões e memória novas:

```bash
hermes profile create research-copy --clone
```

Use cloning com cuidado. OAuth de Claude, OpenAI/Codex e xAI usa tokens de uso único; duplicar um arquivo de credencial pode revogar a sessão de outro perfil. Se um bot precisar de uma conta OAuth própria, autentique esse perfil separadamente. Perfis também não são sandbox de sistema operacional: no backend local, todos os perfis rodam como o mesmo usuário e podem alcançar arquivos que esse usuário consegue ler. Para isolamento de clientes, use usuário, VM, container ou máquina separados.

No Hermes Desktop, a aba **Bots** mostra os perfis como uma lista de agentes nomeados. Crie ou importe os seis perfis, mantenha uma conversa persistente da equipe e use `@mention` para uma coordenação curta. As **Routines** são jobs de cron vinculados ao perfil e aparecem também em `hermes cron list`.

Use conversa para coordenação breve. Use arquivos e Kanban para estado, evidência e handoff. Não deixe o resultado importante preso em um chat.

## Construir o cérebro compartilhado no Obsidian

Crie uma pasta específica para a operação dentro do vault. O exemplo abaixo usa a raiz canônica do seu Obsidian OS; troque `VAULT` se a operação estiver em outro vault:

```bash
: "${ORACLE_VAULT:?Defina ORACLE_VAULT com o caminho do vault escolhido}"
VAULT="$ORACLE_VAULT"
MEDIA="$VAULT/media-company"

mkdir -p "$MEDIA"/{brand,discovery,engine,platforms,campaigns}
touch "$MEDIA/index.md"
touch "$MEDIA/brand/voice.md" "$MEDIA/brand/audience.md" \
      "$MEDIA/brand/offers.md" "$MEDIA/brand/proof.md"
touch "$MEDIA/discovery/signals.md" "$MEDIA/discovery/customer-questions.md" \
      "$MEDIA/discovery/authority-clips.md"
touch "$MEDIA/engine/angles.md" "$MEDIA/engine/hooks.md" \
      "$MEDIA/engine/repurposing.md" "$MEDIA/engine/review.md" \
      "$MEDIA/engine/performance.md"
touch "$MEDIA/platforms/x.md" "$MEDIA/platforms/linkedin.md" \
      "$MEDIA/platforms/newsletter.md" "$MEDIA/platforms/video.md" \
      "$MEDIA/platforms/carousel.md"
```

Estrutura mínima:

```text
media-company/
├── index.md
├── brand/
│   ├── voice.md
│   ├── audience.md
│   ├── offers.md
│   └── proof.md
├── discovery/
│   ├── signals.md
│   ├── customer-questions.md
│   └── authority-clips.md
├── engine/
│   ├── angles.md
│   ├── hooks.md
│   ├── repurposing.md
│   ├── review.md
│   └── performance.md
├── platforms/
│   ├── x.md
│   ├── linkedin.md
│   ├── newsletter.md
│   ├── video.md
│   └── carousel.md
└── campaigns/
    └── YYYY-MM-DD-slug/
```

`index.md` é a entrada comum dos bots. Ele deve responder, em poucas linhas:

- sobre quais problemas você publica;
- para quem publica;
- que evidência é necessária;
- quais formatos e plataformas usa;
- onde ficam os playbooks;
- quais mudanças exigem aprovação humana.

Exemplo de contrato no índice:

```markdown
# Media Company

## Tema
- Sistemas de IA aplicados por operadores.
- Construções de agentes com uso empresarial específico.

## Leitor
- Fundadores.
- Profissionais de marketing.
- Operadores de IA.

## Toda campanha precisa de
- Um resultado claro para o leitor.
- Uma tese central.
- Evidência direta para claims consequenciais.
- Um workflow, framework ou regra reutilizável.
- Distribuição nativa para cada plataforma.

## Roteamento
- Sinais novos → [[discovery/signals]] → Signal Scout.
- Sinais aprovados → Researcher.
- Source packet completo → Content Strategist.
- Angle brief aprovado → Long-form Writer.
- Peça principal aprovada → Distribution Bot.
- Todo asset externo → Editor → aprovação humana.

## Aprovação obrigatória
- Ângulo central.
- Peça principal.
- Claims factuais de consequência real.
- Cada publicação pública.
- Mudanças em voz, público, oferta ou política editorial.
- Lições de desempenho que virarão regra permanente.
```

O vault deve guardar conhecimento aceito, regras atuais, exemplos reutilizáveis e links para fontes. Não guarde cada rascunho rejeitado no cérebro compartilhado; deixe rascunhos e campanhas na pasta da campanha para que possam ser revisados ou descartados.

Use wikilinks para tornar relações navegáveis:

```markdown
A voz de [[brand/voice]] atende o público de [[brand/audience]].
O hook vem de [[engine/hooks]] e precisa de prova em [[brand/proof]].
O formato escolhido segue [[platforms/x]] e a revisão passa por [[engine/review]].
```

O vault é compartilhado, mas a escrita pode ser restrita por contrato. Uma política simples é permitir que Signal Scout escreva em `discovery/`, Researcher em `discovery/` e `campaigns/`, e que somente o Editor proponha alterações em playbooks. A aprovação humana é o gate para tornar uma proposta permanente.

## Contrato dos seis bots

Dê a cada perfil cinco campos explícitos:

```markdown
## Contrato do perfil

- **owns:** qual decisão este bot toma.
- **reads:** quais arquivos e campos de handoff ele pode usar.
- **returns:** qual artefato exato o próximo bot recebe.
- **must not:** decisões que pertencem a outro bot ou à pessoa.
- **done when:** condições observáveis que completam o handoff.
```

Aplicação recomendada:

| Bot | `owns` | `returns` | `must not` |
|---|---|---|---|
| Signal Scout | se o assunto merece pesquisa agora | signal card com fonte, urgência, pergunta e motivo de rejeição | escolher tese ou redigir post |
| Researcher | se os fatos sustentam uma pauta | source packet com 3–7 claims, URLs, clips, contradições e limites | escolher headline sensacionalista |
| Content Strategist | qual história a pesquisa permite contar | angle brief com leitor, resultado, tensão, tese e formato | escrever a peça final |
| Long-form Writer | como explicar a tese profundamente | flagship piece com arquitetura visível e provas | criar todos os assets de plataforma |
| Distribution Bot | qual entrada cada plataforma merece | pacote de assets distintos por plataforma | apenas encurtar o mesmo texto cinco vezes |
| Editor | se o pacote inteiro está coerente e seguro | decisão de revisão e fila de aprovação | publicar ou alterar sozinho a política editorial |

### Signal Scout

Prompt inicial:

```text
Encontre a melhor oportunidade prática criada por uma mudança recente no Hermes Agent.
Priorize um workflow que uma pessoa consiga construir agora.
Retorne: evento, fonte oficial, interesse atual do público, clips ou provas úteis,
pergunta que a peça deve responder, urgência e razões para rejeitar ângulos fracos.
Não escreva conteúdo.
```

O resultado deve ser um **signal card**, por exemplo:

```yaml
signal: "Hermes Bot Mode + Kanban"
source_url: "https://...
audience_question: "Como seis perfis viram uma operação editorial?"
why_now: "..."
authority_clips:
  - "..."
decay: "7 dias"
recommendation: "research"
reject_reason: "..."
```

Descarte mais sinais do que aprova. A função do Scout é proteger o restante da equipe de polir assuntos que ninguém precisava.

### Researcher

O Researcher recebe somente um signal card aprovado. Ele deve verificar a fonte primária, o contexto ao redor, os números e o que ainda não foi provado:

```text
Receba o signal card abaixo e produza um source packet.
Verifique primeiro a fonte oficial e depois fontes secundárias relevantes.
Separe fato verificado, inferência e lacuna.
Retorne 3–7 claims verificáveis, uma URL direta por claim consequencial,
clips ou citações com contexto, contradições, o que as fontes não provam
e 2–3 mecanismos que merecem explicação.
Não escolha uma headline e não escreva o artigo.
```

O source packet é inválido quando tem números sem origem, URLs genéricas, citações sem contexto ou uma conclusão que as fontes não sustentam.

### Content Strategist

O estrategista transforma evidência em uma única recomendação editorial:

```text
Use somente o source packet aprovado.
Escolha um leitor, um resultado, uma tensão central, uma tese, um formato flagship,
um objeto reutilizável e 2–5 entradas de distribuição.
Retorne um angle brief, não um rascunho.
Explique por que os caminhos rejeitados são mais fracos.
Não acrescente fatos ausentes do source packet.
```

Modelo de angle brief:

```markdown
# Angle brief

- reader:
- reader outcome:
- current source:
- central tension:
- thesis:
- what becomes possible:
- flagship format:
- reusable object:
- proof required:
- sections:
- distribution entryways: proof, mechanism, workflow, risk, result
```

### Long-form Writer

O Writer recebe angle brief, source packet, `brand/voice.md` e padrões relevantes. O objetivo é criar a versão mais profunda e reutilizável da ideia: artigo no X, newsletter, guia ou ensaio em vídeo.

```text
Escreva a peça principal a partir do angle brief e do source packet.
Use a voz indicada em brand/voice.md.
Inclua headline orientada a resultado, primeiro écran concreto,
arquitetura visível, claims ligados às fontes, workflow completo,
exemplos nos pontos de atrito e encerramento memorável.
Preserve incertezas e não invente provas.
Entregue a peça principal e uma lista de claims que o Editor deve conferir.
```

O Writer não deve produzir todos os posts derivados. A peça principal é a matéria-prima que o Distribution Bot reconstruirá.

### Distribution Bot

Distribuição não é remover palavras. Cada asset precisa de uma razão própria para existir:

```text
Volte ao angle brief antes de adaptar a peça principal.
Crie entradas independentes para X, LinkedIn, newsletter, vídeo e carrossel.
Para cada asset informe: plataforma, objetivo, claim central, hook, CTA,
fonte necessária e relação com a peça principal.
Não publique e não repita o mesmo hook apenas trocando o limite de caracteres.
```

Para X, use um claim afiado, uma prova, uma sequência de construção ou um clip. Para LinkedIn, extraia a decisão do operador. Para carrossel, mostre um framework. Para vídeo, construa uma narrativa falada em torno de tensão, demonstração e resultado. Para newsletter, acrescente contexto e nuance.

### Editor

O Editor recebe o pacote inteiro de uma vez. Essa visão permite encontrar:

- cinco hooks que fazem a mesma afirmação;
- a mesma história de abertura repetida;
- fatos introduzidos no repurpose sem fonte;
- mudança de tom entre plataformas;
- carrossel que não acrescenta nada à peça principal;
- CTA incompatível com o estágio do leitor;
- uma plataforma que recebeu um asset superficial.

```text
Revise o pacote completo contra o angle brief, source packet, voz e política editorial.
Para cada asset, verifique claim, fonte, plataforma, hook, CTA, mídia e duplicação.
Retorne uma decisão por asset: aprovado, revisão necessária ou rejeitado,
com evidência e mudança concreta.
Prepare a fila de aprovação humana.
Você não pode publicar.
```

## Registro único de campanha

Não faça o próximo bot adivinhar o que importa num bloco de prosa. Mantenha um registro Markdown por campanha:

```markdown
---
campaign: hermes-media-company
status: research
created: 2026-09-10
owner: signal-scout
---

## Signal
- event:
- source:
- urgency:
- audience_question:

## Research
- verified_claims:
- sources:
- authority_clips:
- contradictions:
- unknowns:

## Angle
- reader:
- outcome:
- tension:
- thesis:
- reusable_object:

## Flagship
- format:
- path:
- approval_state: pending

## Distribution
- x:
- linkedin:
- newsletter:
- video:
- carousel:

## Review
- issues:
- final_decision: pending
- human_approver:

## Performance
- reach:
- meaningful_engagement:
- clicks_or_conversions:
- approved_changes:
- next_test:
```

O estado pode usar `signal`, `research`, `angle`, `flagship`, `distribution`, `review` e `performance`. Se um campo obrigatório estiver vazio, devolva a tarefa à etapa anterior. Não preencha a lacuna com uma suposição plausível.

## Colocar a fila no Hermes Kanban

O Kanban é a camada para tarefas duráveis e dependências. Na configuração atual, o dispatcher roda dentro do gateway por padrão; não inicie um daemon separado contra o mesmo banco.

```bash
# inicializar o board padrão
hermes kanban init

# iniciar o gateway, que hospeda o dispatcher
hermes gateway start

# criar a primeira tarefa
hermes kanban create \
  "Encontrar oportunidade editorial sobre Bot Mode" \
  --assignee signal-scout \
  --workspace "dir:$MEDIA" \
  --body "Retorne signal card com fonte oficial, urgência, pergunta do público e rejeições. Não redija posts."

# observar e inspecionar
hermes kanban watch
hermes kanban list
hermes kanban stats
```

Se o shell tratar o caminho com espaços, mantenha o valor entre aspas ou use uma variável:

```bash
MEDIA="${ORACLE_VAULT:?Defina ORACLE_VAULT com o caminho do vault escolhido}/media-company"
hermes kanban create "Verificar source packet" \
  --assignee researcher \
  --workspace "dir:$MEDIA" \
  --body "Use o signal card aprovado e preencha research no registro da campanha."
```

Um worker despachado recebe `HERMES_KANBAN_TASK` e usa as ferramentas `kanban_*` diretamente. Ele não deve executar `hermes kanban` dentro do próprio trabalho. Para uma cadeia, crie tarefas com dependências e handoffs claros:

```bash
SIGNAL=$(hermes kanban create "Signal Scout" \
  --assignee signal-scout --json | jq -r .id)

RESEARCH=$(hermes kanban create "Researcher" \
  --assignee researcher --parent "$SIGNAL" \
  --json | jq -r .id)

ANGLE=$(hermes kanban create "Content Strategist" \
  --assignee content-strategist --parent "$RESEARCH" \
  --json | jq -r .id)

FLAGSHIP=$(hermes kanban create "Long-form Writer" \
  --assignee long-form-writer --parent "$ANGLE" \
  --json | jq -r .id)

DISTRIBUTION=$(hermes kanban create "Distribution" \
  --assignee distribution-bot --parent "$FLAGSHIP" \
  --json | jq -r .id)

hermes kanban create "Editor" \
  --assignee editor --parent "$DISTRIBUTION"
```

A promoção de uma etapa depende da conclusão da anterior. O handoff deve ser estruturado no `summary` e em `metadata`, incluindo arquivos alterados, claims verificados, testes feitos e decisões. Isso torna retry e revisão legíveis sem reabrir seis conversas.

Para um único projeto, o board `default` basta. Use boards separados quando houver domínios que não devem compartilhar fila, workspace ou contexto. `dir:<caminho-absoluto>` preserva o diretório; `scratch` é temporário; `worktree` serve para código. O Kanban local é single-host: não trate um SQLite compartilhado entre máquinas como coordenação distribuída.

## Primeira campanha completa

Use o próprio sistema como exercício. A pergunta do artigo é um bom exemplo:

```text
Encontre a melhor oportunidade prática criada pelo release recente do Hermes Bot Mode.
Priorize um workflow que um operador solo possa construir hoje.
Retorne fonte oficial, interesse do público, clips de autoridade,
a pergunta que a peça deve responder e motivos para rejeitar ângulos fracos.
Não escreva conteúdo.
```

A sequência deve ser:

1. **Signal Scout:** registra Bot Mode como evento e propõe a operação de uma pessoa.
2. **Researcher:** confirma o release, perfis, Bot Mode e Kanban em fontes oficiais; separa colaboração visível de execução durável.
3. **Content Strategist:** escolhe o leitor, o resultado, a tensão e o modelo de seis papéis.
4. **Long-form Writer:** cria a peça principal a partir do evidence packet.
5. **Distribution Bot:** cria entradas diferentes para cada plataforma.
6. **Editor:** compara o pacote, confere claims contra as fontes e abre a fila de aprovação.
7. **Pessoa:** aprova, pede revisão ou rejeita; somente depois uma ação de publicação pode ser executada.

## Sequência de sete dias no X

A proposta do artigo é distribuir uma ideia em sete entradas, sem publicar o mesmo link sete vezes:

| Dia | Entrada | O que mostrar |
|---|---|---|
| 1 | argumento principal | resultado maior e peça flagship |
| 2 | arquitetura | bots são papéis, Obsidian é cérebro, Kanban é mesa de produção |
| 3 | autoridade | clip ou demonstração e o mecanismo que ele revela |
| 4 | construção | seis papéis, árvore do vault ou contrato de handoff |
| 5 | crítica | por que uma conversa escrevendo todos os formatos repete hooks |
| 6 | feedback | quais sinais mudam hook, ângulo, plataforma ou público |
| 7 | compressão | o ciclo completo em um visual ou checklist |

Cada post deve ser útil sem exigir o clique no anterior. Mantenha a tese, a prova e o objetivo editorial; mude a entrada e o formato.

## Aprovação humana e publicação

A primeira versão deve preparar tudo e publicar nada automaticamente. A pessoa continua aprovando:

- o ângulo central;
- a peça principal;
- claims factuais com consequência real;
- cada post público e mídia associada;
- mudanças em voz, público, oferta e política editorial;
- lições de desempenho que serão regras permanentes.

O Editor pode aprovar, pedir revisão ou rejeitar. Ele não publica. Um conector só deve marcar publicação quando o provedor retornar um ID externo real. Uma resposta “parece publicado” ou um botão clicado sem readback não é recibo.

Use o período de aprovação para ensinar critérios. Quando uma decisão se torna previsível, transforme-a em exemplo ou regra do playbook somente depois de aprovação. Não conceda autonomia com base em uma fila que ainda contém muitos erros ou em uma revisão que você não consegue auditar.

## Fechar o ciclo com desempenho

Depois de cada campanha, registre:

- sinal e assunto;
- resultado esperado do leitor;
- ângulo e tipo de hook;
- formato e plataforma;
- alcance ou impressões;
- engajamento significativo;
- cliques, seguidores, respostas ou conversões ligados ao objetivo;
- o que o Editor aprovou ou alterou;
- o próximo teste.

Uma revisão semanal do Editor deve produzir três listas curtas:

| Lista | Regra |
|---|---|
| **manter** | padrão que funcionou repetidamente e ainda combina com a estratégia |
| **testar** | hipótese promissora que precisa de outra tentativa controlada |
| **parar** | padrão repetidamente fraco, duplicado ou caro sem aprendizado |

A mudança no playbook exige aprovação humana e deve apontar os posts que a sustentam. Um resultado isolado cria uma hipótese, não uma lei universal.

## Versão mínima para esta semana

Não crie seis bots autônomos no primeiro dia. Siga este corte:

1. criar o cérebro do Obsidian com voz, público, prova e plataformas mínimas;
2. criar Signal Scout, Researcher e Editor;
3. passar três ideias reais por sinal, pesquisa e revisão;
4. adicionar Content Strategist quando os source packets forem úteis;
5. adicionar Long-form Writer quando os angle briefs limitarem bem o rascunho;
6. adicionar Distribution Bot quando uma peça principal estiver funcionando;
7. registrar desempenho e atualizar playbooks uma vez por semana, sempre com aprovação.

O primeiro resultado útil pode ser apenas um opportunity card pesquisado, um angle brief e um post do X pronto para revisão. Depois acrescente a peça principal, o pacote de plataformas e o loop de desempenho.

## Adaptação para Codex

O Codex pode atuar como operador do vault e como revisor do processo, mas não deve ser apresentado como o roster persistente do Hermes. Uma tarefa Codex pode criar ou editar os arquivos Markdown, comparar diffs, conferir URLs e preparar uma campanha; o estado de Bot Mode, perfis, rotinas e Kanban continua no Hermes instalado.

Prompt para preparar uma campanha no vault:

```text
Trabalhe no diretório media-company dentro do vault escolhido. Confirme esse caminho antes de editar.
Leia index.md, brand/voice.md, brand/audience.md e brand/proof.md antes de editar.
Crie uma pasta de campanha com signal.md, research.md, angle.md e review.md.
Não invente fontes, números, audiência ou resultados.
Não publique nem altere playbooks permanentes.
Ao terminar, mostre o diff, os arquivos alterados e os campos ainda pendentes.
```

Prompt para auditar um pacote:

```text
Audite esta campanha como Editor.
Compare cada claim com a fonte indicada, marque inferência versus fato,
ache hooks repetidos entre plataformas e verifique se o CTA combina com o leitor.
Retorne aprovado, revisão necessária ou rejeitado por asset.
Não escreva uma publicação nova e não faça nenhuma ação externa.
```

Se o Codex estiver trabalhando no mesmo diretório que os perfis Hermes, defina escopo de arquivos no pedido. Não deixe uma tarefa geral alterar `brand/voice.md`, credenciais, configuração do Hermes ou regras permanentes sem uma aprovação explícita.

## Adaptação para o app ChatGPT

O ChatGPT pode servir como sala de planejamento e revisão manual:

- crie um Project com o índice e os arquivos de marca;
- use uma conversa por papel ou uma instrução de papel por rodada;
- cole o handoff estruturado, não o histórico inteiro da conversa anterior;
- peça ao modelo para citar o arquivo e a fonte de cada claim;
- copie somente artefatos aprovados para o vault;
- mantenha publicação e mudanças de playbook atrás de aprovação humana.

O app ChatGPT, sem um Hermes local ou backend conectado, não oferece a persistência, os perfis, a aba Bots, as Routines ou o dispatcher Kanban descritos no artigo. Uma conversa que imita seis papéis é um protótipo manual; não é prova de seis agentes em execução.

Prompt de sessão manual:

```text
Você é o Content Strategist desta campanha.
Use somente o signal card e o source packet abaixo.
Retorne um angle brief com reader, outcome, tension, thesis, flagship format,
reusable object, proof required e distribution entryways.
Não escreva a peça principal, não invente evidência e não publique.

[SIGNAL CARD]
...

[SOURCE PACKET]
...
```

Quando o trabalho precisar continuar sozinho, sobreviver a uma reinicialização ou distribuir tarefas a perfis nomeados, instale e configure o Hermes separadamente. Não trate uma instrução de Project como equivalente a Bot Mode.

## Manutenção e verificações

Depois de atualizar o Hermes, repita a conversa básica antes de mexer na frota:

```bash
hermes --version
hermes profile list
hermes cron list
hermes kanban list
hermes kanban stats
hermes --continue
```

Verifique também:

- cada perfil aponta para a `SOUL.md` e skills esperadas;
- o vault não contém segredos ou tokens;
- cada campanha tem fontes diretas e estado explícito;
- cada worker escreve um handoff antes de encerrar;
- retries, bloqueios e revisões aparecem no histórico do Kanban;
- a aprovação humana está registrada antes de qualquer publicação;
- “publicado” tem ID ou readback do provedor.

Faça backup do vault e do estado do Hermes antes de migrações. Não copie indiscriminadamente `~/.hermes` entre perfis, especialmente arquivos de OAuth, `state.db` e cron jobs. Para compartilhar um perfil, prefira `hermes profile export`, que remove chaves do arquivo exportado, e revise o conteúdo antes de importar.

## Fontes canônicas

- [Tutorial da VibeMarketer no X](https://x.com/VibeMarketer_/status/2093330541177352217)
- [Artigo completo do X](https://x.com/i/article/2093330534495916032)
- [Hermes Agent no GitHub](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent Quickstart](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/quickstart.md)
- [Instalação do Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/installation.md)
- [Bot Mode](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/bot-mode.md)
- [Perfis](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md)
- [Kanban](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban.md)
- [Hermes Desktop](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/desktop.md)
