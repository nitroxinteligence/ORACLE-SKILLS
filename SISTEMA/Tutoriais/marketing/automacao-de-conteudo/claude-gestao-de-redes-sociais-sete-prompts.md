---
title: "Claude para gestão de redes sociais: fluxo completo com sete prompts"
slug: claude-gestao-de-redes-sociais-sete-prompts
language: pt-BR
type: tutorial
category: marketing
subcategory: automacao-de-conteudo
source: https://x.com/pushkersoni72/status/2099772824210817044
source_author: "Pushker Soni (@pushkersoni72)"
source_published_at: "2026-09-15T08:10:27Z"
related_threads:
  - https://x.com/pushkersoni72/status/2029448168304460230
  - https://x.com/pushkersoni72/status/2061700492208853182
  - https://x.com/pushkersoni72/status/2067556004737491410
  - https://x.com/pushkersoni72/status/2080517518360453253
captured_at: 2026-09-16
capture_method: agent-reach/opencli-twitter
tags:
  - claude
  - social-media
  - automacao-de-conteudo
  - estrategia-de-conteudo
  - calendario-editorial
  - prompts
  - comunidade
  - metricas
---

# Claude para gestão de redes sociais: fluxo completo com sete prompts

A thread de Pushker Soni reúne sete prompts para usar o Claude como assistente
de redes sociais. A sequência cobre estratégia, pilares, calendário, posts,
vídeos curtos, comunidade e otimização.

O valor está em usar os prompts como etapas conectadas:

```text
contexto da marca
→ estratégia
→ pilares editoriais
→ calendário de 30 dias
→ produção de cada peça
→ adaptação para vídeo curto
→ interação com a comunidade
→ análise dos resultados
→ nova rodada
```

Prompts isolados não colocam uma conta em “piloto automático”. Eles produzem
planos e rascunhos. Publicar, responder pessoas, acessar métricas e operar
plataformas exige integrações, permissões e critérios de aprovação separados.

## O que apareceu nas threads relacionadas

O autor publicou versões muito semelhantes do mesmo conjunto em março, junho,
julho e setembro de 2026. As versões de junho e setembro repetem os sete
estágios centrais.

As respostas às publicações acrescentam limites úteis:

- uma pessoa relatou que o conteúdo programado funcionou, mas conversas reais
  nas respostas continuaram exigindo intervenção humana;
- outra sugeriu fornecer cinco posts de melhor desempenho e pedir a extração
  dos padrões antes de gerar novos textos;
- vários comentários observaram que estratégia, voz de marca e qualidade
  criativa não surgem automaticamente de um prompt genérico.

Este tutorial incorpora essas correções ao fluxo original.

## 1. Prepare o pacote de contexto

Antes dos sete prompts, reúna:

```text
contexto-da-marca/
├── negocio.md
├── oferta.md
├── publico.md
├── voz-da-marca.md
├── produtos-e-provas.md
├── concorrentes.md
├── restricoes.md
├── melhores-posts.md
├── posts-fracos.md
└── metricas.csv
```

### Negócio

- produto ou serviço;
- modelo de receita;
- diferenciais comprováveis;
- mercado e localização;
- prioridades atuais.

### Público

- situação atual;
- problema;
- objetivo;
- objeções;
- linguagem usada;
- plataformas frequentadas.

### Voz

- tom;
- vocabulário recorrente;
- frases a evitar;
- nível de formalidade;
- exemplos aprovados;
- posição sobre promessas e exageros.

### Restrições

- afirmações que exigem fonte;
- dados privados;
- temas regulados;
- marcas que não podem ser citadas;
- palavras proibidas;
- ações que exigem aprovação.

Sem esse contexto, o modelo tende a produzir conteúdo médio e intercambiável.

## 2. Extraia a voz antes de gerar

Use os cinco melhores posts e alguns exemplos fracos.

```text
Analise os exemplos fornecidos e crie um guia de voz para esta marca.

Separe:
- padrões de abertura;
- tamanho e ritmo das frases;
- vocabulário característico;
- estrutura do argumento;
- uso de histórias, exemplos e provas;
- tipos de CTA;
- características que devem ser preservadas;
- hábitos que tornam o texto genérico ou artificial.

Compare os melhores posts com os posts fracos. Para cada conclusão, mostre o
exemplo que sustenta a análise. Não crie novos posts ainda.
```

Revise o guia e salve a versão aprovada em `voz-da-marca.md`.

## 3. Prompt 1 — arquiteto da estratégia

O primeiro prompt da thread pede análise de negócio, nicho, público,
concorrentes e objetivos. Torne o resultado verificável:

```text
Atue como estrategista de redes sociais para esta marca.

Use os arquivos de contexto fornecidos. Analise:
- negócio e oferta;
- público e estágio de consciência;
- concorrentes;
- plataformas atuais;
- objetivos dos próximos 90 dias;
- recursos e limitações da equipe.

Entregue:
1. diagnóstico atual;
2. posicionamento em uma frase;
3. promessa editorial;
4. públicos prioritários;
5. plataformas recomendadas e função de cada uma;
6. oportunidades de crescimento;
7. riscos e hipóteses ainda não comprovadas;
8. métricas por objetivo;
9. plano de experimentos para quatro semanas.

Não invente dados sobre concorrentes ou público. Marque cada suposição.
```

### Saída esperada

| Campo | Exemplo de decisão |
|---|---|
| Objetivo | gerar conversas qualificadas |
| Público | fundadores com problema específico |
| Plataforma | X para descoberta e LinkedIn para autoridade |
| Promessa | uma transformação clara e demonstrável |
| Métrica | respostas qualificadas e leads, além de alcance |
| Experimento | testar três ângulos de abertura |

## 4. Prompt 2 — pilares de conteúdo

O segundo prompt pede cinco pilares e ideias que eduquem, entretenham ou
inspirem. Acrescente função e prova.

```text
Com base na estratégia aprovada, proponha cinco pilares editoriais.

Para cada pilar, informe:
- nome;
- papel na jornada do público;
- problema que resolve;
- ponto de vista da marca;
- evidências e fontes que podem sustentá-lo;
- formatos adequados;
- dez ideias de conteúdo;
- CTA compatível;
- sinais de repetição ou saturação.

Distribua os pilares entre educação, prova, opinião, bastidores e conversão.
Evite ideias que poderiam pertencer a qualquer marca do nicho.
```

Matriz recomendada:

| Pilar | Objetivo | Fonte | Formato | CTA |
|---|---|---|---|---|
| Educação | gerar compreensão | pesquisa ou experiência | carrossel/thread | salvar |
| Prova | reduzir objeção | caso real | vídeo/post | conversar |
| Opinião | diferenciar | tese da marca | post curto | responder |
| Bastidores | criar confiança | processo real | vídeo/foto | acompanhar |
| Oferta | converter | produto e evidência | demo/case | solicitar acesso |

## 5. Prompt 3 — calendário de 30 dias

O terceiro prompt transforma pilares em um calendário com formato e objetivo.

```text
Crie um calendário editorial de 30 dias usando somente a estratégia e os
pilares aprovados.

Para cada dia, informe:
- data;
- plataforma;
- pilar;
- tema;
- ângulo;
- formato;
- estágio da jornada;
- objetivo;
- fonte necessária;
- CTA;
- responsável;
- status.

Regras:
- evite repetir o mesmo ângulo na mesma semana;
- alterne conteúdo de descoberta, confiança e conversão;
- reserve espaços para notícias e aprendizados recentes;
- não invente estudos, depoimentos ou resultados;
- marque como bloqueado qualquer item sem fonte ou material.

Entregue em tabela e também em CSV.
```

### Colunas mínimas

```csv
date,platform,pillar,topic,angle,format,funnel_goal,source,cta,owner,status
```

O calendário é uma hipótese de distribuição. Não precisa permanecer intacto por
30 dias quando dados novos aparecem.

## 6. Prompt 4 — criação de um post

O quarto prompt da thread pede gancho, valor claro e CTA. Evite transformar
“parar o scroll” em exagero vazio.

```text
Crie um rascunho para este item do calendário:
[COLE A LINHA APROVADA]

Use a voz da marca e estas fontes:
[FONTES]

Estrutura:
1. abertura específica que apresente tensão, descoberta ou consequência;
2. contexto suficiente para compreender o problema;
3. ideia principal;
4. exemplo ou evidência;
5. aplicação prática;
6. CTA coerente com o objetivo.

Produza três opções de abertura e um corpo principal. Não use promessas que as
fontes não sustentam. Ao final, liste cada afirmação factual e sua origem.
```

Checklist editorial:

- [ ] o gancho corresponde ao conteúdo;
- [ ] a ideia principal aparece cedo;
- [ ] há algo específico da marca;
- [ ] fatos possuem fonte;
- [ ] o texto não imita outro criador;
- [ ] o CTA combina com o estágio da audiência;
- [ ] a linguagem soa natural em voz alta.

## 7. Prompt 5 — roteiro para vídeo curto

O quinto prompt adapta uma ideia para Reels, Shorts ou TikTok.

```text
Transforme o conteúdo aprovado abaixo em um roteiro de vídeo vertical de
[DURAÇÃO] segundos para [PLATAFORMA].

Conteúdo-base:
[TEXTO APROVADO]

Entregue uma tabela com:
- tempo;
- fala;
- imagem ou ação;
- texto na tela;
- B-roll;
- efeito sonoro quando necessário;
- fonte da afirmação;
- objetivo do trecho.

Comece com uma promessa específica nos dois primeiros segundos. Use frases
faláveis, preserve a voz da marca e encerre com um único CTA. Não invente cenas,
resultados ou depoimentos que a equipe não possa produzir.
```

Depois, grave ou produza um protótipo. Leia o texto em voz alta e ajuste o tempo
com a performance real.

## 8. Prompt 6 — engajamento e comunidade

O sexto prompt pede iniciadores de conversa, storytelling e táticas de
comunidade. Separe respostas sugeridas de respostas publicadas.

```text
Crie um plano de comunidade para os conteúdos desta semana.

Para cada publicação, entregue:
- pergunta de abertura;
- pergunta no CTA;
- três respostas de continuidade;
- perguntas frequentes previstas;
- objeções prováveis;
- resposta-base para cada objeção;
- situações que exigem resposta humana;
- situações que devem ser ignoradas, ocultadas ou escaladas.

Não publique nem responda ninguém. Gere somente rascunhos para revisão.
```

### Encaminhe para uma pessoa quando houver

- reclamação específica;
- pedido comercial;
- dado pessoal;
- crise ou acusação;
- pergunta jurídica, financeira ou médica;
- ironia ou contexto ambíguo;
- pessoa importante para a relação da marca;
- promessa que possa criar obrigação.

Conversas reais exigem contexto social e responsabilidade. A automação pode
organizar a fila e sugerir respostas, mas não deve fingir relacionamento.

## 9. Prompt 7 — otimização de performance

O sétimo prompt revisa estratégia e posts recentes. Forneça dados reais e peça
comparações justas.

```text
Analise o arquivo de métricas e os conteúdos publicados no período
[DATA INICIAL] a [DATA FINAL].

Considere:
- alcance;
- impressões;
- retenção ou tempo assistido;
- salvamentos;
- compartilhamentos;
- respostas e comentários qualificados;
- visitas ao perfil;
- cliques;
- leads;
- conversões.

Normalize por plataforma, formato, tamanho da audiência e tempo desde a
publicação. Compare conteúdos semelhantes.

Entregue:
1. padrões observados;
2. exemplos que sustentam cada padrão;
3. hipóteses, separadas de conclusões;
4. conteúdos que merecem variação;
5. conteúdos que devem ser interrompidos;
6. três experimentos para a próxima semana;
7. métrica de sucesso e duração de cada experimento.

Não atribua causalidade quando os dados mostram apenas correlação.
```

## Fluxo semanal

### Segunda-feira — diagnóstico

- atualizar métricas;
- registrar aprendizados da semana anterior;
- escolher hipóteses;
- revisar prioridades comerciais.

### Terça-feira — planejamento

- atualizar calendário;
- confirmar fontes e materiais;
- distribuir responsáveis;
- bloquear itens sem evidência.

### Quarta-feira — produção

- gerar rascunhos;
- produzir carrosséis e roteiros;
- revisar voz e fatos;
- adaptar formatos por plataforma.

### Quinta-feira — aprovação

- revisar conteúdo;
- verificar links e fontes;
- aprovar ou rejeitar cada peça;
- programar apenas o que foi aprovado.

### Sexta-feira — comunidade e análise

- responder conversas relevantes;
- encaminhar casos sensíveis;
- coletar dados iniciais;
- registrar correções para o próximo ciclo.

## Como transformar os prompts em um sistema

Use estados explícitos:

```text
ideia
→ pesquisando
→ rascunho
→ revisão factual
→ revisão de marca
→ aprovado
→ programado
→ publicado
→ analisado
```

O modelo pode mover conteúdo até `rascunho`. Uma pessoa ou regra previamente
autorizada decide `aprovado`. A ferramenta de agendamento executa
`programado`. Métricas reais alimentam `analisado`.

Guarde por peça:

- briefing;
- fontes;
- versão do prompt;
- rascunhos;
- aprovação;
- data de publicação;
- URL publicada;
- métricas;
- aprendizados.

## O que “autopilot” não prova

A thread não demonstra:

- integração do Claude com contas sociais;
- agendamento automático;
- publicação automática;
- resposta autônoma a comentários;
- acesso a métricas;
- comparação real com um profissional de US$ 700 por hora;
- ausência de custo do modelo ou das ferramentas.

Os sete prompts são um roteiro de raciocínio. Para operar contas, você ainda
precisa configurar plataformas, consentimentos, credenciais, limites e
aprovação.

## Relação com o pipeline de pesquisa

Este fluxo começa no contexto da marca. Para descobrir conteúdos recentes,
transcrever vídeos, analisar padrões e trabalhar com fontes, use também:

[[pipeline-de-pesquisa-e-criacao-de-conteudo-com-agentes]]

Os dois tutoriais se complementam:

```text
pesquisa recente e fontes
→ estratégia e pilares
→ calendário
→ rascunhos
→ aprovação
→ publicação
→ métricas
→ nova pesquisa
```

## Referências

- [Thread principal de setembro](https://x.com/pushkersoni72/status/2099772824210817044)
- [Versão publicada em março](https://x.com/pushkersoni72/status/2029448168304460230)
- [Versão publicada em 2 de junho](https://x.com/pushkersoni72/status/2061700492208853182)
- [Versão publicada em 18 de junho](https://x.com/pushkersoni72/status/2067556004737491410)
- [Versão publicada em julho](https://x.com/pushkersoni72/status/2080517518360453253)

> Captura feita em 16 de setembro de 2026. As publicações relacionadas repetem
> o mesmo framework em datas diferentes. O tutorial consolida a sequência e
> acrescenta controles editoriais, dados, aprovação e limites operacionais.
