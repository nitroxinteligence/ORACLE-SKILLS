---
id: vibeediting-motion-mcp-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://docs.motion.so/guides/mcp
  - https://docs.motion.so/guides/chatgpt-app
  - https://docs.motion.so/guides/attachments
  - https://docs.motion.so/guides/credits
  - https://developers.openai.com/plugins/deploy/connect-chatgpt
confidence: medium
review_after: 2026-10-16
---
# Motion: conta, envio e render como decisões separadas

Consulta documental em 16 de setembro de 2026; nenhuma conta foi conectada e nenhum asset enviado ou renderizado. O serviço aparece nas páginas atuais como Mosaic Motion. Este guia é uma política operacional original sobre as capacidades documentadas, não permissão do fornecedor para agir na conta.

## 1. Conectar pelo caminho correto
O MCP oficial usa https://mcp.motion.so/mcp e OAuth 2.1. No fluxo padrão, a aprovação ocorre no navegador e não exige uma API key [M1]. Deixe o humano autenticar e revisar os escopos; não leia tokens, cookies ou configurações privadas para substituir esse passo.

Há uma divergência de interface a registrar: o guia Motion descreve Apps e Advanced settings [M2], enquanto a documentação OpenAI consultada usa Developer mode em Security and login e criação em Plugins [O1]. Verifique a superfície real do host e use a OpenAI como autoridade dos menus ChatGPT. Não conclua que a conta tem o recurso apenas por estar documentado.

## 2. Provar leitura antes de enviar
Descubra ferramentas reais. whoami e get_credit_balance permitem conferir identidade e saldo [M1]. Guarde um alias suficiente para distinguir contas, sem persistir detalhes desnecessários. O saldo pode mudar: consulte novamente quando a execução depender dele, sem transformar consulta em aprovação de custo.

Defina qual vídeo será criado e quais materiais existem. Reuse o [brief](../../templates/brief-video.yaml). Um site ou artigo é fonte do argumento somente até o trecho efetivamente lido; uma captura de produto real deve prevalecer sobre tela inventada.

## 3. Preparar anexos com consentimento
O servidor remoto precisa receber arquivos ou URLs alcançáveis; caminhos locais não funcionam como anexos [M3]. Selecione somente bytes necessários e autorizados para sair do computador. Verifique o destinatário real e não envie o vault ou uma pasta inteira por conveniência.

upload_asset fornece uma URL assinada para transferência; depois é utilizada attachment_url [M1]. Aplique o schema observado no host. Separar solicitação de upload, envio dos bytes e disponibilidade do anexo evita declarar um envio que não ocorreu. Não imprima cabeçalhos, tokens ou URLs sensíveis em relatório permanente.

Se a ferramenta local de transferência recusar o host, registre a falha e mantenha o asset não enviado. Não altere URLs, busque caminhos alternativos de exfiltração nem reconstrua o arquivo para vencer o bloqueio. A aprovação de upload é específica ao destinatário e finalidade.

## 4. Aprovar o job, não apenas a ideia
Antes da execução, registre versão da copy, storyboard, anexos, proporção, duração-alvo, conta lógica, quantidade e teto de gasto. Se a cobrança final não puder ser estimada, exponha a incerteza e mantenha o render pendente até uma decisão suficiente.

O serviço expõe criação/refinamento e também ferramentas de cobrança [M1]. Esta skill não usa purchase_credits, subscribe_to_plan, setup_payment_method ou set_auto_topup por um pedido genérico de vídeo. Também não cria conta de serviço nem administra chaves como recuperação automática. Ter saldo ou cartão cadastrado não altera esse limite.

Preços e consumo variam conforme o serviço; use a página de créditos e a resposta atual em vez de congelar um custo por vídeo [M4]. Uma rodada adicional de refinamento precisa caber na autorização aplicável.

## 5. Acompanhar sem duplicar
create_video e create_followup iniciam trabalhos; get_session_status recupera a sessão e seu resultado. O widget pode acompanhar o progresso; job_status é descrito como ferramenta interna do app, não comando exposto ao modelo [M1]. Não invente sua disponibilidade.

Se a chamada sofrer timeout, primeiro tente identificar a sessão existente. Preserve seu ID e estado; não submeta nova criação só porque não há painel visível. Se não houver mecanismo para determinar o resultado, registre resultado_incerto e peça reconciliação da conta antes de autorizar nova cobrança.

## 6. Revisar e recuperar o arquivo
Confira a copy literal, produto, cenas, áudio, duração e enquadramento dentro da cobertura que a ferramenta permitir. Aponte o trecho exato e a alteração pretendida para um follow-up, preservando cenas aprovadas.

Quando a sessão estiver concluída, consulte o resultado oficial. Download URL não é prova de arquivo no disco. A ferramenta de transferência precisa confirmar destino e sucesso; depois a [revisão/exportação](../../video-revisao-exportacao/SKILL.md) verifica os bytes recebidos. Preserve originais e versões anteriores.

## Recuperação

| Situação | Conduta |
|---|---|
| Autorização expirada | Humano renova no fluxo oficial; nenhuma extração de token |
| Asset inacessível | Conferir upload, URL e validade; não iniciar render com referência fictícia |
| Saldo insuficiente | Entregar pendência; compras e autotopup continuam sem autorização |
| Render sem retorno | Recuperar sessão por ID; não duplicar geração |
| Resultado visual divergente | Correção delimitada, mantendo evidência e aprovação da versão |
| Link expirado ou transferência bloqueada | Recuperação oficial ou entrega do estado; sem contorno de host |

## Fontes e limites
- M1 — [Motion MCP](https://docs.motion.so/guides/mcp). Endpoint, OAuth e catálogo de ferramentas lidos. Não comprova disponibilidade nesta conversa.
- M2 — [Motion no ChatGPT](https://docs.motion.so/guides/chatgpt-app). Fluxo do fornecedor lido; nomes de menus divergem da documentação atual OpenAI.
- M3 — [Motion Attachments](https://docs.motion.so/guides/attachments). Requisitos de acesso aos anexos consultados; nenhum upload testado.
- M4 — [Motion Credits](https://docs.motion.so/guides/credits). Modelo de créditos consultado; não foram obtidos preços ou saldo de conta pessoal.
- O1 — [OpenAI: conectar no ChatGPT](https://developers.openai.com/plugins/deploy/connect-chatgpt). Seções de Developer mode e Plugins lidas; o endereço Apps SDK redirecionou a esta página. Menus e disponibilidade exigem conferência no host.
- [Tutorial local Motion](../../../../../tutoriais/criacao-de-videos/edicao-com-ia/motion-mcp-chatgpt-design-de-movimento.md). Lido integralmente; anúncio do X e vídeo incorporado não foram novamente acessados nesta autoria.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md).
