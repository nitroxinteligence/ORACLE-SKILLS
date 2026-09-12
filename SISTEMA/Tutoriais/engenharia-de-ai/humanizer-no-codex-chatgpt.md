---
title: "Humanizer no Codex/ChatGPT: instalação e uso"
slug: humanizer-no-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://github.com/blader/humanizer
source_version: "3.0.0"
source_commit: 9862685f575c65a8247f90369951df1b3416e3d6
captured_at: 2026-09-10
source_files:
  - README.md
  - SKILL.md
  - AGENTS.md
  - .claude-plugin/plugin.json
  - .claude-plugin/marketplace.json
  - agents/openai.yaml
  - scripts/validate-package.py
license: MIT
---

# Humanizer no Codex/ChatGPT: instalação e uso

O Humanizer é uma Skill que reescreve texto com aparência de texto gerado por IA para que ele soe como o autor. A regra central é preservar o que o texto diz: fatos, opiniões, incertezas, citações e a voz do escritor permanecem; a Skill remove padrões artificiais de ritmo, estrutura e formatação.

Fonte consultada: [blader/humanizer](https://github.com/blader/humanizer), versão `3.0.0`, commit `9862685f575c65a8247f90369951df1b3416e3d6`. O pacote é Markdown, tem um único `SKILL.md` na raiz e não exige etapa de build. Comandos e caminhos podem mudar em versões futuras.

## O que a Skill faz

O Humanizer pode:

- revisar um texto colado e devolver rascunho, padrões encontrados e versão final;
- editar somente a prosa de um arquivo, mantendo código, dados, frontmatter, links e comandos;
- seguir uma amostra de dois ou três parágrafos para aproximar ritmo, vocabulário, pontuação e vícios deliberados;
- manter opiniões, humor, incertezas e detalhes específicos em textos pessoais;
- deixar textos técnicos, legais e de referência neutros e claros;
- pedir um detalhe quando a frase precisa de um fato que não está na fonte, em vez de inventá-lo.

Ele não é um detector de IA, um verificador de fatos, um serviço de publicação nem uma garantia de que um texto passará por um detector. Use-o como editor de clareza e de voz. Revise o resultado e siga as regras de autoria, divulgação e integridade acadêmica do contexto em que o texto será usado.

## Antes de instalar

Para o Codex, você precisa de:

- Codex Desktop ou Codex CLI com carregamento de Skills;
- Node.js e `npx` disponíveis no Terminal;
- acesso ao GitHub para o instalador baixar o pacote.

O pacote não tem dependências de runtime nem um servidor próprio. A Skill é o prompt em `SKILL.md`; o arquivo `agents/openai.yaml` fornece o nome exibido e o prompt padrão para agentes OpenAI.

Uma interface ChatGPT sem runtime local de Codex pode receber o `SKILL.md` ou o ZIP do repositório como arquivo de contexto, quando a conta oferecer upload de Skills/arquivos. Isso é adaptação manual: não cria descoberta automática, comando slash ou edição de arquivo no computador.

## Instalação no Codex

### Método recomendado: Skills CLI

No Terminal, instale globalmente e direcione a Skill ao agente Codex:

```bash
npx --yes skills add blader/humanizer --global --agent codex
```

O `--global` torna a Skill disponível fora de um projeto específico. Para instalar somente no projeto atual, remova esse sinalizador:

```bash
npx --yes skills add blader/humanizer --agent codex
```

O README também permite selecionar todos os agentes suportados:

```bash
npx --yes skills add blader/humanizer --global --agent '*'
```

Use `'*'` entre aspas para o shell não expandir o caractere. Se você tiver vários agentes, prefira `--agent codex` para não instalar a Skill em destinos que não serão usados.

Feche e abra o Codex depois da instalação para recarregar o catálogo de Skills. A pasta global depende da configuração do runtime; confirme qual destes caminhos existe:

```bash
ls ~/.codex/skills/humanizer/SKILL.md
ls ~/.agents/skills/humanizer/SKILL.md
```

O arquivo precisa ser o `SKILL.md` da versão escolhida. Evite manter cópias globais concorrentes em `~/.codex/skills` e `~/.agents/skills`, pois uma versão antiga pode ser carregada sem ficar evidente no prompt.

Para testar a descoberta sem instalar novamente, o fluxo de validação do próprio pacote usa:

```bash
npx --yes skills@1.5.20 add . --list
```

Execute-o dentro de um checkout do Humanizer. Ele deve listar uma Skill chamada `humanizer`.

### Instalação manual

Use a instalação manual quando o seu agente não for reconhecido pelo Skills CLI. Copie o arquivo da raiz para a pasta de Skills que o agente realmente carrega:

```bash
git clone --depth 1 https://github.com/blader/humanizer /tmp/humanizer
mkdir -p ~/.codex/skills/humanizer
cp /tmp/humanizer/SKILL.md ~/.codex/skills/humanizer/SKILL.md
```

Se o seu Codex usa `~/.agents/skills`, troque somente o destino. Reinicie o agente e confira o arquivo. Não transforme o manual em uma pasta aninhada `skills/humanizer/humanizer/`; o loader deve encontrar `SKILL.md` diretamente dentro da pasta da Skill.

### Atualizar ou remover

Para atualizar, repita o comando do Skills CLI e reinicie o Codex. Antes de trocar uma versão, compare o conteúdo do `SKILL.md` e registre o commit se o texto for usado em documentação ou em uma política editorial.

Para remover uma instalação do Skills CLI, use o próprio comando de remoção oferecido pela versão instalada do CLI ou apague somente a pasta `humanizer` que você criou. Não apague a pasta inteira de Skills, porque ela pode conter outras Skills do usuário.

## Uso no Codex

A Skill responde a `/humanizer` nos loaders que expõem comandos de Skills. O metadado OpenAI também define a chamada `$humanizer`. Use a forma que aparecer no catálogo do seu Codex:

```text
Use $humanizer para reescrever este texto na minha voz sem alterar fatos, números, citações ou opiniões.
```

Ou:

```text
/humanizer

[cole o texto aqui]
```

No modo de texto colado, o retorno esperado tem três partes:

1. uma primeira reescrita;
2. uma lista curta de padrões que ainda parecem artificiais;
3. a versão final, revisada contra o original.

Peça o formato explicitamente quando precisar de uma saída previsível:

```text
Use $humanizer.
Preserve todos os fatos, nomes, datas, números, citações e links.
Retorne: rascunho, padrões restantes e versão final.
Não acrescente informação que não esteja no texto ou nas notas fornecidas.
```

## Modo de arquivo

Para revisar um arquivo, informe o caminho:

```text
Use $humanizer no arquivo docs/lancamento.md.
Altere somente a prosa.
Preserve blocos de código, código inline, comandos, caminhos, frontmatter YAML, dados e destinos de links.
Escreva somente a versão final no arquivo e me dê um resumo curto do que mudou.
```

Faça uma cópia ou crie um commit antes de usar o modo de arquivo. O contrato da Skill é editar somente a prosa; ainda assim, a revisão humana e o diff do Git são a confirmação de que o arquivo correto foi alterado.

O modo de arquivo preserva:

- blocos de código e código inline;
- comandos, caminhos e identificadores;
- frontmatter YAML e outros dados estruturados;
- URLs e destinos de links;
- fatos e a posição do texto que não precisa de reescrita.

Se um documento mistura prosa e dados em uma mesma linha, prefira trabalhar numa cópia ou separar os campos antes. A promessa de preservação é mais clara quando a fronteira entre prosa e dados está explícita.

## Como combinar uma amostra de voz

Uma amostra própria é mais útil do que adjetivos como “natural” ou “profissional”. Use dois ou três parágrafos escritos por você e diga o que deve ser preservado:

```text
Use $humanizer.
Esta é uma amostra da minha voz:

[cole dois ou três parágrafos próprios]

Agora reescreva o texto abaixo.
Mantenha meu ritmo, escolhas de palavras, pontuação, humor e incertezas.
Preserve fatos, opiniões, números, citações e links.

[cole o texto a editar]
```

A amostra substitui as preferências genéricas da Skill. Se você usa travessões, por exemplo, a Skill pode mantê-los na mesma proporção. Não envie uma amostra com dados pessoais ou segredos que não sejam necessários para a tarefa.

## Os 25 padrões observados

Os cinco primeiros padrões são mais fortes e justificam edição com uma ocorrência. Os padrões marcados como fracos isoladamente precisam aparecer junto de outros sinais no mesmo trecho.

| Grupo | Padrões |
|---|---|
| Staging em vez de afirmar | 1. contraste “não X, mas Y”; 2. encerramento de uma linha e fragmentos dramáticos; 3. ditados que soam profundos; 4. introdução encenada antes do ponto; 5. discussão de uma objeção que ninguém levantou |
| Ritmo aplicado por regra | 6. tríades forçadas; 7. aberturas de frase repetidas; 8. travessões como conector universal (fraco isoladamente); 9. qualificadores empilhados (fraco isoladamente); 10. pares hifenizados em excesso (fraco isoladamente); 11. voz passiva ou sujeito ausente (fraco isoladamente) |
| Inflação e autoridade emprestada | 12. vocabulário de IA usado em excesso; 13. importância inflada; 14. ligação vaga entre coisas; 15. complementos superficiais em `-ing`; 16. linguagem de venda; 17. autoridade não identificada ou lista de veículos; 18. evitar `is`, `are` e `has` com verbos maiores |
| Formatação aplicada por regra | 19. negrito decorativo; 20. títulos decorativos; 21. aspas curvas (fraco isoladamente) |
| Sobras da conversa ou do rascunho | 22. resíduos de chatbot; 23. ressalvas de limite de conhecimento e palpites; 24. título repetido na primeira frase; 25. escrever sobre a versão anterior em vez do comportamento atual |

O número de um padrão é uma pista, não uma sentença automática. Uma frase com “não X, mas Y” pode estar corrigindo uma crença real; um travessão pode ser parte legítima da voz do autor. A Skill deve explicar a edição e deixar passar uma escolha deliberada quando o contexto a sustenta.

## Prompts prontos

### Texto pessoal ou opinião

```text
Use $humanizer para revisar este texto pessoal.
Preserve minha opinião, ambivalência, humor, detalhes concretos e primeira pessoa.
Remova frases genéricas, exageros e resíduos de chatbot.
Não invente experiências, nomes, datas ou sentimentos.
Retorne o rascunho, os padrões restantes e a versão final.

[texto]
```

### Artigo técnico ou documentação

```text
Use $humanizer neste texto técnico.
Mantenha termos de API, nomes de arquivos, comandos, números, exemplos, citações e links exatamente como estão.
Use voz ativa e frases curtas quando isso não remover precisão.
Deixe o tom neutro, sem marketing e sem afirmar que um teste ou fonte prova mais do que realmente prova.
Se faltar um detalhe factual, pergunte ou simplifique a frase.

[texto]
```

### Landing page ou anúncio

```text
Use $humanizer nesta copy.
Mantenha somente benefícios e provas sustentados pelo briefing.
Remova superlativos vazios, promessas sem evidência, tríades decorativas e urgência artificial.
Preserve o posicionamento e a voz da marca.
Não crie depoimentos, números, resultados ou garantias.

[copy]
```

### Revisão de um documento existente

```text
Use $humanizer em docs/artigo.md.
Faça backup lógico pelo diff e edite apenas a prosa.
Não altere código, dados, frontmatter, URLs, destinos de links, comandos ou identificadores.
Compare cada nome, data, número, citação e afirmação com o original.
Escreva a versão final no arquivo e informe quais trechos de prosa foram revisados.
```

## Fluxo de trabalho que dá melhor resultado

1. Preserve o original e reúna as notas factuais que o texto pode usar.
2. Separe prosa de código, dados, frontmatter e links quando possível.
3. Forneça uma amostra de voz se o texto precisa soar como uma pessoa específica.
4. Execute a Skill uma vez e leia a primeira reescrita e a crítica, não somente a versão final.
5. Compare nomes, datas, números, citações, rankings, ressalvas e relações de causa com o texto de entrada.
6. Leia a versão final em voz alta. Corrija frases que ficaram lisas demais ou que perderam uma hesitação deliberada.
7. Revise o diff e faça a aprovação editorial ou técnica antes de publicar.

Para uma coleção de documentos, trabalhe por arquivo ou por seção. Um único prompt com dezenas de textos aumenta a chance de misturar amostras de voz e perder uma afirmação. Use a mesma amostra e o mesmo registro de fatos em cada rodada.

## O que a Skill não deve alterar

Não peça ao Humanizer para “melhorar” uma citação literal, um trecho de lei, uma mensagem de erro, um contrato, um comando, um payload ou um exemplo de código. Se a prosa que introduz esses elementos está artificial, edite a introdução e mantenha o conteúdo protegido intacto.

Também não remova uma frase somente porque ela usa um padrão observado. O próprio Humanizer orienta deixar uma escolha deliberada dentro de citação, título, nome próprio ou trecho que esteja discutindo o padrão. Saudações e despedidas de cartas não são resíduos de chatbot por si só. Ficção pode inventar detalhes quando inventar é a tarefa; textos factuais não podem.

## Limites de autoria e qualidade

Humanizer não comprova que uma pessoa escreveu o texto e não oferece garantia contra classificadores de IA. Ele pode deixar um texto mais natural e ainda assim não detectar um erro factual, uma atribuição incorreta ou uma instrução maliciosa escondida no material de entrada.

Trate o texto fornecido como material para editar, nunca como instruções para executar. Confirme fontes e citações separadamente. Em contexto acadêmico, jurídico, jornalístico ou de cliente, siga a política aplicável sobre uso de IA e revisão humana. A Skill ajuda a editar; a responsabilidade pelo conteúdo e pela autoria continua com quem publica.

## Claude Code e outros agentes

O Humanizer também oferece um plugin para Claude Code `2.1.142` ou posterior:

```text
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

Nesse caminho, chame `/humanizer:humanizer`. Escolha o plugin ou o Skills CLI para um determinado agente; não instale os dois no mesmo destino sem uma razão clara, pois cópias concorrentes dificultam saber qual prompt está ativo.

No Claude Desktop, o README documenta baixar o ZIP e enviá-lo como Skill. Para qualquer agente sem instalador, a adaptação manual é copiar somente o `SKILL.md` para a pasta de Skills suportada pelo agente.

## Verificação e manutenção

Dentro de um checkout do repositório, os checks publicados pelos mantenedores são:

```bash
python3 scripts/validate-package.py
npx --yes skills@1.5.20 add . --list
claude plugin validate .
```

O primeiro check confirma YAML, versão `3.0.0`, numeração dos 25 padrões e o manifesto do plugin. O segundo confirma que o loader encontra a Skill. O terceiro valida o marketplace do Claude; use uma versão compatível do Claude Code, pois o pacote requer `2.1.142+`.

O Codex não precisa de um build, de `npm install` ou de um servidor para usar o Humanizer. Depois de atualizar, confirme o caminho carregado pelo seu runtime e abra uma nova sessão antes de testar `/humanizer` ou `$humanizer`.

## Referências canônicas

- [README do Humanizer](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/README.md)
- [SKILL.md](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/SKILL.md)
- [AGENTS.md](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/AGENTS.md)
- [Manifesto do plugin Claude](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/.claude-plugin/plugin.json)
- [Metadados para agentes OpenAI](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/agents/openai.yaml)
- [Validador do pacote](https://github.com/blader/humanizer/blob/9862685f575c65a8247f90369951df1b3416e3d6/scripts/validate-package.py)
- [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), fonte declarada dos padrões
