# H5 – E2E: positionsförändring

## Syfte

Testa hela arbetsflödet för att avgöra om ett parti eller en kandidat faktiskt har ändrat position över tid.

## Kärnflöde

1. Fastställ startposition och slutposition.
2. Säkerställ samma aktör, nivå och sakfråga.
3. Verifiera tidigare och aktuell OFFICIAL_POLICY när sådan finns.
4. Lägg in mellanliggande:
   - PROPOSAL,
   - VOTE,
   - DECISION,
   - STATEMENT,
   - OUTCOME när relevant.
5. Skilj kompromisser från faktisk positionsförändring.
6. Skilj individ från parti.
7. Skilj lokal/regional/nationell nivå.
8. Hantera frånvaro i senare dokument försiktigt.
9. Klassificera:
   - I HUVUDSAK OFÖRÄNDRAD
   - VISS FÖRSKJUTNING
   - TYDLIG POSITIONSFÖRÄNDRING
   - MOTSTRIDIG EVIDENS
   - OTILLRÄCKLIGT UNDERLAG
10. Ange evidenssäkerhet och alternativa tolkningar.

## Kritiska regressioner

- en intervju blir partiets nya officiella linje,
- lokal/nationell skillnad blir tidsförändring,
- kompromissröst blir ny partilinje,
- frånvaro i dokument blir övergiven position,
- individens förändring överförs till partiet,
- förändrat utfall efter maktskifte tillskrivs fel aktör,
- olika tröskel används för olika partier.
