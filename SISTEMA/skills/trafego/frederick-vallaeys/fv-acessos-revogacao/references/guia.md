---
id: "fv-acessos-revogacao-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://learn.chatgpt.com/docs/extend/mcp?surface=cli", "https://support.google.com/adspolicy/answer/6169371?hl=en", "https://pypi.org/project/meta-ads/", "https://github.com/googleads/google-ads-mcp"]
confidence: "medium"
review_after: "2026-10-16"
---
# Acessos, manutenção e revogação — guia

## Três desligamentos diferentes
Desabilitar o servidor no host interrompe seu uso por aquele host. Revogar no provedor invalida acesso conforme seu contrato. Pausar a campanha modifica a entrega de anúncios. Não confundir essas operações: parar a IA não necessariamente para os anúncios já ativos.

## Procedimento não destrutivo
Leia somente a configuração necessária, omita segredos do relatório, confirme o bloco e guarde uma recuperação segura quando autorizado. Preferir `enabled=false` ao apagar configurações inteiras. O humano conclui revogação no portal; não pedir que envie screenshot contendo token.

## Credencial exposta
Pare o fluxo e oriente revogação/rotação pelo titular. Não reproduza a credencial em diagnóstico, nota, issue ou mensagem. Não validar o vazamento chamando APIs com ela. A limpeza de históricos ou backups é uma tarefa separada com impacto que precisa ser explicitado; não apagar arquivos em massa.

## Atualização futura
Revalidar repositório, release, licença, alterações de schema e compatibilidade antes de atualizar. Repetir teste somente leitura e um cenário controlado antes de uso real. Não usar tag main como garantia de estabilidade nem versionar segredos junto com a mudança. Integrações de terceiro precisam revisão de termos/arquitetura, não só update de pacote.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [Repositório oficial Google Ads MCP](https://github.com/googleads/google-ads-mcp)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
