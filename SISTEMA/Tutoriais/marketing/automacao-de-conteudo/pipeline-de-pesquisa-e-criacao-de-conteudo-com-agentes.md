---
title: "Pipeline de pesquisa e criação de conteúdo com agentes"
slug: pipeline-de-pesquisa-e-criacao-de-conteudo-com-agentes
language: pt-BR
type: tutorial
category: marketing
subcategory: automacao-de-conteudo
source: https://x.com/EXM7777/status/2098414759234457878
source_article: https://x.com/i/article/2098414752120913920
source_author: "Machina (@EXM7777)"
source_published_at: "2026-09-11T14:13:59Z"
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
tags:
  - automacao-de-conteudo
  - pesquisa
  - codex
  - gpt-6-astra
  - gemini
  - social-media
---

# Pipeline de pesquisa e criação de conteúdo com agentes

Um agente de conteúdo é um pipeline de pesquisa com uma etapa de escrita no final.

O erro mais comum é construir primeiro a etapa de escrita. Um pedido vazio para “criar um post viral” não oferece evidência ao modelo. Ele responde com a média do conteúdo que já conhece, produzindo textos genéricos.

A ordem correta é:

```text
descobrir o que funciona agora
→ expandir os perfis vencedores
→ obter transcrições
→ analisar os vídeos
→ carregar o contexto do negócio
→ criar o lote semanal com fontes
→ aguardar aprovação humana
→ salvar correções para a próxima rodada
```

O agente reúne evidências e cria rascunhos. A pessoa verifica as fontes, avalia a qualidade e aprova o que pode ser publicado.

Engajamento mede atenção, não verdade. Um conteúdo viral continua sendo apenas um conteúdo popular.

## Visão geral do sistema

O pipeline completo usa:

- **Last30Days:** descoberta de conteúdos recentes;
- **scrapers de plataforma:** expansão de perfis e publicações;
- **legendas e Whisper:** transformação da fala em texto;
- **Gemini:** análise visual e sonora dos vídeos com timestamps;
- **base de conhecimento:** oferta, público, voz e correções da empresa;
- **Codex com GPT-6 Astra:** agrupamento de padrões e criação de rascunhos;
- **aprovação humana:** decisão final de publicação.

```text
Last30Days
    ↓
Perfis e posts vencedores
    ↓
Scrapers de X, Instagram, TikTok e YouTube
    ↓
Legendas existentes ou transcrição com Whisper
    ↓
Análise visual com Gemini
    ↓
Contexto do negócio
    ↓
Codex + GPT-6 Astra
    ↓
Lote semanal com fontes
    ↓
Aprovação humana
```

## Dois caminhos de implementação

### Caminho rápido: Viktor no Slack

Viktor funciona como um funcionário de IA compartilhado dentro de um workspace do Slack.

A equipe adiciona o agente aos canais selecionados e envia tarefas em linguagem natural no mesmo lugar em que o trabalho acontece. O agente pode entregar:

- briefings de pesquisa;
- rascunhos de conteúdo;
- relatórios;
- rotinas semanais programadas;
- arquivos compartilhados com o conhecimento acumulado.

O acesso acompanha a participação nos canais. O agente lê um canal quando faz parte dele, e sua entrada ou saída exige aprovação explícita.

Tarefas sensíveis permanecem atrás de aprovação humana. O agente não publica somente porque concluiu uma etapa.

Correções feitas por uma pessoa podem entrar nos arquivos compartilhados e influenciar a próxima execução de toda a equipe.

### Caminho próprio: Codex com GPT-6 Astra

No sistema próprio, você controla a cadeia completa:

1. descoberta;
2. coleta;
3. transcrição;
4. análise dos vídeos;
5. conhecimento do negócio;
6. criação;
7. aprovação;
8. aprendizado entre ciclos.

## 1. Defina o trabalho do pipeline

Crie um briefing fixo:

```markdown
# Briefing do pipeline de conteúdo

## Negócio
- empresa:
- produto:
- oferta:
- preço:
- promessa:

## Público
- quem compra:
- problema principal:
- soluções já tentadas:
- conteúdos ignorados:
- objeções:

## Plataformas
- X:
- Instagram:
- TikTok:
- YouTube:
- Reddit:

## Tema da pesquisa
- tema central:
- tópicos relacionados:
- idioma:
- país:
- período:

## Entregas semanais
- quantidade de posts:
- quantidade de vídeos:
- quantidade de roteiros:
- formatos:

## Aprovação
- responsável:
- canal de revisão:
- itens proibidos sem aprovação:
```

## 2. Descubra o que está funcionando agora

Use a skill Last30Days para pesquisar um tema em:

- X;
- Instagram Reels;
- TikTok;
- YouTube;
- Reddit;
- web.

A descoberta precisa retornar:

- publicação;
- autor;
- URL;
- data;
- tema;
- visualizações;
- curtidas;
- comentários;
- compartilhamentos, quando disponíveis;
- transcrição, quando disponível;
- relevância para o assunto pesquisado.

No X, o fluxo consulta timelines e classifica por relevância temática. Também pode identificar perfis e comunidades relacionados ao tema.

No Instagram e TikTok, pesquise palavras-chave, recupere métricas e obtenha transcrições dos principais resultados.

No YouTube, use `yt-dlp` para pesquisa e legendas sem depender de uma chave de API.

Pedido para o agente:

```text
Pesquise o que teve melhor desempenho nos últimos 30 dias sobre [TEMA].

Consulte X, Instagram Reels, TikTok, YouTube, Reddit e web.

Para cada resultado, registre:
- plataforma;
- autor;
- URL;
- data;
- formato;
- métricas disponíveis;
- tema;
- gancho;
- CTA;
- transcrição disponível;
- motivo de relevância.

Ordene primeiro pela aderência ao tema e depois pela atenção recebida.
```

Fontes podem sair do ar, credenciais podem expirar e plataformas mudam a estrutura das páginas. Execute novamente apenas as fontes que falharem.

## 3. Crie uma lista curta de vencedores

Não expanda todos os resultados. Selecione os conteúdos mais úteis para o negócio.

Use uma tabela:

```markdown
| Prioridade | Plataforma | Perfil | Conteúdo | Métrica | Padrão | URL |
|---:|---|---|---|---:|---|---|
```

Critérios:

- aderência ao público;
- relação com a oferta;
- força do gancho;
- clareza da promessa;
- qualidade da prova;
- formato reproduzível;
- atenção recebida;
- recência.

## 4. Expanda os perfis vencedores

Depois da lista curta, use scrapers próprios para cada plataforma.

### X

Colete:

- perfil;
- timeline;
- texto completo;
- data;
- engajamento de cada publicação;
- mídia.

### Instagram

Colete:

- visão geral da conta;
- posts;
- Reels;
- comentários;
- métricas públicas;
- mídia.

### TikTok

Colete:

- perfil;
- vídeos publicados;
- descrições;
- visualizações;
- curtidas;
- comentários;
- mídia.

### YouTube

Colete:

- dados do canal;
- vídeos;
- títulos;
- descrições;
- métricas;
- capítulos;
- legendas existentes.

A entrada dessa camada é uma lista curta. A saída é um conjunto estruturado de perfis, posts, métricas e arquivos de mídia.

O artigo usa Apify, mas qualquer scraper que devolva dados estruturados pode cumprir a mesma função.

## 5. Transforme fala em evidência

Conteúdo curto depende muito da fala. A transcrição é uma das fontes mais ricas para descobrir:

- gancho verbal;
- promessa;
- estrutura do argumento;
- exemplos;
- prova;
- objeções;
- CTA;
- vocabulário usado pelo criador.

Use esta ordem:

```text
legenda manual
→ legenda gerada pela plataforma
→ transcrição por IA
```

No YouTube, `yt-dlp` pode baixar tanto legendas enviadas pelo autor quanto faixas geradas automaticamente.

Se nenhuma legenda utilizável existir:

1. baixe o áudio com `yt-dlp`;
2. transcreva com Whisper local ou por API;
3. preserve timestamps;
4. vincule cada trecho à URL do vídeo.

Pedido:

```text
Obtenha a transcrição deste vídeo usando a seguinte ordem:

1. legenda manual;
2. legenda automática da plataforma;
3. Whisper, somente se nenhuma legenda utilizável existir.

Preserve timestamps e indique qual método produziu o texto.
```

Uma legenda vazia por falha de conexão é diferente de um vídeo sem faixa de legenda. No segundo caso, o texto ainda precisa ser gerado.

A origem das requisições também interfere. O artigo cita um benchmark no qual a conexão residencial recuperou todas as transcrições, enquanto datacenter e ausência de proxy causaram falhas.

## 6. Faça o Gemini assistir aos vídeos

A transcrição explica o que foi dito, mas não mostra:

- primeiro quadro do gancho;
- velocidade dos cortes;
- mudança de cenas;
- prova exibida na tela;
- textos visuais;
- enquadramento;
- música;
- emoção da voz;
- sons que não são fala.

Use Gemini para descrever, segmentar e extrair informações do vídeo com timestamps.

Pedido:

```text
Analise este vídeo e crie um mapa temporal.

Para cada trecho, informe:
- timestamp inicial e final;
- gancho visual;
- gancho verbal;
- enquadramento;
- mudança de cena;
- ritmo dos cortes;
- texto na tela;
- prova mostrada;
- emoção da fala;
- música ou sons relevantes;
- CTA.

Explique como os elementos visuais e sonoros trabalham juntos.
```

### Modo estático

É o modo padrão. O modelo amostra o vídeo a aproximadamente um quadro por segundo em uma única passagem.

É adequado para vídeos curtos com menos movimento. Ações rápidas podem perder detalhes nessa taxa.

### Modo agentic

Nos modelos Flash mais novos, o modo agentic permite que o modelo percorra a timeline, volte aos trechos importantes e use mais quadros onde necessário.

Em conteúdo longo, o artigo relata menor uso de tokens e uma pequena melhora de precisão.

Se um nicho usa cortes muito rápidos, aumente a taxa de quadros na configuração.

Na camada gratuita, o artigo informa limite de oito horas diárias de vídeos do YouTube e suporte somente a vídeos públicos.

## 7. Crie a base de conhecimento do negócio

Evidência de mercado é metade da entrada. A outra metade é o contexto da empresa.

Crie estes arquivos:

```text
knowledge/
├── oferta.md
├── publico.md
├── voz.md
├── exemplos-aprovados.md
├── angulos-rejeitados.md
└── correcoes-permanentes.md
```

### `oferta.md`

Registre em um parágrafo:

- produto;
- preço;
- promessa;
- mecanismo;
- resultado esperado.

### `publico.md`

Inclua:

- quem compra;
- o que já tentou;
- principais dores;
- objeções;
- conteúdos que costuma ignorar;
- linguagem utilizada.

### `voz.md`

Inclua posts reais publicados pela empresa e marque:

- bom;
- ruim;
- motivo;
- padrão que deve continuar;
- padrão que deve ser evitado.

### `exemplos-aprovados.md`

Guarde conteúdos que representam o gosto e a qualidade desejados.

### `angulos-rejeitados.md`

Registre ideias que a empresa não quer repetir e explique o motivo.

### `correcoes-permanentes.md`

Cada observação que seria repetida ao agente deve virar uma regra reutilizável.

Essa base diferencia um agente que escreve para a empresa de um agente que escreve genericamente para a categoria.

## 8. Agrupe padrões

Depois da coleta, peça ao Codex para transformar resultados isolados em padrões.

```text
Agrupe os conteúdos pesquisados por padrões recorrentes.

Para cada padrão, informe:
- nome;
- plataformas onde aparece;
- público provável;
- tipo de gancho;
- estrutura;
- prova;
- CTA;
- exemplos com URLs;
- linhas da transcrição;
- timestamps da análise visual;
- relação possível com nossa oferta.
```

Exemplos de padrões:

- afirmação contrária ao senso comum;
- demonstração antes da explicação;
- erro comum seguido por correção;
- comparação entre antes e depois;
- tutorial em etapas;
- bastidores do processo;
- prova visual com resultado;
- história pessoal que leva à oferta.

## 9. Proponha ângulos para a oferta

Cada ângulo deve combinar:

```text
padrão observado
+ problema do público
+ mecanismo da oferta
+ prova disponível
```

Pedido:

```text
Use os padrões da pesquisa e a base de conhecimento do negócio para propor
[QUANTIDADE] ângulos de conteúdo.

Para cada ângulo, inclua:
- público;
- problema;
- promessa;
- gancho;
- formato;
- prova disponível;
- relação com a oferta;
- fontes que sustentam o padrão.

Não escreva o conteúdo completo ainda.
```

## 10. Crie o lote semanal com recibos

Depois da aprovação dos ângulos, o Codex com GPT-6 Astra cria os rascunhos.

Cada peça deve conter:

- plataforma;
- formato;
- gancho;
- corpo;
- prova;
- CTA;
- fonte original;
- trecho da transcrição;
- timestamp da análise visual;
- relação com a oferta;
- status de aprovação.

Modelo:

```markdown
# Peça [número]

## Plataforma e formato

## Público

## Ângulo

## Gancho

## Rascunho

## CTA

## Recibos
- post de origem:
- transcrição:
- timestamp do vídeo:
- dado do perfil:

## Relação com a oferta

## Status
Aguardando aprovação humana.
```

Prompt:

```text
Crie o lote semanal somente a partir dos ângulos aprovados.

Para cada rascunho:
- adapte o formato à plataforma;
- use a voz documentada da empresa;
- conecte o padrão pesquisado à oferta;
- anexe URLs, linhas da transcrição e timestamps;
- marque claramente inferências;
- pare ao concluir os rascunhos.

Não publique, não agende e não envie nada. Aguarde aprovação humana.
```

Os recibos permitem abrir a publicação que sustenta o padrão. Quando não houver fonte, transcrição ou timestamp, a linha deve ser tratada como criação do modelo.

## 11. Mantenha a aprovação humana

A etapa final deve permanecer separada da geração.

O responsável avalia:

- se a fonte sustenta a afirmação;
- se o padrão combina com o público;
- se o texto representa a empresa;
- se a prova pode ser usada;
- se o CTA está correto;
- se existem riscos jurídicos, reputacionais ou comerciais;
- se a peça deve ser aprovada, corrigida ou rejeitada.

Use estes estados:

```text
rascunho
→ em revisão
→ correção solicitada
→ aprovado
→ agendado
→ publicado
```

O agente para em `rascunho`. Uma pessoa decide a passagem para `aprovado`.

## 12. Faça cada ciclo melhorar o seguinte

Uma execução produz um lote. O ativo é o ciclo acumulado.

Após a revisão:

1. salve os conteúdos aprovados;
2. salve os conteúdos rejeitados;
3. transforme correções recorrentes em regras;
4. atualize a base de voz;
5. registre novos exemplos;
6. compare os vencedores da semana com a biblioteca anterior;
7. repita a pesquisa em uma agenda definida.

Pedido:

```text
Compare o lote revisado com as regras atuais da base de conhecimento.

Transforme as correções do editor em:
- regra permanente;
- preferência contextual;
- exemplo aprovado;
- ângulo rejeitado;
- observação válida apenas para esta campanha.

Atualize os arquivos correspondentes para que a próxima rodada comece mais
próxima do resultado aprovado.
```

## 13. Programe a rotina semanal

```text
Segunda-feira
Descobrir conteúdos dos últimos 30 dias.

Terça-feira
Expandir perfis e coletar posts, métricas e mídia.

Quarta-feira
Obter transcrições e executar análises de vídeo.

Quinta-feira
Agrupar padrões, propor ângulos e criar o lote.

Sexta-feira
Revisar, aprovar e registrar correções.
```

No caminho com Viktor, a tarefa pode ser agendada no Slack. No caminho próprio, o mesmo fluxo pode ser acionado no Codex por uma rotina periódica.

## Limites do pipeline

### X

- a cobertura é parcial;
- algumas publicações não aparecem na pesquisa;
- a timeline pública ranqueada não representa um arquivo completo.

### Instagram

- perfis privados não podem ser coletados;
- métricas públicas são retratos de uma sessão sem login.

### TikTok

- a extração de comentários pode ficar incompleta.

### YouTube

- extração de legendas possui falhas conhecidas;
- alguns vídeos não têm faixa de legenda;
- uma faixa ausente exige geração por transcrição.

### Gemini

- amostragem de um quadro por segundo pode perder movimentos rápidos;
- texto exibido na tela pode ser lido incorretamente;
- capturas estáticas do mesmo trecho podem funcionar melhor;
- limites de duração dependem da plataforma e do modelo.

### Scrapers

- paginação, limites e preços mudam;
- credenciais expiram;
- páginas mudam de estrutura;
- resultados precisam ser atualizados periodicamente.

### Publicação

- o agente classifica atenção;
- a pessoa responde pela verdade;
- a publicação continua atrás de aprovação humana.

## Planilha de execução

```markdown
| Etapa | Entrada | Ferramenta | Saída | Responsável | Status |
|---|---|---|---|---|---|
| descoberta | tema | Last30Days | lista curta | agente |  |
| expansão | perfis | scrapers | dados estruturados | agente |  |
| transcrição | vídeos | captions/Whisper | texto com tempo | agente |  |
| análise visual | vídeos | Gemini | mapa temporal | agente |  |
| contexto | base da empresa | arquivos | regras e exemplos | humano |  |
| criação | evidências | Codex/Astra | lote com recibos | agente |  |
| aprovação | lote | revisão | aprovado/rejeitado | humano |  |
| aprendizado | correções | base da empresa | regras atualizadas | agente + humano |  |
```

## Prompt completo para o agente

```text
Execute o pipeline semanal de conteúdo nesta ordem:

1. Pesquise o que funcionou nos últimos 30 dias sobre [TEMA] em X, Instagram,
TikTok, YouTube, Reddit e web.

2. Classifique os resultados por aderência ao tema e atenção recebida.

3. Selecione os vencedores e expanda seus perfis, publicações, métricas e mídia.

4. Obtenha transcrições com esta prioridade: legenda manual, legenda automática
e Whisper como último recurso.

5. Use Gemini para mapear gancho, ritmo, cenas, provas e CTA com timestamps.

6. Leia os arquivos oferta.md, publico.md, voz.md,
exemplos-aprovados.md, angulos-rejeitados.md e correcoes-permanentes.md.

7. Agrupe a pesquisa em padrões e proponha ângulos que conectem esses padrões à
oferta.

8. Depois da aprovação dos ângulos, crie o lote semanal.

9. Anexe a cada peça as URLs, linhas de transcrição, métricas e timestamps que
sustentam o rascunho.

10. Marque qualquer inferência e não apresente engajamento como verdade.

11. Pare ao concluir os rascunhos. Não publique, agende nem envie conteúdo.

12. Depois da revisão humana, transforme correções recorrentes em regras para a
próxima execução.
```

## Sistema em uma linha

> Last30Days para descoberta → scrapers para perfis completos → legendas e depois Whisper para transcrições → Gemini para análise de vídeo com timestamps → Codex com GPT-6 Astra para agrupar, escrever e anexar fontes → aprovação humana.

O artigo apresenta Viktor como o caminho rápido: um funcionário de IA dentro do Slack, conectado aos scrapers, recebendo tarefas em linguagem natural, trabalhando com conhecimento compartilhado e aguardando aprovação antes de ações sensíveis.

A publicação informa parceria paga e uma oferta de teste do Viktor com US$ 100 em créditos, sem cartão.

## Fonte

- [How to automate content creation — Machina](https://x.com/EXM7777/status/2098414759234457878)
