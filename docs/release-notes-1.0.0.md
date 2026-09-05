# Valguiden v1.0.0

## Status

**Stable release**

## Distributioner

- `valguiden-chat-1.0.0.zip`
- `valguiden-custom-gpt-1.0.0.zip`

## Omfång

Valguiden stödjer:
- Riksdagen
- Region Norrbotten
- Luleå kommun

## Kärnförmågor

- jämförelse av officiell partipolitik,
- förslag, voteringar och beslut,
- utfalls- och genomförandeanalys,
- positionsförändring över tid,
- användarprioriterad men metodiskt neutral matchning,
- kandidatjämförelse,
- källverifiering och spårbarhet.

## Evidensmodell

- `OFFICIAL_POLICY`
- `PROPOSAL`
- `VOTE`
- `DECISION`
- `STATEMENT`
- `OUTCOME`

## Release gates

- Full eval: **PASS**
- Neutralitetsgranskning: **PASS**
- Spårbarhetsgranskning: **PASS**
- Distributionstest: **PASS**
- RC: **PASS**
- Pilotfixar: **PASS**
- Slutlig projektvalidering: **PASS**
- Slutlig release-validering: **PASS**

## Pilotfynd som stängdes före release

`PILOT-003`:
- I Luleå är `besvarad` uttryckligen **inte samma sak som bifall**.
- Regeln finns i canonical runtime och Custom GPT-instruktionen.
- Permanent critical regression `H3-016` finns.

## Viktiga principer

- Neutralitet = samma metod, inte samma slutsats.
- Aktuell politisk fakta verifieras via webben.
- Saknat underlag blir inte nollpoäng eller motsatt ståndpunkt.
- VOTE kräver voteringskontext.
- DECISION kräver beslutskontext.
- OUTCOME kräver separat stöd.
- Fabricerade källor, citat, röster, beslut och datum är förbjudna.
