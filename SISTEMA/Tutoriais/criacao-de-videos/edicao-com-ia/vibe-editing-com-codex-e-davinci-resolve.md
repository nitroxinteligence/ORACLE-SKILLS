---
title: "Vibe editing com Codex e DaVinci Resolve"
slug: vibe-editing-com-codex-e-davinci-resolve
language: pt-BR
type: tutorial
category: criacao-de-videos
subcategory: edicao-com-ia
source: https://x.com/ForwardEditor/status/2098258583028633924
source_article: https://x.com/i/article/2098245706993586182
source_author: "Brian (@ForwardEditor)"
source_published_at: "2026-09-11T03:53:24Z"
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
tags:
  - vibe-editing
  - codex
  - davinci-resolve
  - edicao-de-video
  - mcp
  - criacao-de-conteudo
---

# Vibe editing com Codex e DaVinci Resolve

Vibe editing é um processo de edição de vídeo no qual você orienta o Codex por linguagem natural enquanto ele opera o DaVinci Resolve por meio de MCP.

O processo não cria uma edição perfeita em uma única tentativa. Ele segue o mesmo ciclo de uma edição convencional:

```text
pedido inicial
→ primeiro corte
→ revisão humana
→ correções específicas
→ adição de elementos visuais
→ revisão completa
→ exportação
→ transformação do fluxo em skill
```

A automação retira o trabalho repetitivo, mas o gosto, as escolhas criativas e a aprovação continuam com o editor.

## 1. Prepare o ambiente

O autor recomenda:

- **DaVinci Resolve Studio:** US$ 295 em pagamento único;
- **assinatura do OpenAI Codex:** US$ 200 por mês.

Segundo o fluxo apresentado, a edição por MCP funciona melhor com o DaVinci Resolve Studio. Você também pode começar pela versão gratuita antes de comprar a licença.

## 2. Conecte o Codex ao DaVinci Resolve

Abra o Codex e envie:

```text
Instale ou atualize o DaVinci Resolve e instale o MCP do DaVinci Resolve.
```

Depois da instalação, mantenha o projeto de vídeo e seus arquivos de mídia organizados em uma pasta conhecida pelo Codex e pelo DaVinci Resolve.

Exemplo:

```text
meu-video/
├── projeto/
├── camera/
├── audio/
├── b-roll/
├── imagens/
├── musica/
└── exports/
```

## 3. Explique o resultado desejado

O primeiro pedido deve descrever o tipo de vídeo e os principais problemas que precisam ser resolvidos.

Exemplo do artigo:

```text
Pegue este vídeo em que apareço caminhando, remova meus tropeços de fala e faça
uma correção de cor para deixá-lo mais agradável.

Corrija também o equilíbrio do áudio, porque estou ao ar livre e há vento.
```

Você pode acrescentar:

- formato final;
- duração aproximada;
- plataforma de publicação;
- ritmo desejado;
- proporção da tela;
- arquivos que podem ser usados;
- elementos que não podem ser removidos.

Modelo:

```text
Crie o primeiro corte deste vídeo para [PLATAFORMA].

Objetivo:
[O QUE O VÍDEO PRECISA COMUNICAR]

Formato:
- proporção: [16:9, 9:16 ou 1:1]
- duração aproximada: [TEMPO]
- ritmo: [CALMO, DIRETO, RÁPIDO OU OUTRO]

No primeiro corte:
- remova tropeços de fala;
- remova pausas claramente desnecessárias;
- preserve o sentido e o tom da fala;
- equilibre o volume;
- reduza [RUÍDO ESPECÍFICO];
- aplique uma correção de cor coerente;
- mantenha todo o material original disponível para revisões.

Não faça a edição final ainda. Entregue primeiro um corte bruto para revisão.
```

## 4. Comece pelo corte bruto

Peça um primeiro corte antes de adicionar efeitos, B-roll, música ou uma identidade visual elaborada.

O objetivo dessa etapa é fazer a base de áudio e fala funcionar:

- palavras inteiras;
- ritmo natural;
- ausência de pausas estranhas;
- cortes que não chamam atenção;
- voz compreensível;
- volume equilibrado;
- sequência coerente.

Pedido:

```text
Faça somente o corte bruto.

Priorize a continuidade natural da fala e do áudio. Remova tropeços, repetições
acidentais e pausas que atrapalham o ritmo, sem cortar finais de palavras ou
alterar o sentido.

Não adicione B-roll, legendas, música ou efeitos nesta etapa.
```

Assista ao resultado inteiro antes de pedir novos elementos.

## 5. Revise a fala e o áudio

Assista e escute o vídeo. Procure:

- palavras cortadas;
- finais de palavras incompletos;
- pausas estranhas;
- mudanças bruscas de volume;
- ruído excessivo;
- cortes perceptíveis;
- frases que perderam o sentido;
- áudio e imagem fora de sincronia.

Se algo estiver errado, descreva o problema e peça uma correção específica. Depois, assista novamente ao trecho alterado.

Modelo:

```text
Revise o trecho entre [INÍCIO] e [FIM].

Problema observado:
[DESCREVA EXATAMENTE O QUE SOA OU PARECE ERRADO]

Corrija somente esse problema, preserve o restante da edição e me devolva o
trecho atualizado para nova revisão.
```

## 6. Corrija usando timestamps

Dê uma instrução clara para cada problema.

Exemplos do artigo:

```text
Em 00:27, a última palavra está cortada.
```

```text
Em 00:43, mostre a captura de tela que forneci durante esta explicação. Volte
para a pessoa falando quando a explicação terminar.
```

```text
O punch-in em 01:02 está forte demais. Reduza o zoom e mantenha os olhos na
mesma altura antes e depois do corte.
```

Modelo de lista:

```text
Faça estas correções separadamente:

1. Em [TIMESTAMP], [PROBLEMA]. [CORREÇÃO DESEJADA].
2. Em [TIMESTAMP], [PROBLEMA]. [CORREÇÃO DESEJADA].
3. Entre [INÍCIO] e [FIM], [PROBLEMA]. [CORREÇÃO DESEJADA].

Preserve os trechos que não foram mencionados.
```

Se uma correção criar outro problema, descreva o novo problema e revise novamente.

Você pode ditar as observações durante a reprodução em vez de digitar cada timestamp.

## 7. Adicione B-roll

Adicione elementos visuais depois que o corte bruto e a base de áudio estiverem funcionando.

Pedido do artigo:

```text
Encontre B-roll que combine com o que estou falando e adicione-o onde fizer
sentido.

Se eu tiver fornecido B-roll, priorize esse material. Preserve a continuidade e
o bom ritmo da base de áudio.
```

Você pode fornecer os arquivos ou pedir que o Codex procure materiais adequados.

Para cada inserção, defina:

- a fala que precisa de apoio visual;
- o tipo de imagem desejado;
- a duração;
- o ponto de entrada e saída;
- se a pessoa falando deve continuar visível;
- o material fornecido que deve ser usado.

Modelo:

```text
Entre [INÍCIO] e [FIM], cubra a fala sobre [ASSUNTO] com [TIPO DE B-ROLL].

Use primeiro os arquivos de [PASTA OU ARQUIVO]. Mantenha a fala como áudio
principal e volte para a pessoa falando quando a explicação terminar.
```

## 8. Crie as legendas

Defina a aparência em linguagem direta.

Você pode pedir:

- fonte sans-serif;
- peso bold;
- contorno;
- sombra;
- cor de destaque;
- animação por palavra ou linha;
- posição na tela;
- limite de palavras por linha;
- palavras específicas em destaque.

Exemplo:

```text
Adicione legendas em fonte sans-serif bold.

Use texto branco, contorno preto discreto e sombra curta. Mantenha no máximo
duas linhas por vez. Destaque somente as palavras principais em [COR].

Posicione as legendas dentro da área segura e preserve a legibilidade sobre a
pessoa e o B-roll.
```

Quando houver uma referência visual de outro criador, forneça a imagem ou o vídeo e indique quais características devem ser reproduzidas.

```text
Use esta referência somente para o estilo das legendas.

Reproduza:
- família visual da tipografia;
- peso;
- contorno;
- sombra;
- ritmo de entrada;
- posição.

Não copie o conteúdo, a identidade ou outros elementos do vídeo de referência.
```

## 9. Adicione música

Descreva o sentimento e, quando necessário, o andamento.

Exemplos:

- alegre;
- luminosa;
- tensa;
- minimalista;
- discreta;
- energética;
- determinado BPM.

Pedido:

```text
Adicione uma trilha minimalista e discreta como fundo.

A música deve apoiar o ritmo sem competir com a voz. Reduza o volume durante a
fala, evite mudanças bruscas e faça entradas e saídas suaves.
```

Outra opção:

```text
Encontre uma trilha [SENTIMENTO] com aproximadamente [BPM] BPM que combine com
este vídeo.

Use-a somente se a licença permitir o uso em [PLATAFORMA]. Mantenha a voz como
elemento principal da mixagem.
```

## 10. Ajuste a correção de cor

No pedido inicial, você pode solicitar apenas uma melhoria geral. Depois de assistir ao corte, refine o resultado.

```text
Ajuste a correção de cor para [SENSAÇÃO DESEJADA].

Preserve tons de pele naturais, controle os realces e mantenha consistência
entre os cortes. Não aplique saturação ou contraste excessivos.
```

Para material externo com vento e variação de luz:

```text
Uniformize exposição, balanço de branco e contraste entre os trechos externos.

Preserve tons de pele naturais e evite que o céu ou áreas claras estourem.
```

## 11. Revise cada alteração

O processo é iterativo:

1. peça o corte bruto;
2. assista ao vídeo inteiro;
3. registre timestamps;
4. peça correções específicas;
5. assista novamente aos trechos alterados;
6. adicione B-roll;
7. revise o timing visual;
8. adicione legendas e música;
9. revise novamente;
10. assista ao vídeo completo com som.

Não acumule todos os pedidos criativos no primeiro comando. A construção em camadas permite avaliar cada decisão.

## 12. Faça a revisão final

Antes de exportar, assista à timeline completa com som e confira:

- finais das palavras;
- naturalidade das frases;
- sincronização de áudio e imagem;
- ritmo dos cortes;
- timing do B-roll;
- precisão e legibilidade das legendas;
- volume da voz;
- volume da música;
- ruídos;
- transições;
- punch-ins;
- enquadramento dos olhos;
- consistência de cor;
- início e final do vídeo.

Pedido:

```text
Antes de exportar, reproduza e revise toda a timeline com som.

Confira:
- finais de palavras;
- sincronização;
- legendas;
- timing dos elementos visuais;
- níveis de voz, música e ruído;
- consistência dos cortes e da cor.

Liste qualquer problema encontrado com timestamp. Corrija um item por vez e
revise o trecho depois de cada alteração.
```

## 13. Salve o fluxo como skill

Depois de aprovar a edição, transforme as escolhas que funcionaram em um processo reutilizável.

Prompt do artigo:

```text
Transforme este fluxo de edição aprovado em uma skill reutilizável.

Inclua minhas correções, preferências de ritmo e etapas de verificação. Separe
regras gerais de escolhas específicas deste vídeo.

Use essa skill como ponto de partida para o próximo vídeo. Antes de exportar,
assista à timeline completa com som e verifique finais de palavras,
sincronização, legendas, timing visual e níveis de áudio.
```

A skill pode guardar:

- sequência do primeiro corte;
- regras para retirar tropeços de fala;
- tolerância para pausas;
- ritmo de edição;
- estilo de punch-in;
- regras de enquadramento;
- estilo de legendas;
- tipo de música;
- preferência de cor;
- níveis de áudio;
- checklist de revisão;
- configurações de exportação.

Separe:

```text
Regras gerais
├── naturalidade da fala
├── revisão por timestamps
├── legibilidade das legendas
├── equilíbrio do áudio
└── verificação antes de exportar

Escolhas deste vídeo
├── trilha específica
├── B-roll específico
├── textos e imagens próprios
├── duração
└── identidade visual da campanha
```

## Prompt completo para iniciar uma edição

```text
Edite este vídeo em etapas.

CONTEXTO
- plataforma: [PLATAFORMA]
- proporção: [FORMATO]
- duração desejada: [DURAÇÃO]
- público: [PÚBLICO]
- objetivo: [OBJETIVO]
- estilo: [ESTILO]

ETAPA 1 — CORTE BRUTO
- remova tropeços de fala e repetições acidentais;
- remova somente pausas que prejudiquem o ritmo;
- preserve finais de palavras e naturalidade;
- mantenha o sentido da fala;
- equilibre o áudio;
- reduza [TIPO DE RUÍDO];
- aplique correção básica de cor;
- não adicione B-roll, música, legendas ou efeitos ainda.

Entregue o primeiro corte para minha revisão.

ETAPA 2 — CORREÇÕES
Depois que eu assistir, farei pedidos com timestamps. Altere somente os pontos
indicados e preserve o restante.

ETAPA 3 — ELEMENTOS VISUAIS
Depois da aprovação do corte bruto, adicione B-roll, punch-ins, capturas de tela
e outros elementos nos trechos indicados. Preserve a continuidade do áudio.

ETAPA 4 — LEGENDAS E MÚSICA
Use [ESTILO DE LEGENDA] e uma trilha [ESTILO OU BPM]. Mantenha a voz como
elemento principal.

ETAPA 5 — REVISÃO
Assista à timeline completa com som e verifique palavras, sincronização,
legendas, timing visual, enquadramento, cor e níveis de áudio.

ETAPA 6 — EXPORTAÇÃO
Exporte somente após a aprovação da revisão completa.
```

## Fonte

- [How to start vibe editing — Brian](https://x.com/ForwardEditor/status/2098258583028633924)
