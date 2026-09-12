---
id: "pb-00-sistema-skills-readme"
type: "index"
status: "active"
area: "sistema"
created: "2026-09-05"
updated: "2026-09-07"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: null
---
<!-- Modified for Oracle distribution; exact input/output digests and reasons are in the signed distribution manifest. -->
# Biblioteca de skills do OS

> Registro da instalação de origem: os caminhos `{SOURCE_HOME}` são referências históricas, não destinos configurados neste computador. Dependências e integrações citadas precisam de configuração própria.


Índice das coleções de procedimentos mantidas em `SISTEMA/skills`.

| Coleção | Skills instaladas | Arquivos de origem verificados | Pasta no OS |
|---|---:|---:|---|
| Cybersecurity | 818 | 4532 | [[SISTEMA/skills/cyber-security/README|cyber-security]] |
| Marketing Skills | 50 | 466 | [[SISTEMA/skills/marketing/README|marketing]] |
| Claude Ads | 34 | 339 | [[SISTEMA/skills/ads/README|ads]] |
| Gentle-AI | 37 | 2201 | [[SISTEMA/skills/code/README|code]] |
| First Customer Finder | 1 | 10 | [[SISTEMA/skills/customer-finder/README|customer-finder]] |

- [[SISTEMA/skills/catalogo|Catálogo completo: todas as 940 skills instaladas e referências anteriores]]
- [[SISTEMA/skills/personal-branding/README|Personal branding: biblioteca existente]]
- Especialistas (recurso externo: WIKI/especialistas/README; não incluído nesta distribuição)

## Como usar

No Codex, solicite a skill pelo nome registrado no catálogo. As novas skills ficam disponíveis no próximo turno. Cada skill inclui os arquivos auxiliares fornecidos pela origem. Os cinco repositórios completos também estão em `{SOURCE_HOME}/.codex/skill-sources/`.

No OS, cada pasta de coleção mantém todos os arquivos versionados do repositório, incluindo scripts, referências, documentação e licença. `INSTALACAO-CODEX.json` registra o commit instalado, os nomes no Codex e hashes SHA-256. Os 7.548 arquivos de origem foram comparados nos dois destinos.

## Nomes e dependências

Nomes já usados foram preservados. As novas variantes usam prefixos `marketing-` ou `gentle-`, conforme a relação completa no catálogo. As 37 entradas do Gentle-AI incluem oito variantes repetidas entre as pastas de desenvolvimento e distribuição, mantidas separadamente.

As cópias de origem no OS são íntegras; adaptações de caminhos e metadados ficam no Codex. Não edite as duas versões sem registrar a alteração. Atualizações futuras devem repetir a comparação de arquivos e atualizar o catálogo.

Credenciais, contas de anúncios, serviços externos e ferramentas especializadas exigidas por um procedimento continuam sendo dependências de uso. O configurador completo Gentle-AI não foi aplicado: este trabalho instala suas skills, sem alterar memória, persona ou configurações globais.

SISTEMA/INDEX (recurso externo: SISTEMA/INDEX; não incluído nesta distribuição)

## Dependências locais instaladas

- Claude Ads: ambiente Python 3.12 isolado em `{SOURCE_HOME}/.codex/skills/ads/.venv`, com dependências fixadas por hash e `pip check` aprovado.
- PDF: Pango instalado e geração real de PDF com WeasyPrint verificada.
- Gentle-AI: executável compilado do mesmo commit e instalado em `{SOURCE_HOME}/.local/bin/gentle-ai`; comando de versão verificado. O configurador global não foi executado.
- Navegador: Chromium, Headless Shell e FFmpeg do Playwright instalados; abertura do Chromium e página local verificadas.
