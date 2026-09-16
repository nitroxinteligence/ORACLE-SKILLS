# Acervo Oracle

A branch `main` contém **261 skills em dez departamentos**, 17 prompts e 30 tutoriais. A distribuição `acervo-2026.09.13.1` permanece com 179 skills até a próxima release. Requer Oracle 0.3.3 ou posterior.

## Organização

`SISTEMA/skills/<departamento>/<especialista>/<skill>/SKILL.md`

Departamentos: Código, Conteúdo, Conversão, Entrega, Leads, Marketing, Oferta, Sistemas, Tráfego e Vendas. Em Código, `frontend` reúne as skills de frontend, incluindo Impeccable e Richard Design. Conteúdo inclui Gary Vaynerchuk e Criação de vídeo; Tráfego mantém Ann Handley e expande Frederick Vallaeys com operação conectada e supervisionada para Meta Ads e Google Ads.

`SISTEMA/recursos-skills` contém os procedimentos, scripts, referências e perfis públicos compartilhados pelas skills. Mantenha essa pasta junto do acervo para preservar os links e as dependências. As notas pessoais do vault não fazem parte desta distribuição.

O onboarding do aplicativo instala a skill geral `oracle` diretamente no Codex. Ela localiza as skills disponíveis no host e no vault selecionado; o seu código é distribuído com o [aplicativo Oracle](https://github.com/nitroxinteligence/ORACLE/tree/main/skills/oracle), sem uma segunda cópia no Obsidian.

## Distribuição

A release tem 4.423 arquivos destinados ao vault e outros 4.834 arquivos do GBrain fixado, entregues separadamente nos assets. Prompts e tutoriais foram preservados da versão anterior.

O Oracle verifica a assinatura Ed25519 do manifesto e os hashes dos arquivos antes de instalar. Alterações na branch principal só chegam ao aplicativo quando integram uma [release completa](https://github.com/nitroxinteligence/ORACLE-SKILLS/releases).

Executar uma skill exige um host/modelo e as ferramentas ou serviços indicados nela. A instalação não conecta contas nem executa os procedimentos das skills automaticamente.

## Licenças

As contribuições autorais têm distribuição autorizada pelo titular. As licenças, atribuições e restrições de terceiros foram preservadas nos recursos correspondentes e relacionadas no manifesto assinado. Richard Design mantém seus termos específicos, incluindo a restrição de uso em apostas. Consulte os arquivos LICENSE de cada coleção.
