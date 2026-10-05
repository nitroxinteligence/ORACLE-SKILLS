# Acervo Oracle

A branch main contém o acervo público de skills e seus recursos. A release assinada relaciona os arquivos, as licenças e as identidades de cada skill.

As mudanças aprovadas em `SISTEMA/skills` e `SISTEMA/recursos-skills` acionam o workflow de publicação. O pipeline verifica os caminhos, os recursos declarados, as licenças e o inventário completo antes de assinar uma release. Novas skills e novas licenças precisam constar em `publication-review.json`; arquivos com referências ausentes ou termos alterados bloqueiam a publicação.

O Oracle System consulta essa release e mostra a atualização em **Acervo de skills**. A instalação preserva arquivos editados no vault e coloca as versões recebidas em recuperação. Ela não instala novas versões dos motores de memória. As atualizações do software e dos componentes originais são publicadas no [canal do Oracle System](https://github.com/nitroxinteligence/ORACLE-PLUGIN).

Os grupos legados de prompts, tutoriais e fontes fixadas do aplicativo nativo são preservados com os bytes da distribuição anterior. Eles têm verificações próprias e não são novos canais na interface do Oracle System.

Executar uma skill exige um host/modelo e as ferramentas indicadas nela. Instalar o acervo não conecta contas nem executa suas instruções. As notas pessoais do vault não fazem parte desta distribuição.

As contribuições autorais têm distribuição autorizada pelo titular. As licenças e restrições de terceiros permanecem nos respectivos arquivos e no manifesto assinado. Consulte os arquivos LICENSE de cada coleção.
