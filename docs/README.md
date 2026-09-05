# Dokumentationsöversikt

Dokumentationen i `docs/` är avsedd för användning och långsiktig förvaltning. Tillfälliga stegvalideringar, RC-anteckningar och andra arbetsartefakter sparas inte i releasegrenen.

## Användning

- `user-guide.md` – hur Valguiden används.
- `faq.md` – vanliga frågor och viktiga avgränsningar.
- `release-notes-1.0.0.md` – release notes för första stabila versionen.

## Utveckling och arkitektur

- `developer-guide.md` – utvecklingsflöde, evals, CI och release.
- `development-architecture.md` – source-of-truth och distributionsarkitektur.
- `generated-artifacts.md` – vad som är källmaterial respektive genererat.
- `source-architecture.md` – källarkitektur.
- `source-guide-riksdagen.md`, `source-guide-region-norrbotten.md`, `source-guide-lulea-kommun.md` – nivåspecifika källguider.
- `source-verification.md` och `web-research-flow.md` – verifiering och webbresearch.

## Svars- och kandidatdesign

Filerna `response-design-*.md`, `candidate-model.md`, `candidate-activity-metrics.md` och tillhörande exempel beskriver stabil design som används vid fortsatt utveckling och regressionstestning.

## Versionering

Projektet har inget hårdkodat releaseversionsnummer som source of truth. När en GitHub Release publiceras hämtar `.github/workflows/release.yml` versionen från `github.event.release.tag_name`. En tagg som `v1.2.3` ger distributionsversion `1.2.3` och artefakterna `valguiden-chat-1.2.3.zip` respektive `valguiden-custom-gpt-1.2.3.zip`.
