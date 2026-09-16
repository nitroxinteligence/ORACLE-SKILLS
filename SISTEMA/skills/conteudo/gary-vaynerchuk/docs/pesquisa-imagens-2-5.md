---
id: gv-docs-pesquisa-imagens-2-5
type: playbook
status: active
area: marca
created: '2026-09-16'
updated: '2026-09-16'
sensitivity: internal
sources: []
confidence: medium
review_after: '2026-12-16'
---
# ChatGPT Images 2.5: pesquisa e produção visual


## Produto confirmado

O anúncio oficial foi publicado em 8 de setembro de 2026. As páginas específicas documentam os identificadores gpt-image-2.5-flare e gpt-image-2.5-sunburst, posicionados respectivamente para velocidade e para qualidade/precisão. Não são resultados de um benchmark executado aqui. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa01|OA01]], [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa02|OA02]], [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa03|OA03]] e [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa04|OA04]].

## Não confundir camadas

ChatGPT Images é a experiência do produto; Image API possui geração/edição e parâmetros próprios; Responses API usa um fluxo conversacional com ferramenta; image_gen obedece ao schema efetivamente disponível nesta sessão. A existência de um recurso na interface ou API não significa que o schema nativo exponha esse controle. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa01|OA01]], [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa05|OA05]] e [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa07|OA07]].

A skill local `/codex/skills/.system/imagegen/SKILL.md` e seu prompting foram lidos. Ela orienta uso da ferramenta nativa como padrão; suas instruções antigas de CLI não comprovam qual modelo oculto é usado aqui. Não pedir credenciais para simplesmente criar a biblioteca, nem mudar para API paga sem escolha autorizada.

## Divergências de documentação

O guia específico e as páginas de modelo apresentam 2.5, enquanto partes do guia geral/cookbook ainda usam gpt-image-2. O relatório visual independente também registrou diferenças de redação comercial/tabelas e incertezas de parâmetros por rota. Não se adotaram valores de preço, streaming ou fidelidade como garantias de execução. Consultar contrato e conta no momento da implementação. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa02|OA02]]–[[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa06|OA06]].

## Brief e referências

Antes da geração, resolver finalidade, público, destino, copy aprovada, marca, referências, direitos informados e critérios de aceitação. Perguntar quais referências o usuário quer seguir, quais atributos aprecia e o que deve evitar. A falta de referência não autoriza fingir que uma foi analisada.

Identificar cada entrada como estilo, composição, identidade/produto ou alvo real de edição. Para editar, confirmar a imagem utilizável em contexto. Para representar o próprio usuário, solicitar foto quando ainda não fornecida. Uma referência estética não substitui uma foto real do produto.

## Prompt e iteração

Especificar objetivo, sujeito, cena, composição, meio visual, detalhes, texto literal, invariantes e exclusões. Nomear o papel das entradas. Respeitar os argumentos reais da ferramenta: esquema de brief não é automaticamente uma chamada de API. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa02|OA02]] e [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa06|OA06]].

Iterar com alteração focal e comparação à versão aprovada. Repetir invariantes importantes. Máscaras e instruções de preservação não garantem imutabilidade pixel a pixel. Comparar modelos requer entradas e critérios controlados. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa02|OA02]] e [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa05|OA05]].

## Qualidade e entrega

Conferir texto palavra por palavra, números, relações em diagramas, identidade, geometria do produto, recorte, bordas e coerência de série. Gráfico plausível não é dado verdadeiro. Transparência exige alfa real, não tabuleiro desenhado. Quando texto ou região fixa falha repetidamente, propor composição editável autorizada em vez de declarar perfeição. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa02|OA02]] e [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/oa05|OA05]].

Considerar descrição alternativa e equivalente textual de dados; medir contraste quando se declara atendimento a um critério. A W3C explica 4,5:1 para texto comum e 3:1 para texto grande, com condições; este pacote não certifica uma peça sem medição. Fontes [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/dv01|DV01]] e [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/fontes/dv02|DV02]].

Entregar arquivos realmente produzidos, versão, formato e limitações. Não chamar raster de vetor editável ou prometer arquivo inexistente. Nenhuma geração, edição de imagem ou chamada paga de API foi realizada na construção desta biblioteca. O relatório adicional está em `REVIEWS/pesquisa-conteudo-20260916/results/openai-images.json`.


[[SISTEMA/skills/conteudo/gary-vaynerchuk/indice|Índice do especialista]] · [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/indice|Referências]]
