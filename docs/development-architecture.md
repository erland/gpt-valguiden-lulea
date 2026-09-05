# Utvecklingsarkitektur

## Flöde

```text
assistant/instructions.md
        │
        ├── assistant/policies/
        ├── knowledge/
        ├── tests/evals/
        │
        └── distribution-contract.yaml
                │
        ┌───────┴────────┐
        │                │
   dist/chat/      dist/custom-gpt/
        │                │
        └───────┬────────┘
                │
          scripts/validate.py
                │
        ┌───────┴────────┐
        │                │
   GitHub CI        GitHub Release
```

## Designprinciper

### Canonical first
Runtime-beteende ändras först i kanonisk instruktion.

### Policy for depth
Detaljer som behövs för utveckling och spårbarhet uttrycks i policies.

### Knowledge for stable facts and method
Knowledge ska vara stabilt och inte behöva uppdateras inför varje politisk förändring.

### Eval for enforceability
Viktiga regler ska gå att testa.

### Distribution as generated output
Distributioner är resultat av source-of-truth och ska inte driva designen baklänges.

### Release by tag
GitHub Release-taggen är versionskälla.
