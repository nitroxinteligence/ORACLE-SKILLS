---
id: vibeediting-premiere-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://github.com/leancoderkavy/premiere-pro-mcp
  - https://developer.adobe.com/premiere-pro/uxp/
  - https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-video.html
confidence: medium
review_after: 2026-10-16
---
# Premiere: identidade da ponte e prova de edição

Consulta em 16 de setembro de 2026, sem instalar ou executar Premiere. O projeto comunitário consultado publica premiere-pro-mcp 1.16.0 e diferencia o catálogo publicado de alterações ainda em desenvolvimento [P1]. Não trate a quantidade de métodos em main como capacidade da instalação local.

## 1. Identificar exatamente o pacote
O README alerta que adobe-premiere-pro-mcp, de outro projeto, também pode declarar um executável chamado premiere-pro-mcp [P1]. Verifique package name, versão, caminho real e repository.url. Nome do processo não basta. Esta skill usa leancoderkavy/premiere-pro-mcp como referência, sem presumir endosso da Adobe.

Em tarefa futura de diagnóstico, consulte a versão local e o pacote já presente. Evite npx sem versão por conveniência: ele pode baixar/executar software e trocar a origem do comando. Instalação/atualização são ações independentes, com revisão de fonte e autorização.

## 2. Separar CEP, UXP e host
O projeto mantém CEP como ponte principal; UXP acrescenta capacidades condicionais sem substituí-la automaticamente [P1]. A Adobe documenta UXP e APIs próprias de Premiere [A1]; isso não certifica o MCP comunitário nem torna suas rotas intercambiáveis.

Descubra qual bridge está realmente conectada. Uma leitura da ferramenta deve apontar capacidades vigentes; o código pode ter rotas indisponíveis para a versão do usuário. Não instale um painel extra, altere permissões ou habilite execução de scripts para fazer uma opção experimental parecer pronta.

## 3. Diagnosticar em duas etapas
No fluxo documentado, premiere-pro-mcp --doctor avalia prontidão local; verify_premiere_connection verifica por leitura a conexão com a ponte, projeto e sequência [P1]. Use ambos somente quando o diagnóstico operacional estiver autorizado. Um diagnóstico pode listar ausência de componente sem alterar nada.

Registre resultados por camada: pacote identificado, painel disponível, transporte conectado, projeto aberto e sequência ativa. O painel dizer Running não informa que um corte foi realizado. O diagnóstico inicial deve evitar exposição desnecessária de nomes de mídia ou clientes.

## 4. Transformar o pedido em plano
Confirme o projeto e a sequência exatos antes de editar. Prepare uma cópia versionada e salve o ponto de recuperação. Declare tracks afetadas e diferenças entre inserir, sobrescrever e ripple. Não aplique cortes apenas por um índice que pode ter mudado com uma edição anterior.

Para cada operação, guarde alvo, posição de origem/destino, mudança pretendida e condição de reversão. Comece com uma alteração pequena e verificável; compare clipes, duração e posição após o retorno do servidor. Quando o projeto mudar fora da execução, releia o estado e reconcilie o plano.

## 5. Trabalhar sem escape genérico de script
Prefira ferramentas estruturadas, descobertas no servidor. Se um recurso não existir, descreva o limite e a alternativa; não envie scripts arbitrários como fallback automático. Mesmo quando uma rota genérica existe, ela exige revisão específica do código e autorização correspondente.

Os detalhes de autoria MOGRT, render em After Effects e intercâmbio não comprovam que AE está instalado ou conectado. Uma etapa entre aplicativos deve identificar a saída de um e a entrada do outro, com versão e mídia referenciada; não declarar handoff concluído por existir um arquivo de instrução.

## 6. Revisar e exportar
Readback comprova apenas os campos que retornaram. Para avaliar final de palavra, mixagem, cor e transição, use a mídia e uma revisão com cobertura explícita. Uma captura parada não demonstra áudio nem movimento.

A documentação Adobe distingue a configuração e a execução de exportação [A2]. Registre saída, formato e intervalo selecionado e encaminhe à [revisão/exportação](../../video-revisao-exportacao/SKILL.md). Salvar a sequência ou enviar um job ao encoder não equivale a exportar um arquivo conferido.

## Falhas e recuperação

| Resultado | Conduta |
|---|---|
| Executável existe, origem ambígua | Resolver o pacote antes de configurar cliente |
| Doctor passou, conexão falhou | Verificar painel, app/projeto e sequência; não anunciar conectado |
| UXP conectado sem método necessário | Marcar capacidade indisponível e consultar rota suportada |
| Mutação pode ter sido aplicada | Readback primeiro; preservar resultado incerto sem duplicar corte |
| Projeto alterado por outra pessoa | Reconciliar versão e alvos; não sobrescrever para restaurar o plano |
| Exportação falhou | Inspecionar job e saída parcial; corrigir causa antes de nova submissão |

## Teste futuro, sem alegação de execução
Usar uma sequência sintética autorizada com assets próprios. Conferir leitura, adicionar uma marca ou alteração pequena permitida, ler de volta, reverter quando apropriado e inspecionar o resultado. Registrar ambiente e ferramenta exercitados. A aprovação do teste não generaliza para todos os efeitos ou versões.

## Fontes e limites
- P1 — [leancoderkavy/premiere-pro-mcp](https://github.com/leancoderkavy/premiere-pro-mcp). Seções At a glance, Latest release, Quick Start e First proof lidas. É documentação do mantenedor, não execução em Premiere licenciado. A versão 1.16.0 é a publicação descrita na data consultada, não pin permanente.
- A1 — [Adobe: Premiere UXP API](https://developer.adobe.com/premiere-pro/uxp/). Visão geral oficial lida; documentação do fabricante separada do MCP.
- A2 — [Adobe: exportar vídeo](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-video.html). Página oficial consultada; parâmetros devem seguir o destino e a versão do projeto.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md).
