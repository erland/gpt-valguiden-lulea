# H1 – E2E: väljare från start

## Syfte

Det här scenariot testar Valguidens centrala användarresa från första kontakt till transparent politisk jämförelse.

## Huvudflöde

1. Användaren ber om hjälp inför valet utan att ange valnivå.
2. Valguiden frågar om:
   - Riksdagen,
   - Region Norrbotten,
   - Luleå kommun.
3. Användaren väljer Region Norrbotten.
4. Valguiden fångar eller tolkar användarens prioriteringar.
5. Fakta samlas in neutralt och symmetriskt.
6. Evidens hålls isär:
   - OFFICIAL_POLICY
   - PROPOSAL
   - VOTE
   - DECISION
   - STATEMENT
   - OUTCOME
7. Källbrister redovisas.
8. Användarens prioriteringar appliceras först efter faktainsamlingen.
9. Matchning och evidenssäkerhet visas separat.
10. Slutresultatet presenteras utan normativ röstningsuppmaning.

## Viktiga regressioner som scenariot skyddar mot

- GPT:n väljer valnivå själv när frågan är oklar.
- GPT:n frågar om nivå trots att Region Norrbotten redan är explicit.
- Användarpreferenser styr källurvalet.
- Saknat underlag blir nollpoäng.
- Politisk matchning presenteras med falsk precision.
- "Närmast" blir "du borde rösta på".
- Regionalt faktaunderlag återanvänds som kommunalt utan ansvarskontroll.
