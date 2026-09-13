---
id: "pb-00-sistema-skills-personal-branding-etl-e-manutencao"
type: "playbook"
status: "active"
area: "marca"
created: "2026-09-05"
updated: "2026-09-05"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: null
---
<!-- Modified for Oracle distribution; exact input/output digests and reasons are in the signed distribution manifest. -->
# ETL e manutenção do acervo

## Extração realizada

19 URLs de artigos/episódios e uma entrevista no YouTube. Páginas extraídas com Exa/HTTP; legendas com yt-dlp. Capturas repetidas da mesma URL foram deduplicadas. O material de trabalho fica fora do acervo editorial. As fontes duráveis preservam URL, autoria, cobertura, síntese curta e hashes.

## Transformação realizada

Foram removidas repetições de legendas rolantes na representação normalizada. Navegação, CTAs e placeholders não viraram conhecimento. A inspeção distinguiu notas de episódios de transcrições, detectou conflito de identificação em RV16 e separou coautoria de AJ e influências citadas. Não houve validação integral de ASR contra áudio. A extração de conhecimento é curadoria, não fine-tuning nem RAG vetorial.

## Carga realizada

20 notas de fonte, seis modelos, 21 Q&As, dois playbooks, perfil e lacunas. A skill recupera por índice e tema, abre fonte e registra o que aplicou. O manifesto em `etl/manifest.json` permite verificar cobertura e integridade; o hash `sha256` de cada fonte usa o corpo após H1, incluindo a quebra final.

## Atualizar depois

Capturar uma nova fonte com ID novo; não sobrescrever o corpo de uma fonte preservada. Comparar com modelos existentes, registrar divergências e atualizar apenas as sínteses afetadas. Incrementar a versão do acervo e verificar Q&A, links e consulta. Abrir a fonte original quando a pergunta exigir detalhe não preservado; sem acesso, declarar lacuna. Nenhuma rotina recorrente foi agendada.

SISTEMA/recursos-skills/perfis/rory-vaden/fontes/README (recurso externo: SISTEMA/recursos-skills/perfis/rory-vaden/fontes/README; não incluído nesta distribuição) · como-adicionar-especialista (recurso externo: como-adicionar-especialista; não incluído nesta distribuição)
