---
id: "fv-uso-validacao"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: "2026-10-16"
---
# Uso, validação e limites

## Como iniciar
Abra a pasta deste especialista no Obsidian e leia a skill `fv-trafego-orquestracao/SKILL.md`. Num host com acesso autorizado ao vault, indique o caminho real desse arquivo e o resultado desejado. Exemplo: “Leia esta skill e comece pelo diagnóstico; ainda não instale nem conecte ferramentas”. Não presumir descoberta automática do host.

## Configuração é uma etapa separada
O arquivo `templates/mcp-proposta.toml` está desabilitado e não foi copiado para `~/.codex/config.toml`. Concluir a entrevista pode resultar numa proposta de conexão; o humano faz OAuth, MFA e concessão de permissões. URLs, executáveis e schemas precisam ser verificados no momento de uso.

## Testes locais
`python3 -m unittest discover -s tests -p test_gates.py -v` executa apenas cenários sintéticos do helper em `scripts/gates.py`, a partir desta pasta. Não abre aplicativos, não usa credenciais e não envia requisições. O helper usa um hash do plano como comparação de versão; ele não é assinatura digital nem prova de consentimento humano. O host não o chama automaticamente.

Para avaliar um plano pelo helper, crie um JSON sanitizado com `plan`, `approval`, `context` e opcional `now`, conforme as fixtures do teste. Execute `python3 scripts/gates.py arquivo.json`. Uma decisão `allowed` significa apenas que esses dados passaram por verificações locais; a autorização real e as proteções do host continuam obrigatórias.

## Validação real futura
Depois da escolha e autorização de instalação/conexão: verificar identidade do software e ferramentas, executar leitura mínima, confirmar conta/projeto, usar artefato sintético em operação delimitada e ler o resultado de volta. Só então usar a rota no trabalho real autorizado. Uma configuração bem formada ou teste unitário não substitui isso.

## Oracle e Codex
Esta tarefa não alterou app, catálogo distribuído, links globais de skills, confiança de hooks ou configuração pessoal. A localização em `SISTEMA/skills` é o acervo solicitado. Os bloqueios de descoberta/navegação registrados na rodada anterior precisam validação própria; não foi repetida a auditoria do binário instalado. Use leitura explícita do arquivo enquanto a integração do host não estiver comprovada.

## Manutenção
Rever versões, licenças, permissões e políticas quando forem relevantes a uma execução. Não há atualização automática criada. Mudanças no brief ou nos recursos reais podem invalidar um plano aprovado. O usuário mantém controle de instalação, acesso, alterações, custos, upload e publicação.

[Operação segura](../references/operacao-segura.md) · [Fontes](../references/fontes.md) · [Entrevista](../references/entrevista.md)
