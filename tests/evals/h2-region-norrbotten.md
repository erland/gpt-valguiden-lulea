# H2 – E2E: Region Norrbotten

## Syfte

Det här scenariot testar hela Valguidens regionala arbetsflöde för Region Norrbotten.

## Regionalt kärnflöde

1. Identifiera Region Norrbotten som rätt valnivå.
2. Avgränsa sakfråga och tidsperiod.
3. Prioritera regional officiell partipolitik.
4. Följ relevanta regionala källor:
   - strategisk plan/budget,
   - motioner,
   - interpellationer och frågor,
   - protokoll,
   - reservationer,
   - voteringar,
   - årsredovisning och uppföljning.
5. Skilj:
   - OFFICIAL_POLICY,
   - PROPOSAL,
   - VOTE,
   - DECISION,
   - STATEMENT,
   - OUTCOME.
6. Separera nationella ramar från regionalt handlingsutrymme.
7. Hantera regional/nationell partiskillnad korrekt.
8. Redovisa källluckor och konflikter.
9. Använd samma metod för alla partier.
10. Vid prioriteringsmatchning: applicera användarens vikter först efter faktainsamlingen.

## Kritiska regressioner

- nationell partilinje används som regional linje,
- 'Beslut i korthet' väger tyngre än fullständigt protokoll,
- motion blir beslut,
- beslut blir utfall,
- reservation misstolkas som slutligt beslut,
- voteringskontext tappas,
- regionalt ansvar överdrivs,
- aktivitet för kandidat blir inflytande/kompetens,
- saknat regionalt underlag blir negativ matchning.
