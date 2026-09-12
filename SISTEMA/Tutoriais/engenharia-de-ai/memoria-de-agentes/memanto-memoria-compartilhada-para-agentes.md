---
title: "Memanto: memória compartilhada para agentes de IA"
slug: memanto-memoria-compartilhada-para-agentes
language: pt-BR
type: tutorial
category: engenharia-de-ai
subcategory: memoria-de-agentes
source: https://x.com/liambraus/status/2098367927883862279
source_author: "Liam Braus (@liambraus)"
source_published_at: "2026-09-11T11:07:54Z"
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
repository: https://github.com/moorcheh-ai/memanto
tags:
  - memanto
  - memoria-de-agentes
  - codex
  - claude-code
  - cursor
  - memoria-persistente
---

# Memanto: memória compartilhada para agentes de IA

Memanto é um agente de memória que trabalha ao lado de outros agentes. Ele administra o que deve ser guardado, o que entra em conflito, o que expira e qual parte do conhecimento precisa ser entregue a cada agente.

A proposta apresentada por [Liam Braus](https://x.com/liambraus/status/2098367927883862279) inclui:

- guardar o contexto das sessões;
- classificar o conteúdo em 13 tipos de memória;
- recuperar informações relevantes em menos de 90 ms;
- conectar Claude Code, Cursor, Codex e mais de vinte agentes;
- funcionar sem exigir que você monte um banco vetorial manualmente;
- impedir que o projeto precise ser explicado novamente em cada sessão.

## Como o Memanto funciona

Memanto não funciona apenas como uma biblioteca chamada pelo aplicativo. Ele atua como um segundo agente responsável pela memória da frota.

```text
Agente de trabalho
      ↓
Interações e decisões
      ↓
Memanto observa e extrai conhecimento durável
      ↓
Memanto consolida, reconcilia e aplica expiração
      ↓
Cada agente recebe somente o contexto relevante
```

Ele executa seis funções principais.

| Função | O que faz | Comando principal |
|---|---|---|
| observar e extrair | transforma conversas em decisões, fatos, preferências e aprendizados | `memanto remember --from-conversation` |
| consolidar | combina duplicações e fragmentos em um conjunto canônico | `memanto schedule enable` |
| reconciliar | identifica contradições e preserva o histórico das versões | `memanto conflicts` |
| esquecer | aplica expiração, decaimento e exclusão deliberada | `memanto forget` |
| preparar contexto | entrega a cada agente a menor fatia relevante da memória | `memanto agent bootstrap` |
| transportar conhecimento | exporta o conjunto em Open Knowledge Format | `memanto memory export --okf` |

## 1. Instale o Memanto

```bash
pip install memanto
```

Depois, execute o assistente:

```bash
memanto
```

O assistente oferece dois caminhos:

1. **On-Prem:** execução local com Docker e Ollama;
2. **Cloud:** execução com uma chave gratuita.

## 2. Escolha o backend

### Execução totalmente local

```bash
pip install memanto
memanto
```

No assistente, escolha `On-Prem`. Esse modo usa Docker e Ollama e mantém a operação na infraestrutura local.

### Execução em nuvem

```bash
pip install memanto
memanto
```

No assistente, escolha `Cloud` e informe a chave solicitada.

Para trocar de backend depois:

```bash
memanto config backend
```

## 3. Conecte seus agentes

Conecte o agente desejado com um comando próprio.

### Codex

```bash
memanto connect codex
```

### Claude Code

```bash
memanto connect claude-code
```

### Cursor

```bash
memanto connect cursor
```

O fluxo também oferece conexões para Windsurf, Cline, Continue, Goose, OpenCode, Roo, GitHub Copilot, Antigravity, Gemini CLI e Augment.

## 4. Confira o estado do sistema

```bash
memanto status
```

O comando mostra:

- configuração do ambiente;
- saúde do servidor;
- sessão ativa;
- agentes registrados.

Para ver a configuração:

```bash
memanto config show
```

## 5. Registre uma memória

Uma memória pode ser criada diretamente:

```bash
memanto remember \
  "A autenticação migrou para JWT; cookies de sessão foram descontinuados" \
  --type decision
```

Outro agente conectado pode recuperar a decisão:

```bash
memanto recall "como funciona a autenticação"
```

Também é possível pedir uma resposta fundamentada nas memórias recuperadas:

```bash
memanto answer "por que removemos os cookies de sessão?"
```

## 6. Use os 13 tipos de memória

O Memanto classifica o conhecimento em treze categorias:

1. `instruction` — instrução durável;
2. `fact` — fato conhecido;
3. `decision` — decisão tomada;
4. `goal` — objetivo;
5. `commitment` — compromisso;
6. `preference` — preferência;
7. `relationship` — relação entre pessoas, sistemas ou conceitos;
8. `context` — contexto necessário para o trabalho;
9. `event` — acontecimento;
10. `learning` — aprendizado;
11. `observation` — observação;
12. `artifact` — arquivo ou resultado produzido;
13. `error` — falha conhecida.

Exemplo com preferência:

```bash
memanto remember \
  "O usuário prefere respostas curtas e diretas" \
  --type preference

memanto recall \
  "estilo de comunicação do usuário" \
  --type preference
```

## 7. Extraia memórias de conversas

Para transformar uma conversa em conhecimento durável:

```bash
memanto remember --from-conversation
```

O objetivo é extrair fatos, decisões, preferências, erros e aprendizados em vez de guardar transcrições inteiras como um bloco indiferenciado.

## 8. Faça consultas temporais

O Memanto permite consultar o que era conhecido em um momento anterior.

```bash
memanto recall \
  "política de implantação" \
  --as-of 2026-08-05
```

Para descobrir o que mudou desde uma versão:

```bash
memanto recall \
  "política de implantação" \
  --changed-since v2.1
```

Isso separa duas perguntas:

- o que é considerado verdadeiro agora;
- o que a equipe acreditava em uma data anterior.

## 9. Detecte e resolva contradições

```bash
memanto conflicts
```

Quando uma informação nova contradiz uma memória antiga, o Memanto preserva a origem e o momento de cada versão. A informação anterior pode ser substituída sem perder o histórico do que era conhecido.

Esse comportamento evita que a última gravação apague silenciosamente uma decisão anterior.

## 10. Configure expiração

Liste as políticas predefinidas:

```bash
memanto policy list-preset
```

As opções incluem:

- `conservative`;
- `balanced`;
- `aggressive`.

Aplique uma política:

```bash
memanto policy apply-preset balanced
```

Veja o que seria expirado antes da aplicação:

```bash
memanto policy apply --dry-run
```

Aplique:

```bash
memanto policy apply
```

As políticas ficam em:

```text
~/.memanto/policies/<agent>.yaml
```

Exemplo:

```yaml
retention:
  context: 7d
  event: 30d
  preference: never

rules:
  - name: pinned
    match:
      tags:
        - pinned
    expire_after: never

  - name: low-confidence-guesses
    match:
      provenance:
        - inferred
      confidence_below: 0.5
    expire_after: 14d

purge_expired_after: never
```

Nesse exemplo:

- contexto expira após sete dias;
- eventos expiram após trinta dias;
- preferências não expiram automaticamente;
- itens com a tag `pinned` permanecem ativos;
- inferências com baixa confiança expiram após quatorze dias;
- memórias expiradas não são apagadas automaticamente.

## 11. Expire e restaure manualmente

```bash
memanto memory expire mem-123
memanto memory restore mem-123
```

Uma memória expirada permanece recuperável e aparece marcada como `[EXPIRED]`, junto com o motivo. A exclusão permanente é uma ação diferente.

Para consultar somente memórias ativas ou expiradas:

```bash
memanto recall "tema" --active
memanto recall "tema" --expired
```

## 12. Ative a manutenção diária

```bash
memanto schedule enable
```

O ciclo diário pode:

- tratar novas memórias;
- combinar duplicações entre agentes;
- fortalecer observações repetidas;
- aplicar políticas de expiração;
- apontar contradições para revisão.

Um agente sem política definida não expira memórias automaticamente.

## 13. Abra a interface local

```bash
memanto ui
```

A interface permite navegar, pesquisar e auditar o conjunto de memórias.

Para iniciar a API REST local:

```bash
memanto serve
```

## 14. Gere resumos diários

```bash
memanto daily-summary
```

O resumo apresenta mudanças recentes no conhecimento compartilhado entre os agentes.

## 15. Edite ou exclua memórias

Use os comandos:

```bash
memanto edit
memanto forget
```

- `edit` atualiza campos de uma memória;
- `forget` remove permanentemente uma memória incorreta.

Expirar e excluir não são a mesma ação. Expiração preserva o conteúdo com uma marca de estado; exclusão remove o item.

## 16. Importe arquivos

```bash
memanto upload <arquivo>
```

Tipos aceitos:

- PDF;
- DOCX;
- XLSX;
- JSON;
- TXT;
- CSV;
- Markdown.

O conteúdo entra no namespace do agente escolhido.

## 17. Exporte a memória

O conjunto de memórias pode ser exportado em Open Knowledge Format:

```bash
memanto memory export --okf
```

O resultado usa Markdown portátil, legível, pesquisável, versionável e comparável por diff.

Também é possível sincronizar `MEMORY.md` com projetos:

```bash
memanto memory sync
```

## 18. Migre de outro sistema

```bash
memanto migrate
```

O fluxo aceita importações de:

- Mem0;
- Letta;
- Supermemory;
- pacotes OKF.

## 19. Trabalhe com namespaces

Cada agente possui seu próprio namespace. Assim, um agente de operações de produção não precisa acessar memórias de experimentos temporários.

Fluxo recomendado:

```text
Memórias gerais da organização
├── agente-backend
├── agente-revisao
├── agente-operacoes
└── agente-experimentos
```

Defina quais informações cada agente precisa receber. O bootstrap entrega o contexto correspondente antes da ação:

```bash
memanto agent bootstrap
```

## 20. Exemplo com dois agentes

Na segunda-feira, o agente de backend registra uma decisão:

```bash
memanto remember \
  "A autenticação migrou para JWT; cookies de sessão foram descontinuados" \
  --type decision
```

Na sexta-feira, o agente de revisão recupera a informação:

```bash
memanto recall "como funciona a autenticação"
```

Mesmo sem participar da conversa de segunda-feira, o segundo agente recebe a decisão compartilhada.

## Referência dos comandos

| Capacidade | Comando |
|---|---|
| estado do sistema | `memanto status` |
| API e interface local | `memanto serve`, `memanto ui` |
| ciclo de agentes | `memanto agent ...` |
| criação de memória | `memanto remember` |
| edição e exclusão | `memanto edit`, `memanto forget` |
| importação de arquivos | `memanto upload` |
| recuperação | `memanto recall` |
| resposta fundamentada | `memanto answer` |
| resumo e conflitos | `memanto daily-summary`, `memanto conflicts` |
| sessões e rotinas | `memanto session ...`, `memanto schedule ...` |
| exportação e sincronização | `memanto memory export`, `memanto memory sync` |
| migração | `memanto migrate` |
| configuração | `memanto config show` |
| integração com agentes | `memanto connect ...` |

## Fluxo completo

```bash
pip install memanto
memanto
memanto connect codex
memanto status
memanto remember \
  "A autenticação migrou para JWT; cookies de sessão foram descontinuados" \
  --type decision
memanto recall "como funciona a autenticação"
memanto conflicts
memanto schedule enable
memanto ui
```

## Vídeo da publicação

[Assistir à demonstração do Memanto](https://video.twimg.com/amplify_video/2098366966222491648/vid/avc1/1278x1006/_zFX-Dev1EnoD8wk.mp4?tag=29)

## Fontes

- [Publicação original de Liam Braus no X](https://x.com/liambraus/status/2098367927883862279)
- [Repositório do Memanto](https://github.com/moorcheh-ai/memanto)
- [Documentação do Memanto](https://docs.memanto.ai)
