---
title: "Hypit no Codex: transforme vídeos de referência em workflows editáveis"
slug: hypit-clonar-videos-com-workflows-no-codex
language: pt-BR
type: tutorial
category: criacao-de-videos
subcategory: edicao-com-ia
source: https://x.com/li9292/status/2099687200975720699
source_author: "@li9292"
source_published_at: "2026-09-15T02:30:13Z"
source_repository: https://github.com/hypit-ai/hypit
source_commit: 45bc85e73e628e56afc05865ced0cd84d13fcea2
captured_at: 2026-09-16
capture_method: agent-reach/opencli-twitter+github-cli
license: "Hypit Open Source License — Apache 2.0 modificada com condições"
media_storage: remote_links
tags:
  - hypit
  - codex
  - video-com-ia
  - workflow
  - edicao-de-video
  - conteudo-viral
  - automacao
  - skill
---

# Hypit no Codex: transforme vídeos de referência em workflows editáveis

O [Hypit](https://github.com/hypit-ai/hypit) fornece ao Codex e a outros agentes
uma linguagem e um sistema para criar vídeos. Você pode entregar um vídeo de
referência ou apenas um briefing. O agente descreve o trabalho em arquivos de
texto, prepara os materiais, monta a composição e gera um projeto que pode ser
revisado e executado novamente.

O ponto central do post original é a diferença entre **template fixo** e
**workflow editável**:

```text
vídeo de referência
→ análise da estrutura e do tempo
→ workflow com partes preservadas e partes substituíveis
→ troca de apresentador, texto, produto, B-roll ou idioma
→ nova composição
→ revisão
→ render final
```

![Prévia do Hypit](https://github.com/user-attachments/assets/981c28e8-ddab-4164-85bc-03b5d71275dc)

## O que significa “clonar” um vídeo

Neste contexto, clonar não significa copiar apenas o roteiro ou aplicar um
filtro. O objetivo é reconstruir relações como:

- quando cada cena começa e termina;
- qual frase aciona uma imagem, corte ou efeito;
- posição e comportamento das legendas;
- alternância entre A-roll e B-roll;
- composição de telas divididas, cards e sobreposições;
- ritmo de fala, música e efeitos sonoros;
- elementos que podem ser trocados sem destruir a estrutura.

O resultado é uma composição programável. O código-fonte do vídeo pode entrar
no Git, receber diff e gerar variações com mudanças controladas.

Isso não garante que um vídeo se tornará viral. Tema, timing cultural,
distribuição, autenticidade e qualidade criativa continuam fora do alcance de
uma simples reprodução estrutural.

## Como o Hypit organiza o trabalho

| Arquivo ou componente | Função |
|---|---|
| `.svml` | descreve roteiro, materiais, componentes e composição |
| `.svs` | guarda receitas reutilizáveis de estilo e comportamento |
| `.svrun` | escolhe a fonte, os outputs e o alvo de uma execução |
| `hypit.runtime.json` | seleciona serviços, providers, credenciais e capacidade |
| `.hypit/results/` | preserva resultados e recibos de cada build |
| Hypit Studio | mostra composição, timeline e controles editáveis |
| `FEEDBACK.json` | registra comentários com timestamps |

Os eventos podem ficar ligados às palavras e ao significado do roteiro, em vez
de depender apenas de segundos absolutos. Assim, quando uma frase muda, os
elementos relacionados podem acompanhar o novo timing.

## 1. Pré-requisitos

O repositório consultado exige:

- Node.js `22.15.0` ou mais recente;
- um ambiente de agente com acesso aos arquivos e ao terminal, como Codex ou
  Claude Code;
- espaço para o projeto, mídias e resultados;
- navegador para o Studio;
- contas e créditos dos serviços de geração escolhidos, quando houver.

O Hypit pode compor legendas, motion graphics e visuais produzidos por código
sem usar um modelo gerador. Imagens, vídeo, voz e transcrição hospedada podem
ter cobranças próprias.

## 2. Instale a skill

No terminal:

```bash
npx skills add hypit-ai/hypit -g
```

Esse comando instala a **skill** de produção. Ele não prova que o executável,
os providers, as credenciais e o projeto já estejam prontos.

Existem três ciclos separados:

```text
skill do agente
≠ executável @hypit/hypit
≠ projeto de vídeo e seus resultados
```

Na primeira utilização, a skill orienta o agente a localizar ou preparar o
executável `hypit`. Deixe o Codex relatar onde cada parte foi instalada antes
de gerar conteúdo.

## 3. Crie uma pasta para o vídeo

```bash
mkdir -p ~/Videos/meu-projeto-hypit
cd ~/Videos/meu-projeto-hypit
```

Abra essa pasta no Codex. Mantenha o vídeo de referência e os materiais que
você possui autorização para usar dentro do projeto ou em uma pasta concedida
explicitamente ao processo.

Estrutura prática:

```text
meu-projeto-hypit/
├── referencias/
│   └── video-original.mp4
├── materiais/
│   ├── logo.png
│   ├── produto.png
│   └── b-roll/
├── projeto/
├── output/
└── .gitignore
```

Não envie chaves, credenciais, resultados privados ou mídias licenciadas para
um repositório público.

## 4. Faça o primeiro pedido ao Codex

Para adaptar um vídeo local:

```text
/hypit Clone este vídeo: /caminho/para/video-original.mp4

Objetivo da nova versão:
[DESCREVA O RESULTADO]

Preserve:
- [ESTRUTURA NARRATIVA]
- [RITMO OU RELAÇÃO ENTRE CENAS]
- [ELEMENTOS QUE NÃO DEVEM MUDAR]

Substitua:
- apresentador: [NOVO APRESENTADOR OU MATERIAL]
- tema: [NOVO TEMA]
- produto: [NOVO PRODUTO]
- texto e CTA: [NOVO TEXTO]
- formato: [9:16, 16:9, 1:1 ETC.]

Antes de gerar material pago, entregue:
1. análise do vídeo de referência;
2. lista do que será preservado e substituído;
3. plano do workflow;
4. serviços necessários;
5. estimativa de custo e pontos ainda desconhecidos.
```

Também é possível começar sem referência:

```text
/hypit Crie do zero um vídeo de ranking vertical com 20 segundos.

Tema: [TEMA]
Público: [PÚBLICO]
Gancho: [GANCHO]
Itens: [LISTA]
Conclusão: [PAYOFF]
CTA: [AÇÃO]

Crie primeiro o briefing e o tratamento. Não execute chamadas pagas antes da
minha aprovação do plano e do orçamento.
```

## 5. Separe análise, briefing e tratamento

Antes de produzir mídias, peça que o agente registre:

- **Análise:** por que o vídeo funciona e quais relações foram observadas;
- **Timeline:** acontecimentos localizáveis por fala, cena ou frame;
- **Briefing:** seu objetivo, público, fatos privados e limites;
- **Tratamento:** a resposta criativa proposta para a nova versão;
- **Progresso:** o que já existe, o que falta e o próximo passo.

Revise especialmente:

- abertura e promessa;
- progressão narrativa;
- posição das viradas e do payoff;
- cortes ligados à fala;
- desenho de legendas;
- relação entre apresentador, produto e B-roll;
- elementos que perderiam sentido ao trocar apenas um slot.

Uma substituição de produto pode exigir mudanças de roteiro, cenário,
performance e conclusão. Tratar tudo como troca mecânica costuma produzir um
resultado genérico.

## 6. Configure o runtime

Depois que o executável estiver disponível, inicialize ou selecione o perfil do
projeto:

```bash
hypit runtime init
hypit paths
```

`runtime init` cria e seleciona um `hypit.runtime.json` inicial quando ainda não
existe. Para um perfil já preparado:

```bash
hypit runtime use hypit.runtime.json
```

Essa etapa não autentica contas, não instala tudo automaticamente e não inicia
uma geração paga.

## 7. Escolha os serviços e credenciais

O Hypit recomenda o HypiHub como serviço integrado, mas permite BYOK e
providers próprios. Uma única produção pode usar serviços diferentes para
imagem, vídeo, voz e transcrição.

Confira o estado sem revelar as chaves:

```bash
hypit auth status
```

Depois de escolher conscientemente um serviço, conecte somente o endpoint
necessário. Exemplo documentado para HypiHub:

```bash
hypit auth login hypihub.default
```

Uma chave dá acesso à conta daquele fornecedor; ela não cria automaticamente
um provider compatível. Mantenha segredos fora de `.svml`, `.svs`, `.svrun`,
do perfil versionado e das mensagens do agente.

## 8. Valide antes de gastar

Confira a fonte:

```bash
hypit check reference.svml
```

Inspecione o plano:

```bash
hypit plan reference.svrun
```

O plano mostra alvos, chamadas externas necessárias, parâmetros conhecidos e
problemas de preparação. Ele não inicia a geração.

Consulte os preços declarados pelos providers:

```bash
hypit pricing reference.svrun
hypit pricing reference.svrun --json
```

Essa consulta não é uma garantia do custo final. Duração ainda desconhecida,
preços ausentes e serviços sem informação continuam como incertezas.

Faça também o diagnóstico:

```bash
hypit doctor
```

O diagnóstico verifica o runtime selecionado, endpoints, presença de
credenciais e o repositório de resultados. Ele não envia um pedido de geração.

Checklist antes do build:

- [ ] conta que será cobrada identificada;
- [ ] escopo da geração aprovado;
- [ ] limite de gasto definido;
- [ ] serviços locais ou remotos escolhidos;
- [ ] plano sem dependências inesperadas;
- [ ] materiais com direito de uso;
- [ ] credenciais fora dos arquivos versionados.

## 9. Gere o primeiro build

Somente depois da aprovação de escopo e custo:

```bash
hypit build reference.svrun --title first-cut --follow
```

`--follow` acompanha a execução no terminal. Interromper o acompanhamento não
significa necessariamente cancelar o build; o worker pode continuar.

Cada build recebe um identificador e preserva resultados em `.hypit/results/`.
Uma falha pode deixar outputs aproveitáveis. Não repita chamadas caras antes de
inspecionar o que já foi produzido.

## 10. Abra a composição no Studio

```bash
hypit studio --run reference.svrun
```

Abra o endereço exibido pelo comando. No Studio você pode:

- reproduzir a composição;
- navegar frame a frame;
- examinar a timeline;
- selecionar palavras e elementos gráficos;
- alterar propriedades expostas pelos componentes;
- conferir se os arquivos-fonte foram salvos.

A visualização não equivale ao vídeo final codificado. Ela serve para revisar
composição, hierarquia, timing e transições antes do export.

Na página terminada em `#comments`, registre feedback com timestamp. Os
comentários ficam em `FEEDBACK.json`.

## 11. Revise com precisão

Use uma lista como esta:

```text
Revise o projeto Hypit usando estes comentários:

1. 00:00–00:02 — o gancho entra tarde; antecipe a frase e preserve a música.
2. Na palavra “[PALAVRA]” — troque o B-roll pela imagem do produto real.
3. 00:08–00:11 — a legenda cobre o rosto; mova-a para a área inferior segura.
4. No payoff — mantenha o corte e substitua apenas o texto e o produto.

Reutilize os outputs já aprovados. Mostre o novo plano antes de qualquer chamada
paga adicional.
```

No Hypit, composição e mídia gerada são decisões separáveis. Alterar uma
posição ou animação não deveria obrigar a gerar novamente um apresentador já
aprovado.

## 12. Reutilize resultados aprovados

O Hypit não assume cache implícito. A reutilização deve ser registrada no novo
`.svrun` com referências explícitas aos outputs anteriores.

Para localizar resultados:

```bash
hypit builds
hypit inspect <build-id>
hypit history <nome-do-output>
```

Peça ao agente:

```text
Crie uma nova Run que reutilize os vídeos, imagens e áudios já aprovados do
build [BUILD_ID]. Refaça somente [ELEMENTO]. Mostre no plano quais chamadas
externas continuam necessárias antes de executar.
```

## 13. Exporte o vídeo

O caminho resumido documentado é:

```bash
hypit plan build.svrun
hypit build build.svrun --follow
hypit get <build-id> --output final.video --to output/final.mp4
```

Assista e escute o arquivo final inteiro. Confira:

- resolução, proporção, duração e taxa de quadros;
- áudio e sincronização;
- legendas e área segura;
- cortes, entradas e saídas;
- nomes, números, marca e CTA;
- artefatos gerados por IA;
- direitos dos materiais;
- adequação à plataforma de publicação.

## Para criar variações em escala

Defina claramente as partes estáveis e variáveis.

| Preserve | Permita variar |
|---|---|
| lógica narrativa | gancho |
| posição do payoff | apresentador |
| hierarquia visual | produto |
| relações de timing | texto e idioma |
| regras de área segura | B-roll |
| identidade aprovada | CTA |

Gere primeiro poucas versões diferentes e avalie se elas parecem trabalhos
distintos ou apenas cópias superficiais. Só então amplie o volume.

O comentário mais útil na discussão do post observa que o caráter espontâneo
de um conteúdo pode ser difícil de parametrizar. O tempo economizado na
produção deve ser usado também em tema, argumento e direção criativa.

## Limites e cuidados

- “Código aberto” não significa licença sem restrições. A licença atual é uma
  Apache 2.0 modificada.
- O uso interno e trabalhos da própria organização são permitidos, mas operar
  um serviço multi-tenant ou redistribuir comercialmente o Hypit pode exigir
  licença comercial.
- A licença restringe a remoção de nome, logo e avisos de copyright em certas
  superfícies geradas pelo Hypit.
- Os outputs pertencem ao usuário segundo a licença do projeto, mas serviços e
  modelos terceiros podem impor termos adicionais.
- A skill e o núcleo não cobram assento ou taxa de render do Hypit; o agente,
  APIs, modelos e infraestrutura podem cobrar.
- Clonar conteúdo não transfere direitos autorais, direito de imagem, licença
  musical ou autorização de marca.
- Produzir muitas variações semelhantes pode reduzir a originalidade e ser
  tratado pelas plataformas como conteúdo repetitivo.
- Vídeos longos e narrativas complexas não foram demonstrados pelo autor do
  post; ele próprio indicou que ainda queria testar TVCs e dramas curtos.

## Referências

- [Post original no X](https://x.com/li9292/status/2099687200975720699)
- [Repositório oficial do Hypit](https://github.com/hypit-ai/hypit)
- [Quickstart](https://hypit.ai/quickstart/)
- [Uso com agentes](https://hypit.ai/guide/agents/)
- [Modelos e providers](https://hypit.ai/guide/providers/)
- [Skill do Hypit](https://github.com/hypit-ai/hypit/tree/main/skills/hypit)
- [Licença](https://github.com/hypit-ai/hypit/blob/main/LICENSE)

> Tutorial verificado no commit
> `45bc85e73e628e56afc05865ced0cd84d13fcea2`, consultado em 16 de setembro
> de 2026. O repositório recebeu alterações no período; confira a documentação
> atual antes de instalar, configurar credenciais ou iniciar chamadas pagas.
