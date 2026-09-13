---
name: oracle-skill-68769231dbce179057cc
version: 3.23.1
description: Research what people actually say about any topic in the last 30 days.
  Pulls posts and engagement from Reddit, X, YouTube, TikTok, Hacker News, Polymarket,
  GitHub, and the web. Includes a doctor health check to diagnose broken or missing
  sources.
argument-hint: last30days nvidia earnings reaction | last30days AI video tools | last30days
  what users want in react
allowed-tools: Bash, Read, Write, AskUserQuestion, WebSearch
homepage: https://github.com/mvanhorn/last30days-skill
repository: https://github.com/mvanhorn/last30days-skill
author: mvanhorn
license: MIT
user-invocable: true
metadata:
  openclaw:
    emoji: 📰
    requires:
      env: []
      optionalEnv:
      - SCRAPECREATORS_API_KEY
      - OPENAI_API_KEY
      - XAI_API_KEY
      - OPENROUTER_API_KEY
      - PERPLEXITY_API_KEY
      - PARALLEL_API_KEY
      - BRAVE_API_KEY
      - APIFY_API_TOKEN
      - AUTH_TOKEN
      - CT0
      - BSKY_HANDLE
      - BSKY_APP_PASSWORD
      - TRUTHSOCIAL_TOKEN
      - XIAOHONGSHU_API_BASE
      bins:
      - node
      - python3
    primaryEnv: SCRAPECREATORS_API_KEY
    files:
    - scripts/*
    homepage: https://github.com/mvanhorn/last30days-skill
    tags:
    - research
    - deep-research
    - reddit
    - x
    - twitter
    - youtube
    - tiktok
    - instagram
    - linkedin
    - hackernews
    - polymarket
    - digg
    - bluesky
    - truthsocial
    - xiaohongshu
    - rednote
    - trends
    - recency
    - news
    - citations
    - multi-source
    - social-media
    - analysis
    - web-search
    - hiring-signals
    - ai-skill
    - clawhub
  departamento: marketing
  especialista: analista-de-tendencias
---
<!-- Modified for Oracle distribution: skill name adapted for host discovery; upstream notices retained. -->

# last30days

Especialista digital: Analista de tendências.

Leia e aplique o [procedimento completo](../../../../recursos-skills/last-30-days/skills/last30days/SKILL.md). O original e todas as dependências permanecem juntos em `SISTEMA/recursos-skills/last-30-days/skills/last30days`. Resolva scripts, referências e caminhos relativos a partir dessa pasta de origem, conforme suas instruções. Esta entrada organiza a biblioteca; não instala ferramentas nem configura contas externas.

[[SISTEMA/skills/marketing/analista-de-tendencias/indice|Especialista]] · [[SISTEMA/skills/marketing/indice|Departamento]]
