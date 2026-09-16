---
name: video-revisao-exportacao
description: "Revise uma versão de vídeo e confira sua exportação por conteúdo, imagem, áudio, legendas, metadados e arquivo real. Registre cobertura observada, aprovação da versão e resultado de render sem confundir projeto, preview ou job com entrega final."
metadata:
  departamento: conteudo
  especialista: criacao-de-video
  skill-id: CON-VID-10
  versao: "1.0.0"
---
# Revisão e exportação de vídeo

## Entrada
Projeto/versão ou arquivo a revisar, copy aprovada, especificação do destino, assets, observações anteriores e escopo de autorização para exportar. Se houver job remoto, receba seu identificador existente; não inicie outro para localizar o resultado.

## Leitura necessária
Leia [operação segura](../references/operacao-segura.md) e [guia de verificação](references/guia.md). As regras de formato e aceitação vêm do destino real, não de números universais de resolução, bitrate ou loudness.

## Perguntas por lacunas
Qual versão está sendo aprovada? Qual arquivo/projeto é a origem? Quais formatos e idiomas são necessários? O render está autorizado e dentro do orçamento? Quem verificará áudio e vídeo quando a ferramenta não oferecer percepção integral? Reutilize as decisões do brief.

## Procedimento
1. Fixe a versão a revisar e relacione-a à copy, timeline/composição, materiais e alterações anteriores. Confirme o arquivo/projeto real; não derive um caminho de nome de anexo ou de uma resposta incompleta.
2. Faça a conferência editorial de nomes, números, ressalvas, CTA, direitos informados e consistência da narrativa. Alteração material de texto ou promessa volta à aprovação correspondente antes de finalizar o visual.
3. Revise cortes, palavras, B-roll, enquadramento, cor e transições. Registre intervalos, frames e modo de inspeção; não diga que assistiu ao vídeo inteiro quando só houve amostragem.
4. Confira áudio, sincronismo e legendas dentro da capacidade real. Separe leitura de transcrição, inspeção técnica e escuta; solicite revisão humana para dimensões não percebidas e mantenha-as pendentes.
5. Confronte especificação de saída com container, codec, proporção, resolução, FPS, duração, canais, legendas e tratamento de cor. Use ferramentas de inspeção já disponíveis sem instalar dependências ou reencodar por conveniência.
6. Se a exportação estiver autorizada, confirme intervalo, destino novo, versão e custo aplicável; submeta somente o job necessário. Registre seu ID e acompanhe a operação existente; timeout não autoriza duplicá-la.
7. Após conclusão informada, verifique existência e integridade prática do arquivo recebido, parâmetros e reprodução dentro da cobertura possível. Uma URL, preview ou estado completed não substitui essa conferência dos bytes finais.
8. Entregue projeto/arquivo verificados, especificações observadas, lista de problemas resolvidos/pendentes, cobertura e aprovação vinculada à versão. Use pronto-para-revisao ou pronto-para-publicacao conforme evidência, sem realizar publicação.

## Erros e recuperação
Arquivo ausente: recupere o job existente ou peça a origem correta. Export truncado: preserve diagnóstico e gere nova versão somente após resolver a causa e confirmar autorização. FPS/cor inesperados: compare projeto e preset antes de corrigir. Legenda divergente: revise copy e sincronismo. Sem áudio acessível: não marque mixagem aprovada.

## Entregável
Relatório de revisão por versão com problema, local, correção, evidência e estado; parâmetros efetivamente medidos; arquivo confirmado e origem; cobertura audiovisual e pendências humanas; status separado de exportação e publicação.

## Critérios de aceite
Versão e destino corretos; copy fiel; requisitos técnicos satisfeitos ou desvios explícitos; arquivo existente; metadados e reprodução avaliados proporcionalmente; origem preservada. Uma checagem estrutural ou hash não certifica qualidade estética, áudio ou direitos.
