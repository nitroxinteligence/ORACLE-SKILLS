---
id: "fv-entrevista-banco"
type: "playbook"
status: "active"
area: "sistema"
created: "2026-09-16"
updated: "2026-09-16"
sensitivity: "internal"
sources: []
confidence: "medium"
review_after: "2026-10-16"
---
# Entrevista de tráfego

Use como banco, não formulário obrigatório inteiro. Antes, leia [operação segura](operacao-segura.md). Anote cada campo como respondido por fonte, respondido pelo usuário, conflitante, não aplicável ou desconhecido. Faça blocos curtos de até cinco perguntas relevantes; aprofunde até o limite deste banco quando necessário. Não repita resposta válida nem use um mínimo artificial para travar o trabalho.

1. **resultado** — Qual resultado de negócio a campanha deve apoiar e em que horizonte?
2. **plataforma** — Você quer trabalhar com Meta Ads, Google Ads, ambos ou analisar arquivos sem conectar?
3. **host** — Vai usar ChatGPT na web, ChatGPT Desktop/Work ou Codex local? Qual sistema operacional?
4. **negocio** — Qual negócio, produto ou serviço será anunciado?
5. **publico** — Quem é o público e qual problema concreto ele precisa resolver?
6. **geografia** — Quais localidades e idiomas estão no escopo?
7. **oferta** — Qual oferta, condição e chamada para ação já foram aprovadas?
8. **prova** — Quais resultados e provas podem ser usados publicamente? Onde estão as fontes?
9. **destino** — Qual página ou fluxo receberá o clique e quem mantém esse destino?
10. **conversao** — Qual evento define sucesso: compra, lead qualificado, agendamento ou outro?
11. **qualidade** — Como a qualidade dos leads/vendas será conferida fora da plataforma?
12. **mensuracao** — Quais eventos, tag/pixel, consentimento e dados de teste já foram validados?
13. **historico** — Quais campanhas e períodos anteriores podem ser analisados?
14. **baseline** — Quais métricas atuais são confiáveis e quais ainda têm atraso ou lacunas?
15. **economia** — Quais metas e limites econômicos você autoriza usar, sem expor dados restritos desnecessários?
16. **orcamento** — Qual limite total e diário de gasto, em qual moeda, pode ser proposto?
17. **datas** — Quais datas de início/fim e fuso da conta devem valer?
18. **ativos** — Quais peças, vídeos, textos e ativos possuem autorização e direitos?
19. **restricoes** — Há restrições de marca, claims, público, produto ou setor regulado?
20. **conta** — Qual conta deve ser usada? Você possui acesso necessário e sabe distinguir conta de anúncio, negócio/MCC e projeto Cloud?
21. **acesso** — Quer somente leitura nesta etapa ou também preparar alterações para aprovação?
22. **conector** — Prefere integração oficial/local ou aceita avaliar um fornecedor externo com acesso aos dados?
23. **armazenamento** — Qual mecanismo privado fora do vault será usado para credenciais? Não envie os valores.
24. **operador** — Quem poderá aprovar conexão, alterações, ativação e gastos?
25. **criar** — As campanhas serão novas ou precisamos preservar campanhas existentes?
26. **prioridade** — Qual problema exige atenção primeiro: entrega, tracking, criativo, oferta ou segmentação?
27. **experimento** — Qual hipótese vale testar e quais variáveis devem permanecer estáveis?
28. **parada** — Quais condições autorizadas exigem interromper ou reavaliar um teste?
29. **relatorio** — Qual frequência e nível de detalhe você precisa no relatório? Recorrência só será ativada quando solicitada.
30. **limites** — O que a IA nunca deve alterar ou divulgar sem nova autorização?

## Encerramento
Faça um readback do objetivo, escopo, fontes, limites e lacunas. Peça confirmação somente dos pontos materiais ainda ambíguos. O usuário pode responder que não sabe ou delegar uma recomendação; nesse caso apresente hipóteses como hipóteses. Use o [brief](../templates/brief-trafego.yaml).
