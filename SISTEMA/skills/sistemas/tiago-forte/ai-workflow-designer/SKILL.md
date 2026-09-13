---
name: oracle-skill-786e455fb5f13429631c
description: "Projetar workflow IA com entradas, saídas, ferramentas, falhas e HITL. Use em Sistemas / Tecnologia."
metadata:
  departamento: sistemas
  especialista: tiago-forte
  skill-id: SIS-TEC-01
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# ai-workflow-designer

## Especialista e contexto

Ative a orientação de [[SISTEMA/recursos-skills/perfis/tiago-forte-tecnologia/perfil|Tiago Forte — Tecnologia]] para esta habilidade. Localize esse caminho a partir da raiz do vault, e leia o perfil antes de executar. A identidade é de IA com atribuição; o resultado deve refletir o método, não inventar a pessoa real.

Leia [[SISTEMA/skills/contexto-compartilhado|Contexto de trabalho]] para resolver dados de negócio, caminhos e dependências. Use os dados do pedido e as notas pertinentes já existentes; não invente um perfil do fundador.

## Procedimento

Leia [o procedimento de origem](references/upstream/procedimento.md) e carregue suas referências conforme a tarefa. Preserve a profundidade das etapas, critérios e exemplos; adapte a saída para PT-BR e para o negócio real.

## Adaptação ao OS

Moderada: threat model, logs, custo, fallback e gate de mutação.

As instruções desta camada de integração resolvem os caminhos/limites do pacote: contexto em `.agents/product-marketing.md`, `.agents/sales-context.md` ou `BUSINESS_CONTEXT.md` significa o contexto do projeto atual, se existente. Não crie esses arquivos nem migre notas só para satisfazer um caminho do fornecedor. Saídas usam o destino pedido pelo usuário; caminhos de exemplo do autor não são destinos obrigatórios. Marcas, serviços e equipes citados como exemplo pertencem ao autor, não ao usuário.

Referências a outras skills são rotas opcionais: consulte [[SISTEMA/skills/indice-fundador|o índice]] e use a habilidade disponível pertinente. Não declare integração ativa por existir uma referência. Contas externas e ferramentas só são necessárias para as operações que as usam; uma análise ou rascunho pode usar dados fornecidos. Aplique a autorização existente sem exigir confirmações repetidas.

Números, benchmarks, políticas e limites dos exemplos não são fatos atuais do caso: confira fontes e data quando determinarem a recomendação. Não afirme garantia de conversão, receita, certificação ou conformidade por usar o método.

## Automação determinística e confiabilidade

Uma etapa pode ser determinística, inferência de IA ou decisão humana; não coloque um LLM onde uma regra verificável resolve. Para eventos, defina a chave de idempotência e persista o estado antes de repetir efeitos. Eventos fora de ordem exigem versão/sequência ou reconciliação com a fonte canônica. Em timeout após uma escrita externa, resultado é desconhecido: consulte o estado por ID antes de reenviar. Modele retries limitados com backoff, fila de falhas e registro de evidência, sem chamar timeout de sucesso. Contratos de entrada/saída devem incluir dados necessários e tratamento de ausência. Para cada ação externa, determine o executor e a autorização disponível; um desenho não prova integração ativa.

## Proveniência

Origem: [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills/blob/f67821d42c8c6db20752030e12ded030a623bee3/skills/ai-workflow-designer/SKILL.md). Commit `f67821d42c8c6db20752030e12ded030a623bee3`. Licença MIT em [LICENSE](LICENSE). Adaptação: integração de contexto, especialista, destino e limites no OS; procedimento de origem adaptado como referência; a licença é preservada, e correções estão registradas no relatório de revisão.


## Verificação de uso

Entrada: processo, riscos e sistemas. Saída: workflow com HITL, retries, logs, custos e rollback; nenhuma integração criada.

Este cenário é um exemplo de teste, não um requisito universal para pedidos reais. Respeite o escopo solicitado; não invente entradas ou opções só para cumprir o exemplo. Registre o artefato real quando exercitado.
