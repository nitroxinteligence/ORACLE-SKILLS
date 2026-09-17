---
name: oracle-skill-f8407b49aeae29485eb6
description: "Opere uma interface de edição de vídeo por observação e ações curtas quando uma integração estruturada não bastar. Verifique ferramenta, app permitido, janela, projeto e foco; deixe permissões de sistema e login ao humano."
metadata:
  departamento: conteudo
  especialista: criacao-de-video
  skill-id: CON-VID-09
  versao: "1.0.0"
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->
# Computer use para edição de vídeo

## Entrada
Aplicativo e projeto autorizados, operação específica, host/sistema, estado salvo e ferramenta desktop disponível. O Computer Use oficial OpenAI e o conector Chat On Steroids Desktop são superfícies distintas; não presuma que habilitar uma ativa a outra.

## Leitura necessária
Leia [operação segura](../references/operacao-segura.md) e [guia de interação](references/guia.md). Use documentação oficial para o host e o schema real das ferramentas. Nenhum modelo alternativo ou override é requisito inventado desta skill.

## Perguntas por lacunas
Qual janela/projeto pode ser operado? Qual alteração está autorizada? A ferramenta desktop está disponível e o aplicativo permitido? Existe cópia salva? Qual resultado visual ou estrutural deve confirmar a ação? Não peça senha nem automatize consentimentos.

## Procedimento
1. Confirme o host, o sistema e a ferramenta existente. Descubra sua interface antes de assumir acesso ao desktop. Se faltar componente ou permissão, explique a dependência e mantenha execução não iniciada; não instale ou configure como efeito colateral.
2. Deixe o humano conceder Screen Recording, Accessibility, permissão de aplicativo, login e MFA quando necessários. Não clique nos consentimentos, não controle o próprio host para contorná-los e não altere modelo por suposição.
3. Obtenha uma observação recente da janela autorizada e confirme aplicativo, projeto, timeline/composição e estado salvo. Evite capturar ou ler janelas pessoais sem relação com a tarefa.
4. Defina uma ação curta, seu alvo e resultado esperado. Prefira elemento de interface identificado; quando coordenadas forem necessárias, associe-as à observação atual e não reutilize após mudança de layout, zoom, scroll ou modal.
5. Confirme foco antes de atalho ou arraste. Em uma edição autorizada, use cópia do projeto e faça apenas a mudança planejada; não encadeie muitos cliques sem observar o efeito intermediário.
6. Capture/leia o estado depois da ação e compare com o esperado. Diferencie feedback visual de persistência no projeto; uma janela que mudou não comprova gravação ou exportação concluída.
7. Diante de ambiguidade, observe novamente e reconcilie. Pare em projeto errado, diálogo destrutivo, tela de autenticação, pagamento ou permissão de sistema; preserve o trabalho parcial e não tente fechar o obstáculo às cegas.
8. Entregue registro de ação, alvo, evidência e cobertura. Para playback, marque se houve som e vídeo efetivamente percebidos; capturas de frames não equivalem a assistir tudo. Encaminhe exportação à [revisão](../video-revisao-exportacao/SKILL.md).

## Erros e recuperação
Foco perdido: nova observação e confirmação antes de repetir atalho. Modal inesperado: ler conteúdo e determinar consequência, sem Enter/Escape automático. Coordenada obsoleta: relocalizar o alvo. Resultado incerto: consultar o projeto antes de repetir mutação. Ferramenta ausente: manter plano, sem simular interação.

## Entregável
Plano ou sequência de ações observadas, janela/projeto identificados, estado salvo verificado quando possível, limites de percepção e pendências humanas. Não registre segredos, telas de login ou dados alheios como evidência desnecessária.

## Critérios de aceite
Cada ação tem alvo e consequência observados; permissões foram humanas; originais estão preservados; falhas não foram contornadas; nenhum clique, playback ou salvamento foi inventado. O acesso ao desktop não concede publicação ou gasto.
