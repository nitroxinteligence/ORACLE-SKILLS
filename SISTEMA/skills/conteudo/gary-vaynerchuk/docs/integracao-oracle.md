---
id: gv-docs-integracao-oracle
type: review
status: active
area: marca
created: '2026-09-16'
updated: '2026-09-16'
sensitivity: internal
sources: []
confidence: medium
review_after: '2026-12-16'
---
# Integração Oracle: bloqueios e critério de pronto


## Estado

A hierarquia solicitada foi preservada: `SISTEMA/skills/conteudo/gary-vaynerchuk/gary-<modulo>/SKILL.md`. Recursos ficam dentro do especialista. O manifesto deste pacote é documentação, não um mecanismo de ativação do aplicativo.

## Evidências

`packages/atlas/departments.js:59-75` e `Sources/Oracle/InstallationPresentation.swift:48-55` não reconhecem `conteudo` minúsculo como departamento. `MemorySyncScan.swift:60-72` preserva o caminho, sem normalização corretiva. O caso sintético vira coleção `conteudo` em `department/other`.

Mesmo `Conteúdo` reconhecido não resolve tudo: `packages/atlas/layout.js:99-110` chama agrupamento sem propagar a raiz física. O teste independente obteve uma skill catalogada, mas zero folhas no detalhamento do especialista. `Resources/web/app.js:114-117,192-196` também presume raiz plana em chamadores relacionados.

O manifesto vem do bundle (`Core.swift:62-74`), não de um arquivo arbitrário no vault. Frontmatter não corrige o parser por caminho. Descoberta visual, instalação no host, confiança e execução são estados distintos (`DistributionCodex.swift:45-65,119-140`; `Onboarding.swift:567-582`).

O worker de integração executou 36 testes existentes, aprovados, e sete cenários adicionais em memória que expuseram o problema. São testes de módulos reais com dados sintéticos; não demonstram a versão binária instalada ou a jornada visual do usuário. A working copy já tinha alterações de outras frentes. Relatório: `REVIEWS/pesquisa-conteudo-20260916/results/oracle-integration.json`.

## Correção proposta, não aplicada

Unificar reconhecimento de `conteudo` nos parsers; propagar raiz física em agrupamento, contagem, seleção e navegação; testar a hierarquia real com as 34 skills e recursos; verificar a interface da versão distribuída; depois validar descoberta e uma execução do host separadamente.

Não aplicar somente um alias e declarar tudo resolvido: restaria o defeito de navegação. Não renomear a pasta criada pelo usuário nem duplicar o especialista em outra raiz para ocultar o problema. Nenhum código ou configuração foi alterado nesta tarefa.

## Uso explícito

Um agente com acesso autorizado pode ler diretamente `gary-orquestracao/SKILL.md` e seguir as referências. Manter o especialista completo, pois os módulos usam recursos compartilhados. Isso não implica registro automático no host.

## Critério de pronto da integração

Demonstrar Conteúdo → Gary Vaynerchuk → 34 skills acessíveis, abertura de recursos, descoberta dos caminhos canônicos pelo host e execução que respeite perguntas/aprovações. Não inferir esses estados apenas da existência de arquivos.


[[SISTEMA/skills/conteudo/gary-vaynerchuk/indice|Índice do especialista]] · [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/indice|Referências]]
