---
name: oracle-skill-b01a9873bb85b56714da
description: "Coordene um pedido de conteúdo entre contexto, pesquisa, conteúdo-pilar, derivados, revisão de copy e entrega visual separada. Use para escolher e sequenciar as skills deste departamento."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-01
  versao: "1.0.0"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Orquestração editorial

## Escopo e autoria
Gary orienta a relação conteúdo-pilar, derivados e contexto de distribuição. O roteamento, os recibos de aprovação e a divisão em papéis são engenharia original deste pacote; não são um processo oficial de Gary.

## Entrada
Pedido atual, objetivo, público, canais, material já disponível, restrições e aprovações existentes. Receba caminhos explícitos, sem presumir leitura do vault ou acesso às contas.

## Leitura necessária
Leia [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) e [contexto-e-entrevista](../references/playbooks/contexto-e-entrevista.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Classifique a entrega: estratégia, texto, roteiro, auditoria ou visual. Registre o que foi pedido e quais decisões já foram tomadas nesta conversa.
2. Monte um registro de contexto conhecido, lacunas e cobertura de leitura; encaminhe apenas lacunas reais para contexto-vault ou entrevista. Não exija nova entrevista para uma revisão localizada.
3. Defina a peça-pilar ou, quando não houver material suficiente, um conteúdo autônomo. Relacione cada derivado a uma tese e a uma evidência concretas, sem impor uma quantidade universal.
4. Escolha as skills de pesquisa, redação e plataforma pela entrega. Atribua papéis documentais e critérios de passagem; só descreva execução de ferramenta ou agente quando houver resultado observado.
5. Submeta a copy versionada à revisão e à aprovação correspondente. Encaminhe direção visual somente depois da copy aprovada; mantenha a aprovação visual como decisão separada.
6. Consolide arquivos, fontes, pendências e estado de cada etapa. Use estados como proposto, rascunho, aprovado, executado e não executado; entregue para revisão humana e nunca autopublique.

## Perguntas por lacunas
Qual resultado esta entrega precisa produzir? Qual peça ou canal é prioritário? Existe copy ou direção já aprovada? Pergunte apenas o que ainda não está documentado e mudaria o encaminhamento.

## Contrato de saída
Mapa objetivo → pilar → derivados; fila de skills/papéis; entradas e saídas de cada etapa; versões de copy e visual; evidências de execução; pendências e aprovação necessária. Nenhuma etapa planejada recebe status executado.

## Erro crítico
Tratar um papel descrito como agente ativo, pular a aprovação de copy ou assumir autorização de publicação.

## Referências
- [GV02 — Gary: conteúdo-pilar](../references/fontes/gv02.md): Fundamentar a relação entre material de origem e derivados.
- [GV05 — Gary: exemplos de desdobramento](../references/fontes/gv05.md): Consultar exemplos como repertório, sem transformar a quantidade em obrigação.
- [GV06 — Gary: contexto de plataforma](../references/fontes/gv06.md): Conferir os limites da atribuição sobre adaptação ao contexto.

## Papel
[coordenador](../agents/coordenador.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
