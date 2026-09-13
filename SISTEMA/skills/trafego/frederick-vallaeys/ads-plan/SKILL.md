---
name: oracle-skill-c5d058734bdd0ba0869b
description: "Montar plano de canais, orçamento, medição e riscos. Use em Tráfego / Mídia paga."
metadata:
  departamento: trafego
  especialista: frederick-vallaeys
  skill-id: TRF-MID-02
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# ads-plan

## Especialista e contexto

Ative a orientação de [[SISTEMA/recursos-skills/perfis/frederick-vallaeys-midia-paga/perfil|Frederick Vallaeys — Mídia paga]] para esta habilidade. Localize esse caminho a partir da raiz do vault, e leia o perfil antes de executar. A identidade é de IA com atribuição; o resultado deve refletir o método, não inventar a pessoa real.

Leia [[SISTEMA/skills/contexto-compartilhado|Contexto de trabalho]] para resolver dados de negócio, caminhos e dependências. Use os dados do pedido e as notas pertinentes já existentes; não invente um perfil do fundador.

## Procedimento

Leia [o procedimento de origem](references/upstream/procedimento.md) e carregue suas referências conforme a tarefa. Preserve a profundidade das etapas, critérios e exemplos; adapte a saída para PT-BR e para o negócio real.

## Adaptação ao OS

Moderada: renomear superfície para ORACLE, preservar pacote completo e manter read-only.

As instruções desta camada de integração resolvem os caminhos/limites do pacote: contexto em `.agents/product-marketing.md`, `.agents/sales-context.md` ou `BUSINESS_CONTEXT.md` significa o contexto do projeto atual, se existente. Não crie esses arquivos nem migre notas só para satisfazer um caminho do fornecedor. Saídas usam o destino pedido pelo usuário; caminhos de exemplo do autor não são destinos obrigatórios. Marcas, serviços e equipes citados como exemplo pertencem ao autor, não ao usuário.

Referências a outras skills são rotas opcionais: consulte [[SISTEMA/skills/indice-fundador|o índice]] e use a habilidade disponível pertinente. Não declare integração ativa por existir uma referência. Contas externas e ferramentas só são necessárias para as operações que as usam; uma análise ou rascunho pode usar dados fornecidos. Aplique a autorização existente sem exigir confirmações repetidas.

Números, benchmarks, políticas e limites dos exemplos não são fatos atuais do caso: confira fontes e data quando determinarem a recomendação. Não afirme garantia de conversão, receita, certificação ou conformidade por usar o método.

## Runtime opcional

O CLI `claude_ads_core` incluído em `references/upstream/claude_ads_core` exige Python 3.11 ou superior. Execute-o a partir de `references/upstream`; `python3 -m claude_ads_core --help` confirma apenas o carregamento do CLI. Planejamento com dados fornecidos não exige conta de anúncios nem execução desse CLI.

## Proveniência

Origem: [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads/blob/ac21644933910419529bcf81efb95a9ca71edf81/skills/ads-plan/SKILL.md). Commit `ac21644933910419529bcf81efb95a9ca71edf81`. Licença MIT em [LICENSE](LICENSE). Adaptação: integração de contexto, especialista, destino e limites no OS; procedimento de origem adaptado como referência; a licença é preservada, e correções estão registradas no relatório de revisão.


## Verificação de uso

Entrada: economics, verba e exports. Saída: media-plan JSON válido no schema, owners, guardrails e condição de saída; plataforma sem evidência fica unknown.

Este cenário é um exemplo de teste, não um requisito universal para pedidos reais. Respeite o escopo solicitado; não invente entradas ou opções só para cumprir o exemplo. Registre o artefato real quando exercitado.
