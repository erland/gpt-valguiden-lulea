# J4 – release-validering

## Nya scripts

- `scripts/validate_release.py`
- `scripts/test_release_validation.py`

## Kontroller

Release-valideringen verifierar:

- versionsformat från GitHub release-taggen,
- att versionsnamngivna ZIP-filer finns,
- att Chat- och Custom GPT-ZIP har rätt filnamn,
- att metadata-versionen matchar release-taggen,
- att obligatoriska filer finns i respektive ZIP,
- att Custom GPT-instruktionen håller sig inom 8 000 tecken,
- att Custom GPT Knowledge håller sig inom 20 filer,
- att Chat-releasepaketet inte innehåller utvecklingsmaterial som tests, scripts eller `.github`.

## Workflow-integration

`.github/workflows/release.yml` kör nu både:
- `scripts/validate.py`
- `scripts/validate_release.py`

innan release-assets laddas upp.

## Lokal självtest

`scripts/test_release_validation.py` bygger färska distributioner, skapar test-releasefiler för `v0.0.0-test` och kör samma release-validering som workflowet.
