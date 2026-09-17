---
name: oracle-skill-fc4a246d2b87bbcabd85
description: "Analise dados editoriais autorizados e desenhe experimentos com objetivo, denominador, comparação e critérios de decisão. Use para aprender com resultados sem fabricar causalidade."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-29
  versao: "1.0.0"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Métricas e experimentos editoriais

## Escopo e autoria
Gary/equipe oferecem contexto de análise após publicação. O desenho de experimento, controle de comparabilidade e interpretação de incerteza são engenharia original apoiada em definições oficiais.

## Entrada
Objetivo, conjunto de publicações, dados autorizados, definições de métricas, janela, origem orgânica/paga e versões das peças. Ausência de dados não é resultado zero.

## Leitura necessária
Leia [medicao-e-experimentos](../references/playbooks/medicao-e-experimentos.md) e [pesquisa-e-evidencia](../references/playbooks/pesquisa-e-evidencia.md) e [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Escolha uma métrica principal ligada à decisão e uma proteção contra regressão, como manter clareza e entrega. Separe descoberta, consumo, relacionamento e ação comercial.
2. Construa uma tabela com peça, canal, formato, tema, idade, distribuição, contagens e denominadores. Preserve os dados de origem; diferencie nulo, não disponível e zero observado.
3. Compare coortes semelhantes por janela, idade, objetivo e fonte de tráfego. Não some alcance único entre redes como se não houvesse sobreposição; views do X não representam pessoas únicas.
4. Calcule somente taxas sustentadas pelos campos disponíveis e rotule a fórmula. Descreva mediana/dispersão quando houver amostra adequada, sem fabricar benchmarks ou tamanho mágico de significância.
5. Desenhe o teste com hipótese, variável, comparação, métrica, janela e confundidores. Publicações em datas distintas não são automaticamente A/B aleatório; teste nativo de YouTube depende de elegibilidade e pode ser inconclusivo.
6. Separe achado, explicação possível e decisão. Recomende manter, ajustar, interromper ou investigar com base no objetivo, registrando o que os dados não permitem concluir. Testes e publicações permanecem propostas até autorização.

## Perguntas por lacunas
Qual decisão os dados devem orientar? As definições e janelas são comparáveis? Há distribuição paga misturada? Qual variável pode mudar sem alterar simultaneamente toda a peça?

## Contrato de saída
Tabela de origem e definições, cálculos reproduzíveis, comparação por coorte, incertezas, ficha de experimento e decisão qualificada. Dados privados permanecem minimizados e no escopo autorizado.

## Erro crítico
Confundir correlação com efeito causal, tratar dado ausente como zero ou apresentar taxa sem denominador e janela.

## Referências
- [GV07 — Gary: funções da equipe](../references/fontes/gv07.md): Contexto de análise após publicação, sem presumir estrutura equivalente.
- [YT04 — YouTube: métricas](../references/fontes/yt04.md): Manter definições por formato.
- [YT02 — YouTube: A/B](../references/fontes/yt02.md): Delimitar desenho, elegibilidade e resultados inconclusivos.
- [X01 — X: views](../references/fontes/x01.md): Evitar leitura como pessoas únicas.
- [LI02 — LinkedIn: Analytics](../references/fontes/li02.md): Preservar limites de dados agregados.

## Papel
[analista](../agents/analista.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
