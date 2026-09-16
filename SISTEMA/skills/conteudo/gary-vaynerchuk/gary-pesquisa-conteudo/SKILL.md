---
name: gary-pesquisa-conteudo
description: "Pesquise evidências suficientes para uma pauta delimitada, distinguindo fontes lidas, snippets e hipóteses. Use para sustentar uma afirmação editorial sem abrir uma investigação desnecessária."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-07
  versao: "1.0.0"
---
# Pesquisa para uma pauta

## Escopo e autoria
A coleta, o registro de acesso e a contraprova são engenharia original de pesquisa. Gary complementa a conexão entre aprendizado e conteúdo; não é autor deste protocolo de verificação.

## Entrada
Pergunta da pauta, público, afirmações previstas, prazo de validade dos fatos e fontes já disponíveis. Não receba snippets como se fossem documentos integrais.

## Leitura necessária
Leia [pesquisa-e-evidencia](../references/playbooks/pesquisa-e-evidencia.md) e [voz-e-narrativa](../references/playbooks/voz-e-narrativa.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Converta a pauta em duas ou três perguntas verificáveis e delimite o que fica fora. Liste as afirmações que realmente precisam de fonte, priorizando números, datas e promessas.
2. Busque evidência primária pertinente: documentação da plataforma, estudo original, dados públicos ou declaração do autor. Para OpenAI, use somente domínios oficiais.
3. Abra cada fonte relevante e registre URL, autor, data, acesso, trecho de apoio e estado de leitura. Indique quando houve apenas snippet, bloqueio ou acesso parcial.
4. Confira se população, período e formato da fonte correspondem à afirmação. Não use uma página de vendas de livro como prova de todo o livro nem uma menção como acesso ao conteúdo de X.
5. Procure uma limitação ou contraprova material. Reduza a formulação quando a evidência for indireta, antiga ou conflitante, sem preencher a lacuna com confiança retórica.
6. Entregue um pacote compacto de fatos sustentados, formulações permitidas e lacunas. Encaminhe para pesquisa-aprofundada apenas quando a questão exigir comparação extensa ou reconciliação adicional.

## Perguntas por lacunas
Qual afirmação precisa ser sustentada? Qual público e período ela pretende descrever? É necessária uma comparação ou basta explicar um conceito? Evite perguntar o que já consta na pauta.

## Contrato de saída
Perguntas respondidas; matriz afirmação → fonte → trecho/escopo → limite; links reais; leitura e acesso por fonte; contraprova; redação sugerida e fatos ainda não verificados.

## Erro crítico
Inventar citações, acesso a conteúdo pago ou resultados de ferramentas, ou usar snippets como leitura integral.

## Referências
- [RS01 — Pesquisa aprofundada: protocolo](../references/fontes/rs01.md): Usar rastreabilidade proporcional ao tamanho da pauta.
- [GV11 — Gary: aprendizado](../references/fontes/gv11.md): Consultar somente o que a ficha comprova sobre aprendizado.
- [EX04 — Handley: escrita útil](../references/fontes/ex04.md): Complementar a transformação da evidência em texto claro.

## Papel
[pesquisador](../agents/pesquisador.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
