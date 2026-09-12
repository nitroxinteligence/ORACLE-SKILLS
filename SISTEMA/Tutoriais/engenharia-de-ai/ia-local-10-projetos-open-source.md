---
title: "IA local: como escolher e começar com 10 projetos open source"
slug: ia-local-10-projetos-open-source
language: pt-BR
type: tutorial
category: engenharia-de-ai
source: https://x.com/hasantoxr/status/2098422529677521196
source_author: "Hasan Toor (@hasantoxr)"
source_published_at: "2026-09-11T14:44:52Z"
captured_at: 2026-09-12
repositories:
  - repo: https://github.com/ggml-org/llama.cpp
    commit: 3057bb66c86c46d5781e50e85462a760ba7d1feb
  - repo: https://github.com/janhq/jan
    commit: 6ccd6f4ad227cf5f0f6bfbb118729dfb4f3a8d32
  - repo: https://github.com/ollama/ollama
    commit: 53fed26112817f7c55f664efb9e3f65f06cab7db
  - repo: https://github.com/mudler/LocalAI
    commit: 832123427517cfcf4b0a89c7c78081d053225942
  - repo: https://github.com/Comfy-Org/ComfyUI
    commit: c75d8c966c29cb0392259af791f43373315b72db
  - repo: https://github.com/ml-explore/mlx-lm
    commit: dcbcf786c0cf56f9a12fabe9468c887781431ae2
  - repo: https://github.com/oobabooga/textgen
    commit: c93f8871239550de2ccfe1e95d469aa82616f07e
  - repo: https://github.com/ggml-org/whisper.cpp
    commit: 1da4dc82fa7996d4edda05890dca65aeceaafd6d
  - repo: https://github.com/exo-explore/exo
    commit: 21a54c5ea0230a3bec1e1a786d200126c7e34ec6
  - repo: https://github.com/nomic-ai/gpt4all
    commit: b666d16db5aeab8b91aaf7963adcee9c643734d7
tags:
  - ia-local
  - llm
  - apple-silicon
  - open-source
  - inferencia
  - privacidade
---

# IA local: como escolher e começar com 10 projetos open source

Este tutorial verifica e organiza os dez projetos indicados no [post de Hasan Toor](https://x.com/hasantoxr/status/2098422529677521196). A lista mistura aplicativos de chat, motores de inferência, servidores compatíveis com APIs conhecidas, geração visual, transcrição e computação distribuída. Eles não são dez etapas do mesmo processo e você não precisa instalar todos.

“Rodar por zero dólar” significa que há software disponível sem cobrança por chamada de API. Ainda existem custos de computador, energia, armazenamento e download. Cada modelo também possui sua própria licença e seus próprios requisitos, separados da licença do programa usado para executá-lo.

## Escolha rápida

| Se você quer… | Comece por | Motivo |
|---|---|---|
| conversar com um modelo numa interface de desktop | Jan ou GPT4All | instalação visual e catálogo de modelos |
| usar modelos pelo Terminal ou por uma API local simples | Ollama | fluxo curto de download, execução e API REST |
| controlar formato, quantização e desempenho em baixo nível | llama.cpp | CLI, servidor e muitos backends de hardware |
| executar ou ajustar LLMs em Apple Silicon com Python | MLX-LM | integração direta com MLX e Hugging Face |
| expor várias modalidades atrás de APIs compatíveis | LocalAI | servidor modular para texto, áudio, imagem e outros backends |
| criar fluxos visuais de imagem, vídeo, áudio ou 3D | ComfyUI | grafo de nós, templates e API local |
| usar uma interface web com vários backends e extensões | TextGen | UI, API, treinamento e ferramentas opcionais |
| transcrever áudio localmente | whisper.cpp | ASR leve em C/C++, com Metal e CPU |
| reunir vários computadores para um modelo maior | exo | descoberta e inferência distribuída |
| conversar com documentos locais em uma aplicação pronta | GPT4All | desktop, modelos locais e LocalDocs |

Para um primeiro teste em um Mac com Apple Silicon, escolha um destes caminhos:

1. **Ollama**, se você quer Terminal e integração por API;
2. **Jan**, se prefere uma aplicação visual moderna;
3. **GPT4All**, se o objetivo principal é chat e documentos locais;
4. **MLX-LM**, se você trabalha em Python e quer experimentar inferência ou ajuste fino.

## Antes de instalar

Confira chip, memória e espaço livre no macOS:

```bash
system_profiler SPHardwareDataType | grep -E 'Chip|Memory'
df -h "$HOME"
```

O tamanho do modelo não é o único consumo. O runtime também reserva memória para contexto, cache, buffers e processamento. Como referência publicada pelo Jan:

| Memória do Mac | Faixa inicial indicada pelo projeto |
|---:|---|
| 8 GB | modelos de aproximadamente 3B parâmetros |
| 16 GB | modelos de aproximadamente 7B parâmetros |
| 32 GB | modelos de aproximadamente 13B parâmetros |

Essas faixas são ponto de partida. Quantização, contexto, arquitetura do modelo e outros aplicativos abertos mudam o consumo. Comece pequeno, observe memória e velocidade e só então aumente o modelo.

## 1. llama.cpp: motor de inferência e servidor

Repositório: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

Use o llama.cpp quando você precisa de controle sobre modelos GGUF, quantização, aceleração e parâmetros de inferência. O projeto oferece CLI e servidor compatível com a API da OpenAI. Apple Silicon é tratado como plataforma principal por meio de ARM, Accelerate e Metal; também existem backends para CUDA, HIP, Vulkan, SYCL e CPU.

O início mais simples é baixar um binário da página de releases ou seguir o guia oficial de compilação. Com a CLI atual instalada, o README demonstra um modelo pequeno:

```bash
llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF
```

Para iniciar o servidor:

```bash
llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF
```

Escolha llama.cpp quando o runtime faz parte do seu produto ou quando você quer medir quantizações e backends. Para apenas conversar com um modelo, Ollama, Jan ou GPT4All reduzem a configuração inicial.

Licença do repositório: MIT. A licença do modelo GGUF continua sendo a do modelo.

## 2. Jan: chat local em aplicativo de desktop

Repositório atual: [janhq/jan](https://github.com/janhq/jan)

O endereço `menloresearch/jan` usado no post redireciona atualmente para `janhq/jan`. Jan oferece aplicativo para macOS, Windows e Linux, modelos locais, assistentes, MCP e um servidor compatível com a API da OpenAI em `localhost:1337`.

No Mac:

1. baixe o DMG pelo [site oficial do Jan](https://jan.ai/) ou pelas releases;
2. abra o aplicativo e escolha um modelo compatível com sua memória;
3. confirme que o provedor selecionado é local;
4. faça um teste sem ativar integrações em nuvem.

O Jan também aceita provedores externos. Instalar o aplicativo não significa que toda conversa será local: isso depende do modelo e do provedor escolhidos em cada configuração.

Compilar da fonte exige Node.js, Yarn, Make e Rust. Esse caminho é destinado a desenvolvimento do aplicativo, não ao primeiro uso.

Licença do repositório: Apache 2.0.

## 3. Ollama: modelos locais por CLI e REST

Repositório: [ollama/ollama](https://github.com/ollama/ollama)

O Ollama simplifica download, execução e exposição de modelos. A instalação oficial para macOS oferece DMG e script. Prefira o DMG quando quiser revisar visualmente a origem do instalador; o comando publicado pelo projeto é:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Revise scripts remotos antes de executá-los em ambientes controlados. Depois da instalação, abra o Ollama e escolha um modelo na [biblioteca oficial](https://ollama.com/library). O README atual demonstra:

```bash
ollama run gemma4
```

Verifique o tamanho da variante antes do download. Para testar a API local:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4",
  "messages": [{"role": "user", "content": "Responda apenas: API local ativa"}],
  "stream": false
}'
```

Uma resposta desse endpoint comprova que o serviço local respondeu. Ela não prova que outra aplicação já está configurada para usá-lo.

Licença do repositório: MIT. Modelos baixados pelo Ollama podem usar licenças diferentes.

## 4. LocalAI: camada de API local multimodal

Repositório: [mudler/LocalAI](https://github.com/mudler/LocalAI)

LocalAI é uma camada modular que reúne backends para texto, visão, áudio, imagem e outras modalidades atrás de APIs compatíveis com OpenAI, Anthropic e ElevenLabs. É indicado para aplicações locais ou auto-hospedadas que precisam de uma API comum e mais controles de servidor.

O caminho reproduzível publicado no README é o contêiner CPU:

```bash
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

Depois, carregue somente o backend e o modelo necessários. A primeira execução ainda pode baixar imagens de backend e pesos do modelo.

O projeto oferece um DMG para macOS, mas o próprio README informa que ele não está assinado pela Apple e propõe remover o atributo de quarentena. Não trate essa remoção como etapa automática. Verifique a procedência, a assinatura disponível e o risco antes de alterar a proteção do macOS; use contêiner ou build revisado quando essa garantia for necessária.

LocalAI tem superfície bem maior que Ollama. Use-o quando precisa de múltiplas modalidades, usuários, quotas, autenticação ou compatibilidade de APIs. Para um chat individual, a complexidade adicional pode não se pagar.

Licença do repositório: MIT.

## 5. ComfyUI: workflows visuais de geração

Repositório atual: [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)

O endereço `comfyanonymous/ComfyUI` do post redireciona para a organização atual. ComfyUI usa um grafo visual de nós para montar e reutilizar fluxos de imagem, vídeo, áudio, 3D e texto. Ele suporta execução parcial do grafo, gerenciamento de VRAM e RAM, modelos quantizados, templates e API.

Para começar no macOS ou Windows:

1. baixe o [ComfyUI Desktop](https://www.comfy.org/download);
2. abra um workflow oficial simples;
3. baixe apenas os modelos exigidos por esse workflow;
4. execute uma geração e salve o grafo em JSON;
5. adicione custom nodes somente quando o fluxo básico estiver estável.

O núcleo pode funcionar offline, mas há nós de parceiros e APIs pagas. Na instalação manual, o projeto documenta `--disable-api-nodes` para impedir o uso dos nós de API incluídos. Custom nodes são código de terceiros e devem ser revisados antes da instalação.

Licença do repositório: GPL-3.0. Modelos e custom nodes possuem licenças próprias.

## 6. MLX-LM: LLMs em Apple Silicon com Python

Repositório: [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)

MLX-LM é um pacote para gerar texto, quantizar e ajustar modelos em Macs com Apple Silicon. Ele se integra ao Hugging Face e suporta LoRA, ajuste completo, cache de prompt e execução distribuída.

Crie um ambiente isolado:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install mlx-lm
```

Inicie o chat:

```bash
mlx_lm.chat
```

O modelo padrão documentado é uma variante quantizada de 3B. Para escolher outro:

```bash
mlx_lm.chat --model mlx-community/NOME-DO-MODELO
```

Use somente identificadores que você conferiu no [MLX Community no Hugging Face](https://huggingface.co/mlx-community). Alguns tokenizers pedem `trust_remote_code`; isso permite executar código fornecido pelo repositório do modelo. Leia os arquivos antes de aceitar.

Modelos grandes em relação à memória podem ficar lentos. O README atual informa que a otimização de memória cabeada para esses casos requer macOS 15 ou superior.

Licença do repositório: MIT.

## 7. TextGen: interface web e múltiplos backends

Repositório atual: [oobabooga/textgen](https://github.com/oobabooga/textgen)

O antigo endereço `oobabooga/text-generation-webui` redireciona para `oobabooga/textgen`. O projeto oferece aplicativo local com chat, visão, anexos, API compatível, vários backends, treinamento, geração de imagem e extensões.

Para começar, use os builds portáteis da [página de releases](https://github.com/oobabooga/textgen/releases). O fluxo atual é baixar, extrair e abrir o executável `textgen`. Para uma instalação manual isolada:

```bash
git clone https://github.com/oobabooga/textgen
cd textgen
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements/portable/requirements.txt --upgrade
python server.py --portable --api --auto-launch
```

A interface abre em `http://127.0.0.1:7860`. O modo completo instala PyTorch e aproximadamente 10 GB de dependências segundo o README; use-o somente para backends, treinamento ou extensões que não existem no portátil.

O projeto afirma não usar telemetria, mas extensões e ferramentas adicionadas depois podem fazer rede. Avalie cada componente separado.

Licença do repositório: AGPL-3.0.

## 8. whisper.cpp: transcrição local

Repositório: [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

whisper.cpp executa modelos Whisper para reconhecimento de fala em C/C++. Suporta Apple Silicon com Metal e Core ML, CPU, CUDA, Vulkan, ROCm e outras plataformas.

Para transcrever português, baixe um modelo multilíngue, sem o sufixo `.en`:

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
sh ./models/download-ggml-model.sh base
cmake -B build
cmake --build build -j --config Release
```

A CLI espera WAV PCM de 16 bits no fluxo básico. Converta um MP3 com FFmpeg:

```bash
ffmpeg -i entrada.mp3 -ar 16000 -ac 1 -c:a pcm_s16le entrada.wav
```

Transcreva:

```bash
./build/bin/whisper-cli -m models/ggml-base.bin -f entrada.wav -l pt
```

O README estima cerca de 388 MB de memória para `base`, 852 MB para `small`, 2,1 GB para `medium` e 3,9 GB para `large`. Modelos maiores tendem a melhorar a qualidade, com mais tempo e memória.

Licença do repositório: MIT. Os pesos do Whisper seguem os termos publicados para o modelo.

## 9. exo: cluster de vários dispositivos

Repositório: [exo-explore/exo](https://github.com/exo-explore/exo)

exo conecta dispositivos para dividir inferência de modelos que não cabem em uma única máquina. Ele inclui descoberta automática, dashboard, API e suporte a paralelismo com MLX.

Use exo somente quando você possui vários equipamentos compatíveis e um modelo grande justifica a complexidade. Em um único Mac, Ollama, llama.cpp ou MLX-LM são caminhos mais diretos.

O aplicativo atual para macOS exige macOS Tahoe 26.2 ou posterior e solicita alterações de sistema e perfil de rede. A execução pela fonte exige Xcode, `uv`, Node.js, Rust nightly, build do dashboard e dependências MLX. Confira o README atual antes de instalar, porque os requisitos de RDMA e hardware mudam rapidamente.

Quando montar um cluster:

1. use uma rede isolada e configure um namespace próprio;
2. confirme que todos os nós enxergam somente os dispositivos esperados;
3. teste primeiro com um modelo pequeno;
4. registre versão, topologia, latência e throughput;
5. só depois tente um modelo que dependa da memória agregada.

Licença do repositório: Apache 2.0.

## 10. GPT4All: desktop e documentos locais

Repositório: [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all)

GPT4All oferece aplicativo de chat para computadores comuns, catálogo de modelos e LocalDocs para conversar com arquivos locais. O aplicativo não exige GPU e a versão atual para macOS pede Monterey 12.6 ou posterior, com melhor resultado em Apple Silicon.

Para começar:

1. baixe o instalador na [página oficial do GPT4All](https://www.nomic.ai/gpt4all);
2. selecione um modelo compatível com a memória e leia sua licença;
3. faça um chat simples antes de adicionar documentos;
4. crie uma coleção LocalDocs com arquivos sem dados sensíveis para o primeiro teste;
5. verifique as citações recuperadas antes de confiar na resposta.

Também existe cliente Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install gpt4all
```

O nome “GPT4All” não significa que o aplicativo execute o GPT-4 da OpenAI. Ele usa modelos locais compatíveis escolhidos pelo usuário.

Licença do repositório: MIT. A licença de cada modelo deve ser verificada separadamente.

## Comparação técnica

| Projeto | Interface principal | Apple Silicon | API local | Especialidade | Complexidade inicial |
|---|---|---|---|---|---|
| llama.cpp | CLI e web do servidor | Metal | compatível com OpenAI | inferência e GGUF | média |
| Jan | desktop | sim | compatível em `:1337` | chat e assistentes | baixa |
| Ollama | CLI e integrações | sim | REST em `:11434` | execução simples de modelos | baixa |
| LocalAI | servidor e UI | Metal por backend | várias APIs compatíveis | plataforma multimodal | alta |
| ComfyUI | grafo visual | sim | endpoints próprios | mídia generativa | média |
| MLX-LM | CLI e Python | exclusivo da família MLX/Apple Silicon | servidor disponível | inferência e ajuste fino | média |
| TextGen | desktop/web | sim | OpenAI e Anthropic compatíveis | múltiplos backends | média |
| whisper.cpp | CLI e biblioteca | Metal/Core ML | exemplos e integrações | transcrição | média |
| exo | dashboard e API | foco atual em MLX | várias compatibilidades | cluster distribuído | alta |
| GPT4All | desktop e Python | sim | bindings e integrações | chat e LocalDocs | baixa |

## Licenças do software

| Projeto | Licença verificada no repositório |
|---|---|
| llama.cpp | MIT |
| Jan | Apache 2.0 |
| Ollama | MIT |
| LocalAI | MIT |
| ComfyUI | GPL-3.0 |
| MLX-LM | MIT |
| TextGen | AGPL-3.0 |
| whisper.cpp | MIT |
| exo | Apache 2.0 |
| GPT4All | MIT |

Licença permissiva do runtime não transfere direitos sobre pesos, datasets, vozes, imagens geradas ou custom nodes. Para uso comercial, verifique cada componente que será distribuído ou oferecido como serviço.

## Como verificar que a execução é realmente local

1. Registre o nome exato do modelo, a quantização, a origem e a licença.
2. Conclua os downloads de pesos e backends necessários.
3. Selecione explicitamente o provedor ou modelo local no aplicativo.
4. Execute um prompt simples e registre qual processo respondeu e em qual porta.
5. Desative integrações em nuvem, web search, nós de API e extensões que não serão usados.
6. Repita o teste sem internet quando o produto declarar suporte offline.
7. Confira logs e conexões de rede se a privacidade precisar de evidência técnica.

Um endpoint em `localhost` mostra onde o cliente se conectou. Ele não prova sozinho que nenhum backend, extensão ou ferramenta chamou um serviço externo.

## Roteiro recomendado para um Mac

### Caminho A: chat local rápido

1. Instale Jan ou GPT4All pelo instalador oficial.
2. Baixe um modelo pequeno e quantizado.
3. Confirme o provedor local.
4. Teste um chat sem documentos.
5. Adicione arquivos somente depois que o modelo estiver estável.

### Caminho B: API local para automações

1. Instale Ollama.
2. Baixe um modelo adequado à memória.
3. valide `http://localhost:11434/api/chat`;
4. configure a aplicação cliente para essa URL;
5. registre separadamente a resposta do servidor e a integração do cliente.

### Caminho C: experimentação em Python

1. Crie um ambiente virtual.
2. Instale MLX-LM.
3. Rode o modelo padrão quantizado.
4. Meça tempo para primeiro token, tokens por segundo e pico de memória.
5. Troque uma variável por vez: modelo, quantização ou contexto.

### Caminho D: geração visual

1. Instale ComfyUI Desktop.
2. Use um template oficial simples.
3. Baixe somente os pesos exigidos.
4. Salve o workflow e a seed.
5. Revise custom nodes antes de adicioná-los.

## O que não instalar junto no primeiro teste

- Jan, GPT4All e TextGen cobrem experiências de chat parecidas; escolha uma interface primeiro.
- Ollama, llama.cpp e MLX-LM podem executar modelos de texto, mas atendem níveis de abstração diferentes.
- LocalAI agrega muitos backends e deve entrar quando a necessidade de servidor multimodal estiver clara.
- exo só se justifica quando há mais de um dispositivo e o modelo depende da memória ou do paralelismo agregado.
- ComfyUI e whisper.cpp resolvem modalidades específicas e podem coexistir com um runtime de texto quando houver um fluxo real que os conecte.

## Checklist

- [ ] Defini o caso de uso antes de escolher o projeto.
- [ ] Conferi chip, memória e armazenamento disponível.
- [ ] Escolhi apenas um caminho inicial.
- [ ] Li a licença do runtime e do modelo.
- [ ] Registrei repositório, commit ou versão do instalador.
- [ ] Baixei o modelo de uma origem identificada.
- [ ] Confirmei qual modelo e provedor responderam.
- [ ] Testei a porta ou processo local quando aplicável.
- [ ] Separei funcionamento local de integração com outro aplicativo.
- [ ] Desativei recursos de nuvem e extensões desnecessárias.
- [ ] Medi memória, velocidade e qualidade com uma tarefa real.

## Integridade da captura

- Os dez projetos do post foram conferidos em seus repositórios oficiais em 12 de setembro de 2026.
- As contagens de estrelas do post não foram usadas para classificar qualidade ou adequação, pois mudam continuamente.
- Jan, ComfyUI e TextGen tiveram os redirecionamentos de repositório registrados com seus destinos atuais.
- Os commits consultados estão no frontmatter desta nota.
- Nenhum dos dez projetos foi instalado durante a produção deste tutorial; comandos e requisitos foram revisados nas fontes oficiais.

## Fontes

- [Post original de Hasan Toor](https://x.com/hasantoxr/status/2098422529677521196)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Jan](https://github.com/janhq/jan)
- [Ollama](https://github.com/ollama/ollama)
- [LocalAI](https://github.com/mudler/LocalAI)
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- [MLX-LM](https://github.com/ml-explore/mlx-lm)
- [TextGen](https://github.com/oobabooga/textgen)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp)
- [exo](https://github.com/exo-explore/exo)
- [GPT4All](https://github.com/nomic-ai/gpt4all)
