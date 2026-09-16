---
id: "video-matriz-integracoes"
type: "review"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: "2026-10-16"
---
# Matriz de integrações de vídeo

| Rota | Natureza | O que foi estabelecido | O que não foi comprovado |
|---|---|---|---|
| Resolve 21.1 nativo | Fabricante anuncia AI assistant | Novidade pública confirmada | Endpoint, transporte e schema nativos completos não recuperados; verificar bundle/versão. |
| Resolve MCP comunitário | samuelgursky/davinci-resolve-mcp | Setup e diferenças de edição documentadas pelo autor | Compatibilidade com o Mac e projeto do usuário não testada. |
| Premiere MCP | leancoderkavy, comunidade | CEP e diagnóstico documentados; npm 1.16.0 | Nem todas as ferramentas/efeitos foram testados; UXP preview não equivale à rota estável. |
| After Effects MCP | Dakkshin, comunidade | Bridge JSX e processo local documentados | Não foi instalado nem executado; privilégio de scripts exige consentimento. |
| CapCut/pyCapCut | Comunidade | Construção de drafts; export Windows documentado | Render automático no macOS e MCP oficial CapCut não estabelecidos. |
| Motion MCP | Documentação do fornecedor | MCP remoto OAuth, geração/refinamento e custos separados | Conta, plano e render reais não testados. |
| Hypit | Projeto e licença próprios | Workflow, runtime e builds separados; código de vídeo programável | Nenhum build local ou pago executado; licença não é Apache sem condições. |
| Computer use | Host OpenAI oficial | GUI em Desktop/Work/Codex suportados, com permissões | Disponibilidade na conta e precisão de edição não testadas. |

## Escolha de rota
Começar pelo editor que o usuário usa quando atende ao trabalho. Interface estruturada para ações repetíveis; GUI para lacunas e revisão visual, sem prometer precisão frame a frame de um clique. Motion envia dados a um serviço externo; Hypit pode combinar componentes locais e providers. A escolha deve registrar custo, privacidade, formatos e critérios de revisão.

## Compatibilidade e autoria
Não misturar os pacotes npm `premiere-pro-mcp` e `adobe-premiere-pro-mcp`, embora compartilhem o nome de executável. Não fazer downgrade do Resolve para contornar restrições. CapCut não deve ser tratado como JianYing indiferenciadamente. A documentação não instala bridges nem habilita permissões de sistema.

[Fontes](../references/fontes.md) · [Operação](../references/operacao-segura.md) · [Biblioteca](../indice.md)
