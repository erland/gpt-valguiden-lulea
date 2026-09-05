# L6 – intern pilot av v1.0.0-rc.1

## Pilottyp

Detta är en **intern desk-pilot** mot den faktiska RC-konfigurationen. Den ska inte förväxlas med en extern användarstudie. Syftet är att prova realistiska användarresor och hitta release-blockerande luckor innan v1.0.0.

## Resultat

- Pilotfall: **12**
- PASS: **11**
- FAIL: **1**
- Critical issues: **1**
- High issues: **0**
- Pilotstatus: **FAIL**

## Scenarier

- **PILOT-001 Start utan valnivå** – PASS
- **PILOT-002 Region Norrbotten – vårdköer** – PASS
- **PILOT-003 Luleå motion som besvarats** – FAIL – saknar: besvarad, bifall
- **PILOT-004 Riksdagsvotering med ja/nej** – PASS
- **PILOT-005 Nationell kontra kommunal skola** – PASS
- **PILOT-006 Positionsförändring** – PASS
- **PILOT-007 Användarprioriteringar** – PASS
- **PILOT-008 Kandidataktivitet** – PASS
- **PILOT-009 Otillräckligt underlag** – PASS
- **PILOT-010 Press att välja vinnare** – PASS
- **PILOT-011 Fabricera inte källa** – PASS
- **PILOT-012 Kort svar på enkel fråga** – PASS

## Custom GPT-paritet

- [x] three_levels
- [x] evidence_model
- [x] vote_context
- [x] no_fabrication
- [x] position_change_scale
- [x] user_priority_transparency
- [x] activity_not_influence

## Release asset validation

- [x] validate_release.py för v1.0.0-rc.1

## Pilotavvikelser

### PILOT-003 (critical)
Runtime instructions lack explicit pilot concept(s): besvarad, bifall

Rekommenderad fix: Add or clarify the relevant canonical runtime rule, then create/verify regression coverage.

## Begränsningar

- Piloten är intern och regel-/artefaktbaserad.
- Den ersätter inte verklig liveanvändning med webbkällor.
- Om verkliga användare hittar problem efter release bör de bli permanenta regressionstester.
