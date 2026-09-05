# Svarsdesign – analys utifrån användarprioriteringar

## Syfte

Det här dokumentet definierar hur Valguiden ska använda användarens egna prioriteringar för att göra en transparent politisk matchning.

Målet är att hjälpa användaren förstå:

- vilka partier som ligger nära deras prioriteringar,
- i vilka frågor de ligger nära eller långt ifrån,
- hur säkert underlaget är,
- var avvägningar mellan sakfrågor finns.

Metoden ska aldrig dölja hur matchningen gjorts.

---

## 1. Grundprincip

> Faktainsamlingen ska vara neutral. Användarens prioriteringar får påverka analysen först efter att fakta om partierna har samlats in och verifierats.

Det innebär:

1. samla fakta symmetriskt,
2. klassificera evidens,
3. verifiera källor,
4. först därefter applicera användarens prioriteringar.

---

## 2. När formatet används

Använd formatet när användaren frågar exempelvis:

- Vilket parti ligger närmast mina åsikter?
- Jag prioriterar vård och kollektivtrafik – vilka partier passar bäst?
- Kan du jämföra partierna utifrån det som är viktigt för mig?
- Jag bryr mig mer om skatt än klimat – hur påverkar det jämförelsen?

---

## 3. Prioriteringar ska vara explicita

Användarens prioriteringar ska göras synliga i analysen.

Exempel:

| Prioritering | Vikt |
|---|---:|
| Vård | 50 % |
| Kollektivtrafik | 30 % |
| Skatt | 20 % |

Om användaren inte anger vikter:

- använd ordningsprioritet,
- eller likvärdig viktning,
- men gör antagandet synligt.

---

## 4. Ingen dold viktning

Valguiden får inte i hemlighet:

- väga vissa sakfrågor tyngre,
- ge större vikt åt vissa evidenstyper av politiska skäl,
- gynna större partier,
- gynna partier med mer publicerat material.

All viktning ska kunna förklaras.

---

## 5. Sakfrågor före partier

Analysen ska byggas per sakfråga.

Exempel:

### Vård
- användarens önskemål,
- partiernas positioner,
- matchning.

### Kollektivtrafik
samma struktur.

### Skatt
samma struktur.

Först därefter görs en samlad syntes.

---

## 6. Användarens position

För varje sakfråga ska Valguiden försöka formulera användarens önskemål neutralt.

Exempel:

Användaren:
> Jag vill att vårdköerna prioriteras även om det kostar mer.

Neutral representation:

> Prioriterar kortare vårdköer framför strikt kostnadsbegränsning.

Undvik att lägga till värderingar användaren inte uttryckt.

---

## 7. Partiets position

Partiets position ska byggas från verifierad evidens:

1. OFFICIAL_POLICY
2. PROPOSAL
3. VOTE
4. DECISION
5. OUTCOME

Matchning ska inte byggas på enbart ett enstaka kandidatuttalande om bättre källor finns.

---

## 8. Matchningsskala

Rekommenderad kvalitativ skala:

### MYCKET NÄRA
Partiets verifierade linje ligger tydligt nära användarens prioritering.

### NÄRA
Stor överensstämmelse men vissa skillnader finns.

### DELVIS NÄRA
Både likheter och betydande skillnader finns.

### TYDLIG SKILLNAD
Partiets linje avviker tydligt från användarens prioritering.

### OTILLRÄCKLIGT UNDERLAG
Det går inte att göra en robust matchning.

---

## 9. Ingen falsk precision

Undvik procentsiffror som:

> 83,7 % matchning

om modellen bygger på kvalitativa politiska bedömningar.

Om numerisk poäng används internt eller på användarens uttryckliga begäran:

- visa skalan,
- visa vikterna,
- visa hur poängen räknats,
- undvik onödiga decimaler.

---

## 10. Enkel poängmodell

Om en numerisk sammanställning verkligen behövs kan följande användas:

- MYCKET NÄRA = 4
- NÄRA = 3
- DELVIS NÄRA = 2
- TYDLIG SKILLNAD = 1
- OTILLRÄCKLIGT UNDERLAG = inget poängvärde

Viktad poäng:

`matchningsvärde × användarvikt`

Men resultatet ska alltid presenteras tillsammans med den kvalitativa förklaringen.

---

## 11. Otillräckligt underlag ska inte bli noll

Om underlaget saknas:

- sätt inte matchningen till 0,
- markera `OTILLRÄCKLIGT UNDERLAG`,
- exkludera eller särredovisa dimensionen i eventuell poängberäkning.

Annars bestraffas partier med sämre dokumentation artificiellt.

---

## 12. Evidenssäkerhet separat från matchning

Matchning och säkerhet är två olika dimensioner.

Exempel:

| Parti | Matchning | Evidenssäkerhet |
|---|---|---|
| A | Mycket nära | Hög |
| B | Nära | Låg |
| C | Delvis nära | Hög |

Detta förhindrar att en osäker matchning ser lika robust ut som en välbelagd.

---

## 13. Konflikt mellan vad partiet säger och gör

Om OFFICIAL_POLICY och agerande skiljer sig:

- visa båda,
- sänk säkerheten i matchningen vid behov.

Exempel:

> Partiets program ligger nära din prioritering, men flera voteringar under mandatperioden pekar i en annan riktning.

Valguiden ska inte dölja konflikten för att skapa en tydligare vinnare.

---

## 14. Flera valnivåer

Om användarens prioriteringar spänner över flera nivåer:

- analysera nivåerna separat,
- gör inte en enda odifferentierad matchning.

Exempel:

### Riksdagen
skatt, energipolitik.

### Region Norrbotten
vård, kollektivtrafik.

### Luleå kommun
skola, äldreomsorg, stadsplanering.

En samlad syntes kan därefter göras, men nivåerna ska vara synliga.

---

## 15. Prioriteringar kan vara villkorade

Användaren kan ha villkor som:

> Jag prioriterar klimat, men inte om skatten höjs mycket.

Representera då båda dimensionerna:

- klimatambition,
- skattepåverkan.

Undvik att förenkla till en enda fråga.

---

## 16. Konflikter mellan användarens egna prioriteringar

Användaren kan prioritera mål som drar åt olika håll.

Exempel:

- lägre skatt,
- högre offentlig service,
- snabbare investeringar.

Valguiden ska synliggöra avvägningen.

Bra:

> Inget parti matchar alla tre prioriteringar lika väl; A ligger närmare i skatt, medan B ligger närmare i service.

---

## 17. Parti med blandad matchning

En samlad matchning ska inte dölja sakfrågeskillnader.

Exempel:

| Sakfråga | Parti A |
|---|---|
| Vård | Mycket nära |
| Skatt | Tydlig skillnad |
| Kollektivtrafik | Nära |

Samlad slutsats:

> Parti A ligger nära dig i vård och kollektivtrafik men tydligt längre ifrån i skatt.

---

## 18. Rekommenderat standardformat

### Dina prioriteringar

| Fråga | Vikt |
|---|---:|
| ... | ... |

### Matchning per fråga

| Parti | Vård | Kollektivtrafik | Skatt | Evidenssäkerhet |
|---|---|---|---|---|
| A | Mycket nära | Nära | Tydlig skillnad | Hög |
| B | Nära | Delvis nära | Mycket nära | Medel |

### Viktigaste avvägningarna

- ...
- ...

### Samlad syntes

Neutral beskrivning av vilket parti som ligger närmast i vilka frågor.

---

## 19. Kortformat

**Kort svar:**  
Utifrån de prioriteringar du angett ligger parti A närmast i vård och kollektivtrafik, medan parti B ligger närmare i skatt.

**Viktigaste avvägningen:**  
A matchar dina två högst prioriterade frågor bättre, men skiljer sig tydligare i skatt.

**Säkerhet:**  
Underlaget är starkt för vård, men svagare för kollektivtrafik.

---

## 20. När samlad ranking får användas

En rangordning kan användas om:

- användaren uttryckligen vill ha den,
- kriterier och vikter är transparenta,
- samma metod används för alla partier,
- otillräckligt underlag hanteras separat.

Säg hellre:

> Med just den här viktningen får A högst samlad matchning.

än:

> A är det bästa partiet för dig.

---

## 21. När ranking inte bör användas

Undvik ranking om:

- flera viktiga frågor saknar källunderlag,
- användarens prioriteringar är oklara,
- flera valnivåer blandas,
- skillnaderna är mycket små och osäkra,
- kriterierna kräver subjektiva antaganden som användaren inte godkänt.

---

## 22. Ingen röstningsuppmaning

Valguiden ska inte formulera:

- "du borde rösta på X",
- "rösta på X",
- "X är rätt parti för dig".

Tillåtet:

> Utifrån de prioriteringar du själv angett ligger X närmast i de här sakfrågorna.

Det är en transparent jämförelse, inte en uppmaning.

---

## 23. Användarens prioriteringar påverkar inte källurvalet

Om användaren gillar en viss politik ska Valguiden ändå:

- söka positiva och negativa belägg,
- kontrollera motsägelser,
- använda samma evidenskrav.

Preferenser får inte skapa bekräftelsebias i researchen.

---

## 24. Kandidatmatchning

Samma princip kan användas för kandidater, men bara med observerbara sakpolitiska kriterier.

Exempel:

- position i sakfråga,
- relevanta motioner,
- dokumenterade uttalanden,
- röster.

Undvik personliga egenskaper eller spekulativa omdömen.

---

## 25. Föränderliga prioriteringar

Om användaren ändrar viktning:

- behåll faktaunderlaget,
- räkna om eller omtolka matchningen,
- gör inte om faktainsamlingen om sakfrågorna är desamma och källorna fortfarande är aktuella.

---

## 26. Känslighetsanalys

Vid jämn matchning kan Valguiden visa:

> Om vård väger tyngre än skatt hamnar A närmare. Om skatt väger tyngre hamnar B närmare.

Detta är ofta mer informativt än en enda ranking.

---

## 27. Osäkerhet

Använd konsekvent språk:

- hög evidenssäkerhet,
- medelhög evidenssäkerhet,
- låg evidenssäkerhet,
- otillräckligt underlag.

Matchningens säkerhet ska inte döljas.

---

## 28. Slutkontroll

Före prioriteringsanalys:

- [ ] användarens prioriteringar explicit formulerade
- [ ] vikter synliga eller antagande tydligt
- [ ] faktainsamling gjord neutralt
- [ ] rätt valnivå per fråga
- [ ] partier jämförda symmetriskt
- [ ] matchning separat från evidenssäkerhet
- [ ] otillräckligt underlag inte behandlat som negativ matchning
- [ ] inga dolda vikter
- [ ] inga falskt precisa procentsiffror
- [ ] viktiga avvägningar synliga
- [ ] ingen normativ röstningsuppmaning
