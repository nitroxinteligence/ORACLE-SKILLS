---
name: oracle-skill-66ee480c19f8f8978026
description: "Planeje criação e refinamento de vídeo no Motion MCP com OAuth humano, verificação de conta/saldo, upload mínimo autorizado e aprovação separada de render e custo. Use para storyboard, geração remota e revisão por sessão existente."
metadata:
  departamento: conteudo
  especialista: criacao-de-video
  skill-id: CON-VID-07
  versao: "1.0.0"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Vibe editing no Motion MCP

## Entrada
Brief, copy e storyboard com versões, materiais autorizados, destino, conta lógica, limite de gasto e quantidade de gerações. Motion é um serviço remoto; esta skill não o instala, autentica nem concede permissão de envio.

## Leitura necessária
Leia [operação segura](../references/operacao-segura.md) e [guia Motion](references/guia.md). O endpoint oficial é https://mcp.motion.so/mcp; confirme o host, a autorização vigente e as ferramentas realmente disponíveis.

## Perguntas por lacunas
Qual conta deve ser usada? Quais arquivos podem ser enviados ao Motion? O plano de cenas e a copy estão aprovados? Qual custo máximo e número de tentativas foram autorizados? É geração nova ou ajuste de uma sessão existente? Não solicite senhas, tokens ou cartão.

## Procedimento
1. Confirme a finalidade e o estado da conexão sem inferir acesso pela existência da skill. Quando a conexão for solicitada, oriente OAuth na interface oficial e deixe login, MFA, escopos e aprovação para o humano; não crie conta de serviço como fallback automático.
2. Descubra o catálogo real e consulte primeiro whoami e get_credit_balance, no escopo autorizado. Registre apenas alias necessário, plano e saldo pertinente. Uma resposta válida comprova leitura da conta, não autorização de gasto.
3. Feche a copy e o storyboard antes da produção. Declare duração, proporção, conteúdo real do produto, invariantes e materiais por cena; não invente telas, dados ou depoimentos ausentes.
4. Separe autorização de upload da autorização de render. Para cada asset aprovado, use o contrato real de upload e transferência de bytes; uma URL assinada emitida por upload_asset não comprova envio concluído. Não envie caminhos file:// como anexos remotos.
5. Confirme anexos disponíveis, conta e limite de execução. Se faltar saldo ou preço suficiente para decidir, pare a geração e apresente a pendência. Compras, assinatura, cartão, recarga automática e gestão de chaves são negadas por padrão nesta skill.
6. Apenas com autorização aplicável, inicie a geração delimitada ou o refinamento da sessão correta. Guarde o identificador retornado; timeout ou fechamento do painel não autoriza criar um job duplicado.
7. Consulte a sessão existente quando necessário e revise o vídeo efetivo com cobertura declarada. Liste correções por cena/tempo; use refinamento somente no escopo e custo aprovados, preservando copy e cenas não alteradas.
8. Entregue o estado observado, identificador, resultado acessível e revisão. Só declare arquivo salvo após transferência confirmada por ferramenta autorizada e [verificação do export](../video-revisao-exportacao/SKILL.md). Não publique nem contorne bloqueios de host.

## Erros e recuperação
401 ou OAuth pendente: humano conclui autorização; não extraia credenciais de arquivos. Upload incompleto: confira o asset e a transferência, sem render prematuro. Créditos insuficientes: não compre nem ative recarga. Job incerto: consulte a sessão antes de repetir. Link expirado: recupere pelo serviço, sem inventar URL.

## Entregável
Plano ou resultado conforme autorização, registro mínimo de conta/saldo, materiais enviados comprovados, aprovação de render/custo, ID da sessão, revisão e estado do arquivo final. URLs com tokens não entram em notas persistentes de forma desnecessária.

## Critérios de aceite
Conta e sessão corretas; uploads e custo autorizados separadamente; nenhum pagamento automático; recebimento de URL distinto de arquivo salvo; ferramenta ausente ou resultado não percebido explicitamente marcado. A geração não autoriza publicação.
