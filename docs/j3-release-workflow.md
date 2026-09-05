# J3 – release-workflow

## Workflow

`.github/workflows/release.yml`

## Trigger

Körs när en GitHub Release publiceras.

## Versionsprincip

Versionsnumret hämtas från release-taggen:

- `v1.0.0` → `1.0.0`
- `1.0.0` → `1.0.0`

Release-taggen är därmed versionskälla för distributionsartefakterna.

## Flöde

1. checkout,
2. Python 3.12,
3. installera `pyyaml`,
4. härled version från release-taggen,
5. bygg och validera båda distributionerna,
6. skriv versionsnumret i distributionsmetadata,
7. paketera versionsnamngivna ZIP-filer,
8. validera att assets finns,
9. ladda upp dem till samma GitHub Release via `gh release upload`.

## Release-assets

- `valguiden-chat-<version>.zip`
- `valguiden-custom-gpt-<version>.zip`

## Avgränsning

J3 skapar själva publiceringsflödet. J4 ska därefter göra särskild release-validering och kontroll av att workflow, artifacts och versionsregler hänger ihop.
