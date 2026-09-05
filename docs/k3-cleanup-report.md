# K3 – rensning och förenkling

## Borttaget
- `dist/valguiden-chat-0.0.0-test.zip`
- `dist/valguiden-custom-gpt-0.0.0-test.zip`
- `scripts/__pycache__`

## Filantal per toppnivå
- `.github`: 3 filer
- `.gitignore`: 1 filer
- `CONTRIBUTING.md`: 1 filer
- `PROJECT.md`: 1 filer
- `README.md`: 1 filer
- `STATUS.md`: 1 filer
- `assistant`: 23 filer
- `dist`: 58 filer
- `distribution-contract.yaml`: 1 filer
- `docs`: 92 filer
- `gpt-project.yaml`: 1 filer
- `knowledge`: 7 filer
- `project-status.yaml`: 1 filer
- `scripts`: 10 filer
- `tests`: 75 filer

## Förenklingar
- `.gitignore` tillagt för cache, editorfiler och genererade ZIP-filer.
- policy för source kontra genererade artefakter dokumenterad.
- tillfälliga release-self-test-filer rensas bort.

## Efter bygg/validering

- Python-cache som återskapades av byggsteget rensas efteråt.
- Slutvalideringen körs med `PYTHONDONTWRITEBYTECODE=1` för att hålla projektträdet rent.
