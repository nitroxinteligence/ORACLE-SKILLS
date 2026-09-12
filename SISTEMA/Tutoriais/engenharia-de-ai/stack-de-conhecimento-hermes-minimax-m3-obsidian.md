---
title: "Stack de conhecimento com Hermes, MiniMax M3 e Obsidian"
slug: stack-de-conhecimento-hermes-minimax-m3-obsidian
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/polydao/status/2066904909849440434
source_article: http://x.com/i/article/2065198988287234048
source_author: "Mr. Buzzoni (@polydao)"
source_published_at: "2026-06-16T15:25:06Z"
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
tags:
  - hermes-agent
  - minimax-m3
  - obsidian
  - second-brain
  - gestao-do-conhecimento
  - agentes-de-ai
---

# Stack de conhecimento com Hermes, MiniMax M3 e Obsidian

Este tutorial transforma o [artigo de Mr. Buzzoni](https://x.com/polydao/status/2066904909849440434) em um fluxo prático para unir três camadas:

- **Obsidian:** memória local e fonte principal do conhecimento;
- **Hermes Agent:** operador que lê, organiza e atualiza o vault;
- **MiniMax M3:** modelo responsável pelo raciocínio em contextos extensos.

A ideia é substituir conversas isoladas por um ciclo contínuo no qual o conhecimento entra no Obsidian, é trabalhado pelo agente e volta ao vault como Markdown organizado.

## Por que usar uma stack de conhecimento

Um sistema clássico de gestão de conhecimento pessoal costuma falhar de três formas:

1. as notas são escritas uma vez e nunca mais atualizadas;
2. as conversas com IA começam do zero a cada nova sessão;
3. o contexto de trabalhos longos se perde, tanto para a pessoa quanto para o modelo.

A stack proposta tenta criar:

- um grafo local e conectado de tudo o que você sabe;
- um agente que trabalhe dentro desse grafo;
- um modelo capaz de raciocinar sobre muitas notas e ações durante uma mesma tarefa.

O resultado esperado é um segundo cérebro que melhora conforme novas notas, relações, sínteses e revisões são adicionadas.

## Como as três camadas funcionam

```text
Captura no Obsidian
        ↓
Hermes lê arquivos e executa ferramentas
        ↓
MiniMax M3 organiza, compara e sintetiza
        ↓
Hermes grava o resultado em Markdown
        ↓
O novo conhecimento volta ao Obsidian
```

Cada camada tem uma função própria:

- o **Obsidian** armazena os arquivos, links, tags, notas diárias e mapas de conteúdo;
- o **Hermes** lê pastas, usa ferramentas, consulta conversas anteriores, executa tarefas longas e decide o que deve ser persistido;
- o **MiniMax M3** recebe o contexto, compara documentos e gera a transformação solicitada.

O Hermes não substitui o Obsidian. Ele fica entre o vault e o modelo para transformar conhecimento armazenado em ações e novos documentos.

## Camada 1: use o Obsidian como fonte principal

Mantenha o conhecimento em arquivos Markdown normais no disco. Isso permite pesquisar, criar links, versionar e editar as notas sem prender o conteúdo a uma plataforma de chat.

Princípio operacional:

> Se vale a pena guardar, deve entrar primeiro no Obsidian. Se o agente produziu algo útil, o resultado deve voltar como nota.

Backlinks, visualização em grafo, notas diárias e plugins ajudam ideias relacionadas a formar grupos em vez de desaparecerem no histórico de uma conversa.

Use uma estrutura com funções claras:

```text
Vault/
├── Inbox/
├── Daily/
├── Reading/
├── Projects/
├── Reviews/
└── AI/
```

- `Inbox/` recebe capturas rápidas, ideias brutas e materiais ainda não processados;
- `Daily/` guarda registros diários com pouco atrito;
- `Reading/` reúne artigos, destaques, citações e notas de leitura;
- `Projects/` contém trabalhos em andamento e entregas duráveis;
- `Reviews/` recebe sínteses semanais e mensais;
- `AI/` guarda notas permanentes relacionadas ao tema.

Uma regra simples de permissão:

- humanos escrevem livremente em `Inbox/`, `Daily/` e `Reading/`;
- o Hermes pode resumir e consolidar em `Projects/`, `Reviews/` e pastas temáticas;
- notas permanentes vivem em caminhos estáveis e previsíveis.

O vault continua sendo a fonte principal mesmo quando o Hermes lê, refatora ou cria notas.

## Camada 2: use o Hermes como operador

Hermes Agent é apresentado como um agente open source da Nous Research. Ele mantém contexto persistente sobre o usuário e o trabalho, cria skills a partir da experiência, melhora essas skills durante o uso e pesquisa conversas anteriores para recuperar informações relevantes.

Há duas formas principais de executar o Hermes:

### Hermes CLI

Disponível para Linux, macOS e WSL2. É a opção para quem deseja:

- reproduzir configurações;
- automatizar tarefas por scripts;
- executar o agente em servidor ou VPS;
- controlar ferramentas e variáveis de ambiente;
- manter trabalhos longos em execução.

### Hermes Desktop

Aplicativo nativo para macOS, Windows e Linux. É a opção para quem deseja:

- uma interface gráfica;
- onboarding mais simples;
- interação cotidiana sem depender do terminal;
- acesso ao mesmo núcleo do Hermes em um aplicativo.

Os dois modos podem ser usados juntos: Desktop para interação diária e CLI para configuração, automação e execução remota.

## Configure o Hermes

Depois de instalar o Hermes pelo caminho escolhido, abra o assistente principal:

```bash
hermes setup
```

Para usar o caminho integrado ao Nous Portal:

```bash
hermes setup --portal
```

Em seguida, verifique o ambiente:

```bash
hermes doctor
```

O comando verifica dependências, `PATH`, configuração do provedor e problemas comuns antes da conexão do modelo e das ferramentas.

Mantenha o vault em um caminho normal do sistema de arquivos e disponibilize esse caminho ao Hermes durante a configuração.

## Camada 3: use o MiniMax M3 como mecanismo de raciocínio

O artigo apresenta o MiniMax M3 como modelo de contexto longo, multimodal e orientado a tarefas com ferramentas. Ele é usado no Hermes para trabalhos que dependem da leitura conjunta de muitas notas.

Abra o seletor de modelos:

```bash
hermes model
```

No fluxo interativo:

1. escolha o provedor que oferece acesso ao MiniMax M3;
2. selecione o modelo;
3. salve-o como padrão para tarefas de contexto longo;
4. mantenha um modelo menor e rápido para operações mecânicas.

Quando for necessário definir valores específicos pela CLI, use o fluxo suportado pelo Hermes:

```bash
hermes config set
```

Use um modelo rápido para:

- renomear arquivos;
- localizar uma string;
- formatar YAML;
- executar pequenas transformações.

Use o MiniMax M3 para:

- ler pastas grandes de notas;
- comparar informações distribuídas pelo grafo;
- combinar notas duplicadas ou sobrepostas;
- escrever sínteses estruturadas com a taxonomia do vault;
- executar pesquisas longas cujo contexto cresce durante o trabalho;
- realizar tarefas de código com muitas chamadas de ferramentas.

## Comportamentos observados pelo autor

O autor relata que escolheu o M3 pela experiência diária, não por benchmarks. Nos modelos usados anteriormente, uma nota isolada era resumida corretamente, mas tarefas com dez notas, MOCs e escrita de volta ao vault perdiam coerência.

Os sintomas descritos eram:

- resumo coerente localmente, mas errado no conjunto;
- citação de projeto que não estava no arquivo;
- uso de tag pertencente a outra taxonomia;
- criação de wikilink para uma página inexistente.

Três características se destacaram no uso relatado:

### Uso da taxonomia

Em um esquema fixo com cerca de 41 tags, como `#coin/*`, `#project/*`, `#concept/*`, `#solana-internal` e `#meta`, o modelo selecionava a tag principal correta na primeira tentativa em aproximadamente 90% dos casos. Com um modelo de contexto de 200 mil tokens, o autor estima cerca de 60%.

### Coerência em loops longos

Uma inspeção completa do vault pode exigir mais de 30 chamadas de ferramentas: ler um MOC, seguir wikilinks, contar tags, procurar duplicações e escrever o relatório. Segundo o relato, outros modelos começavam a desviar por volta da oitava ou nona chamada, enquanto o M3 mantinha a tarefa até o fim.

### Referências futuras

Quando um conceito ainda não possui nota própria, o modelo escreve um wikilink mesmo assim. O Obsidian mostra esse link em cinza, e ele pode ser revisado durante a manutenção semanal.

Isso transforma conceitos ausentes em uma fila de notas futuras:

```markdown
Este tema se relaciona com [[Conceito que ainda será criado]].
```

## Pontos relatados pelo autor

- a primeira resposta pode demorar porque o Hermes pré-carrega o contexto;
- o modelo pode criar com confiança um `[[wikilink]]` para uma página inexistente;
- o comportamento de referências futuras exige uma revisão semanal;
- a capacidade multimodal atende imagens e capturas curtas;
- PDFs cheios de diagramas ainda podem exigir uma ferramenta de visão dedicada.

## Primeiro fluxo real com o vault

Comece com uma única pasta e uma única saída.

1. aponte o Hermes para o vault;
2. permita acesso a somente uma pasta inicial;
3. escolha uma transformação clara;
4. peça um único arquivo Markdown como resultado;
5. abra o arquivo no Obsidian;
6. ajuste o pedido até o resultado ficar previsível;
7. acrescente outro fluxo somente depois disso.

Primeiro pedido:

```text
Leia tudo em Reading/AI Agents/ e crie uma nota consolidada chamada
agent-architecture-overview.md.

Organize a nota em seções, preserve links para as fontes e indique quais
conceitos já possuem notas relacionadas no vault.
```

Segundo pedido:

```text
Leia as notas dos últimos sete dias em Daily/ e escreva a revisão semanal em
Reviews/2026-W24.md.

Inclua decisões, tarefas abertas, mudanças de opinião e links para os projetos
citados.
```

Terceiro pedido:

```text
Encontre ideias duplicadas entre Inbox/ e Projects/. Não altere os arquivos.
Crie uma proposta de consolidação com os pares encontrados e o destino sugerido.
```

Cada tarefa deve apontar para pastas reais e produzir arquivos Markdown reais.

## Transforme uma leitura em nota permanente

Crie um modelo de cinco seções:

```markdown
# Perfil

# Contexto na minha pesquisa

# Links para o vault

# Tags

# Relacionados
```

Fluxo:

1. coloque um artigo novo em `Reading/raw/`;
2. peça ao Hermes para ler o arquivo;
3. use o MiniMax M3 para compilar o conteúdo no modelo de cinco seções;
4. escolha uma tag da taxonomia existente;
5. crie wikilinks para notas relacionadas;
6. identifique qual MOC precisa receber o novo item;
7. grave a nota na pasta temática adequada.

Pedido:

```text
Leia o novo artigo em Reading/raw/ e transforme-o em uma nota permanente.

Use as seções Perfil, Contexto na minha pesquisa, Links para o vault, Tags e
Relacionados. Escolha tags que já existem, crie wikilinks para notas relevantes
e informe qual MOC precisa ser atualizado.
```

No fluxo relatado, cada compilação passa a fazer parte do contexto disponível para trabalhos futuros. Após meses de uso, o conjunto ajuda o modelo a reconhecer a voz, a taxonomia e os MOCs usados em cada assunto.

## Trabalhos que valem a automação

Os casos mais fortes não são perguntas isoladas, mas transformações recorrentes:

- transformar a nota de ontem em um resumo estruturado;
- combinar dez notas de leitura em uma nota permanente;
- extrair perguntas abertas de uma pasta de projeto;
- produzir uma revisão semanal a partir de notas espalhadas;
- comparar notas atuais com versões antigas e destacar mudanças de opinião;
- procurar notas órfãs;
- converter novos destaques em notas atômicas conectadas.

Um modelo de contexto curto pode resumir uma única nota. A função do M3 nessa stack é trabalhar sobre uma pasta inteira, cruzar o conteúdo com vários MOCs e gerar uma visão que preserve voz, tags e relações.

## Programe manutenção recorrente

Hermes também pode trabalhar com gateways, agendadores e execução em segundo plano.

Exemplos de rotinas:

```text
Todos os dias às 08:00
Resumir as notas de ontem e gravar o resultado em Reviews/.

Toda sexta-feira
Gerar uma revisão semanal a partir de Daily/ e Projects/.

Uma vez por dia
Procurar notas órfãs, wikilinks ausentes e problemas estruturais.

Todas as noites
Transformar novos destaques de leitura em notas atômicas e conectá-las ao vault.
```

Respostas de chat desaparecem no histórico. A manutenção programada acumula notas, relações e revisões no sistema de conhecimento.

## Fluxo completo

1. instale o Hermes pela CLI ou pelo Desktop;
2. execute `hermes setup` ou `hermes setup --portal`;
3. execute `hermes doctor`;
4. abra `hermes model`;
5. escolha o provedor que disponibiliza MiniMax M3;
6. defina o M3 como modelo para tarefas longas;
7. mantenha um modelo menor para ações mecânicas;
8. aponte o Hermes para o vault do Obsidian;
9. libere somente uma pasta inicial;
10. peça uma transformação com uma saída Markdown definida;
11. abra o resultado no Obsidian;
12. repita até o fluxo ficar estável;
13. adicione novas pastas e rotinas aos poucos;
14. programe revisões e tarefas recorrentes.

O produto desta stack é o ciclo completo: capturar, ler, raciocinar, reorganizar, escrever e reutilizar conhecimento dentro do mesmo vault.

## Fonte

- [Karpathy-Style Knowledge Stack: Why I Put Hermes, MiniMax M3 and Obsidian at the Core](https://x.com/polydao/status/2066904909849440434)
