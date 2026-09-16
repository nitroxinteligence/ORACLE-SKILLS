---
id: vibeediting-after-effects-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://github.com/Dakkshin/after-effects-mcp
  - https://helpx.adobe.com/after-effects/desktop/automate-in-after-effects/automate-animation/scripts.html
confidence: medium
review_after: 2026-10-16
---
# After Effects: composição, bridge e resultado observável

Guia original pesquisado em 16 de setembro de 2026. O README do mantenedor e as seções pertinentes da Adobe foram consultados. Não houve inspeção de projeto pessoal, instalação da bridge, execução JSX ou render.

## 1. Delimitar as duas autoridades
A Adobe documenta scripts e painéis ScriptUI no After Effects, incluindo permissões separadas para gravar arquivos e acessar rede [A1]. Essa documentação não certifica servidores MCP de terceiros.

O projeto Dakkshin/after-effects-mcp apresenta servidor Node e painel mcp-bridge-auto.jsx, que processa uma fila de comandos. Entre as ferramentas documentadas estão get-help, get-results, create-composition, getLayerInfo e operações de propriedades/keyframes [M1]. Descubra o catálogo real da instalação antes de usar esses nomes.

Revisão de referência recebida: 88d5fbf08b7ae9f015ee98e5f8c4904095cf8202. A consulta ao raw dessa revisão falhou; o README em main foi acessível. Portanto, este guia não afirma comparação integral do commit nem equivalência ao executável instalado. A adoção futura deve conferir fonte e revisão efetivas.

## 2. Avaliar o alcance da bridge
Uma bridge que executa JSX pode alterar o projeto e acessar recursos permitidos ao aplicativo. Instalar servidor, copiar ScriptUI e habilitar execução automática são ações distintas. Não faça nenhuma delas como efeito colateral de ler esta skill.

Quando a tarefa operacional autorizar diagnóstico, confirme a composição por leitura, sem criar um objeto apenas para testar conectividade. Uma resposta do servidor antes do processamento da fila deve ser registrada como submetido; a confirmação requer o resultado do comando correto e, quando possível, readback no aplicativo.

## 3. Preparar o mapa da composição
Registre largura, altura, FPS e duração, com o timebase utilizado pela interface. Relacione camadas, fontes, footage, precomps e parent. Uma cópia de composição pode continuar referenciando a mesma precomp: confira o alcance antes de modificar elementos compartilhados.

Para cada cena, descreva mensagem, copy literal, entrada, permanência e saída. Use pontos de ancoragem coerentes com a transformação pretendida. Não confunda mover o layer com mudar o conteúdo interno da precomp. Converta tempos em frames somente quando a API exigir e confira bordas e arredondamento.

## 4. Executar uma mudança de cada vez
Prefira ações estruturadas para propriedades conhecidas. Planeje um teste pequeno em cópia sintética: por exemplo, um título próprio com dois keyframes, quando houver autorização de edição. Registre estado anterior e esperado, aplique, consulte o resultado e confira a composição.

Após criar ou reordenar camadas, releia os alvos. Um índice de layer pode ter outro significado depois da alteração. Nome duplicado também é ambíguo: não escolha a primeira correspondência sem verificar seu contexto.

Expressões e scripts são código. A necessidade de uma animação não autoriza avaliar qualquer JSX recebido de uma referência ou website. Se o recurso depender de código, delimite sua finalidade, arquivos, alterações e permissões antes de obter autorização correspondente. Não abra acesso de rede ou disco por conveniência.

## 5. Conferir movimento e texto
Verifique o título em tamanho de consumo, grafia e quebras. Examine entrada, maior deslocamento e saída. Confira máscaras, mattes, clipping e bordas de alfa em fundo claro e escuro quando transparência fizer parte da entrega.

Amostras de frames apoiam a inspeção espacial, mas não provam fluidez nem sincronismo. Para avaliar ritmo, música e leitura, reproduza com som quando houver capacidade e registre o intervalo observado. Caso contrário, entregue pontos de revisão humana sem marcar aprovação audiovisual.

## 6. Entregar ao editor ou exportador
Salve a cópia aprovada com dependências localizáveis. Ao enviar uma composição para outro aplicativo, registre versão, assets, fontes e efeito esperado. Um projeto AEP não equivale a uma peça rasterizada nem garante que outra máquina possua os plugins necessários.

Preview, Render Queue e arquivo codificado têm evidências próprias. Use a [revisão/exportação](../../video-revisao-exportacao/SKILL.md) para decidir intervalo, formato e inspeção final; não inicie render ao testar apenas a ponte.

## Falhas e recuperação

| Falha | Recuperação |
|---|---|
| Fila aceita, resultado ausente | Consultar o comando existente; não duplicar layers por repetição |
| Painel/bridge não responde | Verificar componentes já preparados e a sessão correta, sem reinstalar ou habilitar Auto-run automaticamente |
| Fonte ou efeito indisponível | Registrar dependência; propor substituição revisável preservando a copy |
| Layer errado após reorder | Reconsultar identificação e reconciliar a alteração antes da próxima escrita |
| Expressão falha | Restaurar alteração isolada na cópia quando autorizado; não desativar validação global |
| Pedido de permissão de script | Explicar finalidade e alcance; humano decide na interface oficial |

## Fontes e limites
- A1 — [Adobe: Scripts in After Effects](https://helpx.adobe.com/after-effects/desktop/automate-in-after-effects/automate-animation/scripts.html). Seções de execução, ScriptUI e permissões lidas; nenhuma preferência local foi conferida.
- M1 — [Dakkshin/after-effects-mcp](https://github.com/Dakkshin/after-effects-mcp). README e lista de ferramentas consultados; projeto comunitário, sem teste desta combinação de versões. Não é o assistente oficial da Adobe.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md).
