---
title: "Retratos profissionais no ChatGPT e Codex: 10 prompts editáveis"
slug: retratos-profissionais-chatgpt-codex-prompts
language: pt-BR
type: prompt-library
category: engenharia-de-ai
source: https://x.com/David_TornAI/status/2098434909295534312
source_author: "@David_TornAI"
source_published_at: "2026-09-11"
captured_at: 2026-09-12
official_sources:
  - https://learn.chatgpt.com/docs/image-generation
  - https://developers.openai.com/api/docs/guides/image-prompting
tags:
  - prompts
  - chatgpt
  - codex
  - imagegen
  - retrato
  - marca-pessoal
---

# Retratos profissionais no ChatGPT e Codex: 10 prompts editáveis

Esta biblioteca adapta para português os dez cenários do [fio de
@David_TornAI no X](https://x.com/David_TornAI/status/2098434909295534312).
Os prompts foram reescritos para preservar sinais de identidade, manter textura
natural da pele e separar o que deve mudar do que deve permanecer igual.

A documentação oficial recomenda descrever assunto, composição, estilo e
restrições; em edições, é melhor dizer com clareza o que muda e o que permanece.
Também recomenda fazer revisões pequenas, uma por vez. Consulte
[geração de imagens no ChatGPT e Codex](https://learn.chatgpt.com/docs/image-generation)
e o [guia oficial de prompts para imagens](https://developers.openai.com/api/docs/guides/image-prompting).

## Como usar

1. Escolha uma foto recente, nítida e sem filtro, com o rosto visível.
2. Substitua todos os campos entre colchetes no prompt escolhido.
3. Anexe a foto e envie somente um prompt por geração.
4. Compare o rosto, a idade aparente, a pele, o cabelo e as proporções com a
   referência antes de usar a imagem.
5. Se precisar corrigir algo, use um dos prompts de ajuste no fim desta nota e
   mude um elemento por vez.

No ChatGPT, anexe a imagem no compositor e cole o prompt. No Codex, anexe a
imagem de referência e inclua `$imagegen` antes do prompt. A disponibilidade e
os limites de geração dependem do plano e das regras do workspace.

Use uma foto sua ou de alguém que autorizou o uso. A instrução para preservar a
identidade melhora a direção da edição, mas não garante reprodução exata. Não
use um retrato gerado como documento oficial ou como prova de uma situação que
não aconteceu.

## Campos mais usados

| Campo | Exemplos |
|---|---|
| `[roupa]` | blazer azul-marinho e camisa branca; camisa preta lisa; tricô bege |
| `[fundo]` | cinza-claro; branco quente; bege; grafite |
| `[cor da marca]` | azul-petróleo e areia; vinho e creme |
| `[ambiente]` | escritório moderno; biblioteca; auditório; estúdio |
| `[lado]` | esquerda; direita |
| `[formato]` | 1:1; 4:5; 16:9 |

## 1. Headshot natural para LinkedIn

Use para LinkedIn, currículo, página de equipe ou assinatura profissional.

```text
Edite a foto anexada e transforme-a em um retrato profissional natural para
LinkedIn. Preserve a identidade da pessoa: formato e proporções do rosto,
distância entre os olhos, nariz, boca, mandíbula, sinais, linhas de expressão,
tom de pele, idade aparente, textura da pele, cabelo e linha do cabelo.

Vista a pessoa com [roupa] em [cor]. Use fundo liso [cinza-claro / branco quente
/ bege], luz de estúdio suave vindo da frente e levemente de um lado, sombras
discretas e brilho natural nos olhos. Expressão confiante e acessível, postura
reta e enquadramento do peito para cima.

Resultado: fotografia realista, limpa e profissional, em formato 1:1, com espaço
seguro ao redor da cabeça para o recorte circular do perfil. Preserve poros e
pequenas assimetrias naturais. Não afine o rosto, não aumente os olhos, não
clareie a pele, não remova sinais permanentes, não aplique filtro de beleza, não
use pele plástica e não adicione texto, logotipo ou marca-d'água.
```

## 2. Retrato de marca pessoal

Use para site, perfil de consultor, página de vendas ou apresentação.

```text
Edite a foto anexada e crie um retrato de marca pessoal para um(a)
[consultor(a) / criador(a) / mentor(a) / empreendedor(a)] da área de [área].
Preserve a identidade, a idade aparente e todos os traços reconhecíveis da
pessoa. Mantenha textura de pele, cabelo, sinais e assimetrias naturais.

Coloque a pessoa em um espaço de trabalho contemporâneo, claro e realista, com
o fundo suavemente desfocado. Use [roupa] e introduza as cores da marca
[cores] apenas em detalhes discretos do cenário ou da roupa. Luz natural de
janela, postura relaxada, contato visual direto e expressão segura e acolhedora.

Resultado: fotografia editorial sóbria, vertical 4:5, com aparência de sessão
real de marca pessoal. Evite cenário luxuoso genérico, excesso de objetos,
retoque cosmético, pele lisa artificial, mudança corporal, texto, logotipo e
marca-d'água.
```

## 3. Retrato editorial sofisticado

Use para imprensa, capa de perfil, portfólio ou anúncio institucional.

```text
Transforme a foto anexada em um retrato editorial sofisticado. Preserve com
fidelidade a identidade, as proporções faciais, a idade aparente, o tom de pele,
a textura da pele, o cabelo e os sinais reconhecíveis da pessoa.

Vista a pessoa com [terno preto de corte simples / vestido elegante / conjunto
minimalista] e acessórios discretos [descrever ou escrever "sem acessórios"].
Use fundo de estúdio texturizado em [grafite / creme / vinho profundo], luz
direcional lateral, sombras suaves e gradação de cor contida. Enquadramento da
cintura para cima, composição vertical 4:5 e expressão [serena / firme /
contemplativa].

O resultado deve parecer uma fotografia editorial real, sem glamour excessivo.
Mantenha poros, linhas de expressão e pequenas assimetrias. Não altere o rosto
ou o corpo, não use filtro de beleza, não suavize demais a pele, não imite uma
revista ou fotógrafo específico e não adicione texto, logotipo ou marca-d'água.
```

## 4. Retrato externo na hora dourada

Use para marca pessoal, redes sociais ou uma apresentação menos formal.

```text
Edite a foto anexada e coloque a mesma pessoa em [rua urbana / parque / praia /
terraço] durante a hora dourada. Preserve identidade, proporções do rosto e do
corpo, tom de pele, idade aparente, cabelo, textura da pele e sinais naturais.

Vista a pessoa com [roupa]. Use luz solar quente vindo de trás e de um lado,
criando um contorno sutil no cabelo, com o rosto exposto de forma natural e sem
estourar os realces. Fundo suavemente desfocado, cores realistas, sombras
coerentes com o ambiente e pose espontânea. Expressão [sorriso leve / serena /
confiante].

Resultado: fotografia profissional feita no local, em formato vertical 4:5.
Evite pôr do sol artificialmente saturado, halo recortado no cabelo, pele
encerada, dentes excessivamente brancos, alteração de traços, texto, logotipo e
marca-d'água.
```

## 5. Foto espontânea em café

Use para Instagram, bastidores, newsletter ou perfil de criador.

```text
Transforme a foto anexada em uma cena espontânea de marca pessoal dentro de um
café contemporâneo e discreto. Preserve a identidade, a idade aparente, o tom e
a textura natural da pele, o cabelo, as proporções e os sinais reconhecíveis.

Mostre a pessoa sentada perto de uma janela, usando [roupa], com [laptop /
caderno / xícara] posicionado de forma natural. A pessoa está [escrevendo /
olhando pela janela / conversando fora de quadro], em um instante real de ação,
sem pose publicitária. Use luz suave de janela, tons neutros quentes, fundo com
desfoque óptico e poucos elementos visuais.

Resultado: fotografia realista, vertical 4:5, com composição simples. Preserve
mãos anatomicamente plausíveis e objetos coerentes. Não mude o rosto ou o corpo,
não aplique retoque cosmético, não exagere o desfoque, não adicione texto,
logotipo ou marca-d'água.
```

## 6. Retrato executivo de CEO

Use para página institucional, conselho, imprensa ou apresentação corporativa.

```text
Edite a foto anexada e crie um retrato executivo sóbrio da mesma pessoa.
Preserve fielmente a identidade, as proporções faciais, a idade aparente, o tom
de pele, a textura natural, o cabelo e os sinais reconhecíveis.

Vista a pessoa com [terno / blazer] de cor [cor] e [camisa / blusa] em [cor].
Coloque-a em um escritório contemporâneo plausível, com janelas amplas e uma
vista urbana discreta e desfocada. Use iluminação profissional equilibrada,
postura ereta, ombros naturais, contato visual direto e expressão calma e
segura. Enquadramento do peito para cima, vertical 4:5.

O resultado deve transmitir experiência e clareza sem criar símbolos artificiais
de riqueza. Não rejuvenesça, não afine o rosto, não aumente ombros, não remova
linhas de expressão, não use pele plástica, não acrescente prêmios, marcas,
texto, logotipo ou marca-d'água.
```

## 7. Retrato criativo de estúdio

Use para perfil de artista, criador, designer ou profissional de tecnologia.

```text
Crie um retrato criativo de estúdio a partir da foto anexada. Preserve a
identidade, as proporções do rosto, a idade aparente, o tom e a textura da pele,
o cabelo e os sinais naturais da pessoa.

Vista a pessoa com [roupa] e use um fundo contínuo [cor]. Acrescente uma luz de
recorte discreta em [cor] vindo do lado [esquerdo / direito] e uma luz neutra e
suave no rosto. Composição limpa, sombras coerentes, detalhes faciais nítidos e
pose [descrever pose] que seja marcante sem parecer teatral.

Resultado: fotografia moderna e realista em formato [1:1 / 4:5]. A luz colorida
deve afetar somente as áreas que receberiam essa luz no mundo real. Não altere
o rosto, o corpo ou a idade, não use pele plástica, não transforme a imagem em
ilustração e não adicione texto, logotipo ou marca-d'água.
```

## 8. Foto promocional de podcast

Use para capa de episódio, miniatura ou divulgação do apresentador.

```text
Edite a foto anexada e crie uma fotografia promocional realista de apresentador
de podcast. Preserve identidade, proporções faciais, idade aparente, tom e
textura natural da pele, cabelo e sinais reconhecíveis.

Coloque a pessoa em um estúdio de gravação contemporâneo, sentada diante de um
microfone profissional plausível, com os fones [na cabeça / apoiados no
pescoço]. Vista-a com [roupa]. Use luz quente e suave, fundo discretamente
desfocado e expressão atenta, como se estivesse ouvindo ou falando com alguém.
Mantenha cabos, microfone, suporte e mãos anatomicamente coerentes.

Crie a imagem em formato 16:9 e deixe espaço negativo limpo no lado [esquerdo /
direito] para inserir o título depois. Não gere texto dentro da imagem, não
invente logotipos, não altere o rosto ou o corpo, não aplique filtro de beleza e
não adicione marca-d'água.
```

## 9. Retrato de palestrante ou autor

Use para evento, contracapa, mídia kit ou anúncio de palestra.

```text
Transforme a foto anexada em um retrato profissional de [palestrante / autor(a)
/ especialista]. Preserve a identidade, as proporções faciais, a idade aparente,
o tom de pele, a textura natural, o cabelo e os sinais reconhecíveis.

Mostre a pessoa em pé em [biblioteca contemporânea / auditório / estúdio
minimalista], usando [roupa]. Use luz direcional suave, postura profissional sem
rigidez e expressão serena e atenta. O fundo deve ser reconhecível, mas
discretamente desfocado.

Formato vertical 4:5. Posicione a pessoa no terço [esquerdo / direito] e deixe
espaço negativo real no lado oposto para inserir título, citação ou dados do
evento depois. Não gere texto na imagem, não coloque livros com títulos
inventados, não altere rosto, corpo ou idade, não aplique retoque cosmético e não
adicione logotipo ou marca-d'água.
```

## 10. Retrato de revista em preto e branco

Use para perfil editorial, site pessoal ou peça institucional mais atemporal.

```text
Converta a foto anexada em um retrato fotográfico em preto e branco. Preserve a
identidade, a estrutura e as proporções do rosto, a idade aparente, o cabelo, os
sinais e a textura natural da pele.

Use fundo escuro simples, luz direcional lateral, contraste rico com detalhes
nas áreas claras e escuras, olhos nítidos e granulação fina de filme. Vista a
pessoa com [camisa preta / gola alta / terno simples]. Faça um enquadramento
fechado de cabeça e ombros, com expressão [calma / firme / contemplativa].

Resultado: fotografia elegante e atemporal em formato [1:1 / 4:5]. Não suavize
as linhas de expressão, não crie brilho metálico na pele, não aumente o
contraste até perder detalhes, não transforme em ilustração, não imite fotógrafo
específico e não adicione texto, logotipo ou marca-d'água.
```

## Prompts de correção

Use estes comandos na mesma conversa, sempre sobre a última versão. Corrija um
problema por vez para reduzir a deriva da composição.

### Corrigir mudança de identidade

```text
Refaça a última edição usando a foto original como referência principal. Corrija
somente a identidade facial: restaure o formato do rosto, testa, sobrancelhas,
distância entre os olhos, nariz, boca, mandíbula, orelhas, linha do cabelo,
sinais, tom de pele e idade aparente da referência. Preserve cenário, roupa,
iluminação, pose, enquadramento e proporção da última versão. Não embeleze,
rejuvenesça ou simetrize o rosto.
```

### Remover aparência de pele plástica

```text
Edite somente a pele da última imagem. Restaure textura natural, poros discretos,
linhas de expressão e variações reais de tom presentes na foto original.
Remova o efeito encerado, o filtro de beleza e a suavização excessiva. Preserve
identidade, cabelo, olhos, dentes, roupa, cenário, luz, pose e enquadramento.
```

### Corrigir apenas roupa ou cenário

```text
Na última imagem, altere somente [a roupa / o cenário] para [descrição exata].
Preserve o rosto e a identidade, cabelo, pele, idade aparente, corpo, pose,
expressão, iluminação, enquadramento, cores e todos os outros elementos. Não
adicione texto, logotipo ou objetos que não foram pedidos.
```

### Corrigir enquadramento e espaço para texto

```text
Reenquadre a última imagem em [1:1 / 4:5 / 16:9]. Preserve a pessoa, o rosto, a
identidade, a roupa, a pose, a luz, as cores e o cenário. Não estique nem corte
partes importantes do corpo. Deixe espaço negativo limpo no lado [esquerdo /
direito] para eu inserir texto depois. Não gere nenhum texto na imagem.
```

### Corrigir mãos e objetos

```text
Corrija somente as mãos e os objetos em contato com elas na última imagem.
Mantenha anatomia plausível, cinco dedos por mão quando visíveis, pegada natural,
perspectiva e sombras coerentes. Preserve rosto, identidade, corpo, roupa,
expressão, cenário, luz, composição e todos os demais elementos.
```

## Prompt de conferência antes de publicar

Use este prompt para analisar a versão escolhida ao lado da referência. Ele não
substitui sua inspeção visual.

```text
Compare a imagem gerada com a foto original e faça uma revisão crítica, sem
gerar outra imagem ainda.

Verifique:
1. identidade e proporções do rosto;
2. idade aparente, tom e textura da pele;
3. cabelo, linha do cabelo e sinais reconhecíveis;
4. anatomia das mãos e coerência dos objetos;
5. direção da luz, sombras e perspectiva;
6. roupa, cenário e finalidade profissional;
7. enquadramento e espaço seguro para o uso pretendido;
8. texto, logotipos, marcas-d'água ou artefatos não solicitados.

Responda em uma tabela com: item, aprovado ou reprovado, evidência visual e
correção mínima recomendada. Se houver falha, escreva ao final um único prompt
de edição que corrija apenas o problema mais importante e preserve todo o resto.
```

## Critério de escolha

Escolha a versão que ainda parece a pessoa da foto original em uma situação
fotográfica plausível. Descarte versões com rosto remodelado, idade diferente,
pele sem textura, mãos estranhas, iluminação incoerente ou símbolos de status
inventados. Para perfis profissionais, clareza e reconhecimento costumam valer
mais do que acabamento publicitário.
