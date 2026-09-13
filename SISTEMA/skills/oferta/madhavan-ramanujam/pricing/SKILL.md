---
name: oracle-skill-c8eab047ffe72c6f57d9
description: "Definir arquitetura de preço, packaging e pesquisa de disposição a pagar. Use em Oferta / Produto e preço."
metadata:
  departamento: oferta
  especialista: madhavan-ramanujam
  skill-id: OFE-PRC-01
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# pricing

## Especialista e contexto

Ative a orientação de [[SISTEMA/recursos-skills/perfis/madhavan-ramanujam-produto-e-preco/perfil|Madhavan Ramanujam — Produto e preço]] para esta habilidade. Localize esse caminho a partir da raiz do vault, e leia o perfil antes de executar. A identidade é de IA com atribuição; o resultado deve refletir o método, não inventar a pessoa real.

Leia [[SISTEMA/skills/contexto-compartilhado|Contexto de trabalho]] para resolver dados de negócio, caminhos e dependências. Use os dados do pedido e as notas pertinentes já existentes; não invente um perfil do fundador.

## Procedimento

Leia [o procedimento de origem](references/upstream/procedimento.md) e carregue suas referências conforme a tarefa. Preserve a profundidade das etapas, critérios e exemplos; adapte a saída para PT-BR e para o negócio real.

## Adaptação ao OS

Moderada: impostos/moeda Brasil, margem, faixa de confiança e teste.

As instruções desta camada de integração resolvem os caminhos/limites do pacote: contexto em `.agents/product-marketing.md`, `.agents/sales-context.md` ou `BUSINESS_CONTEXT.md` significa o contexto do projeto atual, se existente. Não crie esses arquivos nem migre notas só para satisfazer um caminho do fornecedor. Saídas usam o destino pedido pelo usuário; caminhos de exemplo do autor não são destinos obrigatórios. Marcas, serviços e equipes citados como exemplo pertencem ao autor, não ao usuário.

Referências a outras skills são rotas opcionais: consulte [[SISTEMA/skills/indice-fundador|o índice]] e use a habilidade disponível pertinente. Não declare integração ativa por existir uma referência. Contas externas e ferramentas só são necessárias para as operações que as usam; uma análise ou rascunho pode usar dados fornecidos. Aplique a autorização existente sem exigir confirmações repetidas.

Números, benchmarks, políticas e limites dos exemplos não são fatos atuais do caso: confira fontes e data quando determinarem a recomendação. Não afirme garantia de conversão, receita, certificação ou conformidade por usar o método.

## Proveniência

Origem: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/pricing/SKILL.md). Commit `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`. Licença MIT em [LICENSE](LICENSE). Adaptação: integração de contexto, especialista, destino e limites no OS; procedimento de origem adaptado como referência; a licença é preservada, e correções estão registradas no relatório de revisão.


## Verificação de uso

Entrada: custos, WTP e cohorts. Saída: 3 opções de packaging com faixa e sensibilidade; distinguir dado observado/declarado.

Este cenário é um exemplo de teste, não um requisito universal para pedidos reais. Respeite o escopo solicitado; não invente entradas ou opções só para cumprir o exemplo. Registre o artefato real quando exercitado.
