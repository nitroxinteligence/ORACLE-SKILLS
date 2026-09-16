---
name: gary-revisao-final
description: "Revise uma entrega editorial contra o brief, as fontes, as versões aprovadas e os arquivos reais. Use antes da entrega final, distinguindo pronto para publicação de publicado."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-34
  versao: "1.0.0"
---
# Revisão final de conteúdo e visual

## Escopo e autoria
A revisão final é engenharia original. Handley complementa atenção à escrita; documentação técnica e fontes do conteúdo orientam verificações. Não é certificação, endosso ou método oficial de Gary.

## Entrada
Brief, copy, fontes, versão aprovada, arquivos visuais quando existentes, especificações do destino e resultados reais de verificações. Ausência de evidência deve permanecer visível.

## Leitura necessária
Leia [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) e [pesquisa-e-evidencia](../references/playbooks/pesquisa-e-evidencia.md) e [visual-e-referencias](../references/playbooks/visual-e-referencias.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Confronte a entrega com objetivo, público, promessa e escopo aprovados. Localize mudanças materiais e identifique qual aprovação precisa ser renovada, sem reiniciar contexto por mero ajuste tipográfico.
2. Verifique afirmações centrais, números, datas, citações e experiências pessoais contra fontes realmente lidas. Preserve ressalvas e autoria; não promova curadoria, marketing ou inferência a fato demonstrado.
3. Revise voz, clareza, progressão, conclusão e adequação à plataforma. Retire repetição, promessa sem entrega e linguagem de autoridade inventada.
4. Inspecione os arquivos visuais disponíveis, não apenas seus prompts: texto literal, dados, identidade, ordem, dimensões, recorte, transparência e acessibilidade pertinente. Sem arquivo ou ferramenta, marque o item como não verificado.
5. Confira versões e recibos de aprovação editorial/visual. Validação de YAML, links ou campos não comprova qualidade de conteúdo nem execução; revisão serial não é revisão independente.
6. Entregue decisão por item: aprovado para entrega, requer ajuste ou bloqueado por evidência. Liste correção objetiva, responsável documental e o que foi realmente verificado; pronto para publicação não significa publicado.

## Perguntas por lacunas
A versão final é a mesma que foi aprovada? Algum fato depende de fonte ausente? Há arquivo real para inspeção? Qual pendência impede considerar a peça pronta para entrega?

## Contrato de saída
Parecer por peça/versão, verificações realizadas, evidências, falhas com correção objetiva, aprovações válidas/pendentes e estado final. Nenhuma publicação, teste de plataforma ou revisão independente é inventado.

## Erro crítico
Aprovar um arquivo não inspecionado, confundir validação estrutural com verdade ou relatar publicado quando só existe rascunho.

## Referências
- [EX04 — Handley: escrita](../references/fontes/ex04.md): Complementar atenção à clareza sem atribuir a rubrica à autora.
- [RS01 — Pesquisa: validação](../references/fontes/rs01.md): Reforçar a diferença entre cobertura de campos e verdade.
- [OA05 — OpenAI: limites da geração](../references/fontes/oa05.md): Verificar saída real em vez de presumir fidelidade.
- [DV01 — W3C: alternativas textuais](../references/fontes/dv01.md): Revisar equivalente textual conforme a função da imagem.
- [DV02 — W3C: contraste](../references/fontes/dv02.md): Distinguir inspeção visual de medição objetiva.

## Papel
[revisor](../agents/revisor.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
