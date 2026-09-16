---
id: "fv-meta-conectar-guia"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: ["https://pypi.org/project/meta-ads/", "https://github.com/facebook/facebook-python-business-sdk", "https://www.facebook.com/business/help/1456422242197840", "https://learn.chatgpt.com/docs/extend/mcp?surface=cli"]
confidence: "medium"
review_after: "2026-10-16"
---
# Meta Ads — conexão oficial e permissões — guia

## Caminho local de referência
Em 16/09/2026, o PyPI apresenta `meta-ads` 1.1.0 como CLI oficial, com mantenedor `facebook`, Python >=3.12 e licença proprietária. Inspecione os wheels da versão para o sistema e ABI escolhidos. Os arquivos observados não justificam uma promessa universal para Windows; no Mac há diferenças entre wheels CPython 3.12 e 3.13. Não substitua o Python do sistema.

Depois de autorização para instalar, uma opção isolada é `pipx install 'meta-ads==1.1.0'` usando um Python compatível já provisionado. O comando é uma proposta, não foi executado nesta pesquisa. Confirme com `meta --help` e `meta auth --help`; não presuma um subcomando `login` sem observar o help.

## Credenciais — procedimento para o humano
Abra os portais oficiais Meta com sua conta, confirme o negócio e a conta de anúncios e selecione o fluxo indicado para sua aplicação. Para a CLI, a documentação exige um access token e o ID `act_...`. O fluxo Marketing API pode envolver aplicativo habilitado, atribuição de ativos e permissões de leitura ou gestão. Conta própria, acesso de agência e aplicação para terceiros têm requisitos diferentes. Consulte a ajuda oficial para confirmar os nomes atuais de permissões e menus; não conceda todas por conveniência.

O usuário conclui login/MFA, registra a credencial num armazenamento privado fora de Obsidian/Git e disponibiliza ao processo apenas as variáveis necessárias: `ACCESS_TOKEN`, `AD_ACCOUNT_ID`; `BUSINESS_ID` é opcional. A IA não deve abrir o armazenamento para imprimir o valor. Não use exemplos `export TOKEN=valor-real` em um terminal registrado. Registre expiração, responsável e revogação sem o segredo.

## Primeiro teste
Descubra `meta ads adaccount --help`. As leituras documentadas incluem:
```sh
meta ads campaign list --output json
meta ads insights get --date-preset last_7d
```
Restrinja a conta pelo mecanismo verificado, não pela primeira conta retornada. A listagem não altera orçamento. Evite `--debug` e redija o retorno removendo dados desnecessários. Um erro de permissão não é evidência de conta vazia.

## Alternativa MCP
O anúncio/ajuda Meta consultado exigiu login. Não foi obtido um contrato público completo de endpoint e OAuth nesta rodada. Abra a ajuda oficial com o usuário, confira o endereço realmente oferecido e a elegibilidade; mantenha o status “documentação de conta pendente” até então. Um endereço visto em snippet não deve virar servidor automaticamente confiado. A CLI é o caminho com contrato público mais claro nesta pesquisa.

## Diagnóstico e reversão
Executável ausente: instalação ainda não realizada. Wheel incompatível: selecionar runtime compatível ou rota diferente, sem downgrade cego. Token expirado: humano reautoriza privadamente. Sem ativos: conferir atribuição da conta. Para revogar, encerre o uso do conector, invalide o token/integração no portal oficial e remova somente a configuração aprovada. Desabilitar o servidor local sozinho não invalida o token remoto.

## Evidência e limites
Pesquisa documental em 16/09/2026; não houve instalação, OAuth, teste de conta, escrita, publicação ou gasto. Consultas e exemplos são procedimentos para execução futura autorizada.

- [Meta Ads CLI oficial](https://pypi.org/project/meta-ads/)
- [SDK oficial Meta](https://github.com/facebook/facebook-python-business-sdk)
- [Ajuda oficial Meta — acesso condicionado ao login](https://www.facebook.com/business/help/1456422242197840)
- [MCP no ChatGPT/Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

[Skill](../SKILL.md) · [Operação segura](../../references/operacao-segura.md)
