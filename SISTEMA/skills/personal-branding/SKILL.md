---
name: oracle-skill-4c8e68258d687729a01e
description: Consultar o acervo atribuído de Rory Vaden para analisar posicionamento, público, conteúdo, histórias, reputação, oferta e uso de IA em marca pessoal. Use quando uma decisão de personal branding precisar dos modelos e das fontes do especialista, com aplicação contextualizada e rastreável.
---
<!-- Modified for Oracle distribution; exact input/output digests and reasons are in the signed distribution manifest. -->

# Rory Vaden — Personal Branding

> Requisito para a consulta especializada: o corpus Rory Vaden e seu mapa de fontes devem ser fornecidos separadamente. Esses recursos não integram esta distribuição. Se estiverem ausentes, solicite-os antes de aplicar os modelos; não simule uma consulta ao acervo.

Use o acervo curado no Obsidian OS como uma fonte especializada para decisões de marca pessoal. Recupere o modelo pertinente, confira sua base e traduza-o para o contexto real da pessoa ou do projeto.

## Consulta mínima

Antes de dar uma recomendação substantiva:

1. Abra a entrada `wiki/especialistas/rory-vaden/overview` e `wiki/especialistas/rory-vaden/perfil-e-limites` na fonte `obsidian-os`.
2. Escolha o modelo correspondente ao pedido usando o mapa do acervo (recurso externo: references/corpus-map.md; não incluído nesta distribuição).
3. Abra o modelo e pelo menos uma fonte RV citada nele. Para afirmações específicas, a fonte é necessária; o índice ou a Q&A não bastam.
4. Compare o modelo com as evidências atuais da pessoa, do público, da oferta e do projeto. Aplique, adapte ou rejeite o modelo com uma razão concreta.
5. Informe de forma proporcional qual lente foi usada, as fontes consultadas e os limites relevantes.

Quando GBrain estiver disponível, consulte com `query`, usando `source_id="obsidian-os"` e `expand=false`, e leia as páginas escolhidas com `get_page`. Preserve `canonical_path` ou `origin_source_path` ao citar a origem. Se GBrain não estiver disponível, leia os mesmos arquivos na raiz canônica indicada no mapa. Não trate lembrança anterior como consulta atual.

## Limites

- O corpus tem versão própria e cobertura limitada. Não o apresente como reprodução integral da obra, clone cognitivo, afiliação ou endosso.
- Não responda “como Rory”, não imite sua voz e não atribua ao especialista uma síntese ou adaptação criada pelo assistente.
- Separe Rory, AJ Vaden, entrevistadores, convidados e influências citadas. Preserve a autoria registrada em cada fonte.
- Q&A é síntese do acervo, não entrevista literal. RV10 e RV15 têm notas sem transcrição; RV20 usa legendas automáticas; RV16 contém conflito editorial de identificação.
- Exemplos de receita, audiência e frequência são contextuais. Não os converta em previsão, regra diária ou garantia.
- A ordem de decisão é: instrução do usuário, decisões e evidências atuais, modelo contextualizado do especialista e, por último, hipótese do assistente.

## Entrega

Responda ao pedido no formato necessário. Inclua um registro curto quando a consulta influenciar a decisão:

```yaml
expert_consultation:
  expert: Rory Vaden
  corpus_version: versão lida na entrada do acervo
  model: slug do modelo consultado
  source_ids: [RVxx]
  application: como a lente foi aplicada, adaptada ou rejeitada
  limits: limites de cobertura ou atribuição que afetam a conclusão
```

Em respostas curtas, transforme esse registro em uma frase natural. Não crie um documento separado apenas para comprovar a consulta.

Use `$personal-branding` quando o pedido também exigir coordenação ampla de provas, voz, direção editorial ou execução por outros módulos.
