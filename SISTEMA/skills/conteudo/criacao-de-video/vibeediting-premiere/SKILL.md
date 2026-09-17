---
name: oracle-skill-094a9093b076b56473ba
description: "Conduza edição supervisionada no Premiere com o conector comunitário leancoderkavy/premiere-pro-mcp, verificando identidade do pacote, CEP, conexão de leitura, plano, readback e revisão. Use para sequências e entregas Premiere."
metadata:
  departamento: conteudo
  especialista: criacao-de-video
  skill-id: CON-VID-05
  versao: "1.0.0"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Vibe editing no Premiere

## Entrada
Projeto/sequência autorizados, versão do Premiere, host local, origem do pacote MCP, mídia, roteiro e critérios de entrega. O [guia](references/guia.md) identifica a versão pública consultada e o limite entre CEP principal e suporte UXP em evolução.

## Leitura necessária
Leia [operação segura](../references/operacao-segura.md) e [guia Premiere](references/guia.md). Não confunda premiere-pro-mcp de leancoderkavy com adobe-premiere-pro-mcp de outro mantenedor: o nome do executável pode coincidir.

## Perguntas por lacunas
Qual pacote/repositório e versão foram escolhidos? Qual projeto e sequência podem receber edição? A ponte CEP já foi preparada? Há montagem/copy aprovada? Qual operação mínima deve comprovar o fluxo? Pergunte somente o que não puder ser conferido no contexto autorizado.

## Procedimento
1. Confira a identidade do pacote por origem e versão, além do nome do binário. Registre instalado apenas com evidência local; não instale ou atualize pacote, CEP ou UXP durante uma leitura de documentação.
2. Identifique a ponte efetiva e mantenha host, conector e Premiere no ambiente compatível. Trate UXP como capacidade específica a descobrir, sem herdar todas as capacidades do CEP ou do código de desenvolvimento.
3. Em diagnóstico autorizado, use --doctor para prontidão local e verify_premiere_connection para leitura real da conexão. Um retorno de doctor não comprova projeto acessível nem edição realizada.
4. Confirme a sequência autorizada, mídia, FPS e versão do projeto; prepare cópia quando a edição estiver autorizada. Liste ferramentas efetivamente disponíveis antes de formular argumentos ou assumir métodos de script.
5. Construa plano por trechos com source in/out, faixa, destino e intenção de ripple. Comece por corte bruto, preservando palavras e ressalvas; submeta mudanças materiais de copy à aprovação pertinente.
6. Execute um lote delimitado usando operações estruturadas e leia o resultado de volta. Scripts arbitrários e recursos de execução genérica ficam fora do caminho padrão; falta de ferramenta não concede autorização para usá-los.
7. Revise áudio, legendas, timing, composição e cor. Diferencie readback estrutural de percepção visual/auditiva e anote uma mutação salva mas ainda não confirmada como resultado incerto ou revisão pendente.
8. Entregue projeto/sequência, operações e limitações; encaminhe à [revisão/exportação](../video-revisao-exportacao/SKILL.md). Filas de render, Media Encoder e integrações AE precisam de escopo e verificação próprios; nunca autopublique.

## Erros e recuperação
Pacote ambíguo: suspenda configuração até identificar a origem. CEP ausente: relate o requisito, não habilite debug silenciosamente. Sem sequência: peça/identifique a correta. Timeout de mutação: consulte o estado antes de repetir. Ponte UXP sem capacidade: reduza o escopo ou proponha rota compatível, sem declarar sucesso.

## Entregável
Registro de versão e origem do conector, resultados distintos de doctor/conexão, plano ou projeto versionado, operações com readback, revisão e estado da exportação.

## Critérios de aceite
Pacote correto, projeto/sequência corretos, ponte e ferramentas verificadas, originais preservados, nenhuma execução arbitrária implícita e nenhuma afirmação de edição/render baseada apenas em diagnóstico de instalação.
