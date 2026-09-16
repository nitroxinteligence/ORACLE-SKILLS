---
id: gv-templates-mapa-contexto
type: playbook
status: active
area: marca
created: '2026-09-16'
updated: '2026-09-16'
sensitivity: internal
sources: []
confidence: medium
review_after: '2026-12-16'
---
# Mapa contexto

Modelo para copiar a um projeto autorizado. Valores nulos são campos a preencher, não inferências sobre o usuário. Preservar este template e registrar a versão preenchida fora da biblioteca compartilhada.

```json
{
  "vault_root": null,
  "date": null,
  "authorized_scope": [],
  "coverage": {
    "eligible_files": null,
    "fully_read": null,
    "partially_read": null,
    "excluded": null,
    "inaccessible": null
  },
  "files": [
    {
      "path": null,
      "read_status": "pendente",
      "sections": [],
      "hash": null
    }
  ],
  "personal_claims": [
    {
      "statement": null,
      "origin": "desconhecido",
      "source": null,
      "date": null,
      "public_use_authorized": false
    }
  ],
  "contradictions": [],
  "questions": []
}
```

[[SISTEMA/skills/conteudo/gary-vaynerchuk/indice|Índice do especialista]] · [[SISTEMA/skills/conteudo/gary-vaynerchuk/references/indice|Referências]]
