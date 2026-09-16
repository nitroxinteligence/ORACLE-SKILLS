---
id: "fv-conector-terceiros-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://github.com/amekala/ads-mcp", "https://support.google.com/adspolicy/answer/6169371?hl=en", "https://learn.chatgpt.com/docs/extend/mcp?surface=cli"]
confidence: "medium"
review_after: "2026-10-16"
---
# Conectores de tráfego — avaliação e conexão opcional — guia

## Candidato identificado: Adspirer
O repositório `amekala/ads-mcp` documenta um serviço remoto em `https://mcp.adspirer.com/mcp` com OAuth 2.1/PKCE e gestão de anúncios. O repositório distribui plugins e instruções; sua licença MIT não demonstra que todo o backend hospedado esteja disponível para auto-hospedagem. Funcionalidade e segurança descritas são declarações do fornecedor, não testes deste pacote.

## Condição importante para Google
A política Google Ads Developer Policies consultada trata explicitamente de proxies, MCPs e wrappers e exige acesso verificável com projeto/acesso da entidade, com possibilidade de revisão de interfaces secundárias. Não concluímos a conformidade de Adspirer nem de qualquer concorrente. Antes de conectar Google via terceiro, obtenha documentação do fluxo que se aplica ao usuário e prova de requisitos/revisão quando cabível. Consentimento do usuário sozinho não elimina a política. Se isso não puder ser esclarecido, use a implementação oficial/local com acesso próprio.

## Fluxo opcional, não executado
O usuário escolhe o fornecedor e entende quem receberá os dados. No host compatível, preparar um bloco remoto com URL oficial, `enabled=false` e aprovação de ferramentas em modo prompt. Depois da decisão humana, habilitar e iniciar OAuth; vincular somente a plataforma/conta selecionada. O fornecedor pode ter uma segunda tela para conectar Meta/Google. Uma conta Adspirer criada não prova que as contas de anúncios foram vinculadas.

## Primeira consulta
Descobrir ferramentas e pedir identificação das plataformas conectadas. Conferir cada conta antes de dados detalhados. Não executar exemplos promocionais de criação de campanha para “ver se funciona”. Não comprar plano ou exceder cota por padrão. As ferramentas cobradas pelo SaaS e o orçamento de anúncios são custos distintos.

## Saída da relação
Documentar como revogar grants na plataforma de origem, desconectar o fornecedor e desabilitar/remover o bloco local. A política de retenção deve esclarecer o que permanece no serviço após desconectar. Não prometer exclusão remota sem resposta comprovada. Registrar incertezas sem acusar o fornecedor de algo que não foi auditado.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Adspirer — fornecedor terceiro](https://github.com/amekala/ads-mcp)
- [Google Ads Developer Policies](https://support.google.com/adspolicy/answer/6169371?hl=en)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
