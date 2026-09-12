---
title: "5 skills de UI para design engineers que usam agentes"
slug: 5-skills-de-ui-para-design-engineers-com-agentes
language: pt-BR
type: tutorial
category: design
subcategory: skills-de-ui
source: https://x.com/SubhanHQ/status/2098420125879918949
source_author: "Subhan (@SubhanHQ)"
source_published_at: "2026-09-11T14:35:19Z"
captured_at: 2026-09-12
capture_method: agent-reach/twitter-cli
tags:
  - ui
  - design-engineering
  - agentes-de-ai
  - animacao
  - acessibilidade
  - shadcn
---

# 5 skills de UI para design engineers que usam agentes

Este tutorial reúne as cinco skills de interface indicadas por [Subhan](https://x.com/SubhanHQ/status/2098420125879918949) para design engineers que trabalham com agentes:

1. `emil-design-eng`;
2. `make-interfaces-feel-better`;
3. `12-principles-of-animation`;
4. `fixing-accessibility`;
5. `shadcn`.

Use a skill relacionada à etapa atual do trabalho. Cada uma resolve uma parte diferente da interface: direção de design, acabamento, movimento, acessibilidade ou composição com componentes.

## 1. emil-design-eng

**Skill:** [emil-design-eng](https://www.ui-skills.com/skills/emilkowalski/emil-design-eng)

A skill aplica a filosofia de design engineering de Emil Kowalski. O foco é construir interfaces que pareçam corretas pelo acúmulo de pequenos detalhes.

Princípios centrais:

- bom gosto é treinado pela observação e pela prática;
- detalhes que o usuário não percebe conscientemente se acumulam;
- beleza e bons padrões de interação diferenciam o produto;
- toda animação deve ter uma finalidade;
- ações executadas com muita frequência devem ser instantâneas;
- botões e elementos pressionáveis precisam responder ao toque;
- popovers devem surgir a partir do elemento que os acionou;
- movimento precisa preservar a sensação de velocidade da interface.

### Decida se deve animar

Use a frequência da interação:

| Frequência | Decisão |
|---|---|
| centenas de vezes por dia | não anime |
| dezenas de vezes por dia | remova ou reduza bastante |
| ocasional | use uma animação padrão |
| rara ou primeira experiência | pode incluir mais personalidade |

Não anime ações iniciadas pelo teclado. Paletas de comando, atalhos e navegação repetida precisam responder imediatamente.

### Defina a finalidade

Uma animação pode:

- manter consistência espacial;
- indicar mudança de estado;
- explicar como algo funciona;
- confirmar uma ação;
- suavizar uma mudança brusca.

Se ela existe somente para parecer bonita e será vista muitas vezes, remova-a.

### Escolha o easing

- entrada ou saída rápida com acomodação: `ease-out`;
- movimento ou transformação dentro da tela: `ease-in-out`;
- alteração de cor ou hover: `ease`;
- progresso contínuo: `linear`.

Curvas sugeridas:

```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
}
```

### Use durações curtas

| Elemento | Duração |
|---|---:|
| resposta ao pressionar botão | 100–160 ms |
| tooltip ou popover pequeno | 125–200 ms |
| dropdown ou select | 150–250 ms |
| modal ou drawer | 200–500 ms |

Interações comuns devem permanecer abaixo de 300 ms.

### Faça botões responderem

```css
.button {
  transition: transform 160ms ease-out;
}

.button:active {
  transform: scale(0.97);
}
```

Use uma escala discreta entre `0.95` e `0.98`.

### Não anime a partir de `scale(0)`

```css
.entering {
  opacity: 0;
  transform: scale(0.95);
}
```

Começar próximo do tamanho final produz uma entrada mais natural.

### Faça o popover nascer do gatilho

```css
.popover {
  transform-origin: var(--transform-origin);
}
```

Modais continuam centralizados porque não pertencem visualmente a um gatilho específico.

### Use springs quando houver física

Springs funcionam bem em:

- arrastar com impulso;
- gestos que podem ser interrompidos;
- elementos decorativos que seguem o ponteiro;
- componentes que precisam ultrapassar e acomodar.

```js
const springRotation = useSpring(mouseX * 0.1, {
  stiffness: 100,
  damping: 10,
});
```

## 2. make-interfaces-feel-better

**Skill:** [make-interfaces-feel-better](https://www.ui-skills.com/skills/jakubkrehel/make-interfaces-feel-better)

Essa skill revisa tipografia, superfícies, animações, ícones e desempenho para corrigir pequenos detalhes que deixam uma interface estranha.

Antes de alterar o código, identifique o sistema visual já usado pelo projeto. Aplique a correção com Tailwind, CSS ou CSS-in-JS conforme a base existente.

Durante a revisão, reduza a velocidade das animações para 10% no painel de animações do navegador. Percorra os estados:

- hover;
- focus;
- active;
- loading;
- empty.

Problemas discretos na velocidade normal ficam visíveis em câmera lenta.

### Checklist de acabamento

1. **Raios concêntricos:** raio externo = raio interno + padding.
2. **Alinhamento óptico:** ajuste ícones e formas assimétricas visualmente.
3. **Sombras para elevação:** preserve bordas para estrutura e estado.
4. **Transições interruptíveis:** use CSS transitions em interações.
5. **Entradas divididas:** anime grupos semânticos em sequência quando necessário.
6. **Saídas discretas:** mova poucos pixels e use menos destaque do que na entrada.
7. **Ícones contextuais:** combine opacidade, escala e blur entre estados.
8. **Suavização de fonte:** aplique antialiasing no layout raiz no macOS.
9. **Números tabulares:** evite deslocamento em valores que mudam.
10. **Quebra de texto:** `balance` em títulos e `pretty` em parágrafos.
11. **Contorno de imagem:** use uma linha de 1 px com baixa opacidade.
12. **Escala ao pressionar:** use `scale(0.96)`.
13. **Sem entrada no carregamento:** evite animações involuntárias na primeira renderização.
14. **Nunca use `transition: all`:** informe propriedades específicas.
15. **Use `will-change` com moderação:** somente onde existir travamento perceptível.
16. **Área de toque:** prefira 44 × 44 px em touch e pelo menos 40 × 40 px em desktop denso.
17. **Peso do ícone:** combine o traço com o peso óptico do texto.
18. **Um SVG por ícone:** altere estados com `currentColor` e opacidade.
19. **Movimento contido:** não crie animações chamativas em ações frequentes.

### Tipografia

```css
html {
  -webkit-font-smoothing: antialiased;
}

h1,
h2,
h3 {
  text-wrap: balance;
}

p {
  text-wrap: pretty;
}

.metric {
  font-variant-numeric: tabular-nums;
}
```

### Transições específicas

```css
.control {
  transition-property: transform, opacity;
  transition-duration: 160ms;
  transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1);
}
```

### Ícones em mudança de estado

Use os dois ícones no DOM e faça uma transição entre eles:

- escala de `0.25` para `1`;
- opacidade de `0` para `1`;
- blur de `4px` para `0`;
- spring com duração de `0.3` e `bounce: 0` quando a biblioteca de motion já existir.

## 3. 12-principles-of-animation

**Skill:** [12-principles-of-animation](https://www.ui-skills.com/skills/raphaelsalaja/12-principles-of-animation)

Essa skill adapta princípios da animação tradicional para interfaces web e revisa o código em quatro categorias:

1. timing;
2. easing;
3. física;
4. staging.

### Regras de timing

- animações iniciadas pelo usuário devem terminar em até 300 ms;
- elementos semelhantes precisam usar durações iguais;
- menus de contexto devem aparecer sem animação de entrada.

```css
.button-primary,
.button-secondary {
  transition: transform 200ms;
}
```

### Regras de easing

- use `ease-out` nas entradas;
- use `ease-in` nas saídas;
- reserve `linear` para indicadores de progresso;
- use rampas exponenciais para decaimento natural.

```css
.modal-enter {
  animation-timing-function: ease-out;
}

.modal-exit {
  animation-timing-function: ease-in;
}
```

### Regras de física

- elementos interativos precisam de estado pressionado;
- squash e stretch devem permanecer entre `0.95` e `1.05`;
- use spring quando houver overshoot e acomodação;
- limite o intervalo de stagger a 50 ms por item.

```jsx
<motion.button whileTap={{ scale: 0.98 }} />

<motion.div
  transition={{ type: "spring", stiffness: 500, damping: 30 }}
/>
```

### Regras de staging

- somente um elemento deve receber destaque de movimento por vez;
- o fundo de modais deve escurecer para direcionar a atenção;
- elementos animados devem respeitar a hierarquia de camadas.

Formato de revisão sugerido:

```text
arquivo:linha - [regra] descrição do problema
```

Exemplo:

```text
components/modal.tsx:45 - [timing-under-300ms] A saída dura 400 ms.
components/button.css:12 - [physics-active-state] O botão não possui estado
pressionado.
```

## 4. fixing-accessibility

**Skill:** [fixing-accessibility](https://www.ui-skills.com/skills/ibelick/fixing-accessibility)

Essa skill identifica e corrige problemas de acessibilidade em HTML, componentes interativos, formulários, dialogs, menus, foco, teclado, contraste, mídia e movimento.

Use-a ao:

- criar botões, links e campos;
- construir menus, dialogs, tabs e dropdowns;
- implementar validação e mensagens de erro;
- adicionar atalhos e interações próprias;
- trabalhar com controles formados somente por ícones;
- criar conteúdo que aparece apenas no hover.

### Nomes acessíveis

- todo controle interativo deve ter nome acessível;
- botões com somente ícone precisam de `aria-label` ou `aria-labelledby`;
- inputs, selects e textareas precisam de label;
- links devem possuir texto significativo;
- ícones decorativos devem usar `aria-hidden`.

```html
<button aria-label="Fechar">
  <svg aria-hidden="true"></svg>
</button>
```

### Teclado

- prefira elementos nativos;
- todos os controles devem ser alcançados com Tab;
- o foco precisa permanecer visível;
- não use `tabindex` maior do que zero;
- Escape deve fechar dialogs e overlays quando aplicável.

```html
<button onclick="save()">Salvar</button>
```

### Foco e dialogs

- prenda o foco dentro do modal aberto;
- defina foco inicial dentro do dialog;
- restaure o foco ao gatilho quando fechar;
- evite deslocar a página ao abrir.

### Semântica

- use `button`, `a`, `input`, `ul`, `ol`, `li` e `th` conforme a função;
- não pule níveis de heading;
- adicione atributos ARIA obrigatórios quando um `role` for realmente necessário.

### Formulários e erros

```html
<label for="email">E-mail</label>
<input
  id="email"
  aria-describedby="email-error"
  aria-invalid="true"
/>
<span id="email-error">E-mail inválido.</span>
```

- associe erros ao campo com `aria-describedby`;
- anuncie campos obrigatórios;
- use `aria-invalid` em campos inválidos;
- associe textos auxiliares aos controles;
- explique por que o envio está desabilitado.

### Anúncios e estados

- use `aria-live` para erros críticos;
- use `aria-busy` ou texto de status durante carregamento;
- não dependa somente de toasts para informações importantes;
- use `aria-expanded` e `aria-controls` em controles expansíveis;
- não use somente cor para comunicar um estado;
- respeite `prefers-reduced-motion` em animações dispensáveis.

Faça correções pequenas e direcionadas. Prefira HTML nativo antes de acrescentar ARIA e não troque a biblioteca de interface sem necessidade.

## 5. shadcn

**Skill:** [shadcn](https://www.ui-skills.com/skills/shadcn-ui/shadcn)

Essa skill fornece um fluxo consciente do projeto para pesquisar, adicionar, combinar e corrigir componentes shadcn/ui.

Use o executor de pacotes já adotado pelo projeto:

```bash
npx shadcn@latest
pnpm dlx shadcn@latest
bunx --bun shadcn@latest
```

### Fluxo principal

```bash
npx shadcn@latest info --json
npx shadcn@latest search
npx shadcn@latest docs button dialog select
npx shadcn@latest view @shadcn/button
npx shadcn@latest add button card dialog --dry-run
npx shadcn@latest add button card dialog
```

1. leia o contexto do projeto com `info`;
2. confira os componentes já instalados;
3. pesquise componentes antes de criar markup próprio;
4. abra a documentação e os exemplos;
5. visualize o item do Registry;
6. examine o diff;
7. adicione ou atualize o componente;
8. confira imports, composição e biblioteca de ícones.

### Princípios de composição

- use componentes existentes antes de criar versões próprias;
- combine componentes pequenos para formar telas;
- prefira variantes prontas;
- use cores semânticas como `bg-primary` e `text-muted-foreground`;
- use `gap-*` em flex e grid;
- use `size-*` quando largura e altura forem iguais;
- use `cn()` para classes condicionais;
- preserve a composição completa de `Card`;
- coloque itens dentro de seus respectivos grupos;
- inclua título em `Dialog`, `Sheet` e `Drawer`;
- inclua `AvatarFallback` em `Avatar`;
- use `Skeleton`, `Spinner`, `Alert`, `Badge`, `Separator` e `Empty` em vez de versões improvisadas.

### Formulários

Use `FieldGroup` e `Field`:

```jsx
<FieldGroup>
  <Field>
    <FieldLabel htmlFor="email">E-mail</FieldLabel>
    <Input id="email" />
  </Field>
</FieldGroup>
```

Validação:

```jsx
<Field data-invalid>
  <FieldLabel>E-mail</FieldLabel>
  <Input aria-invalid />
  <FieldDescription>E-mail inválido.</FieldDescription>
</Field>
```

### Ícones em botões

```jsx
<Button>
  <SearchIcon data-icon="inline-start" />
  Pesquisar
</Button>
```

O componente controla o tamanho do ícone. Use a biblioteca de ícones já definida no projeto.

### Selecione componentes pela função

| Necessidade | Componente |
|---|---|
| ação | `Button` |
| formulário | `Input`, `Select`, `Switch`, `Checkbox`, `RadioGroup` |
| conjunto de opções | `ToggleGroup` |
| exibição de dados | `Table`, `Card`, `Badge`, `Avatar` |
| navegação | `Sidebar`, `Breadcrumb`, `Tabs`, `Pagination` |
| sobreposição | `Dialog`, `Sheet`, `Drawer`, `AlertDialog` |
| feedback | `Alert`, `Progress`, `Skeleton`, `Spinner`, toast |
| layout | `Card`, `Separator`, `Resizable`, `ScrollArea` |
| estado vazio | `Empty` |
| menu | `DropdownMenu`, `ContextMenu`, `Menubar` |
| informação contextual | `Tooltip`, `HoverCard`, `Popover` |

## Ordem de uso em uma tarefa

Use as cinco skills como um fluxo:

1. **shadcn:** escolha e componha os componentes;
2. **emil-design-eng:** defina o comportamento e a sensação da interface;
3. **make-interfaces-feel-better:** refine tipografia, superfícies, ícones e microinterações;
4. **12-principles-of-animation:** revise timing, easing, física e staging;
5. **fixing-accessibility:** corrija nomes, teclado, foco, semântica, formulários e estados.

Pedido para o agente:

```text
Revise esta interface em cinco etapas:

1. confirme se os componentes existentes do projeto foram reutilizados;
2. avalie hierarquia, tipografia, superfícies e microinterações;
3. revise as animações por timing, easing, física e staging;
4. revise nomes acessíveis, teclado, foco, semântica, formulários e estados;
5. apresente somente mudanças concretas relacionadas ao escopo solicitado.

Para cada problema, indique arquivo, trecho atual, mudança proposta e motivo.
```

## Acesso às skills

- [emil-design-eng](https://www.ui-skills.com/skills/emilkowalski/emil-design-eng)
- [make-interfaces-feel-better](https://www.ui-skills.com/skills/jakubkrehel/make-interfaces-feel-better)
- [12-principles-of-animation](https://www.ui-skills.com/skills/raphaelsalaja/12-principles-of-animation)
- [fixing-accessibility](https://www.ui-skills.com/skills/ibelick/fixing-accessibility)
- [shadcn](https://www.ui-skills.com/skills/shadcn-ui/shadcn)
- [Demonstração citada na publicação](https://amicro.vercel.app/)

## Fonte

- [Publicação original de Subhan no X](https://x.com/SubhanHQ/status/2098420125879918949)
