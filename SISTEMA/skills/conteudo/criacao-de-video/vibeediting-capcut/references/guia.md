---
id: vibeediting-capcut-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://www.capcut.com/tools/desktop-video-editor
  - https://github.com/GuanYixuan/pyCapCut
  - https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md
confidence: medium
review_after: 2026-10-16
---
# CapCut: draft compatível antes de vídeo final

Pesquisa em 16 de setembro de 2026. Este guia original não instala biblioteca, acessa drafts pessoais nem executa CapCut. A página oficial apresenta o produto Desktop [C1]; o contrato Python vem de um projeto comunitário [P1]. Não foi encontrado nesta revisão um contrato MCP oficial que substitua essa distinção.

## 1. Duas rotas com provas próprias
**GUI nativa.** Operar o editor pela interface exige versão compatível, ferramenta desktop disponível, app autorizado e alvo observado. A saída precisa ser verificada no próprio CapCut. Uma limitação do pyCapCut não prova limitação de toda a interface nativa.

**pyCapCut.** O README documenta uso em macOS/Linux para produzir drafts, com exportação no CapCut Windows [P1]. Isso não certifica exportação automatizada no Mac. Aceite entrega de draft ou verifique outra rota separada com o usuário. Não apresente um wrapper comunitário como integração oficial.

## 2. Preparar o template
A biblioteca aceita draft_content.json não encriptado como template [P1]. Antes de editar, confirme origem, versão e pasta de destino. Duplicar o projeto pode preservar estruturas que um novo draft não representaria; ainda assim, a cópia precisa abrir no editor. Não grave por cima de um projeto em uso nem edite arquivos concorrentes sem reconciliação.

Defina o que será alterado: texto, assets, segmentos ou tracks. Nome de arquivo não basta para identificar uma mídia: confira caminho autorizado, tamanho e, quando apropriado, hash. Se o asset não existe, mantenha a pendência; não reutilize outro arquivo do mesmo basename.

## 3. Mapear os tempos
O README descreve microssegundos e strings de tempo; trange recebe início e duração [P2]. Exemplo de interpretação: início de cinco segundos com duração de dois termina em sete segundos. Aplique essa distinção à origem e ao destino e mantenha a taxa de quadros da edição visível.

Calcule a duração esperada de cada track antes de salvar. Em mudança de velocidade, compare material consumido e duração de saída; em troca por mídia mais curta, decida se será encurtado o segmento ou se outra solução deve ser proposta. Não faça extensão ou ripple sem saber que elementos posteriores serão deslocados.

## 4. Construir tracks com intenção
Use nomes funcionais, como fala, apoio visual, trilha e legendas. Registre ordem de composição e vínculo entre imagem e som. Comece por um trecho representativo; compare a estrutura esperada com a abertura real no CapCut.

O projeto documenta restrições para editar tracks importadas e alerta sobre IDs preservados ao importar a mesma track repetidamente [P2]. Evite depender de manipulação manual de IDs para vencer uma limitação. Para uma capacidade ausente, proponha um draft menor, track nova suportada ou edição nativa revisada.

## 5. Revisar o que o JSON não comprova
Leia os textos e confira fontes, recursos, máscara, transição e alinhamento ao tempo. Um campo escrito pode ser ignorado por incompatibilidade. A prova visual vem do editor/render, não da mera presença da chave.

Ao revisar áudio, confirme se a ferramenta realmente permitiu ouvir. Uma transcrição pode apoiar o corte, mas não comprova que a música ficou equilibrada. Registre conferência humana quando for ela a fonte da avaliação.

## 6. Entregar e exportar
Entregue draft, mapa de mídias e requisitos do ambiente que o abre. Identifique exportação Windows do caminho pyCapCut ou exportação GUI nativa como operação separada, com parâmetros, versão, destino e status próprios. Encaminhe o arquivo resultante à [revisão/exportação](../../video-revisao-exportacao/SKILL.md).

Não altere preferências globais, não instale versões antigas e não descubra pasta pessoal de drafts por varredura ampla para executar um exemplo. Solicite o caminho do projeto quando ele não puder ser resolvido dentro do escopo.

## Falhas e recuperação

| Falha | Recuperação específica |
|---|---|
| Draft encriptado | Parar o caminho de template; solicitar material suportado ou escolher GUI nativa |
| Draft abre sem mídia | Conferir referências absolutas/relativas e mapa de assets, preservando o original |
| Texto some | Conferir fonte/recurso compatível e visualização no app, sem prometer que salvar JSON corrige |
| Cortes deslocados | Rever unidade, início/duração, velocidade e decisão de ripple |
| Track duplicada | Reconstituir em cópia a partir do template limpo; não duplicar IDs por tentativa |
| Exportação Mac solicitada via biblioteca | Registrar limitação documentada; validar rota GUI separadamente |

## Teste futuro de compatibilidade
Em cópia sintética autorizada, usar dois assets próprios, uma faixa de áudio e uma legenda com acentos; gerar o draft, abri-lo, conferir tempos e a posição do texto. Se exportação estiver autorizada no sistema apropriado, verificar o vídeo em separado. Reportar somente as funções exercitadas.

## Fontes e limites
- C1 — [CapCut Desktop](https://www.capcut.com/tools/desktop-video-editor). Página do fabricante consultada; não demonstra MCP nem instalação local.
- P1 — [GuanYixuan/pyCapCut](https://github.com/GuanYixuan/pyCapCut). Seções de compatibilidade, templates e exportação lidas. Projeto comunitário em desenvolvimento; README não é homologação do app instalado.
- P2 — [README em inglês do pyCapCut](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md). Seções pertinentes de tempo/tracks e template consultadas. As duas versões do README pertencem ao mesmo projeto, não são confirmação independente.

[Voltar à skill](../SKILL.md) · [Computer use](../../vibeediting-computer-use/SKILL.md) · [Operação segura](../../references/operacao-segura.md).
