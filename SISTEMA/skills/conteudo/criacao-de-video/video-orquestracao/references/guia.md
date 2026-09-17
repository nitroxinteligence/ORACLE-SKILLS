---
id: video-orquestracao-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://learn.chatgpt.com/docs/extend/mcp?surface=cli
  - https://hypit.ai/quickstart/
  - https://docs.motion.so/guides/mcp
confidence: medium
review_after: 2026-10-16
---
# Escolha do caminho e passagem entre etapas

Este guia é uma síntese operacional original. As capacidades factuais vêm das fontes ao final e dos guias de cada editor. A consulta documental foi feita em 16 de setembro de 2026; não houve instalação, conexão, edição ou render nesta autoria.

## 1. Definir a unidade de entrega
Diferencie uma instrução de montagem, um projeto que abre no editor, um preview temporário e um arquivo final reproduzível. Defina a versão da copy, duração-alvo, canal e como o usuário reconhecerá sucesso. Uma solicitação para documentar integração termina em documento; não precisa de conta conectada.

Material recebido pode ser referência de ritmo, insumo de montagem ou objeto a modificar. Registre cada papel. Um vídeo citado por URL e ainda não acessado é referência indicada, não vídeo analisado. Para conteúdo real, registre autorização de uso de pessoas, voz, marca e música sem coletar documentos pessoais desnecessários.

## 2. Selecionar o editor pelo trabalho
A tabela orienta encaminhamento, não classifica ferramentas por qualidade universal. Capacidades instaladas são verificadas em cada execução.

| Necessidade | Encaminhamento | Evidência exigida antes de operar |
|---|---|---|
| Montagem e finalização no Resolve escolhido | [DaVinci Resolve](../../vibeediting-davinci-resolve/SKILL.md) | Versão/edição, contrato do conector, leitura do projeto e timeline |
| Projeto CapCut ou automação de draft | [CapCut](../../vibeediting-capcut/SKILL.md) | Caminho nativo ou pyCapCut escolhido; compatibilidade do draft; exportador efetivo |
| Sequência Premiere | [Premiere](../../vibeediting-premiere/SKILL.md) | Identidade do pacote, painel e verificação real da ponte |
| Animação por composição/camadas | [After Effects](../../vibeediting-after-effects/SKILL.md) | Composição-alvo, bridge revisada e leitura antes da alteração |
| Geração remota Motion | [Motion MCP](../../vibeediting-motion-mcp/SKILL.md) | Conta/saldo, arquivos autorizados para upload e orçamento |
| Vídeo em fontes programáveis | [Hipit/Hypit](../../vibeediting-hypit/SKILL.md) | Skill, CLI, runtime e providers avaliados separadamente |
| Operação que precisa de inspeção da interface | [Computer use](../../vibeediting-computer-use/SKILL.md) | Ferramenta disponível, app permitido e janela observada |

Host local e serviço remoto não são equivalentes: Codex local suporta processos STDIO e Streamable HTTP; o navegador ChatGPT não acessa diretamente o localhost do usuário. A documentação atual oferece conexões remotas e caminhos de túnel próprios, que requerem configuração e autorização específicas [H1]. Não abra túnel ou porta como solução implícita.

## 3. Montar o plano de montagem
Proponha uma unidade pequena de revisão, com origem e destino claros. Para cada trecho, registre a fala que deve sobreviver, o motivo do corte, a cobertura visual e uma condição de falha. Defina se o corte desloca os trechos seguintes ou preserva lacunas. Fixe o referencial de tempo: origem, timeline ou exportação, com a taxa de quadros quando disponível.

Um pedido como retirar hesitações não autoriza reescrever a fala, remover ressalvas ou inventar um depoimento. O rough cut deve demonstrar continuidade e sentido antes de títulos, música e efeitos. Revisões por timestamp devem trazer também uma frase ou cena âncora, pois o tempo muda após cortes anteriores.

## 4. Usar estados com evidência

| Estado | O que registrar | O que ainda não comprova |
|---|---|---|
| documentado | Guia e fonte consultados | Software disponível |
| configuracao_proposta | Exemplo adaptado ao host, sem aplicação | Instalação ou conexão |
| instalado | Versão e caminho observados | App acessível ao agente |
| conectado_leitura | Resposta de ferramenta sobre o alvo correto | Edição concluída |
| teste_controlado | Alteração autorizada, readback e reversibilidade | Produção final |
| executado_verificado | Operação, alvo, versão e verificação | Aprovação estética ou publicação |
| revisao_pendente | Cobertura que falta | Falha ou aprovação automática |

Esses estados implementam [operação segura](../../references/operacao-segura.md). Não são campos de uma API externa. Uma operação pode estar salva no projeto e ainda não ter confirmação visual; registre resultado_incerto ou revisão pendente em vez de repetir a escrita.

## 5. Distinguir as decisões remotas
No Motion, upload e criação de vídeo são ferramentas distintas [M1]. No Hypit, a skill ensina o fluxo, mas o executável e os serviços têm preparação e custos próprios [HY1]. Transforme isso em decisões concretas: quais bytes podem ser enviados, para onde, qual resultado será pedido e qual gasto está coberto. Não use o saldo como autorização.

## 6. Fazer o handoff
Entregue ao próximo operador: caminho do projeto, versão, materiais aprovados, trechos alterados, estado das aprovações, operações com resultado incerto e critério de aceitação. Preserve a relação entre fonte, projeto e exportação. Evite reenviar todo o contexto quando apenas um trecho mudou.

Use o [brief](../../templates/brief-video.yaml), a [entrevista](../../video-entrevista/SKILL.md) e a [revisão final](../../video-revisao-exportacao/SKILL.md). Se faltar capacidade de áudio/vídeo, o handoff deve pedir revisão humana com cobertura definida, sem alegar que o agente assistiu e escutou tudo.

## Fontes e limites
- H1 — [OpenAI: MCP no host Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). Seções de hosts e transportes lidas; não testa este computador.
- HY1 — [Hypit: Quickstart](https://hypit.ai/quickstart/). Seções de skill, serviços e custo lidas; não é evidência de geração.
- M1 — [Motion: MCP](https://docs.motion.so/guides/mcp). Seções de ferramentas e OAuth lidas; disponibilidade depende da conexão real.
- [Tutoriais locais de referência: Resolve](../../../../../Tutoriais/criacao-de-videos/edicao-com-ia/vibe-editing-com-codex-e-davinci-resolve.md), [Hypit](../../../../../Tutoriais/criacao-de-videos/edicao-com-ia/hypit-clonar-videos-com-workflows-no-codex.md) e [Motion](../../../../../Tutoriais/criacao-de-videos/edicao-com-ia/motion-mcp-chatgpt-design-de-movimento.md) foram lidos integralmente como pistas. Não houve nova leitura dos posts/vídeos do X citados neles.

[Voltar à skill](../SKILL.md).
