---
id: vibeediting-davinci-resolve-guia
type: playbook
status: active
area: sistema
created: 2026-09-16
updated: 2026-09-16
sensitivity: internal
sources:
  - https://www.blackmagicdesign.com/
  - https://www.blackmagicdesign.com/products/davinciresolve
  - https://github.com/samuelgursky/davinci-resolve-mcp
confidence: medium
review_after: 2026-10-16
---
# Resolve: contrato técnico, montagem e revisão

Consulta: 16 de setembro de 2026. Procedimento editorial original, informado pelo tutorial local e documentação pública. Nenhum bundle, licença, preferência, projeto ou integração instalada foi inspecionado nesta autoria.

## 1. Qual interface está disponível?
A página inicial da Blackmagic anuncia DaVinci Resolve 21.1 com integração de assistentes de IA [B1]. A página de produto consultada não forneceu o endpoint ou o schema técnico necessário para operar o MCP nativo [B2]. Não complete esses dados por analogia. Em uma tarefa operacional autorizada, localize a documentação que acompanha o aplicativo instalado e confira a configuração exibida por ele.

O repositório de Samuel Gursky é comunitário e usa a API de scripting do Resolve [R1]. O autor orienta Studio com External scripting using em Local e relata restrição de Python na edição gratuita 21.1. O relato não deve virar afirmação de homologação de todas as plataformas. Este fluxo não usa downgrade, bridge de edição gratuita ou alteração de licença para contornar a restrição.

Pin de referência recebido para o projeto comunitário: 570b9eb0d8aea8e6daff23af53585318015146f2. O README público foi lido; o hash de um checkout instalado e sua equivalência ao bundle não foram verificados. Antes de adotar um conector, confirme proprietário, revisão, dependências e contrato realmente instalado. Não confunda esse projeto com o assistente nativo do fabricante.

## 2. Diagnóstico sem modificar o projeto
Comece pela pergunta concreta: o host consegue consultar o Resolve? Depois: consegue localizar a timeline autorizada? Use os nomes e argumentos publicados pelo servidor conectado. A presença de um pacote não torna todos os métodos da Scripting API ferramentas MCP.

Registre app/edição/versão, mecanismo de conexão, resposta de leitura, timeline, FPS e início. Minimize nomes de clientes e caminhos privados no relatório. Uma resposta de transporte ou processo em execução não comprova acesso ao projeto. Se não houver um método de leitura adequado, registre a limitação e avalie inspeção por GUI autorizada.

## 3. Preparar uma alteração recuperável
Escolha uma cópia da timeline ou projeto dentro do escopo. Dê nome de versão que não colida com trabalho existente. Confirme que a cópia foi criada e selecionada; não basta a intenção de duplicar.

Defina uma tabela de edição com asset, source in/out, destino, motivo, fala preservada e observação. Diferencie segundos decimais, frames e timecode. FPS fracionário e drop-frame exigem o formato correto da interface; não arredonde 29,97 para 30 silenciosamente. Se a API exigir frames, documente o arredondamento e confira a borda do corte.

## 4. Construir o rough cut
Proponha uma sequência que entregue a mensagem aprovada. Ao reduzir hesitações, mantenha respirações necessárias, últimas sílabas e contexto. Ao remover um trecho, defina se haverá ripple e qual material posterior se moverá. Após o lote, confira início/fim dos clipes e a sincronização dos áudios vinculados.

Use revisão com duas âncoras: trecho falado e posição na versão atual. Quando uma edição anterior deslocar o tempo, recalcule a posição antes da próxima instrução. Corrija uma classe de problema por vez para facilitar comparação.

## 5. Aplicar acabamento verificável
Associe B-roll ao argumento que ilustra e preserve a voz principal quando for essa a intenção. Trabalhe com mídia fornecida ou licenciada e identificada. Não invente tela de produto para substituir gravação ausente.

Nas legendas, valide grafia, tempo de leitura, entradas e saídas. Na mixagem, ouça voz, trilha e ruído em combinação; picos visuais não comprovam inteligibilidade. Em cor, preserve características do produto e pele, comparando planos equivalentes. Ausência de scopes ou áudio acessível deve aparecer como limite da revisão.

## 6. Passar para exportação
Revise os trechos alterados e depois a sequência completa quando houver capacidade. Entregue cobertura real: intervalos visualizados, áudio escutado, frames amostrados e pendências. A [revisão/exportação](../../video-revisao-exportacao/SKILL.md) verifica um arquivo final separado; salvar projeto ou acrescentar job à fila não fecha essa etapa.

## Recuperação por sintoma

| Sintoma | Próxima verificação | Limite |
|---|---|---|
| App aberto, servidor não lê | Edição, versão, interface escolhida e permissões já aprovadas | Não mudar para Network ou bridge alternativa silenciosamente |
| Timeline não corresponde ao pedido | Identificador e seleção atual | Nenhuma mutação até resolver |
| Mídia offline | Caminho autorizado e identidade do arquivo | Não buscar o vault inteiro nem trocar asset por semelhança |
| Corte retornou timeout | Readback da cópia e bordas dos clipes | Não repetir automaticamente |
| Efeito/legenda não aparece | Capacidade efetiva e resultado visual | Não declarar suporte pelo nome do método |
| Render pendente | Job existente e saída | Não criar um segundo job por falta de retorno |

## Ensaio futuro, ainda não executado
Em projeto sintético autorizado, importar dois clipes próprios, duplicar timeline, fazer um corte simples e verificar a posição antes/depois. Critério: fonte inalterada, timeline recuperável, readback coerente e inspeção visual do corte. Isso testa apenas essa operação e combinação de versões, não toda a integração.

## Fontes e limites
- B1 — [Blackmagic Design: anúncio na página inicial](https://www.blackmagicdesign.com/). Seção Introducing DaVinci Resolve 21.1 lida. Confirma o anúncio de assistentes; não descreve endpoint técnico.
- B2 — [Blackmagic: DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve). Página de produto consultada. Não comprova licença ou disponibilidade neste Mac.
- R1 — [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp). README, Quick Start e Free edition lidos; projeto comunitário, sem execução nesta revisão.
- [Tutorial local: vibe editing](../../../../../Tutoriais/criacao-de-videos/edicao-com-ia/vibe-editing-com-codex-e-davinci-resolve.md). Leitura integral. O pedido de instalar/atualizar e preços citados no tutorial não foram adotados como requisito automático.

[Voltar à skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md).
