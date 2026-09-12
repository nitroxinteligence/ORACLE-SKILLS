---
title: "Restauração e aprimoramento fotográfico — 6 prompts de AI Explorer Tim"
slug: restauracao-e-aprimoramento-fotografico-ai-explorer-tim
language: pt-BR
original_language: zh
type: prompt-library
category: engenharia-de-ai
source: https://x.com/AIExplorerTim/status/2098227284826280214
source_author: "AI探路者Tim (@AIExplorerTim)"
source_published_at: "2026-09-11T01:49:02Z"
captured_at: 2026-09-12
capture_status: completa
capture_method: agent-reach/twitter-cli
official_sources:
  - https://learn.chatgpt.com/docs/image-generation
  - https://developers.openai.com/api/docs/guides/image-prompting
tags:
  - prompts
  - chatgpt
  - codex
  - imagegen
  - fotografia
  - restauracao
---

# Restauração e aprimoramento fotográfico — 6 prompts de AI Explorer Tim

Esta coleção adapta para português os seis prompts da [thread de AI Explorer Tim](https://x.com/AIExplorerTim/status/2098227284826280214). Os textos foram reorganizados para separar a mudança desejada das características que devem permanecer iguais.

| # | Finalidade | Post de origem |
|---|---|---|
| 1 | Corrigir foto desfocada | [2098227287032480169](https://x.com/AIExplorerTim/status/2098227287032480169) |
| 2 | Corrigir iluminação forte, fraca ou irregular | [2098227288718610484](https://x.com/AIExplorerTim/status/2098227288718610484) |
| 3 | Dar acabamento profissional a uma foto comum | [2098227290270572569](https://x.com/AIExplorerTim/status/2098227290270572569) |
| 4 | Trocar um fundo confuso | [2098227291931463737](https://x.com/AIExplorerTim/status/2098227291931463737) |
| 5 | Restaurar foto antiga ou de baixa qualidade | [2098227293697241228](https://x.com/AIExplorerTim/status/2098227293697241228) |
| 6 | Aplicar tratamento cinematográfico | [2098227295391793611](https://x.com/AIExplorerTim/status/2098227295391793611) |

## Como usar

No ChatGPT, anexe a fotografia e cole um dos prompts. No Codex, anexe a imagem, indique `$imagegen` e inclua o prompt. Use uma foto sua ou de alguém que autorizou a edição.

A documentação oficial recomenda descrever de forma concreta o assunto, a composição, a luz, as cores, o resultado e as restrições. Em uma edição, diga explicitamente o que deve mudar e o que precisa ser preservado. Faça correções pequenas, uma de cada vez. Consulte [geração de imagens no ChatGPT](https://learn.chatgpt.com/docs/image-generation) e o [guia de prompts para imagens](https://developers.openai.com/api/docs/guides/image-prompting).

A instrução para preservar identidade reduz mudanças indesejadas, mas não garante reprodução exata. Compare sempre o resultado com a referência.

## Bloco comum de preservação

Acrescente este bloco ao prompt escolhido quando houver uma pessoa reconhecível:

```text
Use a fotografia anexada como referência principal. Preserve a identidade da pessoa: formato e proporções do rosto, distância entre os olhos, olhos, nariz, boca, mandíbula, orelhas, tom e textura natural da pele, sinais permanentes, cabelo, linha do cabelo, idade aparente e proporções corporais. Não embeleze, rejuvenesça, afine o rosto, aumente os olhos, remova sinais nem aplique filtro de beleza. Altere somente os elementos solicitados.
```

## 1. Corrigir uma foto desfocada

Use quando o rosto ou a imagem perderam definição por movimento, foco, ruído ou compressão.

```text
Melhore tecnicamente a fotografia anexada, reduzindo desfoque, ruído, pixelização e artefatos de compressão. Recupere a nitidez principalmente a partir das informações visíveis na referência e mantenha o resultado fotográfico, natural e coerente.

Preserve a identidade, a expressão, a pose, o enquadramento, a roupa, o ambiente e a direção original da luz. Restaure contornos do rosto, olhos, cabelo e textura da pele com moderação. Equilibre exposição e contraste sem criar halos, contornos duros, poros artificiais ou nitidez excessiva.

Quando uma região não possuir informação suficiente, faça a reconstrução mais conservadora possível. Não invente texto, acessórios, dentes, fios de cabelo ou detalhes faciais específicos que não estejam sustentados pela imagem.
```

Correção isolada:

```text
Mantenha todo o resultado. Reduza somente a nitidez artificial ao redor dos olhos e do cabelo, preservando detalhes naturais e transições suaves.
```

## 2. Corrigir iluminação forte, fraca ou irregular

Use quando sombras, realces estourados ou diferença de temperatura de cor prejudicam o retrato.

```text
Corrija a iluminação da fotografia anexada e produza um retrato com acabamento de estúdio natural. Preserve a pessoa, a expressão, a pose, a roupa, o fundo, o ângulo da câmera e o enquadramento.

Equilibre realces, sombras, exposição, contraste e temperatura de cor. Recupere tons de pele naturais e detalhe nas áreas claras e escuras, respeitando a direção da luz já presente na cena. Mantenha sombras fisicamente coerentes e transições suaves no rosto.

Não altere os traços faciais, não clareie o tom de pele, não elimine todas as sombras e não transforme a pele em uma superfície lisa ou brilhante.
```

Correção isolada:

```text
Preserve pessoa, fundo e composição. Reduza apenas a intensidade dos realces na testa e nas bochechas, mantendo o volume natural do rosto.
```

## 3. Dar acabamento profissional a uma foto comum

Use para melhorar uma fotografia casual sem transformar o momento em uma sessão artificial.

```text
Aprimore a fotografia anexada para que tenha acabamento profissional, mantendo sua espontaneidade, seu contexto e a aparência de um momento real.

Preserve identidade, expressão, pose, roupa, objetos e ambiente. Ajuste com moderação exposição, contraste, balanço de branco, luz e harmonia de cores. Melhore a definição onde houver informação suficiente e mantenha textura natural na pele, no cabelo, nos tecidos e no cenário.

Se a composição puder melhorar, faça apenas um recorte discreto que não remova elementos importantes. Não substitua o ambiente, não crie uma pose nova, não aplique estética publicitária e não adicione elementos que não existiam na cena.
```

Correção isolada:

```text
Mantenha todo o conteúdo e a edição. Desfaça somente o recorte e recupere o enquadramento original, preservando os demais ajustes.
```

## 4. Trocar um fundo confuso

Substitua `[NOVO FUNDO]` por uma descrição concreta, como “parede cinza-clara com textura discreta” ou “escritório realista iluminado por janela”.

```text
Substitua somente o fundo confuso da fotografia anexada por [NOVO FUNDO]. Preserve sem alterações a pessoa, o rosto, a expressão, a pose, o corpo, o cabelo, a roupa, os acessórios e o enquadramento.

Integre o novo ambiente respeitando o ângulo da câmera, a perspectiva, a escala, o horizonte, a profundidade de campo e as relações espaciais da fotografia original. Faça a direção, a intensidade e a temperatura da luz coincidirem entre pessoa e cenário. Preserve bordas naturais no cabelo e na roupa e crie sombras de contato plausíveis.

O resultado deve parecer capturado naquele ambiente. Não recorte a pessoa com halo, não aplique desfoque uniforme, não altere a anatomia e não adicione texto, logotipo ou marca-d'água.
```

Correção isolada:

```text
Mantenha pessoa, enquadramento e novo fundo. Corrija somente as bordas do cabelo e a sombra de contato para eliminar a aparência de recorte.
```

## 5. Restaurar foto antiga ou de baixa qualidade

Use para recuperar legibilidade visual. A restauração não comprova a aparência exata de detalhes ausentes.

```text
Restaure a fotografia antiga ou de baixa qualidade anexada. Preserve identidade, expressão, pose, idade representada, roupa, objetos, composição e características históricas visíveis.

Reduza poeira, riscos, manchas, ruído, granulação excessiva, pixelização, compressão e desfoque. Recupere contraste, exposição e detalhes finos de forma conservadora. Preserve grão fotográfico quando ele fizer parte do material original e mantenha pele, cabelo, tecidos e superfícies com textura natural.

Não modernize roupas, penteados, objetos ou cenário. Não altere a idade, não embeleze a pessoa e não invente inscrições ou detalhes documentais. Se uma área estiver destruída, reconstrua apenas uma versão visualmente plausível e não a trate como recuperação factual.
```

Para colorização, faça uma etapa separada:

```text
Mantenha exatamente a restauração aprovada. Agora faça somente a colorização, usando cores historicamente plausíveis e discretas. Quando a cor original não puder ser determinada, prefira tons conservadores e não apresente a escolha como fato.
```

## 6. Aplicar tratamento cinematográfico

Substitua `[CLIMA]` por uma direção como “drama noturno frio”, “fim de tarde acolhedor” ou “suspense com contraste moderado”.

```text
Aplique à fotografia anexada um tratamento cinematográfico realista com clima [CLIMA], como se tivesse sido capturada naturalmente com câmera full-frame e lente profissional. Preserve a identidade, a expressão, a pose, a roupa, o ambiente, o ângulo e a composição.

Melhore com moderação a nitidez óptica, os detalhes finos, a faixa dinâmica, o equilíbrio da luz, a profundidade das cores e a gradação tonal. Use color grading cinematográfico contido, contraste coerente com a cena e profundidade de campo fisicamente plausível. Mantenha tons de pele naturais e textura realista.

Não imite um filme ou diretor específico, não crie bokeh falso ao redor do corpo, não use cores excessivamente saturadas, não esmague as sombras, não aplique nitidez artificial e não modifique os traços da pessoa.
```

Correção isolada:

```text
Preserve composição, identidade e iluminação. Reduza somente a intensidade do color grading em cerca de 25%, mantendo o clima cinematográfico e os tons naturais de pele.
```

## Escolha rápida

| Problema principal | Prompt |
|---|---|
| rosto ou imagem fora de foco | 1. Corrigir foto desfocada |
| luz dura, escura ou desigual | 2. Corrigir iluminação |
| foto correta, mas sem acabamento | 3. Acabamento profissional |
| ambiente distrai ou compromete a imagem | 4. Trocar fundo |
| dano, ruído ou baixa resolução antiga | 5. Restaurar foto |
| imagem tecnicamente boa, mas sem direção visual | 6. Tratamento cinematográfico |

Não empilhe os seis prompts numa única geração. Corrija primeiro o defeito técnico principal, aprove o resultado e faça a próxima mudança em uma nova etapa.

## Checklist de comparação

- [ ] O formato e as proporções do rosto permanecem reconhecíveis.
- [ ] A idade aparente, o tom de pele e os sinais naturais foram preservados.
- [ ] Olhos, dentes, cabelo e acessórios não ganharam detalhes incoerentes.
- [ ] A luz e as sombras seguem a mesma direção em toda a cena.
- [ ] As bordas da pessoa não apresentam halo ou recorte artificial.
- [ ] A textura da pele não ficou lisa, encerada ou excessivamente nítida.
- [ ] Texto, logotipos e objetos não foram inventados.
- [ ] A edição alterou somente o que o prompt solicitou.

## Integridade da captura

- O post principal e os seis prompts publicados pelo autor foram capturados integralmente com `agent-reach` pelo backend `twitter-cli` em 12 de setembro de 2026.
- O sexto post foi expandido antes da leitura; o comentário final do autor não contém outro prompt.
- O encerramento promocional e respostas de terceiros foram excluídos.
- A imagem do post principal contém somente a identificação visual “GPT 6 Astra”; não acrescenta instruções.
- Os prompts foram traduzidos e ampliados em português, preservando a finalidade de cada publicação sem reproduzir toda a redação original.
- A alegação de que a edição não muda os traços foi tratada como objetivo, não como garantia técnica.

## Fontes

- [Thread original de AI Explorer Tim](https://x.com/AIExplorerTim/status/2098227284826280214)
- [Image generation — ChatGPT Learn](https://learn.chatgpt.com/docs/image-generation)
- [Image prompting — OpenAI API](https://developers.openai.com/api/docs/guides/image-prompting)
