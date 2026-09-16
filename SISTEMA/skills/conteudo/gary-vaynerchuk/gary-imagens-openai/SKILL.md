---
name: gary-imagens-openai
description: "Execute geração ou edição de imagem com a ferramenta OpenAI realmente disponível, após aprovação editorial e visual, verificando alvo, referências e saída. Não prometa seleção de modelo não exposta."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-31
  versao: "1.0.0"
---
# Geração e edição de imagens OpenAI

## Escopo e autoria
Este fluxo de produção e QA é engenharia original com documentação OpenAI. Gary não é autor de um método de imagens ou da operação da ferramenta; anúncio de produto não comprova disponibilidade na sessão.

## Entrada
Copy/brief aprovado, direção visual aprovada, destino, texto literal, referências autorizadas e alvo real quando houver edição. Reutilize aprovações válidas da mesma versão sem pedi-las novamente.

## Leitura necessária
Leia [visual-e-referencias](../references/playbooks/visual-e-referencias.md) e [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) e [pesquisa-e-evidencia](../references/playbooks/pesquisa-e-evidencia.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Verifique as aprovações de mensagem/copy e direção visual e a autorização de produzir a peça. Para imagem sem texto, use o brief aprovado como referência editorial.
2. Inspecione ferramentas e schemas disponíveis; leia a skill local imagegen quando estiver acessível. No schema image_gen observado em 2026-09-16 não existe seletor para modelo 2.5: não declare uso de Flare, Sunburst ou outra versão sem evidência.
3. Classifique geração ou edição e confira cada entrada. Edição exige imagem-alvo utilizável no contexto; nome, ID opaco ou alegação de imagem anterior não bastam. Para representar o usuário sem foto dele nesta conversa, solicite a imagem antes de gerar.
4. Prepare instruções de finalidade, cena, composição, texto literal, papéis das referências e invariantes. Envie apenas campos aceitos pelo schema real; uma especificação de prompt não é um conjunto de parâmetros de API.
5. Use a ferramenta integrada quando disponível e autorizada. Sem ferramenta, registre não executado e entregue o brief; não substitua silenciosamente por API paga, instalação de dependências ou outro modelo. Siga as instruções de interação e apresentação da ferramenta.
6. Inspecione cada saída disponível: texto, números, identidade, produto, composição, recorte e transparência quando pedida. Registre o que foi verificado, reprovado ou continua desconhecido, sem prometer fidelidade perfeita.
7. Faça alterações pontuais preservando invariantes e versões, dentro do esforço autorizado. Confirme o arquivo real antes de registrar caminho ou entrega; transferência bloqueada permanece bloqueada, sem contorno. Geração não equivale à aprovação final nem à publicação.

## Perguntas por lacunas
Qual é o alvo real de edição? Qual referência representa estilo e qual representa identidade? Que texto precisa ser literal? Qual erro invalidaria a peça? Pergunte somente lacunas que bloqueiam a produção.

## Contrato de saída
Imagem efetivamente gerada/editada quando houver ferramenta e autorização; referência real do arquivo, modo usado, modelo exposto ou não exposto, versão, verificações e pendências. Sem execução, entregue somente brief e estado não executado.

## Erro crítico
Gerar edição sem alvo, afirmar modelo 2.5 sem seletor/evidência, inventar arquivo concluído ou transferir a produção para API paga sem escolha explícita.

## Referências
- [OA01 — OpenAI: anúncio Images 2.5](../references/fontes/oa01.md): Distinguir anúncio público de recurso disponível na sessão.
- [OA02 — OpenAI: prompting](../references/fontes/oa02.md): Consultar seções pertinentes de instrução e preservação.
- [OA05 — OpenAI: geração e edição](../references/fontes/oa05.md): Verificar diferenças de interfaces e limites do contrato atual.
- [OA06 — OpenAI: cookbook](../references/fontes/oa06.md): Aplicar princípios de texto literal e iteração, sem confundir versões.
- [OA07 — OpenAI: Images no ChatGPT](../references/fontes/oa07.md): Consultar experiência do produto sem presumir acesso específico da conta.

## Papel
[operador-imagem](../agents/operador-imagem.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
