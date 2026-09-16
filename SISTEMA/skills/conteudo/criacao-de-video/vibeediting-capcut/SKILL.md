---
name: vibeediting-capcut
description: "Planeje edição no CapCut e criação de drafts com pyCapCut, verificando formato, compatibilidade, unidades de tempo e exportador. Diferencie operação nativa, draft gerado e vídeo exportado, especialmente no macOS."
metadata:
  departamento: conteudo
  especialista: criacao-de-video
  skill-id: CON-VID-04
  versao: "1.0.0"
---
# Vibe editing no CapCut

## Entrada
Brief, versão/sistema do CapCut, projeto ou draft autorizado, mídias, roteiro e destino final. Informe se o objetivo é operar a interface, gerar um novo draft ou exportar uma versão existente.

## Leitura necessária
Leia [operação segura](../references/operacao-segura.md) e [guia CapCut](references/guia.md). pyCapCut é uma biblioteca comunitária, não um MCP oficial do CapCut. Seu caminho documentado gera drafts em macOS/Linux e exporta no CapCut Windows.

## Perguntas por lacunas
O draft é legível e não encriptado? Qual versão do CapCut o criou? Há exportação Windows disponível para o caminho pyCapCut, ou o pedido é pela GUI nativa? Quais assets e textos podem mudar? Qual saída deve existir? Não repita escolhas do brief.

## Procedimento
1. Identifique aplicativo, versão, sistema e mecanismo escolhido. Registre a diferença entre CapCut Desktop disponível, biblioteca Python instalada, draft compatível e exportação verificada.
2. Para operação nativa, descubra a ferramenta real e confirme a janela/projeto; encaminhe inspeção visual ao [computer use](../vibeediting-computer-use/SKILL.md). Para pyCapCut, confira pacote/revisão e requisitos documentados sem instalar incidentalmente.
3. Verifique o draft e os assets apenas no escopo autorizado. Trabalhe em cópia nova e identificada; aceite templates não encriptados suportados. Diante de encriptação ou formato incompatível, pare essa rota sem tentar decifrar ou rebaixar o aplicativo.
4. Monte uma tabela de origem, início, duração, destino e trilha. No pyCapCut, confira a unidade de tempo e lembre que o segundo argumento de trange representa duração, não tempo final; valide limites da mídia antes de gerar o draft.
5. Construa primeiro o corte bruto com tracks nomeadas. Preserve IDs quando exigido pelo template e evite importar a mesma track duas vezes para o mesmo draft. Trate alterações de duração e movimento de clipes posteriores como decisões explícitas.
6. Acrescente texto, legendas, trilha e efeitos em lotes curtos. Verifique recursos realmente disponíveis na versão do editor; não presuma que assets de template, fontes ou efeitos são portáveis ou licenciados.
7. Quando edição/teste estiverem autorizados, abra a cópia no CapCut apropriado e confira clipes, texto, som e transições. Um JSON gerado sem abertura no editor fica draft_gerado, não projeto validado visualmente.
8. Entregue o draft e relatório de compatibilidade. Exportação por pyCapCut no Mac permanece não comprovada; uma exportação pela GUI nativa é outra rota que exige teste próprio e [revisão final](../video-revisao-exportacao/SKILL.md).

## Erros e recuperação
Draft rejeitado: preserve a cópia e registre versão/formato. Mídia ausente: solicite o asset exato. Duração errada: reconcilie unidade e source range. Efeito perdido: revise suporte antes de refazer tudo. Exportação interrompida: confira job/arquivo existente antes de repetir. Não prometa exportMac por haver import Python bem-sucedido.

## Entregável
Plano ou novo draft conforme escopo, mapa de assets e trilhas, tempos verificados, incompatibilidades, estado de abertura no editor e rota de exportação escolhida. Arquivo final só é declarado depois de existir e ser inspecionado.

## Critérios de aceite
Original preservado; rota técnica identificada; draft legível no formato suportado; referências de mídia válidas; cortes e texto conferidos; exportação separada por sistema e ferramenta; nenhum MCP oficial ou compatibilidade não demonstrada foi inventado.
