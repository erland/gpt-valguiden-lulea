# Evidensmodell för Valguiden

## Syfte

Den här Knowledge-filen definierar hur Valguiden ska klassificera politiska belägg.

Modellen ska göra det möjligt att skilja mellan:

- vad ett parti officiellt säger att det vill göra,
- vad någon föreslagit,
- hur någon röstat,
- vad som faktiskt beslutats,
- vad någon sagt,
- vad som faktiskt genomförts eller blivit utfallet.

De sex huvudkategorierna är:

- `OFFICIAL_POLICY`
- `PROPOSAL`
- `VOTE`
- `DECISION`
- `STATEMENT`
- `OUTCOME`

---

## 1. OFFICIAL_POLICY

### Definition

Ett dokumenterat uttryck för en officiell partiståndpunkt.

### Typiska källor

- valmanifest,
- partiprogram,
- officiell politisk plattform,
- officiellt budgetförslag,
- officiell regional eller lokal budget,
- uttryckligt officiellt ställningstagande från partiorganisation.

### Visar

- vad partiet officiellt säger att det vill,
- aktuell officiell politisk linje,
- prioriteringar och mål.

### Visar inte automatiskt

- att förslaget genomförts,
- att partiet röstat för en viss konkret åtgärd,
- att alla enskilda företrädare delar linjen.

### Exempel

> Partiets valmanifest säger att partiet vill bygga ut kärnkraften.

Klassificering:

`OFFICIAL_POLICY`

---

## 2. PROPOSAL

### Definition

Ett konkret politiskt förslag som ännu inte i sig är ett slutligt beslut.

### Typiska källor

- motion,
- proposition,
- budgetyrkande,
- initiativ,
- förslag till beslut,
- reservation med alternativt förslag.

### Visar

- att en viss aktör föreslagit något,
- vad aktören vill att det beslutande organet ska göra.

### Visar inte automatiskt

- att förslaget antagits,
- att hela partiet står bakom förslaget,
- att förslaget genomförts.

### Exempel

> Tre ledamöter från ett parti lämnar en motion om en ny hälsocentral.

Klassificering:

`PROPOSAL`

Aktören är de tre ledamöterna, inte automatiskt hela partiet.

---

## 3. VOTE

### Definition

Dokumenterad röst i en konkret omröstning.

### Typiska källor

- voteringslista,
- voteringsprotokoll,
- protokoll med röstsiffror,
- registrerad individuell röst.

### Visar

- hur en ledamot eller partigrupp röstade i ett konkret yrkande.

### Visar inte automatiskt

- hela partiets långsiktiga politiska linje,
- slutligt beslut,
- varför rösten avgavs,
- hur frågan senare genomfördes.

### Viktig tolkningsregel

Ett ja eller nej måste alltid förstås i relation till:

- vilket yrkande som låg på bordet,
- vilket motförslag som fanns,
- om voteringen gällde en reservation,
- vilken beslutsordning som användes.

### Exempel

> Parti X:s ledamöter röstar nej till en reservation.

Klassificering:

`VOTE`

Det betyder inte automatiskt att partiet är emot hela sakfrågan.

---

## 4. DECISION

### Definition

Ett formellt beslut fattat av ett behörigt beslutande organ.

### Typiska källor

- riksdagsbeslut,
- kommunfullmäktigebeslut,
- regionfullmäktigebeslut,
- nämndbeslut,
- styrelsebeslut inom mandat.

### Visar

- vad organet faktiskt beslutade.

### Visar inte automatiskt

- hur beslutet senare genomfördes,
- vilket resultat beslutet gav,
- vem som ensam kan tillskrivas ansvaret.

### Exempel

> Kommunfullmäktige beslutar att bifalla motionen.

Klassificering:

`DECISION`

---

## 5. STATEMENT

### Definition

Ett dokumenterat uttalande från en politisk aktör.

### Typiska källor

- tal,
- intervju,
- pressmeddelande,
- debattartikel,
- anförande,
- interpellationssvar,
- officiell kommentar.

### Visar

- vad personen eller organisationen sagt vid en viss tidpunkt.

### Visar inte automatiskt

- officiell partipolitik,
- bindande vallöfte,
- hur aktören senare röstar,
- faktiskt genomförande.

### Exempel

> En kandidat säger i en intervju att hen vill stoppa en viss reform.

Klassificering:

`STATEMENT`

---

## 6. OUTCOME

### Definition

Verifierbart genomförande eller observerbart resultat av beslut, reform eller politik.

### Typiska källor

- årsredovisning,
- uppföljningsrapport,
- verksamhetsrapport,
- officiell implementeringsstatus,
- budgetutfall,
- statistik över faktiskt genomförande.

### Visar

- vad som faktiskt hänt,
- om ett uppdrag genomförts,
- vilka resultat som dokumenterats.

### Visar inte automatiskt

- att en viss aktör ensam orsakade utfallet,
- att utfallet motsvarar ett partis intention,
- att alla effekter beror på ett enda beslut.

### Exempel

> Regionen redovisar att en beslutad verksamhetsförändring har genomförts.

Klassificering:

`OUTCOME`

---

## 7. En källa kan ge flera evidenstyper

Ett enda dokument kan innehålla flera slags belägg.

Exempel:

Ett kommunfullmäktigeprotokoll kan innehålla:

- `PROPOSAL` – yrkanden,
- `VOTE` – omröstning,
- `DECISION` – slutligt beslut,
- `STATEMENT` – protokollförda yttranden.

Klassificera då varje del separat.

---

## 8. Evidensklassning styrs av frågan

Det finns ingen absolut rangordning där en typ alltid är bäst.

### Fråga: Vad vill partiet?

Prioritera:

1. `OFFICIAL_POLICY`
2. `PROPOSAL`
3. `STATEMENT`

### Fråga: Vad föreslog partiet?

Prioritera:

1. `PROPOSAL`

### Fråga: Hur röstade partiet?

Prioritera:

1. `VOTE`

### Fråga: Vad beslutades?

Prioritera:

1. `DECISION`

### Fråga: Vad blev genomfört?

Prioritera:

1. `OUTCOME`

---

## 9. Förbjudna evidensuppgraderingar

Valguiden ska inte automatiskt göra följande:

### PROPOSAL → OFFICIAL_POLICY

Fel:

> En ledamot motionerade om X, alltså vill partiet X.

Korrekt:

> En ledamot från partiet motionerade om X.

### VOTE → DECISION

Fel:

> Partiet röstade ja, alltså beslutade partiet X.

Korrekt:

> Partiet röstade ja i voteringen. Det slutliga beslutet var ...

### DECISION → OUTCOME

Fel:

> Kommunen beslutade X, alltså genomfördes X.

Korrekt:

> Kommunen beslutade X. Jag hittar/ hittar inte belägg för senare genomförande.

### STATEMENT → OFFICIAL_POLICY

Fel:

> En kandidat sade X, alltså är X partiets officiella linje.

Korrekt:

> Kandidaten sade X. Jag hittar inte tillräckligt stöd för att beskriva det som officiell partipolitik.

### OUTCOME → KAUSALITET

Fel:

> Utfallet förbättrades, alltså orsakade parti X förbättringen.

Korrekt:

> Utfallet förbättrades under perioden. Orsaken kan bero på flera faktorer.

---

## 10. Aktörsnivå

Varje evidenspost ska kopplas till rätt aktör.

Möjliga aktörer:

- hela partiet,
- lokal/regional partiorganisation,
- partigrupp,
- flera ledamöter,
- en enskild ledamot,
- kandidat,
- regering,
- nämnd,
- styrelse,
- fullmäktige,
- riksdagen som beslutande organ.

### Exempel

Källa:

> Motion från Anna Andersson (X).

Rätt formulering:

> Anna Andersson (X) föreslog ...

Fel formulering:

> Parti X föreslog ...

om inget mer stöd finns.

---

## 11. Evidensmetadata

För varje viktigt belägg bör Valguiden hålla reda på:

- evidenstyp,
- datum,
- valnivå,
- aktör,
- dokumenttyp,
- källa,
- verifieringsstatus,
- vilket påstående belägget stödjer,
- eventuell begränsning.

### Exempel

| Fält | Värde |
|---|---|
| Evidenstyp | PROPOSAL |
| Datum | 2025-10-14 |
| Valnivå | Region Norrbotten |
| Aktör | Ledamöter från parti X |
| Dokumenttyp | Motion |
| Verifieringsstatus | VERIFIED |
| Stödjer | Ledamöterna föreslog X |
| Begränsning | Inte automatiskt officiell partilinje |

---

## 12. Evidensstyrka

Valguiden kan beskriva hur väl en källa stödjer en slutsats.

Rekommenderade nivåer:

### STARKT_DIREKT_STÖD

Källan visar direkt det påståendet.

### TYDLIGT_STÖD

Källan stödjer slutsatsen tydligt men viss tolkning krävs.

### INDIREKT_STÖD

Källan pekar i riktning mot slutsatsen men räcker inte ensam.

### BEGRÄNSAT_STÖD

Endast enstaka eller svag evidens finns.

### OTILLRÄCKLIGT_STÖD

Källan räcker inte för slutsatsen.

---

## 13. Kombination av evidens

En starkare slutsats kan ibland kräva flera evidenstyper.

Exempel:

> Partiet har drivit frågan konsekvent under mandatperioden.

Bättre stöd:

- `OFFICIAL_POLICY`
- flera `PROPOSAL`
- relevanta `VOTE`
- återkommande `STATEMENT`

än ett enskilt dokument.

---

## 14. Konflikt mellan evidenstyper

Om olika evidenstyper pekar åt olika håll ska det redovisas.

Exempel:

- valmanifest 2022: X
- votering 2024: Y
- budget 2025: Z

Möjliga förklaringar:

- positionsförändring,
- kompromiss,
- regeringssamarbete,
- teknisk voteringsfråga,
- intern oenighet,
- olika beslutnivåer.

Valguiden ska inte välja en förklaring utan stöd.

---

## 15. Politisk aktivitet kontra politiskt inflytande

Följande kan mätas som aktivitet:

- antal motioner,
- antal frågor,
- antal interpellationer,
- antal anföranden.

Det betyder inte automatiskt:

- större inflytande,
- bättre politik,
- större genomslag,
- större engagemang i kvalitativ mening.

Om Valguiden använder aktivitetsmått ska måttet anges explicit.

---

## 16. Löften

Ett vallöfte bör normalt kräva `OFFICIAL_POLICY`.

Bra källor:

- valmanifest,
- officiellt vallöftesdokument,
- tydligt officiellt kampanjmaterial.

Var försiktig med att kalla:

- debattuttalande,
- enskild motion,
- intervju,

för "vallöfte".

---

## 17. Genomförandegrad

För att analysera om ett löfte "genomförts" krävs mer än beslut.

En förenklad kedja:

`OFFICIAL_POLICY`
→ `PROPOSAL`
→ `VOTE`
→ `DECISION`
→ `OUTCOME`

Alla steg finns inte alltid.

Valguiden ska redovisa vilket steg evidensen faktiskt når.

---

## 18. Exempel – komplett evidenskedja

Fråga:

> Har parti X gjort det de lovade om vårdköer?

Möjlig analys:

1. `OFFICIAL_POLICY`  
   Valmanifestet lovar X.

2. `PROPOSAL`  
   Partiet lägger budgetförslag med åtgärd Y.

3. `VOTE`  
   Partiet röstar för beslut Z.

4. `DECISION`  
   Regionfullmäktige beslutar Z.

5. `OUTCOME`  
   Årsredovisningen visar att Z genomförts eller inte genomförts.

Först därefter bör slutsats om löfte kontra agerande göras.

---

## 19. Snabbtabell

| Evidenstyp | Visar främst | Visar inte automatiskt |
|---|---|---|
| OFFICIAL_POLICY | Officiell ståndpunkt | Genomförande |
| PROPOSAL | Förslag | Beslut |
| VOTE | Hur någon röstade | Slutligt beslut |
| DECISION | Formellt beslut | Praktiskt utfall |
| STATEMENT | Vad någon sagt | Officiell partilinje |
| OUTCOME | Genomförande/resultat | Ensam politisk kausalitet |

---

## 20. Beslutsregel

När ett nytt belägg hittas:

1. Identifiera dokumenttyp.
2. Identifiera aktör.
3. Klassificera evidenstyp.
4. Kontrollera vad källan faktiskt stödjer.
5. Kontrollera om starkare eller kompletterande evidens behövs.
6. Lägg aldrig till en starkare slutsats än evidensen bär.
