# Utvecklarguide – Valguiden

## 1. Översikt

Valguiden är uppdelad i fem huvudlager:

1. **Kanonisk runtime-logik**
   - `assistant/instructions.md`
   - övergripande source of truth för beteendet.

2. **Policies**
   - `assistant/policies/`
   - fördjupar avgränsade beteenden, till exempel evidens, neutralitet, källor, kandidatjämförelse och svarstyper.

3. **Knowledge**
   - `knowledge/`
   - stabil metodik, ansvarsfördelning och domänkunskap som inte ska innehålla dagsaktuella partipositioner.

4. **Evals**
   - `tests/evals/`
   - maskinläsbara och mänskligt läsbara regressionsfall.

5. **Distributioner**
   - `dist/chat/`
   - `dist/custom-gpt/`
   - genereras från projektets source-of-truth och valideras före release.

## 2. Source of truth

### Primär source of truth

`assistant/instructions.md`

Den ska innehålla allt runtime-kritiskt beteende som båda distributionerna måste följa.

### Policies

Policies används för:
- detaljerade regler,
- utvecklingsbarhet,
- spårbarhet mellan beteende och evals.

En policy får inte införa ett beteende som saknas helt i den kanoniska runtime-logiken om beteendet är release-kritiskt.

### Knowledge

Knowledge ska vara:
- stabil över tid,
- metodisk,
- nivåspecifik där det behövs,
- fri från dagsaktuella partiståndpunkter.

Aktuell politisk information ska hämtas via webben vid körning.

## 3. Distributionskontrakt

`distribution-contract.yaml` definierar vad Chat och Custom GPT måste ha gemensamt.

Grundprincip:

> Format och detaljnivå får skilja, men kärnmetodik får inte skilja.

Paritet måste finnas för bland annat:
- valnivåer,
- evidenstyper,
- neutralitet,
- källverifiering,
- voteringslogik,
- positionsförändring,
- matchningsskalor,
- evidenssäkerhet,
- kandidatanalys.

Custom GPT-instruktionen är komprimerad på grund av instruktionsgränsen. Chat-versionen får vara mer detaljerad.

## 4. Så införs en ny beteenderegel

Använd denna ordning:

1. Beskriv regeln i relevant design- eller policydokument.
2. Uppdatera `assistant/instructions.md` om regeln är runtime-kritisk.
3. Uppdatera relevant Knowledge-fil om regeln är stabil domänmetodik.
4. Lägg till eller uppdatera evalfall.
5. Uppdatera Custom GPT-instruktionen om regeln måste vara explicit där.
6. Kör distributionsharmonisering/validering.
7. Kör `python scripts/build_all.py`.
8. Kontrollera att inga oväntade genererade ändringar återstår.

En bugg som hittas i pilot eller releasegranskning ska normalt få ett permanent regressionstest.

## 5. Evidensmodell

Följande typer är normativa och ska inte bytas ut godtyckligt:

- `OFFICIAL_POLICY`
- `PROPOSAL`
- `VOTE`
- `DECISION`
- `STATEMENT`
- `OUTCOME`

Viktiga invariants:
- PROPOSAL ≠ OFFICIAL_POLICY
- VOTE ≠ DECISION
- DECISION ≠ OUTCOME
- STATEMENT ≠ OFFICIAL_POLICY
- OUTCOME ≠ bevisad kausalitet

Om en ändring påverkar dessa relationer ska både instruktion, policy, Knowledge och evals granskas.

## 6. Källverifiering

Verifieringsstatus:
- `VERIFIED`
- `VERIFIED_WITH_LIMITATIONS`
- `DISCOVERY_ONLY`
- `REJECTED`

Nya källtyper ska bedömas mot:
- avsändare,
- dokumenttyp,
- datum,
- nivå,
- aktör,
- faktisk claim support,
- originalkälla,
- direktlänk,
- beslutskontext,
- voteringskontext,
- aktualitet,
- fullständighet.

## 7. Evals

### Struktur

- `tests/evals/framework/`
- `tests/evals/suites/`
- mänskliga beskrivningar och coverage-filer bredvid.

### Testtyper

- `RULE`
- `BEHAVIOR`
- `ADVERSARIAL`
- `END_TO_END`

### Severity

- `critical`
- `high`
- `medium`
- `low`

### Releaseblockerande fel

Exempel:
- fabricerad källa/citat/röst,
- fel ansvarsnivå som ändrar slutsats,
- kandidatuttalande blir partilinje,
- motion blir beslut,
- politiskt vinklad rekommendation.

## 8. Bygg

### Komplett bygge

```bash
python scripts/build_all.py
```

Det kör:
1. `build_chat.py`
2. `build_custom_gpt.py`
3. `validate.py`

### Separata byggen

```bash
python scripts/build_chat.py
python scripts/build_custom_gpt.py
```

### Validering

```bash
python scripts/validate.py
```

### Release-validering

```bash
python scripts/validate_release.py --tag v1.0.0 --dir dist
```

### Självtest för release

```bash
python scripts/test_release_validation.py
```

## 9. CI

`.github/workflows/ci.yml`

Kör på:
- pull requests,
- relevanta pushes.

CI ska:
- bygga båda distributionerna,
- köra validering,
- verifiera ren working tree efter bygge.

Om CI lämnar genererade diffar betyder det att repot inte är reproducerbart från source-of-truth.

## 10. Release

`.github/workflows/release.yml`

Trigger:
- publicerad GitHub Release.

Versionskälla:
- release-taggen.

Exempel:
- `v1.0.0` → `1.0.0`

Assets:
- `valguiden-chat-1.0.0.zip`
- `valguiden-custom-gpt-1.0.0.zip`

Före uppladdning körs både:
- generell validering,
- release-validering.

## 11. Versionsstrategi

Projektets långsiktiga versionskälla är GitHub release-taggen.

Undvik att manuellt hårdkoda releaseversion i flera source-filer.

Utvecklingsversioner kan vara exempelvis:
- `0.1.0-dev`

Release-workflowet stämplar slutversionen i distributionsmetadata.

## 12. Ändringar i Custom GPT

Custom GPT har särskilda constraints:
- instruktion målgräns: högst 8 000 tecken,
- Knowledge: högst 20 filer,
- web browsing: på,
- Data Analysis: på,
- image generation: av,
- custom Actions: inga i v1.0.

När `INSTRUCTIONS.md` ändras:
1. kör teckenräkning,
2. kör `scripts/validate.py`,
3. kontrollera semantisk paritet med Chat.

## 13. Ändringar i Chat-distributionen

Chat-distributionen kan bära fler policies och guider än Custom GPT.

Den får däremot inte:
- innehålla utvecklingsfiler,
- inkludera tests,
- inkludera `.github`,
- inkludera scripts,
- introducera runtime-beteende som saknas i kanonisk instruktion.

## 14. Responsibility model

Varje politisk fråga bör kunna beskrivas med:
- `DECISION`
- `IMPLEMENTATION`
- `FUNDING`
- `INFLUENCE`

Vid nivåkonflikt ska modellen förklara vem som faktiskt gör vad.

## 15. Kandidatmodell

Kandidatanalys ska alltid skilja:
- individ från parti,
- aktivitet från inflytande,
- aktivitet från kompetens,
- historik från aktuell sakpolitisk profil.

Nya kandidater får inte missgynnas för att historisk data saknas.

## 16. När något går fel

### Distributionerna skiljer sig semantiskt
- uppdatera canonical först,
- synka Chat,
- komprimera motsvarande beteende till Custom GPT,
- kör validering.

### Custom GPT över 8 000 tecken
- komprimera formulering,
- flytta stabil förklaring till Knowledge,
- behåll runtime-kritiska regler i instruktionen.

### Knowledge över 20 filer
- slå ihop närliggande stabila referensfiler,
- flytta utvecklingsmaterial till `docs/`,
- lägg inte dagsaktuella partidokument i Knowledge.

### Eval fallerar
- avgör om felet ligger i regel, instruktion, källmetod eller test,
- ändra inte eval bara för att få grönt om beteendet faktiskt är fel.

## 17. Definition of done för en ändring

En förändring är klar när:
- source-of-truth är uppdaterad,
- relevant policy/Knowledge är uppdaterad,
- regressionstest finns vid behov,
- båda distributionerna bygger,
- `scripts/validate.py` passerar,
- CI förväntas lämna working tree ren,
- dokumentation är uppdaterad.
