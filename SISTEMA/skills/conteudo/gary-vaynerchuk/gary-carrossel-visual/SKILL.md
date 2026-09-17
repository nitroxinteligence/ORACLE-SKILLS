---
name: oracle-skill-0fb827aa7e2b2f60f083
description: "Converta a copy aprovada de um carrossel em uma série visual consistente, com piloto, hierarquia, revisão por slide e sequência. Use na etapa posterior à aprovação editorial."
metadata:
  departamento: conteudo
  especialista: gary-vaynerchuk
  skill-id: CON-GV-32
  versao: "1.0.0"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Produção visual de carrossel

## Escopo e autoria
Sistema visual, piloto e QA de série são engenharia original. Gary oferece apenas contexto de distribuição; OpenAI e W3C sustentam orientações técnicas de produção e acessibilidade.

## Entrada
Copy numerada e aprovada, direção visual aprovada, formato de destino, referências reais e ativos autorizados. Não reconstrua texto ausente a partir de uma ideia genérica.

## Leitura necessária
Leia [visual-e-referencias](../references/playbooks/visual-e-referencias.md) e [fluxo-e-aprovacoes](../references/playbooks/fluxo-e-aprovacoes.md) e [plataformas-e-auditorias](../references/playbooks/plataformas-e-auditorias.md) antes de aplicar o fluxo e consulte [o mapa de referências](references/indice.md). Nada é carregado automaticamente. Se um guia ou ficha estiver indisponível, registre a lacuna e não invente seu conteúdo.

## Procedimento
1. Congele a versão de copy e vincule cada slide à sua função e fonte. Qualquer alteração de promessa, número ou sentido volta ao responsável editorial.
2. Defina um sistema de série com margens, hierarquia, tipografia, cores e variações permitidas. Confira dimensões atuais do destino e áreas que precisam sobreviver ao recorte.
3. Escolha uma unidade representativa como piloto quando a série exigir consistência. Faça o piloto somente com ferramenta e autorização reais; um layout descrito não é uma imagem produzida.
4. Verifique legibilidade no tamanho de consumo, texto literal, contraste medido quando aplicável e coerência com a referência. Resolva o sistema visual antes de multiplicar um erro por toda a sequência.
5. Produza ou encaminhe os demais slides com identidade comum. Para geração raster, use imagens-openai e seus limites de alvo/schema; para composição editável, registre a ferramenta real e os arquivos efetivamente criados.
6. Inspecione cada slide e a sequência completa: ordem, cortes, repetição, dados, fontes e conclusão. Entregue alternativas textuais, versão e estado de aprovação visual; não publique nem chame raster de arquivo editável.

## Perguntas por lacunas
Qual versão de copy está aprovada? Quais atributos devem permanecer iguais na série? Que slide concentra a maior dificuldade visual? Há necessidade real de arquivo editável além de exportações?

## Contrato de saída
Série visual real ou plano marcado não executado, arquivos por ordem, versão de copy, especificações, registro de QA por slide, alternativas textuais e aprovação visual pendente/concluída com evidência.

## Erro crítico
Multiplicar um piloto reprovado, mudar o texto para caber sem autorização ou declarar exportações que não existem.

## Referências
- [OA06 — OpenAI: prompting e iteração](../references/fontes/oa06.md): Orientar preservação de texto e invariantes na série.
- [DV01 — W3C: alternativas textuais](../references/fontes/dv01.md): Preparar equivalente útil da informação.
- [DV02 — W3C: contraste](../references/fontes/dv02.md): Verificar legibilidade sem certificação presumida.
- [IG01 — Instagram: contexto de formato](../references/fontes/ig01.md): Revalidar requisitos do destino quando for Instagram.

## Papel
[diretor-arte](../agents/diretor-arte.md) é o contrato responsável por esta etapa. O arquivo não cria nem ativa um agente. Execute apenas o escopo solicitado; publicação nunca é automática.
