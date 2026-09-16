---
id: gv-tests-validacao
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
# Validação da biblioteca no vault

Executar `python3 tests/validate_package.py` e `python3 -m unittest discover -s tests -p test_gates.py -v` a partir da pasta do especialista.

O primeiro verifica estrutura, metadados, contagens e existência dos links. O segundo verifica 27 cenários de aprovação, três entradas inválidas e dois casos de proteção do auxiliar puro. Não chama um modelo, não executa ferramentas e não publica.

`tests/resultado-validacao.json` registra a execução observada quando produzido. Uma aprovação estrutural não comprova comportamento do host. As limitações de descoberta e navegação do Oracle permanecem independentes e documentadas. O agente precisa ler e seguir as instruções; este auxiliar não foi integrado ao aplicativo.

A revisão de links não demonstra que cada fonte sustenta semanticamente toda a redação. A análise de autoria, nível de acesso e limitações está nas fichas. Os cenários de uso adicionais são propostas de ensaio, não resultados declarados.

[[SISTEMA/skills/conteudo/gary-vaynerchuk/indice|Índice do especialista]] · [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/indice|Referências]]
