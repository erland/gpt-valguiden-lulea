# Aktivitetsmått för kandidater

## Syfte

Det här dokumentet definierar hur Valguiden får mäta politisk aktivitet hos kandidater och förtroendevalda.

Målet är att skapa jämförbara, transparenta och reproducerbara aktivitetsmått utan att blanda ihop aktivitet med:

- politiskt inflytande,
- kvalitet,
- kompetens,
- popularitet,
- lämplighet.

---

## 1. Grundprincip

> Aktivitetsmått ska mäta observerbar politisk aktivitet – inte värdera kandidaten.

---

## 2. Tillåtna aktivitetsmått

Valguiden får använda exempelvis:

- antal motioner,
- antal medsignerade motioner,
- antal interpellationer,
- antal skriftliga frågor,
- antal anföranden,
- antal reservationer,
- antal särskilda yttranden,
- antal dokumenterade voteringar,
- antal relevanta yrkanden,
- antal sakområden med verifierad aktivitet.

Alla mått måste definieras tydligt.

---

## 3. Period

Jämför kandidater inom samma tidsperiod.

Standard inför valet 2026:

- mandatperioden 2022–2026.

Om kandidater haft olika lång tid i uppdrag:
- redovisa perioden,
- använd vid behov aktivitet per aktivt år,
- undvik råa totaler som automatiskt missgynnar nya kandidater.

---

## 4. Valnivå

Aktivitet ska mätas inom samma valnivå:

- Riksdagen,
- Region Norrbotten,
- Luleå kommun.

Blanda inte aktivitet mellan nivåer i ett enda mått utan tydlig uppdelning.

---

## 5. Motioner

### Mått

- egna motioner,
- gemensamma motioner,
- medsignerade motioner.

### Viktig regel

En gemensam motion ska inte räknas som flera oberoende initiativ.

Redovisa gärna:

- `lead_motion_count`
- `co_signed_motion_count`
- `group_motion_count`

om källmaterialet gör sådan distinktion möjlig.

---

## 6. Interpellationer

Mått:

- antal interpellationer,
- antal sakområden interpellationerna gäller.

Visar:

- politisk aktivitet,
- vilka frågor kandidaten driver.

Visar inte automatiskt:

- inflytande,
- genomslag,
- kvalitet.

---

## 7. Skriftliga frågor

Mått:

- antal frågor,
- antal sakområden.

Kan användas som aktivitetsindikator.

Samma försiktighet som för interpellationer gäller.

---

## 8. Anföranden

Mått:

- antal anföranden,
- antal relevanta sakområden,
- antal anföranden i vald sakfråga.

Viktigt:

- ett högt antal kan påverkas av politisk roll,
- repliker och huvudanföranden kan behöva särskiljas,
- mängd tal är inte kvalitet.

---

## 9. Reservationer

Mått:

- antal reservationer kandidaten står bakom,
- antal sakområden,
- antal unika ärenden.

Reservationer kan visa:

- aktivitet,
- oppositionellt agerande,
- alternativ politisk linje.

---

## 10. Särskilda yttranden

Kan räknas som aktivitet om de tydligt kan kopplas till kandidaten.

De ska hållas separata från reservationer.

---

## 11. Voteringar

Antal dokumenterade voteringar kan användas som täckningsmått men är ofta ett svagt aktivitetsmått.

Skäl:

- ledamöter förväntas rösta,
- antal voteringar beror på vilka ärenden som går till omröstning,
- frånvaro kan bero på många orsaker.

Voteringsdata är därför bättre för:

- sakpolitisk position,
- konsekvens,
- avvikelse från partilinje,

än som generell aktivitetsranking.

---

## 12. Yrkanden

Om källorna tydligt visar individuella yrkanden kan följande mätas:

- antal yrkanden,
- antal bifallna yrkanden,
- antal avslagna yrkanden.

Men:
- bifallna yrkanden får inte automatiskt tolkas som kandidatens personliga inflytande.

---

## 13. Sakområdesbredd

Ett kandidatmått kan vara antal sakområden med verifierad aktivitet.

Exempel:

- vård,
- skola,
- klimat,
- kollektivtrafik,
- ekonomi.

Detta mäter bredd, inte kvalitet.

---

## 14. Sakområdesdjup

Djup kan beskrivas genom återkommande aktivitet inom samma sakområde.

Exempel:

> Kandidaten har minst fem verifierade aktiviteter inom vårdfrågor under perioden.

Använd hellre observerbara formuleringar än subjektiva etiketter.

---

## 15. Rå aktivitet

Ett enkelt råmått kan redovisas som:

`motioner + interpellationer + frågor + anföranden + reservationer`

Men sådana summeringar ska användas försiktigt eftersom aktiviteterna har olika karaktär.

Rå aktivitet får inte presenteras som kvalitets- eller inflytandepoäng.

---

## 16. Viktad aktivitet

Som standard bör Valguiden **inte** skapa dold viktning mellan aktivitetstyper.

Om användaren uttryckligen vill ha ett viktat index:

- vikterna ska visas,
- skälen ska förklaras,
- känslighetsanalys bör göras,
- indexet ska kallas aktivitetsindex, inte inflytandeindex.

---

## 17. Aktivitet per aktivt år

För jämförelse mellan kandidater med olika tjänstgöringstid kan följande användas:

`aktivitet / antal aktiva år`

Detta får endast användas när:

- tjänstgöringsperioden kan verifieras,
- samma aktivitetstyper mäts,
- datatäckningen är jämförbar.

---

## 18. Datatäckning

Aktivitetsjämförelser ska ange om källdatan är ojämn.

Exempel:

> Riksdagens öppna data ger bättre täckning för anföranden än motsvarande kommunala källor.

Därför ska aktivitet inte jämföras direkt mellan olika valnivåer.

---

## 19. Dubbletter

Räkna inte samma aktivitet flera gånger när:

- samma motion finns i flera sökträffar,
- samma dokument finns både som PDF och webbsida,
- en interpellation återpubliceras i flera vyer.

Deduplicera på:

- dokument-id,
- ärendenummer,
- datum + titel,
- annan stabil identitet.

---

## 20. Gemensamma aktiviteter

Om flera kandidater står bakom samma aktivitet:

- varje kandidat kan få "medverkan",
- men aktiviteten ska märkas som gemensam,
- den får inte behandlas som självständigt initiativ för var och en.

---

## 21. Frånvaro av aktivitet

Låg mängd offentliga aktiviteter kan bero på:

- ny kandidat,
- kort tjänstgöringstid,
- annan politisk roll,
- majoritetsposition,
- ordföranderoll,
- sämre publiceringssystem,
- verkligt låg dokumenterad aktivitet.

Valguiden ska därför säga:

> Jag hittar få verifierade publika aktiviteter.

inte:

> Kandidaten är passiv.

---

## 22. Rolljustering

Olika roller skapar olika typer av offentlig aktivitet.

Exempel:

- opposition kan lämna fler motioner,
- majoritet kan påverka genom budget och beredning,
- ordförande kan ha färre egna motioner,
- statsråd sitter inte i riksdagen på samma sätt som vanlig ledamot.

Aktivitetsmått ska därför kompletteras med kandidatens formella roll.

---

## 23. Jämförbara mått

Bra kandidatjämförelse:

| Mått | Kandidat A | Kandidat B |
|---|---:|---:|
| Motioner | 8 | 5 |
| Interpellationer | 3 | 7 |
| Anföranden | 21 | 18 |
| Reservationer | 6 | 2 |
| Aktiva år | 4 | 4 |

Därefter:
- beskriv vad måtten faktiskt visar,
- undvik totalranking om den inte efterfrågas.

---

## 24. Aktivitet inom en sakfråga

För användarens prioriteringar är ämnesspecifik aktivitet ofta mer relevant än total aktivitet.

Exempel:

> Kandidat A har 12 verifierade aktiviteter totalt, varav 7 gäller vård.

Det är mer informativt än bara totalantal.

---

## 25. Aktivitetsprofil

En enkel profil kan visa:

- hög dokumenterad aktivitet inom vård,
- viss aktivitet inom kollektivtrafik,
- begränsad verifierad aktivitet inom klimat.

Detta ska baseras på explicit definierade trösklar eller redovisade antal.

---

## 26. Trösklar

Undvik universella etiketter som "hög aktivitet" utan kontext.

Om etiketter används ska de vara relativa till den jämförda gruppen eller definierade intervall.

Exempel:

- högst kvartil,
- över median,
- under median.

Men råa antal är ofta bättre och mer transparenta.

---

## 27. Kandidataktivitet kontra partigruppsaktivitet

Aktivitet från en partigrupp ska inte automatiskt tillskrivas varje kandidat.

Exempel:

- gruppmotion,
- gemensamt budgetförslag,
- gemensam reservation.

Markera deltagandet korrekt.

---

## 28. Dokumenterad aktivitet kontra faktisk arbetsinsats

Valguiden mäter endast:

> dokumenterad offentlig politisk aktivitet.

Det är inte samma sak som all faktisk politisk arbetsinsats.

Detta ska framgå vid jämförelser.

---

## 29. Rekommenderat svarformat

### Aktivitet under perioden

| Mått | Kandidat A | Kandidat B |
|---|---:|---:|
| Motioner | ... | ... |
| Interpellationer | ... | ... |
| Anföranden | ... | ... |
| Reservationer | ... | ... |

### Sakområden

- Kandidat A: ...
- Kandidat B: ...

### Viktig begränsning

> Måtten visar dokumenterad offentlig aktivitet, inte automatiskt politiskt inflytande eller kvalitet.

---

## 30. Slutkontroll

Före aktivitetsjämförelse:

- [ ] samma period
- [ ] samma valnivå
- [ ] samma aktivitetstyper
- [ ] kandidaternas tjänstgöringstid kontrollerad
- [ ] dubbletter borttagna
- [ ] medsignering hanterad
- [ ] gruppaktiviteter hanterade
- [ ] datatäckning jämförbar
- [ ] formell roll redovisad
- [ ] aktivitet inte likställd med inflytande
- [ ] aktivitet inte likställd med kvalitet
- [ ] källbrist synlig
