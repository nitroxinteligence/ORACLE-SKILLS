---
title: "GPT-6 Astra no Codex/ChatGPT: AGENTS.md, conclusão e verificação"
slug: gpt-6-astra-agents-md-no-codex-chatgpt
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/adiix_official/status/2097014889990545608
source_article: https://x.com/i/article/2097004537156366336
source_title: "How to Make GPT-6 Astra Actually Finish (AGENTS.md Setup Guide)"
source_published_at: "2026-09-07"
captured_at: 2026-09-10
official_sources:
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
  - https://learn.chatgpt.com/docs/config-file/config-reference
  - https://learn.chatgpt.com/docs/config-file/config-advanced
  - https://learn.chatgpt.com/docs/hooks
  - https://learn.chatgpt.com/docs/agent-approvals-security
  - https://learn.chatgpt.com/docs/agent-configuration/subagents
  - https://learn.chatgpt.com/docs/customization/memories
  - https://developers.openai.com/plugins/concepts/skills
---

# GPT-6 Astra no Codex/ChatGPT: AGENTS.md, conclusão e verificação

O artigo de `@adiix_official` parte de uma observação prática: um modelo que segue instruções com mais literalidade pode obedecer também a regras antigas que o fazem parar cedo. A adaptação útil para Codex/ChatGPT é simples: reduzir instruções vagas, definir o que significa terminar, deixar as permissões explícitas e conferir o resultado com evidência.

Fonte consultada: [post original no X](https://x.com/adiix_official/status/2097014889990545608) e [artigo associado](https://x.com/i/article/2097004537156366336), publicado em 7 de setembro de 2026. A disponibilidade de páginas do X pode depender de login; o conteúdo do artigo foi recuperado para leitura pelo endpoint público que expõe o artigo associado. A documentação de produto foi conferida nas páginas oficiais da OpenAI indicadas ao longo deste tutorial.

O artigo mistura documentação oficial, relatos de usuários, issues ainda recentes e opiniões do autor. As regras de processo abaixo são uma adaptação operacional. Quotas de planos, resultados de benchmarks, números de issues, classificadores de segurança e comportamentos observados por uma única conta devem ser tratados como sinais datados; confirme-os no cliente e na documentação atual antes de tomar uma decisão de custo ou segurança.

## A mudança de modelo mental

O risco que o artigo chama de **under-completion** é a tarefa terminar depois de um plano, de uma primeira edição ou de uma pergunta desnecessária. A correção não é remover toda regra. É trocar frases que descrevem humor por contratos que podem ser verificados:

| Problema | Regra vaga | Regra operacional |
|---|---|---|
| Escopo | “Leia tudo antes de editar” | “Leia os arquivos necessários para esta mudança e registre as fontes usadas.” |
| Testes | “Sempre rode todos os testes” | “Rode os checks afetados e amplie somente se falhar ou se o risco justificar.” |
| Aprovação | “Pergunte antes de qualquer coisa arriscada” | “Execute ações reversíveis autorizadas; pare antes de envio externo, pagamento, exclusão fora do workspace, mudança de permissão, deploy de produção ou merge.” |
| Conclusão | “Faça o melhor possível” | “Satisfaça a lista `DONE`; entregue diff, comandos e recibos.” |
| Skills | “Use em qualquer tarefa parecida” | “Ative quando o objetivo e o gatilho descritos na primeira frase coincidirem.” |

GPT-6 Astra é descrito oficialmente como mais capaz em fluxos longos e mais sensível a instruções em `AGENTS.md` e skills. A mesma documentação alerta que isso pode levá-lo a perguntar ou pausar quando você esperava uma suposição razoável. Ela também registra que Astra pode testar além do necessário em tarefas pequenas e delegar menos do que um fluxo precisa. Consulte o [guia oficial de comportamento e prompting do GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model) para a versão vigente dessas recomendações.

## O que é confirmado e o que vem do artigo

Use esta separação antes de copiar qualquer trecho para uma configuração:

| Evidência | Pode ser usada como base |
|---|---|
| Documentação oficial | Astra usa o id `gpt-6-astra` na API, aceita esforços `low`, `medium`, `high`, `xhigh` e `max`, possui janela de 1.050.000 tokens na página da API e é mais sensível a instruções de skills e `AGENTS.md`. |
| Documentação oficial do Codex | A cadeia de `AGENTS.md`, o limite `project_doc_max_bytes`, o catálogo de skills, hooks, políticas de aprovação, agentes personalizados e gerenciamento experimental de contexto têm contratos próprios. |
| Relato do artigo | Tabelas de mensagens por plano, porcentagens de benchmarks, pausas em issues específicas, valores mostrados por uma conta e comparações com outros modelos. Podem ter mudado ou não ser reproduzíveis. |
| Inferência operacional | Um contrato `DONE` mais curto e uma segunda verificação tendem a ser mais úteis que um roteiro enorme. Meça no seu projeto; não trate isso como garantia do modelo. |

O artigo não é uma configuração oficial da OpenAI e não concede acesso a Astra. Selecionar `gpt-6-astra` no arquivo local não cria autorização, quota ou disponibilidade em uma conta.

## 1. Confirme onde Astra está disponível

Na API, o modelo aparece como `gpt-6-astra`. A [página oficial do modelo](https://developers.openai.com/api/docs/models/gpt-6-astra) informa, no momento desta captura, janela de contexto de 1.050.000 tokens, máximo de 128.000 tokens de saída, esforços de raciocínio de `low` a `max` e preços por milhão de tokens. No Codex e no ChatGPT, o modelo disponível depende do cliente, do método de autenticação, do plano e das regras do workspace. A [documentação de disponibilidade por workspace](https://learn.chatgpt.com/docs/enterprise/workspace-model-availability) recomenda verificar cada interface separadamente.

No Codex, veja o modelo no seletor ou use `/model` em uma sessão interativa. Em uma execução única, o CLI aceita o modelo explícito:

```bash
codex --model gpt-6-astra
```

Para um padrão local, use uma camada de configuração revisável:

```toml
# ~/.codex/config.toml ou um perfil local
model = "gpt-6-astra"
model_reasoning_effort = "low"
```

Comece em `low` para uma tarefa conhecida e aumente quando a tarefa exigir mais planejamento ou verificação. O esforço é uma escolha por tarefa; não copie um valor de benchmark como se fosse um padrão universal. O modelo de um novo chat do Codex e o modelo de uma tarefa Cloud também podem ser determinados por regras do cliente ou do workspace.

Não conte com uma troca de modelo para obter uma segunda quota. O artigo relata pools compartilhados, mas as quotas são uma propriedade do produto e da conta, não do arquivo `AGENTS.md`. Confirme o medidor que aparece no cliente.

### API e Codex têm limites diferentes

Uma janela de 1,05 milhão na página da API não prova que uma sessão do Codex autenticada pelo ChatGPT exponha essa mesma capacidade. O status de contexto do cliente é a referência para aquela sessão. `model_context_window` informa ao Codex um valor de configuração; não aumenta a capacidade concedida pelo provedor.

O limite de compactação também é um gatilho, não uma expansão de contexto:

```toml
# Exemplo: escolha um valor abaixo do limite real da sua sessão.
# Confirme o indicador de contexto antes de adotar este número.
model_auto_compact_token_limit = 240000
```

Na API, a página do modelo informa que pedidos acima de 272.000 tokens de entrada são cobrados com multiplicadores para **o pedido inteiro**. Isso é uma regra de preço da API capturada em 10 de setembro de 2026; consulte a [página atual do modelo](https://developers.openai.com/api/docs/models/gpt-6-astra) antes de estimar custo. Em uma assinatura, use o indicador do cliente e faça compactações antes do esgotamento; não use a tarifa da API para inferir a quota do ChatGPT.

## 2. Descubra a cadeia de instruções que realmente carregou

O Codex monta a cadeia de instruções quando a sessão começa. A regra oficial é:

1. No diretório do Codex, `~/.codex/AGENTS.override.md` vence `~/.codex/AGENTS.md`.
2. Do root do projeto até o diretório atual, cada diretório pode contribuir com no máximo um arquivo: `AGENTS.override.md`, `AGENTS.md` ou um nome de fallback configurado.
3. Os arquivos são concatenados do root para baixo; o mais próximo do diretório atual aparece por último e tem precedência textual.
4. A leitura para quando atinge `project_doc_max_bytes`, que é 32 KiB por padrão.

Veja a [documentação oficial de `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md) antes de mudar a hierarquia. Um arquivo aninhado que não entrou na cadeia não pode ter causado a pausa que você está investigando.

Para registrar o diretório de log em uma sessão descartável:

```bash
codex -c log_dir=./.codex-log
```

Depois leia `./.codex-log/codex-tui.log` e procure os arquivos de instrução carregados. Faça essa inspeção antes de deletar uma regra:

```bash
rg -n -i \
  'AGENTS|project_doc|instruction|loaded|truncat|compact' \
  ./.codex-log/codex-tui.log
```

Faça a mesma busca nos arquivos que podem influenciar a sessão:

```bash
rg -n -i \
  'antes de cada|antes de qualquer|sempre|peça antes|arrisc|pare|stop|ask before|always' \
  ~/.codex/AGENTS*.md AGENTS*.md .codex skills 2>/dev/null
```

Leia o contexto de cada ocorrência. Uma regra que protege pagamentos ou dados de produção não é equivalente a uma regra que pede uma pausa antes de um `git diff`.

## 3. Troque as seis travas vagas por referências úteis

### “Leia todos os documentos antes de cada edição”

A documentação oficial usa justamente esse contraste: exigir o mapa inteiro do repositório para um typo consome contexto. Mantenha os ponteiros e defina quando cada um é necessário:

```text
RUIM
Antes de toda edição, leia architecture.md, database.md e deployment.md.

MELHOR
Use architecture.md para limites entre serviços, database.md para mudanças
de schema e deployment.md quando preparar um deploy. Leia apenas o que a
mudança atual exigir.
```

### “Sempre rode todos os testes”

O comportamento oficial de Astra já inclui verificação cuidadosa; em tarefas pequenas, isso pode gerar testes mais amplos que o necessário. Use um contrato proporcional:

```text
Não crie testes que apenas espelham uma mudança reversível e de baixo impacto.
Se escolher testar, use checks que comprovem o comportamento alterado.
Rode os testes apropriados e os checks obrigatórios. Depois que passarem,
amplie a cobertura somente por uma falha, uma mudança nova ou um risco claro.
```

Essa regra não elimina testes necessários. Ela evita que o modelo interprete “sempre” como uma ordem para reexecutar uma suíte inteira depois de cada linha.

### “Pergunte antes de qualquer coisa arriscada”

“Arriscado” não é uma classe verificável. Delimite ações e preserve a aprovação onde há efeito externo ou irreversível:

```text
Você pode executar tarefas reversíveis, ações somente de leitura, reviews,
correções e checks autorizados nesta sessão sem pedir novamente.

Pare antes de enviar algo a terceiros, pagar, apagar fora do workspace,
mudar permissões, publicar em produção, fazer merge ou alterar uma conta.
Prepare o diff e o recibo para minha aprovação final.
```

Esse texto descreve um limite de operação; ele não substitui o sandbox, a política de aprovação, as permissões do sistema ou os controles do provedor.

### “Implemente e pare para eu revisar”

Se a revisão é o último passo, diga isso. Para uma mudança já autorizada, peça que o agente implemente, execute, inspecione e corrija antes de retornar:

```text
Implemente a mudança, execute os checks apropriados, inspecione o resultado,
corrija falhas causadas por ela e entregue um diff revisável com os comandos
e os resultados. A aprovação humana é o último passo antes de publicar,
enviar, fazer merge ou executar outra ação irreversível.
```

Se você quer revisar um desenho antes do código, declare a parada de propósito e diga qual mensagem retoma a implementação. Não deixe as duas intenções em arquivos diferentes.

### Descrições de skills que tentam ser escolhidas sempre

O catálogo disponível de skills recebe um orçamento que, por padrão, equivale a cerca de 2% da janela de contexto; o limite explícito pode chegar a 10.000 tokens. Quando há muitas skills, as descrições são encurtadas e algumas podem nem aparecer no catálogo inicial. A [documentação oficial de skills](https://developers.openai.com/plugins/concepts/skills) recomenda colocar o objetivo e os gatilhos no começo da descrição e manter os detalhes no corpo da skill.

```yaml
# amplitude excessiva
description: Ajuda com bancos, queries, modelos, persistência e qualquer tarefa de backend.

# gatilho verificável
description: Cria ou valida migrações Postgres ao adicionar, alterar ou revisar uma migração.
```

Para uma skill que deve existir, mas só ser usada quando chamada pelo nome, o arquivo `agents/openai.yaml` pode desativar a invocação implícita:

```yaml
policy:
  allow_implicit_invocation: false
```

Ela continua disponível por `$nome-da-skill`. Não use esta chave sem confirmar que a skill e o cliente realmente a suportam.

### Skills que são receitas enormes

Uma skill deve orientar decisões e apontar referências; scripts devem conter passos determinísticos. Uma estrutura pequena costuma ser suficiente:

```text
minha-skill/
├── SKILL.md             # nome, gatilho e roteador do workflow
├── references/          # abrir somente quando o caso exigir
├── scripts/             # verificações determinísticas
├── assets/              # arquivos que entram no resultado
└── agents/openai.yaml   # apresentação e política da skill
```

Separe instruções específicas de um modelo sob um título que indique o modelo. Não remova uma restrição de segurança ou de compliance apenas porque Astra consegue inferir o caminho; remova apenas redundância, ambiguidades e etapas que não mudam uma decisão.

## 4. Defina `DONE` antes da primeira mensagem

Um contrato de conclusão é um predicado, não uma persona. Cada linha precisa poder ser conferida por um comando, uma requisição, um diff ou uma leitura objetiva.

```text
DONE SIGNIFICA
- a suíte afetada termina com código 0 em um checkout limpo desta branch;
- o endpoint novo responde às três requisições em docs/contract.http;
- CHANGELOG.md registra a mudança;
- somente src/ e tests/ foram alterados.

AINDA NÃO ESTÁ PRONTO
- existe apenas um plano;
- a primeira implementação não foi executada;
- o resumo diz “deve funcionar” sem comando ou recibo.

ROTA
Escolha os arquivos e as ferramentas a partir do que a tarefa exigir. Não
me pergunte quais arquivos ler quando o repositório permitir descobrir isso.

PARE PARA MIM SOMENTE SE
- uma linha de DONE exigir uma ação irreversível;
- duas linhas de DONE forem incompatíveis;
- faltar uma autorização que não possa ser inferida da sessão.
```

Para documentação ou conteúdo, troque os predicados por critérios do artefato:

```text
DONE SIGNIFICA
- o Markdown tem frontmatter YAML válido;
- todos os links oficiais respondem;
- os exemplos de código são sintaticamente válidos;
- a fonte, a data de captura e as limitações estão registradas;
- nenhuma afirmação comunitária é apresentada como documentação oficial.
```

O contrato deve caber no prompt da tarefa ou no `AGENTS.md` mais próximo. Não coloque um checklist de cada projeto no `~/.codex/AGENTS.md`: isso aumenta a cadeia global e pode impedir instruções locais de carregar.

## 5. Mantenha um ledger de autorização

No início de uma tarefa longa, escreva o que já está autorizado e o que continua bloqueado. Isso evita que uma compactação ou uma mudança de subagente transforme uma autorização anterior em uma pergunta repetida:

```text
AUTORIZADO NESTA TAREFA
- ler arquivos do repositório;
- executar a suíte local com fixtures descartáveis e sem acesso à produção;
- instalar dependências de desenvolvimento declaradas no projeto;
- criar ou trocar de branch e abrir um draft local;
- corrigir falhas causadas pela mudança e repetir os checks afetados.

AINDA NÃO AUTORIZADO
- fazer push para main ou para um remoto;
- enviar e-mail, Slack, webhook ou mensagem a terceiros;
- pagar, publicar, fazer merge ou excluir dados fora do workspace;
- mudar permissões, credenciais ou configuração de produção.
```

Use classes concretas. “Qualquer coisa perigosa” não informa se `pytest` é seguro; “fixtures descartáveis, sem acesso à produção” informa. A autorização do ledger ainda está sujeita ao sandbox e às políticas do cliente.

Inclua também duas linhas de precedência no `AGENTS.md` ou no prompt quando skills de fontes diferentes entrarem na mesma sessão:

```text
As instruções explícitas do usuário têm precedência sobre orientações de uma
skill. Se uma skill pedir uma pausa ou divergir do objetivo do usuário,
identifique o SKILL.md, a instrução conflitante e o efeito que ela causou.
```

Essa segunda linha transforma uma pausa sem explicação em um diagnóstico com arquivo e trecho, sem mandar o modelo ignorar uma restrição legítima.

## 6. Use um Stop hook como verificador, com limite de uma continuação

Hooks são scripts ou ferramentas que executam em eventos do ciclo do Codex. O evento `Stop` roda quando o modelo considera que terminou. Se um hook síncrono devolve `decision: "block"`, o Codex não desfaz a ação concluída: cria uma nova mensagem de continuação usando o motivo do hook. O campo `stop_hook_active` informa se aquela rodada já foi continuada.

A [documentação oficial de hooks](https://learn.chatgpt.com/docs/hooks) exige JSON em `stdout` para `Stop`; texto livre é inválido. Hooks não gerenciados também precisam ser revisados e confiados pelo usuário. Use `/hooks` no CLI e confira o hash sempre que a definição mudar.

### Configuração mínima

Prefira resolver o hook pelo root Git para que uma sessão iniciada em um subdiretório encontre o mesmo script:

```toml
# ~/.codex/config.toml ou .codex/config.toml de um projeto confiável
[[hooks.Stop]]

[[hooks.Stop.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/contract.py"'
timeout = 120
statusMessage = "Verificando contrato de conclusão"
```

A forma JSON em `.codex/hooks.json` também é válida. Não defina os dois formatos na mesma camada sem motivo: a documentação informa que eles são mesclados e um aviso aparece no início.

### Checker seguro para começar

O script abaixo é um esqueleto. Troque `CHECKS` pelos predicados do seu projeto, mantenha os comandos sem rede e não inclua ações destrutivas. Ele usa o diretório da sessão recebido pelo hook e continua no máximo uma vez:

```python
#!/usr/bin/env python3
# .codex/hooks/contract.py
import json
import subprocess
import sys

event = json.load(sys.stdin)

# Nunca crie um loop de continuação.
if event.get("stop_hook_active"):
    raise SystemExit(0)

CHECKS = [
    ("testes afetados", ["npm", "test", "--silent"]),
    ("contrato HTTP", ["bash", "docs/contract_check.sh"]),
]

cwd = event.get("cwd") or "."
failed = []
for name, command in CHECKS:
    result = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )
    if result.returncode:
        output = (result.stdout + result.stderr).strip().splitlines()
        tail = output[-5:] or [f"código de saída: {result.returncode}"]
        failed.append(f"- {name} (exit {result.returncode})\n  " + "\n  ".join(tail))

if not failed:
    raise SystemExit(0)

print(json.dumps({
    "decision": "block",
    "reason": "O contrato DONE ainda falha. Corrija e conclua:\n"
              + "\n".join(failed),
}))
```

Teste-o em um repositório descartável com uma linha `DONE` que falhe de propósito. Confirme que a continuação aparece, que o segundo disparo sai sem novo bloco e que o hook não escreve logs em `stdout`. Um hook que nunca foi executado não é evidência de que o contrato está protegido.

### Limites do Stop hook

- Ele verifica o resultado; não concede autorização para editar ou publicar.
- `decision: "block"` não reverte o comando que já terminou.
- O hook só deve chamar checks previsíveis e curtos; não faça uma migração de produção a partir dele.
- Hooks de projeto carregam apenas quando o projeto está confiável. Hooks de usuário e do sistema têm camadas próprias.
- Um hook pode falhar, expirar ou estar desabilitado. Registre a saída e faça uma verificação manual quando o recibo for importante.

## 7. Mova aprovações de adjetivos para classes de ação

Na configuração atual, `approval_policy = "untrusted"` não é mais aceito e `on-failure` está depreciado. A referência oficial usa `on-request`, `never` ou uma tabela granular. Para operação interativa com uma fronteira clara:

```toml
approval_policy = "on-request"
approvals_reviewer = "user"
sandbox_mode = "workspace-write"
```

`never` pode ser apropriado em uma automação fechada e previamente testada, mas remove a parada interativa. `danger-full-access` amplia a superfície de arquivos e rede; não o use como forma de “fazer Astra terminar”. O [guia oficial de aprovações e segurança](https://learn.chatgpt.com/docs/agent-approvals-security) explica a relação entre sandbox, aprovação e rede.

Quando o objetivo é manter algumas categorias interativas e rejeitar outras automaticamente, use a forma granular somente depois de revisar cada campo:

```toml
approval_policy = { granular = { sandbox_approval = true, rules = true, mcp_elicitations = true, request_permissions = true, skill_approval = false } }
```

### PermissionRequest para um caso seguro

Um hook `PermissionRequest` roda quando Codex está prestes a pedir aprovação. Ele pode permitir, negar ou não decidir. Se vários hooks decidirem, qualquer `deny` vence; um `allow` evita o prompt quando não há deny. O script abaixo permite apenas o executor de testes e deixa todo o resto seguir o fluxo normal:

```toml
[[hooks.PermissionRequest]]
matcher = "^Bash$"

[[hooks.PermissionRequest.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/allow_tests.py"'
timeout = 10
```

```python
#!/usr/bin/env python3
# .codex/hooks/allow_tests.py
import json
import re
import sys

event = json.load(sys.stdin)
command = str((event.get("tool_input") or {}).get("command", ""))

if re.match(r"^(npm|pnpm|yarn) (test|run test)\b", command):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {"behavior": "allow"},
        }
    }))

# Sem decisão: a aprovação normal continua para outras classes.
raise SystemExit(0)
```

Faça o regex tão estreito quanto a sua suíte permite. Não autoaprove `Bash` inteiro, não devolva `allow` para comandos concatenados e não coloque segredos no hook. `PermissionRequest` não aceita `updatedInput` nem `updatedPermissions` na forma documentada atual.

O [Auto-review oficial](https://learn.chatgpt.com/docs/sandboxing/auto-review) é outra opção: troca o revisor humano por um agente revisor para pedidos elegíveis, mas não aumenta o sandbox nem concede uma permissão nova. Continue usando `on-request` ou uma política granular e leia a política do revisor antes de adotá-lo.

## 8. Dê ao resultado uma segunda leitura

O agente que implementou uma mudança pode produzir um resumo correto, mas o resumo é uma afirmação do próprio executor. Para tarefas com contrato importante, crie um agente de revisão somente leitura. A [documentação oficial de subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents) coloca agentes personalizados em `~/.codex/agents/` ou `.codex/agents/` e exige `name`, `description` e `developer_instructions`.

Exemplo de `.codex/agents/verifier.toml`:

```toml
name = "verifier"
description = "Confere um DONE list depois da implementação, antes do relatório final."
developer_instructions = """
Você é somente leitura. Trate o resumo do agente executor como uma afirmação
não verificada. Execute cada predicado DONE por conta própria. Para cada linha,
retorne PASS ou FAIL, o comando executado e o código de saída. Não corrija
arquivos, não instale dependências e não publique nada.
"""
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
```

Peça a revisão explicitamente no prompt do Codex ou no fluxo que gerencia os agentes. O modelo guia informa que Astra pode delegar menos do que uma aplicação precisa; se a segunda leitura for obrigatória, transforme-a em uma etapa do contrato ou peça a delegação diretamente.

Para defaults de subagentes, a configuração oficial aceita:

```toml
[agents]
default_subagent_model = "gpt-5.6-terra"
default_subagent_reasoning_effort = "medium"
max_concurrent_threads_per_session = 4
```

Escolha `terra` ou `luna` para leitura, extração e checks repetíveis; reserve Astra para decisões que realmente exigem o modelo mais capaz. Modelos e esforços disponíveis dependem do cliente e podem mudar.

## 9. Faça o contexto sobreviver sem virar autoridade

O gerenciamento experimental de contexto do Codex usa notas e histórico pesquisável em vez de apenas compactar tudo em um resumo. A [referência oficial de configuração](https://learn.chatgpt.com/docs/config-file/config-reference) documenta a opção:

```toml
[features.context_management]
experimental_mode = true
```

A disponibilidade publicada atualmente é para clientes Codex compatíveis com login ChatGPT Plus ou Pro; a documentação de modelos informa que o recurso não está disponível, no lançamento descrito, para Business, Enterprise ou autenticação por chave de API. Confirme a elegibilidade da conta e o cliente antes de depender dele.

Depois de ativar, verifique um recibo real: abra a nota ou histórico que deveria ter sido escrito e confirme que a próxima continuação o encontra. Um indicador de “contexto experimental ligado” não prova que o backend salvou a informação.

Regras que precisam valer sempre devem permanecer em `AGENTS.md`, documentação versionada ou no contrato da tarefa. A [documentação de memórias](https://learn.chatgpt.com/docs/customization/memories) separa a memória web do ChatGPT do armazenamento local do Codex e recomenda tratar memórias como uma camada de recuperação, não como a única autoridade. Use `/memories` para ver o estado da conversa quando o cliente oferecer esse comando.

Não salve tokens, cookies, chaves ou dados de produção em `AGENTS.md`, notas, skills ou hooks. O cliente pode redigir alguns campos, mas o operador continua responsável por revisar os arquivos antes de compartilhá-los.

## 10. Controle custo por contexto e número de passos

A página atual de Astra informa, para a API, entrada a US$ 10 por milhão, entrada em cache a US$ 1, gravação de cache a US$ 12,50 e saída a US$ 50; pedidos acima de 272K de entrada recebem os multiplicadores descritos na página. Esses números são uma fotografia de 10 de setembro de 2026, não uma tabela de assinatura.

Na prática, o custo e a latência costumam crescer quando um workflow repete a mesma cadeia de ferramentas, reabre arquivos grandes ou chama um revisor redundante. Meça antes de otimizar:

```text
para cada execução, registre
- modelo e esforço;
- número de mensagens e chamadas de ferramenta;
- tokens de entrada, cache e saída quando o cliente expuser esses dados;
- compactações e continuations;
- checks executados e resultado;
- tempo até DONE e motivo de cada pausa.
```

Use `low` ou `medium` para uma tarefa clara, um contexto curto e um check objetivo. Suba para `high`, `xhigh` ou `max` quando a decisão, o código ou a análise justificarem mais raciocínio. A [documentação de modelos do Codex](https://learn.chatgpt.com/docs/models) descreve essa escolha por tarefa.

No fluxo multiagente, deixe o agente principal definir o contrato e faça um subagente barato executar uma leitura delimitada. Isso reduz o custo de cada etapa, mas pode aumentar o número total de tokens; compare o custo total e a qualidade do recibo.

## 11. Diferencie uma pausa de instrução, permissão, segurança e cliente

Nem toda pausa é causada por `AGENTS.md`. Antes de editar uma regra, identifique a evidência:

| Sinal observado | Hipótese mais provável | Próximo passo |
|---|---|---|
| O modelo cita uma linha de skill ou `AGENTS.md` e para | conflito, ordem ou cap de instruções | ler a cadeia e simplificar a regra que realmente carregou |
| O cliente mostra um pedido de sandbox, rede ou permissão | fronteira de execução | decidir a classe no cliente ou em um hook confiável |
| O evento `Stop` retorna `decision: block` | contrato incompleto | ler a razão do hook e corrigir o predicado ou a implementação |
| O aviso cita monitoramento de segurança ou comportamento potencialmente inseguro | monitor assíncrono do provedor | não tente contornar com prompt; leia o aviso e siga o fluxo oferecido |
| O mesmo reconhecimento não persiste ou a UI entra em loop | possível defeito do cliente | registrar versão, mensagem e reprodução; testar uma nova tarefa se for permitido |
| O contexto desaparece depois de compactar | limite ou backend de contexto | conferir o indicador e as notas; reduzir o escopo antes de continuar |

A OpenAI documenta monitoramento assíncrono de desalinhamento para Astra. Uma pausa desse monitor não é uma regra que possa ser neutralizada por `AGENTS.md`. O artigo relaciona falsos positivos e códigos de issues a uma janela de poucos dias; mantenha esses relatos como observações e nunca como instruções para escapar de controles de segurança.

Em um CLI, um bloqueio de segurança ou aprovação pode terminar a tarefa sem oferecer a mesma retomada disponível no Desktop. Em uma automação agendada, a ação final pode exigir confirmação no momento da execução. Teste a etapa irreversível em um ambiente descartável antes de agendar ou publicar.

## 12. Teste de aceitação do setup

O teste abaixo adapta os sete predicados do artigo para um ambiente Codex atual. Cada linha deve produzir um recibo. “Parece funcionar” não é PASS.

```text
T1  `codex -c log_dir=./.codex-log` registra a cadeia de AGENTS.md que você
    esperava, e os arquivos cabem em `project_doc_max_bytes`.

T2  A busca em AGENTS.md e skills encontra “antes de cada”, “sempre”,
    “peça antes”, “arriscado” e “pare”. Cada ocorrência tem uma classe de
    ação clara ou foi removida após revisar o motivo.

T3  O catálogo de skills cabe no orçamento publicado (por padrão cerca de
    2% da janela). A sessão não mostra aviso de truncamento ou skill omitida.

T4  Toda tarefa sem supervisão possui um DONE list com predicados que um
    comando, uma requisição, um diff ou uma leitura pode avaliar.

T5  Existe um Stop hook síncrono, sua definição foi revisada em `/hooks` e o
    checker usa `stop_hook_active` para continuar no máximo uma vez.

T6  Quando ocorre uma pausa de instrução, Astra consegue apontar o arquivo e
    o trecho que a causou; você não está editando um arquivo que nem carregou.

T7  Você consegue separar uma pausa de segurança ou de permissão de uma pausa
    de instrução porque registrou a mensagem, a versão do cliente e o evento.
```

Comandos auxiliares para T2 e T3:

```bash
rg -n -i \
  'antes de cada|sempre|peça antes|arrisc|pare|ask before|always|risky|stop' \
  ~/.codex/AGENTS*.md AGENTS*.md .codex skills 2>/dev/null

find ~/.codex/skills ./.codex/skills -name SKILL.md -print 2>/dev/null | sort
```

O aviso de catálogo é observacional e depende do cliente. Se a sua versão não o exibir, registre o tamanho das descrições e mantenha o gatilho na primeira frase; não invente um PASS a partir da ausência de uma mensagem.

## 13. Setup mínimo que vale a pena manter

Comece com cinco mudanças pequenas e mensuráveis:

1. Selecione Astra e um esforço adequado no cliente; registre o modelo e o contexto observado.
2. Inspecione a cadeia de `AGENTS.md` e skills; troque regras universais por ponteiros e classes de ação.
3. Coloque um `DONE` list e um ledger de autorização no prompt ou no `AGENTS.md` mais próximo.
4. Adicione um verifier read-only ou um Stop hook somente quando um contrato real justificar a manutenção; teste e confie no hook antes de usá-lo.
5. Entregue diff, checks, mensagens de erro, versão do cliente e recibos de saída.

Um prompt inicial portátil para Codex, ChatGPT Work ou ChatGPT web:

```text
Execute esta tarefa até satisfazer o contrato abaixo. Faça suposições rotineiras
e registre-as; pergunte somente quando a resposta mudar o resultado ou quando
uma ação irreversível não estiver autorizada.

DONE
- [predicado verificável 1]
- [predicado verificável 2]
- [recibo que precisa existir]

AUTORIZADO
- ler o material necessário;
- executar checks locais descartáveis;
- fazer mudanças reversíveis no escopo definido.

PARE ANTES DE
- enviar a terceiros, pagar, publicar, fazer merge, mudar permissões ou apagar
  fora do workspace.

ENTREGA
- arquivos alterados;
- comandos executados e códigos de saída;
- falhas corrigidas e limitações restantes;
- recibo ou evidência de cada linha DONE.
```

## 14. Como adaptar entre Codex, ChatGPT e API

### Codex Desktop, CLI e extensão IDE

Use o modelo do cliente, `AGENTS.md`, `.codex/config.toml`, skills e hooks locais. O projeto precisa estar confiável para que configuração e hooks locais sejam carregados. A [referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference) é a fonte para nomes de chaves; não copie tabelas antigas do artigo, especialmente `untrusted`.

No Desktop, a disponibilidade do modelo aparece no seletor. No CLI, `/model`, `--model` e `/hooks` permitem conferir modelo, esforço e confiança nos hooks. A extensão IDE usa o host Codex conectado; confirme qual host e qual `CODEX_HOME` estão ativos.

### ChatGPT e ChatGPT Work

ChatGPT web e Work não carregam o `AGENTS.md` local do seu Mac como um Codex local. Use instruções do projeto, um prompt de tarefa com `DONE` e arquivos de referência anexados ou disponíveis no workspace. A disponibilidade do modelo, a memória, as aprovações e as automações seguem políticas da conta e do workspace.

O contrato continua portátil: resultado esperado, autorização, limites e recibos cabem em uma mensagem. O Stop hook e o verifier TOML são mecanismos do runtime Codex; em Work, reproduza o verifier como uma etapa explícita do fluxo ou de um agente de revisão hospedado.

### API OpenAI

Na API, use o id documentado e passe o esforço no objeto de raciocínio. Para tool calling, o guia do modelo recomenda a Responses API; confira parâmetros incompatíveis antes de migrar um cliente antigo:

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-6-astra",
    reasoning={"effort": "low"},
    input="Execute a tarefa e retorne os predicados DONE com evidência.",
)
print(response.output_text)
```

O guia oficial informa que `temperature`, `top_p` e `top_logprobs` não devem ser enviados para Astra; Chat Completions continua disponível, mas tool calling exige Responses. Um Stop hook do Codex não existe automaticamente na API. Implemente o mesmo contrato no seu orquestrador: leia a saída, rode os checks fora do modelo e faça uma nova chamada apenas quando a política permitir.

Não use uma chave de API em um exemplo de `AGENTS.md`, não misture a quota da API com créditos do ChatGPT e não declare uma execução “concluída” somente porque a API retornou HTTP 200.

## 15. Manutenção e observabilidade

Faça uma revisão curta a cada mudança de modelo, cliente ou plugin:

- confirme o modelo e o esforço efetivos;
- examine a cadeia de instruções e o log de contexto;
- reduza descrições de skills e marque invocação explícita onde fizer sentido;
- valide que hooks continuam confiáveis e que o hash corresponde ao arquivo revisado;
- execute o acceptance test em um repositório descartável;
- registre pausas por categoria: instrução, permissão, segurança, contexto ou defeito do cliente;
- compare taxa de conclusão, mensagens repetidas, continuations, custo e tempo;
- mantenha contratos, evidências e decisões versionados junto do projeto.

Não remova controles porque um relato de quatro dias sugere que “Astra já sabe”. Preserve limites necessários de produção e segurança, e retire apenas uma etapa redundante depois de observar o fluxo real. Um setup mais curto é uma hipótese de engenharia; o recibo é o que decide se ele está funcionando.

### Links canônicos

- [Artigo original no X](https://x.com/adiix_official/status/2097014889990545608)
- [Artigo associado no X](https://x.com/i/article/2097004537156366336)
- [Guia oficial de GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model)
- [Página do modelo GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [Instruções com AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Configuração avançada](https://learn.chatgpt.com/docs/config-file/config-advanced)
- [Hooks](https://learn.chatgpt.com/docs/hooks)
- [Aprovações e segurança](https://learn.chatgpt.com/docs/agent-approvals-security)
- [Subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Memórias](https://learn.chatgpt.com/docs/customization/memories)
- [Skills](https://developers.openai.com/plugins/concepts/skills)
- [Modelos do Codex](https://learn.chatgpt.com/docs/models)
