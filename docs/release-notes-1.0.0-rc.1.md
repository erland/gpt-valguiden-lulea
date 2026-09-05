# Valguiden v1.0.0-rc.1

## Status

**Release Candidate**

Denna version är avsedd för pilotkörning före `v1.0.0`.

## Distributioner

- `valguiden-chat-1.0.0-rc.1.zip`
- `valguiden-custom-gpt-1.0.0-rc.1.zip`

## Release gates

- L1 full eval: **PASS**
- L2 neutralitetsgranskning: **PASS**
- L3 spårbarhetsgranskning: **PASS**
- L4 distributionstest: **PASS**
- Release-validering: **PASS**

## Funktionellt omfång

Valguiden stödjer:
- Riksdagen
- Region Norrbotten
- Luleå kommun

Kärnförmågor:
- partijämförelse,
- evidensklassning,
- källverifiering,
- voteringsanalys,
- positionsförändring,
- analys utifrån användarprioriteringar,
- kandidatjämförelse.

## Viktiga principer

- Neutralitet = samma metod, inte samma slutsats.
- Aktuell politisk fakta verifieras via webben.
- PROPOSAL, VOTE, DECISION, STATEMENT och OUTCOME hålls isär.
- Fabricerade källor, röster, beslut, citat och datum är förbjudna.
- Saknat underlag ska redovisas som osäkerhet, inte fyllas med antaganden.

## Pilotmål

Piloten ska framför allt fånga:
- otydliga eller för långa svar,
- brister i källspårbarhet,
- fel ansvarsnivå,
- felaktig voteringskontext,
- asymmetri mellan partier,
- kandidat/parti-sammanblandning,
- praktiska problem i Chat- eller Custom GPT-distributionen.
