---
name: gary-planejamento
description: "Monte uma fila editorial executável com dependências, capacidade, versões e datas propostas. Use quando a estratégia precisa virar pautas e entregas organizadas."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-06
  versao: "1.0.0"
---
# Planejamento de produção

## Escopo e autoria
O encadeamento de pilar e derivados se apoia em Gary. Estimativa de esforço, estados de trabalho e aprovação por versão são engenharia original deste pacote.

## Entrada
Estratégia ou objetivo confirmado, capacidade disponível, backlog, materiais de origem, datas relevantes fornecidas e aprovações existentes.

## Leitura necessária
Leia [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) e [medicao-e-experimentos](../references/playbooks/medicao-e-experimentos.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Transforme cada frente editorial em pautas identificadas por objetivo, tese, formato e evidência necessária. Elimine duplicações que apenas mudam o título sem oferecer utilidade distinta.
2. Associe cada pauta a um pilar existente ou a uma produção nova. Registre dependências: pesquisa, autorização de exemplo, gravação, transcrição, copy, revisão e visual.
3. Distribua trabalho pela capacidade declarada, incluindo tempo de aprovação. Use estimativas como hipóteses e explicite folgas; não invente disponibilidade de pessoas.
4. Sequencie pesquisa e texto antes de visual. Marque copy aprovada e visual aprovado como estados separados, com versão e responsável por cada decisão.
5. Proponha janelas de produção e publicação com datas absolutas quando fornecidas. Uma data no plano é proposta; não crie eventos, compromissos ou publicações automaticamente.
6. Entregue uma fila priorizada com próximo passo e bloqueio por item. Defina como reagendar quando a evidência ou aprovação atrasar, preservando qualidade e rastreabilidade.

## Perguntas por lacunas
Qual capacidade semanal foi confirmada? Qual prazo é real e qual é apenas preferência? Quem revisa a copy e quem aprova o visual? Há materiais prontos que reduzam a produção?

## Contrato de saída
Fila por ID com objetivo, origem, formato, canal, esforço estimado, dependência, responsável confirmado ou pendente, data proposta, versão, estado e próximo passo.

## Erro crítico
Marcar como agendado/publicado algo que existe apenas no plano ou usar uma aprovação antiga para uma versão alterada.

## Referências
- [GV05 — Gary: desdobramento](../references/fontes/gv05.md): Tratar exemplos de produção como opções adaptáveis à capacidade.
- [GV07 — Gary: trabalho de equipe](../references/fontes/gv07.md): Consultar contexto de equipe sem presumir estrutura equivalente.
- [GV02 — Gary: pilar e derivados](../references/fontes/gv02.md): Manter a dependência entre fonte e entregas.

## Papel
[coordenador](../agents/coordenador.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
