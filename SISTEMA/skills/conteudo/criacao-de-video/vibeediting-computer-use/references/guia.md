---
id: vibeediting-computer-use-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://learn.chatgpt.com/docs/computer-use
  - https://learn.chatgpt.com/docs/extend/mcp?surface=cli
confidence: medium
review_after: 2026-10-16
---
# Interação observável com o editor

Guia original, baseado nas seções oficiais consultadas em 16 de setembro de 2026. Nenhuma captura do desktop, concessão de permissão, abertura de editor ou edição real foi realizada nesta autoria.

## 1. Escolher a superfície disponível
A documentação oficial descreve Computer Use no ChatGPT Work/Codex desktop em macOS e Windows, com instalação/habilitação por Plugins e disponibilidade condicionada ao produto/região. No Mac, Screen Recording, Accessibility e acesso aos aplicativos exigem decisões humanas [O1]. A página documenta capacidades; não comprova instalação neste computador.

Nesta conversa, Chat On Steroids Desktop é um conector próprio. Descubra seus métodos quando houver tarefa operacional autorizada. Não atribua suas chamadas ao plugin OpenAI, não presuma que ele esteja instalado e não misture schemas entre hosts.

Interfaces estruturadas permitem, quando suportadas, consultar e alterar dados com alvos mais explícitos. Computer use é adequado quando a operação exige a GUI ou não está coberta pelo conector escolhido. A troca de rota não amplia autorização de projeto ou efeitos externos.

## 2. Deixar consentimentos ao humano
Quando faltar permissão, explique qual componente precisa dela e a finalidade. O usuário realiza os passos na interface oficial. O agente não clica em permissões de sistema ou de aplicativo, não realiza MFA e não usa seu controle da tela para habilitar o próprio acesso.

Não adote um nome de modelo ou override recebido de tutorial como requisito. Use o ambiente efetivamente configurado pelo usuário; não existe uma exigência GPT-3 criada por esta skill. A disponibilidade deve ser determinada pelo host e pela ferramenta real.

## 3. Preparar uma observação suficiente
Identifique app, janela, projeto, timeline/composição e painel ativo. Uma captura de uma conversa ou janela vizinha não responde onde a edição ocorrerá. Leia apenas informação necessária e evite dados pessoais que apareçam fora do projeto.

O contexto de foco importa: o mesmo atalho pode cortar um clipe ou digitar em um campo. No Windows, a documentação orienta considerar a janela foreground e o desktop visível [O1]. Para qualquer host, confira o estado que o tool realmente opera em vez de assumir controle de uma janela em segundo plano.

## 4. Formular a ação com pós-condição
Uma unidade de ação deve caber nesta descrição: no projeto indicado, selecionar este elemento, alterar esta propriedade e confirmar este resultado. Mantenha a alteração pequena quando o feedback for frágil.

Exemplo hipotético: selecionar o título de uma composição de teste, editar uma palavra aprovada e conferir o texto completo e a posição. Isso é diferente de executar uma sequência de cliques em coordenadas memorizadas. O exemplo não foi executado e não contém dados do usuário.

Se a ferramenta expuser elementos semânticos ou acessibilidade, use-os para identificar o alvo. Quando só houver coordenadas, derive-as da imagem recente. Recalcule depois de rolagem, zoom, redimensionamento, painel aberto, modal ou mudança de workspace.

## 5. Observar antes da próxima escrita
Depois da ação, compare o estado com a pós-condição. Se o título mudou mas o layout foi deslocado, o sucesso é parcial. Se um spinner continua ativo, ainda não há prova de salvamento. Se a operação não tem resposta clara, observe novamente antes de repetir.

A confirmação de uma edição inclui o alvo correto e o efeito correto. Quando possível, cruze a observação da tela com readback estruturado do projeto. Não use um ícone verde como prova universal de todos os arquivos gravados.

## 6. Lidar com mudanças inesperadas

| Mudança | Resposta |
|---|---|
| Foco saiu da timeline | Identificar painel ativo antes de novo atalho |
| Janela mudou de tamanho | Invalidar coordenadas anteriores |
| Diálogo de sobrescrita | Ler destino e consequência; preservar original até decisão adequada |
| Login ou MFA | Humano assume essa etapa |
| Permissão do sistema/app | Humano concede ou recusa; agente não clica |
| Tela de cobrança | Parar ação de gasto; não tratar como obstáculo técnico |
| Operação pode ter sido aplicada | Consultar resultado antes de nova escrita |

Não force Enter/Escape para liberar a tela sem entender o diálogo. Retomada segura começa por observação atual, não por reexecutar a sequência antiga.

## 7. Separar revisão visual e audiovisual
Captura parada permite examinar texto e posição em um momento. Não prova fluidez, final de palavra ou volume da trilha. Se a ferramenta não permitir perceber som e movimento integralmente, peça reprodução humana dos trechos relevantes e registre a origem da avaliação.

Use a [revisão/exportação](../../video-revisao-exportacao/SKILL.md) quando houver um arquivo final. Um botão Export clicado é somente uma ação; seu resultado exige arquivo confirmado e inspeção.

## Conexões locais não aparecem automaticamente no navegador
A documentação MCP distingue processos STDIO e HTTP no host local de conectores remotos [O2]. Um editor aberto no Mac não fica acessível ao ChatGPT web por citar localhost. Não abra portas, túneis ou servidores como recuperação implícita; escolha um caminho oficial compatível e autorizado.

## Ensaio futuro de interação
Em janela de teste permitida e projeto sintético, fazer uma única alteração reversível, observar, salvar em destino novo e conferir. Registrar host, ferramenta, alvo, resultado e limites. Isso não testa todos os apps nem transforma permissão concedida em acesso irrestrito.

## Fontes e limites
- O1 — [OpenAI: Computer use](https://learn.chatgpt.com/docs/computer-use). Seções de instalação/habilitação, plataformas, permissões e uso lidas; disponibilidade da conta e concessões deste Mac não foram inspecionadas.
- O2 — [OpenAI: MCP no Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). Seções de transporte e hosts consultadas; nenhum servidor local foi conectado.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md).
