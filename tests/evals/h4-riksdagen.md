# H4 – E2E: Riksdagen

## Syfte

Det här scenariot testar hela Valguidens nationella arbetsflöde för Riksdagen.

## Nationellt kärnflöde

1. Identifiera Riksdagen som rätt valnivå.
2. Avgränsa sakfråga och mandatperiod.
3. Prioritera nationell OFFICIAL_POLICY.
4. Följ riksdagskedjan:
   - motion/proposition,
   - betänkande,
   - reservationer,
   - votering,
   - riksdagsbeslut.
5. Använd Sagt och gjort för dokumenterad ledamotsaktivitet.
6. Använd Riksdagens öppna data för discovery/statistik och originaldokument för exakt kontext.
7. Separera:
   - PROPOSAL,
   - VOTE,
   - DECISION,
   - OUTCOME.
8. Separera nationell styrning från regionalt/kommunalt genomförande.
9. Redovisa datakvalitetsproblem och källluckor.
10. Använd samma metod för alla partier.

## Kritiska regressioner

- proposition blir beslut,
- reservation blir beslut,
- rå ja/nej-röst tolkas utan yrkandekontext,
- riksdagsbeslut blir automatiskt genomförande,
- API-data används utan originalkontext,
- nationellt ansvar blandas ihop med region/kommun,
- ledamotsaktivitet blir inflytande eller kompetens.
