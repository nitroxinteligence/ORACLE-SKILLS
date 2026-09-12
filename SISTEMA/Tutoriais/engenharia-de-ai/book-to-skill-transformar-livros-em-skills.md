---
title: "Book-to-Skill: transforme livros e documentos em skills para agentes de IA"
slug: book-to-skill-transformar-livros-em-skills
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/naldzyul/status/2098376173243814345
source_author: "naldz. (@naldzyul)"
source_published_at: "2026-09-11T11:40:40Z"
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
repository: https://github.com/virgiliojr94/book-to-skill
repository_commit: 01f8a742aeb9022df59ad61870469d07f299c479
official_sources:
  - https://github.com/virgiliojr94/book-to-skill
  - https://github.com/virgiliojr94/book-to-skill/blob/master/docs/install.md
  - https://github.com/virgiliojr94/book-to-skill/blob/master/docs/usage.md
  - https://github.com/virgiliojr94/book-to-skill/blob/master/docs/how-it-works.md
  - https://github.com/virgiliojr94/book-to-skill/blob/master/SECURITY-NOTICE.md
tags:
  - book-to-skill
  - skills
  - agentes-de-ia
  - codex
  - claude-code
  - hermes-agent
  - livros
  - gestao-do-conhecimento
---

# Book-to-Skill: transforme livros e documentos em skills para agentes de IA

O [post de naldz.](https://x.com/naldzyul/status/2098376173243814345) apresenta o **book-to-skill**, uma ferramenta open source que transforma um livro ou conjunto de documentos em uma skill estruturada para agentes de IA.

Em vez de colocar o livro inteiro no contexto a cada pergunta, a ferramenta prepara um índice, os principais modelos mentais e arquivos separados por capítulo. O agente carrega o arquivo correspondente quando você consulta um tema específico.

O projeto funciona com hosts compatíveis com o padrão Agent Skills, incluindo Codex, Claude Code, GitHub Copilot CLI, Amp e Hermes Agent.

Fonte oficial consultada: [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill), commit `01f8a742aeb9022df59ad61870469d07f299c479`.

![Imagem da publicação](https://pbs.twimg.com/media/HR7uAfHWAAM8oKj.jpg)

## O que a ferramenta gera

Uma conversão completa cria uma pasta de skill com esta estrutura:

```text
nome-do-livro/
├── SKILL.md
├── chapters/
│   ├── ch01-titulo.md
│   ├── ch02-titulo.md
│   └── ...
├── glossary.md
├── patterns.md
└── cheatsheet.md
```

Cada parte possui uma função própria:

| Arquivo | Conteúdo |
|---|---|
| `SKILL.md` | modelos mentais centrais, princípios e índice de capítulos e assuntos |
| `chapters/*.md` | conceitos, técnicas, exemplos, padrões e conclusões de cada capítulo |
| `glossary.md` | termos importantes em ordem alfabética, com referência aos capítulos |
| `patterns.md` | técnicas, algoritmos, padrões, situações de uso e trade-offs |
| `cheatsheet.md` | regras de decisão, matrizes, limites, padrões de reconhecimento e referência rápida |

O objetivo não é produzir apenas um resumo. A skill tenta converter a estrutura do material em conhecimento acionável: quando usar um método, como aplicá-lo, quais decisões ele orienta e quais erros evitar.

## Por que separar o conteúdo por capítulo

Um livro completo pode ocupar dezenas ou centenas de milhares de tokens. O post usa como exemplo um livro de 400 páginas que exigiria cerca de 200 mil tokens se fosse carregado por inteiro.

No book-to-skill, o arquivo principal permanece compacto e aponta para capítulos específicos. Quando você pergunta sobre replicação, pricing, arquitetura ou outro assunto indexado, o agente abre somente os arquivos relacionados.

Isso permite manter várias skills instaladas sem colocar todo o conteúdo delas no contexto ao mesmo tempo. A documentação do projeto relata uma redução de **24 a 51 vezes** no consumo de tokens para responder uma pergunta, em comparação com despejar o livro no contexto. O ganho real varia conforme tamanho, estrutura, formato, pergunta e comportamento do agente.

## Formatos aceitos

O conversor aceita:

- PDF;
- EPUB;
- DOCX;
- TXT e Markdown;
- reStructuredText e AsciiDoc;
- HTML;
- RTF;
- MOBI, AZW e AZW3 com Calibre.

Também é possível fornecer uma pasta, um padrão glob ou vários arquivos para criar uma única skill. Isso serve para livros divididos em volumes, documentação interna, coleções de artigos, normas, pesquisas e sistemas de marca.

## 1. Instale o book-to-skill

### Instalação compartilhada para Codex, Amp e Copilot CLI

O método recomendado pelo projeto usa o instalador de skills:

```bash
npx skills add virgiliojr94/book-to-skill
```

Você também pode instalar manualmente no diretório compartilhado:

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git \
  ~/.agents/skills/book-to-skill
```

O Codex lê `~/.agents/skills`. Abra uma nova sessão depois da instalação para atualizar o catálogo de skills.

### Claude Code

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git \
  ~/.claude/skills/book-to-skill
```

### Hermes Agent

```bash
git clone https://github.com/virgiliojr94/book-to-skill.git \
  "${HERMES_HOME:-$HOME/.hermes}/skills/productivity/book-to-skill"
```

Em um projeto local do Hermes, instale em `.hermes/skills/<categoria>/book-to-skill`, marque o projeto como confiável e confira a descoberta:

```bash
hermes skills trust /caminho/do/projeto
hermes skills list
```

## 2. Confira os extratores disponíveis

Entre na pasta da skill e execute:

```bash
cd ~/.agents/skills/book-to-skill
python3 scripts/extract.py --check
```

O comando mostra quais extratores já estão instalados e o que falta para cada formato.

Para documentos de texto simples, Markdown, reStructuredText e AsciiDoc, o Python padrão é suficiente. Outros formatos podem usar dependências opcionais:

| Material | Extrator indicado |
|---|---|
| PDF com prosa e poucas tabelas | `pdftotext`, com fallback para `pypdf` ou `pdfminer.six` |
| PDF técnico com código, tabelas ou fórmulas | `docling` |
| PDF escaneado | OCR prévio com `ocrmypdf` |
| EPUB | `ebooklib` e `beautifulsoup4`, com fallback nativo |
| DOCX | `python-docx`, com fallback por ZIP/XML |
| HTML | `beautifulsoup4`; `trafilatura` melhora a remoção de boilerplate |
| RTF | `striprtf`, com fallback por expressão regular |
| MOBI/AZW/AZW3 | `ebook-convert`, incluído no Calibre |

Para instalar o conjunto comum de extratores pela CLI do projeto:

```bash
pip install "book-to-skill[pdf,epub,docx] @ git+https://github.com/virgiliojr94/book-to-skill.git"
book-to-skill --check
```

Essa instalação por `pip` fornece apenas o mecanismo de extração. Ela não registra a skill no agente. Para obter o fluxo completo, mantenha também a instalação em uma pasta de skills.

## 3. Classifique o tipo de livro

Antes da extração, escolha o modo correto:

- **technical:** preserve código, tabelas, fórmulas, comandos, APIs e sintaxe;
- **text:** priorize velocidade para livros de prosa, negócios, estratégia ou conteúdo com poucas estruturas técnicas.

Para PDFs técnicos, o Docling tende a conservar melhor blocos de código e tabelas, mas é mais lento. Para texto corrido, `pdftotext` costuma ser suficiente.

Se o PDF for apenas uma sequência de imagens, faça OCR primeiro:

```bash
ocrmypdf livro-escaneado.pdf livro-com-ocr.pdf
```

## 4. Converta um documento

Em uma sessão do agente que tenha a skill instalada, peça:

```text
/book-to-skill ~/Livros/meu-livro.pdf
```

Você pode definir o slug da skill no mesmo comando:

```text
/book-to-skill ~/Livros/meu-livro.pdf meu-livro
```

O nome deve usar letras minúsculas, números e hífens.

## 5. Converta vários arquivos ou uma pasta

### Vários documentos em uma única skill

```text
/book-to-skill ~/Pesquisas/artigo-1.pdf ~/Pesquisas/notas.md pesquisa-unificada
```

### Todos os documentos aceitos de uma pasta

```text
/book-to-skill ~/Projetos/manual-interno/ manual-do-projeto
```

### Arquivos selecionados por padrão

```text
/book-to-skill "~/Livros/*.epub" biblioteca-tecnica
```

Use uma skill unificada quando as fontes tratam do mesmo domínio e precisam ser consultadas juntas. Materiais sem relação ficam mais fáceis de encontrar e manter quando são convertidos em skills separadas.

## 6. Acompanhe o processo de conversão

O fluxo do book-to-skill possui duas partes:

```text
Documento, pasta ou conjunto de arquivos
                ↓
Extrator Python determinístico
                ↓
full_text.txt + metadata.json
                ↓
Agente identifica capítulos, conceitos e estrutura
                ↓
SKILL.md + chapters/ + glossary.md + patterns.md + cheatsheet.md
                ↓
Scanner de segurança da skill gerada
                ↓
Skill instalada no diretório escolhido
```

O extrator limpa o texto e produz metadados. Depois, o agente identifica título, autoria, sumário, capítulos, conceitos, frameworks, técnicas e anti-padrões. A etapa final cria os arquivos e executa um scanner antes de recomendar o carregamento ou a publicação da skill.

Se um dos arquivos de uma entrada múltipla falhar, o conversor pode ignorar essa fonte com um aviso e continuar com as demais. Leia o relatório final para confirmar quais documentos realmente entraram na skill.

## 7. Use a skill criada

Suponha que o slug criado seja `designing-data-intensive-apps`.

Carregue os principais modelos mentais:

```text
/designing-data-intensive-apps
```

Consulte um assunto:

```text
/designing-data-intensive-apps replication
```

Abra um capítulo específico:

```text
/designing-data-intensive-apps ch05
```

Veja o índice disponível:

```text
/designing-data-intensive-apps "quais capítulos você tem?"
```

O índice de tópicos presente no `SKILL.md` ajuda o agente a localizar o capítulo correto antes de responder.

## 8. Atualize uma skill existente

Para incorporar um novo documento sem reconstruir tudo do zero, informe a nova fonte e a pasta da skill existente:

```text
/book-to-skill ~/Artigos/novo-artigo.pdf \
  ~/.agents/skills/conhecimento-do-projeto
```

O modo de atualização extrai o novo material e combina conceitos, capítulos e índices com a estrutura existente. Depois, confira se o relatório reconheceu o destino correto e quais arquivos foram alterados.

## 9. Aplique a ferramenta além de livros

O mesmo processo funciona com:

- documentação de arquitetura e decisões técnicas;
- runbooks e guias de onboarding;
- manuais de marca, voz e design;
- conjuntos de artigos e papers;
- RFCs, padrões e contratos de API;
- documentação de produto;
- notas próprias sobre um domínio.

Um bom candidato é um conjunto de documentos que você consulta com frequência e que contém decisões, regras, métodos ou conceitos reutilizáveis.

## 10. Verifique o resultado

Antes de usar a nova skill em trabalho real, abra os arquivos gerados e confira:

1. se título, autor e capítulos foram reconhecidos corretamente;
2. se todos os arquivos de entrada aparecem nos metadados;
3. se o índice aponta para arquivos que realmente existem;
4. se nomes de frameworks, comandos e conceitos foram preservados;
5. se tabelas e blocos de código importantes sobreviveram à extração;
6. se o scanner de segurança terminou sem apontamentos pendentes;
7. se uma pergunta de teste leva o agente ao capítulo esperado.

A organização reduz o volume de contexto e facilita a recuperação, mas não garante que toda resposta esteja correta. Para uma decisão importante, abra o capítulo correspondente e compare a resposta com o documento original.

## Privacidade e direitos autorais

O extrator roda localmente e o repositório não inclui conteúdo de livros. Se o agente usa um modelo em nuvem, o texto enviado durante a análise segue as regras de dados daquele provedor.

Use documentos que você possui ou tem autorização para processar. As skills geradas contêm sínteses derivadas do material. Skills de livros protegidos de terceiros devem permanecer privadas. Não publique uma skill derivada de conteúdo protegido sem autorização de redistribuição.

## Aviso de segurança sobre cópias falsas

O mantenedor informa que o único repositório oficial é:

```text
https://github.com/virgiliojr94/book-to-skill
```

O arquivo `SECURITY-NOTICE.md` do projeto alerta para uma cópia maliciosa em `Leutenegger/book-to-skill`, que não é afiliada ao projeto oficial. Essa cópia foi descrita como contendo desativação de TLS, coleta de informações do sistema, enumeração de dados ligados a carteiras e envio de arquivos para um endpoint externo.

Instale somente com o identificador oficial:

```bash
npx skills add virgiliojr94/book-to-skill
```

## Referências

- [Publicação original no X](https://x.com/naldzyul/status/2098376173243814345)
- [Repositório oficial](https://github.com/virgiliojr94/book-to-skill)
- [Instalação](https://github.com/virgiliojr94/book-to-skill/blob/master/docs/install.md)
- [Uso](https://github.com/virgiliojr94/book-to-skill/blob/master/docs/usage.md)
- [Como funciona](https://github.com/virgiliojr94/book-to-skill/blob/master/docs/how-it-works.md)
- [Aviso de segurança](https://github.com/virgiliojr94/book-to-skill/blob/master/SECURITY-NOTICE.md)

