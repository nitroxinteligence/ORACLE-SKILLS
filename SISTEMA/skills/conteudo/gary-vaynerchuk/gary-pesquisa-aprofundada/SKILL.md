---
name: gary-pesquisa-aprofundada
description: "Investigue questões editoriais complexas com subperguntas, campos, evidências primárias, contraprova e registro de incertezas. Use quando uma pesquisa de pauta não resolve a decisão."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-08
  versao: "1.0.0"
---
# Pesquisa aprofundada para conteúdo

## Escopo e autoria
O protocolo combina a estrutura research-deep com engenharia original de evidência e revisão. Gary oferece contexto de conteúdo; nenhuma etapa de pesquisa ou validação é apresentada como método oficial dele.

## Entrada
Pergunta principal, decisão que depende da resposta, mercado/período, fontes existentes, limites de acesso e profundidade solicitada.

## Leitura necessária
Leia [pesquisa-e-evidencia](../references/playbooks/pesquisa-e-evidencia.md) e [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Decomponha a pergunta em subperguntas cuja resposta possa mudar a decisão. Defina outline, campos de saída e critérios de encerramento antes de colecionar fontes.
2. Leia a skill research-deep disponível no ambiente antes de usar seu fluxo. Localize ferramentas reais; frentes descritas em documentos não são agentes ativos, e passagens seriais devem ser identificadas como tais.
3. Pesquise cada subpergunta com consultas sem dados privados. Priorize originais, documentação e estudos; use apenas domínios oficiais para OpenAI e não contorne paywalls ou bloqueios.
4. Registre para cada fonte URL/caminho, autoria, datas, trecho, extensão lida e falhas. Diferencie entrevista vista, notas do entrevistador, catálogo de curso e conteúdo pago efetivamente acessado.
5. Construa uma matriz de alegações e procure contraprovas capazes de alterar a conclusão. Reconcilie divergências de período, definição e população; preserve incertezas residuais.
6. Entregue JSON nos campos definidos, marcando valores incertos e mantendo uma lista uncertain. Execute um validador disponível com caminho real e resultado registrado; cobertura de campos não comprova verdade.
7. Revise os argumentos centrais contra as fontes e derive implicações editoriais separadas dos achados. Encerre com cobertura, lacunas e fatos que não podem entrar na copy, sem anunciar pesquisa exaustiva da internet.

## Perguntas por lacunas
Qual decisão mudará com a resposta? Quais comparações são essenciais? Há fontes ou períodos obrigatórios? Uma lacuna ainda exige aprofundar ou já permite uma conclusão qualificada?

## Contrato de saída
Outline, síntese, matriz de evidência/contraprova, registro de fontes e acesso, JSON com incertezas, resultado real de validação e recomendações identificadas como derivadas.

## Erro crítico
Usar um JSON válido como prova factual, inventar frentes executadas ou afirmar acesso integral a materiais apenas indexados.

## Referências
- [RS01 — Research-deep: estrutura](../references/fontes/rs01.md): Consultar origem do fluxo e limites do validador.
- [GV16 — Gary em evento: relato](../references/fontes/gv16.md): Exemplo de separar o que o autor defendeu de eficácia comprovada.
- [EX01 — MrBeast: notas de entrevista](../references/fontes/ex01.md): Exemplo de delimitar notas lidas versus vídeo integral.
- [GV08 — Gary: catálogo de livros](../references/fontes/gv08.md): Exemplo de bibliografia que não equivale à leitura das obras.

## Papel
[pesquisador](../agents/pesquisador.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
