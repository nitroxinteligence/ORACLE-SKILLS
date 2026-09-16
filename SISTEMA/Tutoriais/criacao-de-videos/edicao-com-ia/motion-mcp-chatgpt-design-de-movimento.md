---
title: "Motion MCP no ChatGPT: crie vídeos e motion design por conversa"
slug: motion-mcp-chatgpt-design-de-movimento
language: pt-BR
type: tutorial
category: criacao-de-videos
subcategory: edicao-com-ia
source: https://x.com/motion_so/status/2100280160234721660
source_author: "Motion (@motion_so)"
source_published_at: "2026-09-16T17:46:26Z"
source_site: X
source_product: https://motion.so/
source_documentation:
  - https://docs.motion.so/guides/chatgpt-app
  - https://docs.motion.so/guides/mcp
  - https://motion.so/learn/mcp-video-generation
captured_at: 2026-09-16
capture_method: agent-reach/opencli-twitter+jina-reader
media_storage: remote_links
tags:
  - motion
  - motion-design
  - chatgpt
  - mcp
  - criacao-de-videos
  - video-com-ia
  - animacao
  - product-video
---

# Motion MCP no ChatGPT: crie vídeos e motion design por conversa

O [Motion](https://motion.so/) é um agente de criação de vídeos e motion design.
Com o Motion MCP, o ChatGPT pode iniciar uma produção, enviar referências,
acompanhar o render e pedir alterações sem depender da operação manual de uma
timeline.

O anúncio original resume o fluxo assim:

```text
conecte o ChatGPT ao Motion pelo MCP
→ forneça seus arquivos e referências
→ descreva o vídeo desejado
→ o ChatGPT conduz ideias, animações e transições dentro do Motion
→ revise o resultado
→ peça refinamentos
```

[![Demonstração do Motion MCP](https://pbs.twimg.com/amplify_video_thumb/2100279057514364928/img/-hb7W5FiA5qhjOAK.jpg)](https://video.twimg.com/amplify_video/2100279057514364928/vid/avc1/480x270/VXhlRwwMrwG6HDC_.mp4?tag=29)

[Abrir o vídeo de lançamento](https://video.twimg.com/amplify_video/2100279057514364928/vid/avc1/480x270/VXhlRwwMrwG6HDC_.mp4?tag=29)

## O que pode ser criado

O Motion apresenta o MCP para trabalhos como:

- vídeos de lançamento;
- demonstrações de produto;
- explainers;
- anúncios e peças sociais;
- trailers;
- animações de logo;
- motion graphics;
- transformação de artigos, sites, documentos ou ideias em vídeo.

O serviço pode pesquisar o contexto fornecido, montar direção visual e
storyboard, produzir cenas e receber correções posteriores. A qualidade do
resultado ainda depende de um briefing claro e de revisão humana.

## 1. O que você precisa

- uma conta no ChatGPT com acesso a **Apps**, **conectores MCP personalizados**
  e **Developer mode**;
- uma conta no Motion;
- créditos do Motion para gerar vídeos;
- arquivos de marca e referências que você tenha direito de usar;
- um navegador para concluir a autorização OAuth.

O servidor MCP oficial é:

```text
https://mcp.motion.so/mcp
```

O fluxo padrão usa OAuth 2.1. Você não precisa criar uma chave de API para a
conexão normal pelo ChatGPT.

## 2. Conecte o Motion ao ChatGPT

Na documentação oficial consultada, a configuração é feita assim:

1. Abra **Settings → Apps → Advanced settings** no ChatGPT.
2. Ative **Developer mode**.
3. Volte para **Settings → Apps**.
4. Selecione **Create app**.
5. Preencha os campos abaixo.

| Campo | Valor |
|---|---|
| Nome | `Motion` |
| URL MCP | `https://mcp.motion.so/mcp` |
| Autenticação | OAuth |

Descrição sugerida:

```text
Crie e refine vídeos com o Motion. Use este app para vídeos de lançamento,
explainers, anúncios, trailers, motion graphics, demonstrações de produto,
clipes sociais e transformação de sites, documentos ou ideias em vídeos.
```

6. Inicie a autorização.
7. Entre ou crie sua conta no Motion.
8. Leia os escopos solicitados e autorize apenas se estiver de acordo.
9. Em uma conversa, selecione **Developer mode** no compositor.
10. Ative o app **Motion** para aquela conversa.

Os nomes e a posição dos menus podem mudar conforme a versão do ChatGPT. Use a
[documentação oficial do Motion para ChatGPT](https://docs.motion.so/guides/chatgpt-app)
como referência atual.

## 3. Confirme a conexão antes de produzir

Faça primeiro uma consulta que não inicia um render:

```text
Use o Motion para mostrar minha conta conectada, meu plano e meu saldo atual de
créditos. Não compre créditos e não inicie nenhuma geração.
```

Essa verificação separa quatro estados:

```text
app configurado
≠ autorização concluída
≠ ferramentas disponíveis
≠ créditos suficientes para renderizar
```

Só continue quando o ChatGPT conseguir consultar a conta e o saldo.

## 4. Prepare o briefing

Um bom pedido deve informar:

- objetivo do vídeo;
- público;
- mensagem principal;
- duração;
- proporção;
- canal de publicação;
- identidade visual;
- estrutura narrativa;
- ritmo e referências;
- materiais obrigatórios;
- chamada para ação;
- elementos proibidos.

Use este modelo:

```text
Crie no Motion um vídeo de [TIPO] para [PRODUTO OU MARCA].

Objetivo:
[RESULTADO QUE O VÍDEO PRECISA PRODUZIR]

Público:
[QUEM DEVE ENTENDER OU AGIR]

Mensagem principal:
[UMA FRASE]

Formato:
- duração: [MENOS DE 10S, 10–30S, 30S–1MIN OU 1–5MIN]
- proporção: [16:9, 9:16, 1:1, 4:5 OU 21:9]
- destino: [SITE, YOUTUBE, INSTAGRAM, APRESENTAÇÃO ETC.]

Direção visual:
- estilo: [DESCRIÇÃO]
- cores: [PALETA]
- tipografia: [REGRAS]
- ritmo: [CALMO, CINEMATOGRÁFICO, RÁPIDO ETC.]
- referência: [URL OU ARQUIVO]

Estrutura:
1. [ABERTURA]
2. [PROBLEMA OU CONTEXTO]
3. [DEMONSTRAÇÃO]
4. [RESULTADO]
5. [CTA]

Materiais obrigatórios:
[LOGO, CAPTURAS, IMAGENS, VÍDEOS, ÁUDIO OU DOCUMENTOS]

Restrições:
[O QUE NÃO DEVE SER INVENTADO, ALTERADO OU USADO]

Antes de gerar, apresente um plano de cenas para minha aprovação.
```

Pedir o plano antes do render reduz retrabalho e consumo desnecessário de
créditos.

## 5. Envie os arquivos corretamente

O Motion não lê caminhos locais como `file:///...`. Quando um arquivo existe
somente no seu computador, o app deve usar a ferramenta de upload do Motion e
depois anexar a URL retornada à geração.

Pedido sugerido:

```text
Envie estes arquivos locais para o Motion e use as URLs retornadas como anexos:

- [CAMINHO DO LOGO]
- [CAMINHO DA CAPTURA DE TELA]
- [CAMINHO DO VÍDEO DO PRODUTO]

Confirme quais arquivos foram enviados. Não inicie a geração ainda.
```

Depois, confira se:

- todos os arquivos esperados foram enviados;
- o logo tem boa resolução e fundo adequado;
- os vídeos estão na orientação correta;
- os arquivos não contêm dados pessoais ou segredos;
- você possui autorização para usar o material.

O Motion aceita até 100 anexos por geração segundo a documentação consultada,
mas uma seleção pequena e organizada costuma produzir um briefing mais claro.

## 6. Gere a primeira versão

Depois de aprovar o plano de cenas:

```text
Use o Motion para criar o vídeo conforme o plano aprovado.

Use os anexos já enviados. Preserve nomes, logotipo, textos e dados do produto
exatamente como foram fornecidos. Não invente depoimentos, números, telas ou
funcionalidades.

Proporção: 16:9
Duração: 30 segundos a 1 minuto

Inicie uma única geração e me mostre o acompanhamento do trabalho.
```

A ferramenta `create_video` inicia um trabalho assíncrono. Em versões do
ChatGPT com suporte a MCP Apps, um painel interativo pode acompanhar o render e
reproduzir o resultado dentro da conversa. Em outros clientes, o retorno pode
aparecer como dados e um link.

## 7. Revise a primeira versão

Assista ao vídeo inteiro e avalie:

- se a mensagem é compreendida sem explicação externa;
- se a primeira cena prende a atenção;
- se cada cena apresenta uma ideia clara;
- se o produto aparece no momento certo;
- se a tipografia é legível;
- se o ritmo combina com a marca;
- se animações e transições ajudam a narrativa;
- se o áudio está equilibrado;
- se o CTA é visível;
- se nomes, números e telas estão corretos;
- se a duração e a proporção estão corretas.

Registre cada problema com cena, timestamp e correção desejada.

```text
Revise o vídeo gerado e organize minhas observações em uma lista antes de
alterá-lo:

1. 00:00–00:03 — [PROBLEMA] → [CORREÇÃO]
2. 00:08–00:12 — [PROBLEMA] → [CORREÇÃO]
3. 00:21–00:25 — [PROBLEMA] → [CORREÇÃO]

Preserve tudo que não foi mencionado.
```

## 8. Refine sem reiniciar o trabalho

Para alterar um vídeo concluído, peça um follow-up sobre a sessão existente.

```text
Crie um refinamento do vídeo concluído no Motion.

Faça somente estas alterações:

1. Entre 00:00 e 00:03, reduza a velocidade da entrada do título.
2. Entre 00:08 e 00:12, substitua a imagem genérica pela captura enviada.
3. Na cena final, aumente o contraste do CTA e mantenha o logo intacto.

Preserve roteiro, duração, proporção, áudio e todas as cenas não citadas.
```

Faça rodadas pequenas. Misturar mudanças de roteiro, estilo, duração, áudio e
identidade em um único pedido dificulta descobrir qual alteração piorou o
resultado.

## 9. Recupere o resultado e baixe o vídeo

Se o painel fechar ou a conversa for retomada mais tarde, use o identificador
do trabalho:

```text
Consulte no Motion o estado do trabalho [JOB_ID]. Não inicie uma nova geração.
Se estiver concluído, mostre o vídeo e o link oficial de download.
```

Quando o estado for `completed`, a resposta pode conter um endereço de download
em `output.download_url`.

Antes de publicar, salve:

- vídeo final;
- prompt aprovado;
- arquivos de origem;
- identificador do trabalho;
- lista das alterações;
- versão vertical ou quadrada, se necessária;
- comprovantes de licença dos materiais usados.

## 10. Modelos rápidos

### Vídeo de lançamento

```text
Crie um vídeo de lançamento de 30 segundos em 16:9 para [PRODUTO].

Abra com [GANCHO]. Mostre o problema, demonstre três benefícios reais usando as
capturas anexadas e termine com [CTA]. Use tipografia cinética, transições
limpas e a paleta da marca. Não invente interfaces ou resultados.

Apresente o storyboard antes de iniciar o render.
```

### Demonstração de produto

```text
Crie uma demonstração de produto entre 30 e 60 segundos.

Use apenas as gravações de tela anexadas. Organize a narrativa em problema,
ação no produto e resultado. Destaque o cursor e os elementos relevantes sem
obstruir a interface. Preserve todos os textos do produto.
```

### Anúncio vertical

```text
Crie uma versão 9:16 de 15 segundos para redes sociais.

Use um gancho visual nos dois primeiros segundos, frases curtas, legendas
grandes e CTA final. Mantenha textos e elementos essenciais dentro da área
segura. Não corte o logo nem a interface principal.
```

### Transformar artigo em vídeo

```text
Transforme este artigo em um vídeo de 45 segundos: [URL].

Extraia somente afirmações sustentadas pelo artigo. Resuma a tese, três ideias
centrais e a conclusão. Mostre as fontes na tela quando necessário e não
invente dados ausentes.
```

## Ferramentas que o Motion MCP oferece

| Ferramenta | Finalidade |
|---|---|
| `create_video` | iniciar a geração de um vídeo a partir do prompt |
| `create_followup` | refinar um vídeo concluído |
| `upload_asset` | enviar imagem, áudio ou vídeo local e obter uma URL utilizável |
| `get_session_status` | consultar ou reabrir um trabalho existente |
| `get_credit_balance` | consultar plano e saldo de créditos |
| `show_plans_and_credits` | mostrar planos e opções de recarga |
| `whoami` / `get_settings` | conferir conta e configuração da conexão |

O servidor também expõe ferramentas de assinatura, compra de créditos,
pagamento automático e gerenciamento de chaves. Essas ações podem gerar
cobrança ou alterar credenciais; peça confirmação explícita antes de executá-las.

## Privacidade, custos e segurança

- O Motion é um serviço externo. Arquivos enviados saem do ambiente local.
- Remova segredos, dados pessoais e informações de clientes que não sejam
  necessários para o vídeo.
- Leia os escopos apresentados durante o OAuth.
- Verifique o saldo antes do render e não ative recarga automática sem decisão
  consciente.
- Não permita compra de créditos, assinatura ou configuração de cartão dentro
  de um prompt amplo de criação.
- Use somente materiais, músicas, imagens, marcas e vozes com autorização.
- Revogue a conexão nas configurações do ChatGPT ou do Motion quando ela não
  for mais necessária.
- Revise o vídeo antes de publicar. A geração pode criar textos, imagens ou
  afirmações incorretas.

## Checklist final

- [ ] app Motion conectado pelo endereço MCP oficial;
- [ ] conta e saldo confirmados sem iniciar geração;
- [ ] arquivos revisados antes do upload;
- [ ] briefing com objetivo, público, formato e restrições;
- [ ] storyboard aprovado;
- [ ] uma única primeira versão gerada;
- [ ] revisão completa com timestamps;
- [ ] refinamentos limitados ao que foi solicitado;
- [ ] nomes, dados, telas e CTA conferidos;
- [ ] vídeo final baixado e arquivado;
- [ ] direitos e autorização de publicação confirmados.

## Fontes

- [Anúncio do Motion MCP no X](https://x.com/motion_so/status/2100280160234721660)
- [Motion](https://motion.so/)
- [Configuração oficial do Motion no ChatGPT](https://docs.motion.so/guides/chatgpt-app)
- [Documentação oficial do Motion MCP](https://docs.motion.so/guides/mcp)
- [Guia oficial de geração de vídeo por MCP](https://motion.so/learn/mcp-video-generation)

> Captura feita em 16 de setembro de 2026. Como menus, ferramentas, preços e
> permissões podem mudar, confira a documentação oficial antes de conectar ou
> autorizar pagamentos.
