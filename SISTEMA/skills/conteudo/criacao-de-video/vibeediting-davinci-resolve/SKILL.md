---
name: vibeediting-davinci-resolve
description: "Planeje e conduza edição por etapas no DaVinci Resolve, verificando edição, versão, projeto e interface disponível. Use para corte bruto, áudio, B-roll, legendas, cor e revisão por timecode com originais preservados."
metadata:
  departamento: conteudo
  especialista: criacao-de-video
  skill-id: CON-VID-03
  versao: "1.0.0"
---
# Vibe editing no DaVinci Resolve

## Entrada
Projeto/timeline autorizados, mídia identificada, copy ou fala a preservar, formato de entrega e versão/edição do Resolve. A integração nativa e o servidor comunitário são caminhos distintos, descritos no [guia](references/guia.md).

## Leitura necessária
Leia [operação segura](../references/operacao-segura.md) e [guia Resolve](references/guia.md), incluindo a diferença entre anúncio do fabricante e contrato técnico realmente disponível. Um pedido documental não autoriza instalação ou edição.

## Perguntas por lacunas
Qual edição/versão está instalada? Qual projeto e timeline podem ser modificados? Quais pausas ou ressalvas precisam permanecer? O objetivo é apenas corte bruto ou também acabamento? Qual padrão de exportação e destino foram aprovados? Reutilize o brief conhecido.

## Procedimento
1. Identifique Resolve, edição, versão e host sem alterar preferências. Confira a documentação do bundle quando houver acesso autorizado; a menção a AI assistant não fornece por si só endpoint, transporte ou schema MCP.
2. Descubra a interface realmente disponível. Para o caminho comunitário escolhido, confira proprietário, revisão e requisitos de scripting; respeite restrições de edição/licença. Não ative bridges alternativas, downgrade ou acesso de rede para contornar uma falha.
3. Faça primeiro uma consulta de leitura da sessão e do projeto autorizado. Confirme timeline ativa, taxa de quadros, início e mídia disponível. Sem resposta do aplicativo, registre conexão não verificada.
4. Com autorização de edição, prepare cópia versionada do projeto ou timeline e registre o ponto de recuperação. Verifique source in/out e destino antes de cortar; não use os timestamps de uma exportação antiga como posições atuais sem conversão.
5. Monte o corte bruto preservando finais de palavras, sincronismo e ressalvas. Trabalhe por trechos pequenos, mantendo handles de áudio/imagem e registrando a intenção de cada corte; leia de volta o estado após operações.
6. Revise o corte e aplique correções ancoradas em fala/cena e timecode. Depois da aprovação pertinente, adicione B-roll autorizado, legendas e música; trate cor e redução de ruído como ajustes a avaliar, não melhoria presumida.
7. Confira palavras, níveis, enquadramento, continuidade e efeitos no material efetivo. Registre o intervalo visto/escutado e peça revisão humana quando a ferramenta não der percepção audiovisual suficiente.
8. Entregue projeto/timeline e lista de revisão. Só prepare ou inicie exportação no escopo aprovado, usando [video-revisao-exportacao](../video-revisao-exportacao/SKILL.md); uma fila criada não comprova arquivo final.

## Erros e recuperação
Projeto incorreto exige parar antes de escrever. Mídia offline exige localizar o asset autorizado, sem substituir por outro de nome parecido. Falha de scripting exige diagnóstico de versão/edição/interface, sem bypass. Timeout após corte exige readback antes de repetir. Efeito ausente exige relatar incompatibilidade ou propor alternativa.

## Entregável
Plano ou projeto versionado conforme autorização, mapa de cortes com referencial de tempo, mídia utilizada, parâmetros confirmados, recibo da integração, revisão por trechos e estado separado da exportação.

## Critérios de aceite
Projeto/timeline corretos; origem preservada; ferramentas e capacidades comprovadas; fala e sincronismo revisados dentro de cobertura declarada; nenhum endpoint, melhoria visual ou render foi inventado. Ausência de teste real permanece nao_testado.
