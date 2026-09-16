---
name: gary-contexto-vault
description: "Mapeie contexto editorial em notas autorizadas do vault com leitura em lotes, cobertura explícita e evidência por caminho. Use antes de entrevistas ou quando houver contexto local a incorporar."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-02
  versao: "1.0.0"
---
# Contextualização pelo vault

## Escopo e autoria
A contextualização com proveniência e cobertura é engenharia original. A relação com Gary limita-se a usar experiências documentadas como matéria-prima; não implica que ele proponha este protocolo de leitura.

## Entrada
Escopo autorizado de pastas, objetivo editorial e informações já conhecidas. Leitura ampla autorizada pode avançar em lotes; não reduza a cobertura a poucos snippets nem acesse credenciais.

## Leitura necessária
Leia [contexto-e-entrevista](../references/playbooks/contexto-e-entrevista.md) e [pesquisa-e-evidencia](../references/playbooks/pesquisa-e-evidencia.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Delimite as áreas autorizadas e os arquivos necessários ao objetivo. Exclua segredos, tokens, autenticação e dados de terceiros sem utilidade editorial. Nesta skill, autorização de leitura não autoriza divulgação.
2. Inventarie os candidatos por caminho e classifique cada um como localizado, lido parcialmente, lido integralmente, não lido ou indisponível. Planeje lotes verificáveis para a extensão solicitada.
3. Leia os lotes com continuidade de intervalos, registrando caminhos e trechos que sustentam cada fato. Um resultado de busca orienta a leitura e não equivale ao arquivo inteiro.
4. Separe fatos declarados, observações, inferências e desconhecidos. Preserve versões conflitantes com data e fonte, sem escolher silenciosamente a versão mais conveniente à narrativa.
5. Produza um pacote mínimo de contexto editorial: público, oferta, voz, exemplos autorizados, temas e limites de exposição. Não copie corpos extensos nem dados pessoais para ferramentas externas.
6. Informe a cobertura real e as lacunas restantes. Encaminhe à entrevista apenas perguntas sem resposta ou conflitos materiais; solicite validação específica antes de transformar contexto privado em conteúdo público.

## Perguntas por lacunas
Qual uso público é permitido para os exemplos encontrados? Entre duas versões conflitantes, qual vale para esta entrega? Há áreas já excluídas do escopo? Não repita perguntas respondidas por fontes atuais e claras.

## Contrato de saída
Registro de cobertura com contagens/intervalos, fatos com caminhos e origem, conflitos, contexto editorial minimizado, limites de divulgação e perguntas restantes. Declare explicitamente a diferença entre conteúdo localizado e efetivamente lido.

## Erro crítico
Dizer que leu todo o vault a partir de buscas parciais, expor segredos ou converter uma inferência pessoal em fato.

## Referências
- [GV03 — Gary: documentar experiências](../references/fontes/gv03.md): Distinguir matéria-prima documentada de fatos inventados.
- [GV09 — Gary: documentação em contexto recente](../references/fontes/gv09.md): Consultar somente dentro do escopo que a ficha efetivamente comprova.
- [RS01 — Procedimento de pesquisa aprofundada](../references/fontes/rs01.md): Usar para rastreabilidade; não atribuir seu protocolo a Gary.

## Papel
[curador-contexto](../agents/curador-contexto.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
