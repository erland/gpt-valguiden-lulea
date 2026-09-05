# Genererade artefakter och projektstädning

## Source kontra genererat

Följande betraktas som source-of-truth och ska versionshanteras:

- `assistant/`
- `knowledge/`
- `docs/`
- `tests/evals/`
- `scripts/`
- `.github/workflows/`
- `README.md`
- `PROJECT.md`
- `CONTRIBUTING.md`
- `distribution-contract.yaml`
- `gpt-project.yaml`
- `project-status.yaml`

Följande kataloger innehåller genererade distributionsfiler:

- `dist/chat/`
- `dist/custom-gpt/`

ZIP-filer direkt under `dist/` är byggartefakter och kan återskapas med:

```bash
python scripts/build_all.py
```

## Tillfälliga releasefiler

Självtestet för release kan skapa filer med testversionen `0.0.0-test`.
De är tillfälliga och ska inte sparas i repot.

## Städprincip

Ta bort:
- Python cache,
- editor-/OS-filer,
- temporära release-assets,
- dubbletter av genererade ZIP-filer.

Behåll:
- canonical source,
- policies,
- Knowledge,
- evals,
- dokumentation,
- scripts,
- workflow-filer,
- distributionskatalogerna som används för reproducerbarhetskontroll.
