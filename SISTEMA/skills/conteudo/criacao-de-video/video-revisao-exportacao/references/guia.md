---
id: video-revisao-exportacao-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://ffmpeg.org/ffprobe.html
  - https://www.w3.org/WAI/media/av/captions/
  - https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-video.html
confidence: medium
review_after: 2026-10-16
---
# Critérios para considerar um vídeo entregue

Guia original com fontes técnicas consultadas em 16 de setembro de 2026. Nenhum vídeo real foi renderizado, ouvido ou submetido a ffprobe nesta autoria. Os testes indicados abaixo são procedimentos para uma tarefa operacional futura autorizada.

## 1. Congelar a versão de revisão
Associe a revisão à versão do projeto e da copy. Anote como o arquivo final foi produzido e a que operação pertence. Um timestamp sem versão é ambíguo depois de alterações de duração; acrescente cena/fala âncora e indique se o tempo é de origem, timeline ou exportação.

Conferir o nome do arquivo não basta quando existe versão anterior no destino. Use caminho confirmado, tamanho, data e, quando útil, hash. O hash identifica bytes; não comprova que o vídeo comunica corretamente nem que todas as dependências são reproduzíveis.

## 2. Revisar a mensagem
Compare nomes, números, telas e CTA com fontes e copy aprovadas. Preserve ressalvas que mudam a interpretação de uma fala. Verifique se o hook é respondido e se uma montagem criou uma associação inexistente.

Registre o uso autorizado de música, pessoas, imagens e marcas no projeto. Não transforme metadados do arquivo em certificado de direitos. Se a aprovação de texto pertence a outra versão, encaminhe apenas a diferença material para decisão.

## 3. Definir a cobertura da inspeção

| Dimensão | Evidência útil | Limite a relatar |
|---|---|---|
| Copy e números | Comparação com roteiro e fontes | Não comprova áudio final |
| Layout | Frames e tamanho de consumo | Não comprova movimento contínuo |
| Cortes/transições | Reprodução dos intervalos e bordas | Amostra não representa toda a duração |
| Voz/trilha | Escuta dos trechos e medição pertinente | Transcrição não comprova mixagem |
| Sincronismo | Som e imagem percebidos juntos | Metadados isolados são insuficientes |
| Arquivo técnico | Probe e abertura em player compatível | Metadados não certificam qualidade estética |

Registre o intervalo e quem fez a avaliação. Uma revisão humana relatada é evidência do humano, não ação do agente. Se uma dimensão não foi observada, mantenha revisao_pendente em vez de preenchê-la como aprovada.

## 4. Verificar imagem, áudio e legenda
Examine começo e fim, cortes alterados, títulos, nomes, frames de transição e limites do enquadramento. Confira se resize ou rotação cortou informação. Analise cor em relação ao contrato do projeto: tags de SDR/HDR, espaço de cor e aparência são verificações relacionadas, não idênticas.

No áudio, verifique inteligibilidade, clipping, mudanças de nível, sincronismo e competição da trilha. Não imponha um único alvo de loudness a todos os destinos; registre o padrão realmente exigido e o método de medição disponível.

Legendas acessíveis podem precisar representar falante e sons relevantes, além de diálogo [W1]. Confira texto literal, timing e tempo de leitura. Diferencie legenda queimada, track selecionável e arquivo auxiliar: cada formato deve ser conferido no destino contratado.

## 5. Inspecionar metadados sem alterar mídia
ffprobe documenta seleção de informações com show_entries e saída estruturada JSON [F1]. Quando a ferramenta já existir e a leitura do arquivo estiver autorizada, use o caminho realmente confirmado. O exemplo é somente ilustrativo; não foi executado nesta autoria:

~~~sh
ffprobe -v error -show_entries format=duration,size:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels -of json 'output/final.mp4'
~~~

O comando lê informações; não garante decodificação integral ou ausência de defeitos. Confira também dados de rotação, cor, legendas ou outros streams quando exigidos pelo destino. Ausência de um campo não equivale a zero. Preserve valores racionais de FPS e investigue diferenças entre taxa nominal/média antes de alterar a edição.

Não instale ffmpeg/ffprobe apenas para satisfazer esta etapa. Se estiver ausente, use inspeção já disponível ou registre a checagem técnica pendente. Uma exportação não deve ser refeita apenas para produzir um campo de relatório.

## 6. Autorizar e verificar exportação
Defina projeto, sequência/composição, intervalo, formato, destino novo e versão. A documentação Adobe explica o fluxo de exportar vídeo a partir da sequência [A1]; outros editores têm controles próprios que precisam ser conferidos. Salvar preset, colocar na fila e terminar o render são estados diferentes.

Quando o serviço cobra por render, verifique aprovação de conta, custo e quantidade antes de submeter. Se o pedido for somente revisão de arquivo existente, não é necessário renderizar novamente. Se houver timeout, recupere a operação antes de repetir.

Após conclusão, confirme que o arquivo foi realmente recebido no caminho informado. Compare duração, streams e tamanho com a expectativa e abra em player compatível. Reproduza o que a ferramenta permitir e solicite revisão humana para a cobertura restante. Um arquivo não vazio pode estar truncado ou conter a versão errada.

## 7. Registrar correções sem perder rastreabilidade
Cada item de revisão deve ter versão, local, problema, impacto, correção proposta, resultado e evidência. Ao alterar algo, preserve o artefato anterior e volte a revisar a região afetada e suas bordas. Quando houver mudança global, como FPS ou escala de saída, a revisão precisa cobrir as consequências globais.

Não reexecute toda a produção para corrigir uma legenda antes de avaliar a composição/projeto editável. Em serviços com cobrança, confira o plano de nova execução e a autorização aplicável.

## Falhas e recuperação

| Falha | Verificação antes de agir |
|---|---|
| Job completed, arquivo ausente | Origem do job, output correto e transferência confirmada |
| Vídeo truncado | Estado do render, tamanho/duração e leitura do arquivo; preservar evidência |
| Formato/FPS errado | Projeto, preset e intervalo selecionados; não arredondar valores silenciosamente |
| Cor muda no player | Metadados, gerenciamento de cor e ambiente de visualização |
| Áudio não percebido | Revisão humana ou ferramenta adequada; nunca marcar ouvido por inferência |
| Legenda cobre elemento essencial | Corrigir layout na versão editável e revisar enquadramento final |

## Contrato de entrega
Informe arquivo confirmado, versão, parâmetros observados, relação com o projeto, fontes/direitos informados, aprovação aplicável e cobertura da revisão. Registre pendências sem escondê-las sob pronto. Pronto para publicação é um estado documental; esta biblioteca nunca autopublica.

## Fontes e limites
- F1 — [FFmpeg: ffprobe](https://ffmpeg.org/ffprobe.html). Seções de inspeção, show_entries e formato JSON consultadas. Não houve medição de mídia nesta execução.
- W1 — [W3C WAI: Captions/Subtitles](https://www.w3.org/WAI/media/av/captions/). Orientação de conteúdo das legendas lida; não certifica um arquivo sem avaliação.
- A1 — [Adobe: exportar vídeo](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-video.html). Página do fluxo de exportação consultada; não valida automaticamente parâmetros de Resolve, CapCut, AE, Motion ou Hypit.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md) · [Orquestração](../../video-orquestracao/SKILL.md).
