---
id: "fv-matriz-integracoes"
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
# Matriz de integrações de mídia paga

| Rota | Natureza | Capacidades documentadas | Condição para operar |
|---|---|---|---|
| Meta CLI `meta-ads` / `meta` | Publicação oficial Meta, proprietária | Grupos de leitura e gestão da Marketing API | Runtime compatível, credencial privada, conta e schema verificados. Criações seguras antes de ativação. |
| Meta MCP oficial | Ajuda/anúncio oficial, acesso incompleto na pesquisa | Não foi fechado um contrato técnico público completo | Confirmar endpoint, OAuth e elegibilidade na documentação disponível à conta; não tratar snippet como configuração pronta. |
| Google Ads MCP | Repositório/documentação oficiais | Consulta de contas, GAQL e metadata; somente leitura | Acesso do projeto Cloud e da conta; OAuth/ADC; transporte compatível. |
| Google Ads API/SDK | Oficial | Mutações conforme API e permissões | Executor separado, acesso próprio e diff aprovado. Não é recurso de escrita do MCP acima. |
| Adspirer | Terceiro hospedado | Gestão multiplataforma declarada pelo fornecedor | Escolha consciente, dados/custos e, no Google, arquitetura/uso permitido e revisão aplicável. Conformidade não certificada. |

## Distinções que evitam erros
Uma CLI não vira MCP ao ser listada em config. Um servidor stdio local não fica acessível ao ChatGPT web. Escopo OAuth não cria ferramentas de escrita. Um recurso pausado é uma mutação, embora não seja uma ativação. Instalação do pacote não concede acesso da plataforma. Um ID de conta não é segredo, mas continua dado de contexto a minimizar.

## Versões observadas
Meta CLI 1.1.0; Google MCP HEAD `7a40eae9655194a84d5291c63af817bb20d02ea8`. Pins indicam identidade examinada, não distribuição instalada. Revalidar publicação, licença e compatibilidade antes de instalar. Novo onboarding Google não deve repetir automaticamente o fluxo antigo de developer token.

## Decisão para este pacote
Meta: oferecer primeiro o caminho local publicamente documentado quando o host o comporta. Google: leitura oficial e escrita oficial separadas. Terceiro remoto é opcional e condicionado à diligência, não padrão silencioso. Offline permanece possível para planejamento e análise de arquivos.

[Fontes](../references/fontes.md) · [Operação](../references/operacao-segura.md) · [Biblioteca](../conectado.md)
