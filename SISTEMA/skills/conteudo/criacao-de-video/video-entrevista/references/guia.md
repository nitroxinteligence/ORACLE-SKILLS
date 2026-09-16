---
id: video-entrevista-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://hypit.ai/quickstart/
  - https://www.w3.org/WAI/media/av/captions/
confidence: medium
review_after: 2026-10-16
---
# Transformar respostas em decisões de produção

Este guia detalha uma entrevista original. As fontes primárias foram consultadas em 16 de setembro de 2026 para delimitar serviços e acessibilidade; não fornecem uma entrevista oficial de 28 perguntas. O [banco compartilhado](../../references/entrevista.md) é a lista canônica: leia-o, não mantenha uma cópia concorrente.

## Começar pela decisão seguinte
Para editar um vídeo já gravado, a primeira incerteza pode ser qual fala preservar. Para animação de produto, pode ser a copy e a captura correta. Para geração remota, a saída de arquivos do computador e o custo podem bloquear execução. Pergunte pelo que muda essa decisão, não pelo que preenche mais campos.

Use estados por resposta: respondido por fonte, respondido pelo usuário, conflitante, não aplicável e desconhecido. Vincule origem/data e a tarefa à qual a resposta se aplica. Uma preferência de outro cliente ou projeto não é transferida automaticamente.

## Agrupar o banco sem impor cotas

| Grupo | Campos do brief | Decisão produzida |
|---|---|---|
| Intenção | objetivo, publico, canal, roteiro | Promessa e conteúdo que precisam sobreviver |
| Caminho técnico | editor, host, local, material | Operação local, draft, bridge ou serviço remoto |
| Linguagem | referencias, atributos, evitar, narrativa, ritmo | O que aproveitar e o que preservar |
| Acabamento | broll, legendas, audio, musica, cor, marca, efeitos | Materiais e critérios de acabamento |
| Entrega | formato, versoes, aprovador, destino, prazo, aceitacao | Outputs, revisão e local de gravação |
| Direitos e custo | direitos, custo, autorizações por ação | Limites para uso, transferência e gasto |

A tabela corresponde ao [brief existente](../../templates/brief-video.yaml). Campos inicialmente nulos não devem receber respostas inventadas. Se o usuário delegar uma decisão criativa, registre a recomendação e a justificativa, preservando fatos ainda desconhecidos.

## Aprofundamentos que mudam o plano
**Montagem de fala.** Peça uma frase obrigatória, uma ressalva que não pode desaparecer e exemplos de pausas intencionais. A frase cortar tudo que está lento exige interpretação: proponha um trecho piloto com handles, não um corte cego de todos os silêncios.

**Referência estética.** Pergunte qual atributo interessa: contraste, disposição de títulos, ritmo dos cortes, uso de câmera ou densidade de legenda. Ter um link não comprova acesso ou direitos. Quando a referência não puder ser inspecionada, peça um arquivo acessível ou uma descrição e registre essa origem.

**Áudio e legendas.** Confirme idioma, grafia de nomes, sons relevantes e se o destino precisa de legenda selecionável, queimada ou ambas. A W3C trata legendas acessíveis como informação auditiva necessária, incluindo identificação de falante e sons pertinentes [A1]. Não transforme a opção gráfica em prova de acessibilidade sem revisão.

**Serviço externo.** Pergunte quais arquivos podem ser enviados, para qual serviço e qual conta lógica deve ser usada. Não solicite a chave. O quickstart do Hypit distingue o ambiente do agente dos serviços de geração e pede acordo sobre trabalho e custo [HY1]. Registre autorização aplicável, não consentimento genérico para qualquer provider.

**Entrega técnica.** Quando faltarem especificações, ofereça uma proposta condicional à plataforma. Não fixe bitrate, loudness, resolução ou duração universal. Peça exigências de quem receberá o arquivo quando houver broadcaster, cliente ou plataforma com contrato próprio.

## Exemplo de condução
Situação hipotética: o pedido já define Reel vertical, arquivo de fala e legenda em português; editor e upload permanecem desconhecidos. Não pergunte novamente canal, idioma ou material. O próximo bloco pode fechar editor/host, permissão de saída de mídia e quais frases manter. Depois, aprofunde problemas de áudio constatados ou relatados, não os invente.

O exemplo não representa o usuário nem uma inspeção real. Nenhum nome de pessoa, valor de orçamento ou preferência deve ser fabricado para tornar o brief aparentemente completo.

## Readback e encaminhamento
Devolva a mensagem a comunicar, material disponível, abordagem proposta, invariantes, formato, limites e pontos que ainda dependem de teste. Use confirmação dirigida: esta alteração muda a promessa? este arquivo pode ir ao serviço escolhido? Evite uma aprovação global que esconda decisões distintas.

Um brief pode estar suficiente para pesquisa e insuficiente para render. Registre a etapa liberada e a etapa bloqueada. Na retomada, releia apenas o que mudou ou perdeu validade. O pedido de uma correção pontual não exige refazer todas as perguntas.

## Falhas e recuperação
- **Informação conflitante:** preserve as duas versões e peça decisão somente quando o conflito alterar produção.
- **Sem editor definido:** encaminhe recomendação pela natureza da entrega à [orquestração](../../video-orquestracao/SKILL.md), considerando o que já existe.
- **Sem referência real:** mantenha referência não inspecionada e peça material, sem simular análise.
- **Sem orçamento:** siga com plano e pesquisa; não submeta chamadas pagas.
- **Sem acesso audiovisual:** descreva análise textual/metadados e peça revisão humana das dimensões não percebidas.

## Fontes e limites
- A1 — [W3C WAI: Captions/Subtitles](https://www.w3.org/WAI/media/av/captions/). Texto das seções de função e conteúdo das legendas consultado; não é certificação da peça.
- HY1 — [Hypit: Quickstart](https://hypit.ai/quickstart/). Seções de referência, serviços e acordo de custo lidas; não houve acesso a conta nem geração.
- [Tutorial local de edição em camadas](../../../../../tutoriais/criacao-de-videos/edicao-com-ia/vibe-editing-com-codex-e-davinci-resolve.md). Lido integralmente como repertório de revisão; preços e instalação nele descritos não foram adotados como requisitos.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md).
