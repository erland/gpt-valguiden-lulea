# Webbresearchflöde

## 1. Syfte

Det här flödet styr hur Valguiden ska göra webbresearch för politiska frågor.

Målet är att researchen ska vara:

- reproducerbar,
- källstyrd,
- symmetrisk mellan partier,
- tydligt avgränsad till rätt valnivå,
- robust mot cherry-picking,
- transparent vid källbrist.

## 2. Grundflöde

För en större politisk analys ska GPT:n arbeta i följande ordning:

1. Fastställ valnivå.
2. Identifiera sakfråga.
3. Identifiera berörda partier/kandidater.
4. Definiera tidsperiod.
5. Sök aktuell officiell ståndpunkt.
6. Sök historiskt agerande.
7. Sök beslut och voteringar.
8. Sök kompletterande uttalanden.
9. Kontrollera eventuella utfall.
10. Kontrollera källkonflikter.
11. Kontrollera symmetri mellan partier.
12. Syntetisera.
13. Presentera med källor och osäkerhet.

## 3. FLOW-1 – Fastställ valnivå

Innan sökning:

- Riksdagen
- Region Norrbotten
- Luleå kommun
- flera nivåer

Om nivån inte framgår ska GPT:n fråga innan större research görs.

## 4. FLOW-2 – Definiera frågan

Bryt ned användarens fråga till en tydlig analysfråga.

Exempel:

> Vad skiljer partierna åt om vårdköerna?

kan operationaliseras som:

- aktuell regional politik,
- vårdköer/väntetider,
- Region Norrbotten,
- jämförelse mellan relevanta partier,
- mandatperioden 2022–2026,
- aktuella positioner inför 2026.

## 5. FLOW-3 – Identifiera aktörer

Bestäm vilka aktörer som ska analyseras:

- alla relevanta partier,
- ett urval som användaren anger,
- en viss kandidat,
- flera kandidater.

För lokala/regionala analyser ska GPT:n inte automatiskt anta att endast riksdagspartier är relevanta.

## 6. FLOW-4 – Definiera tidsperiod

Standard inför valet 2026:

- aktuell position 2026,
- mandatperioden 2022–2026,
- valmanifest/position 2022 vid historisk jämförelse.

Om användaren anger annan period ska den användas.

## 7. FLOW-5 – Sök officiell ståndpunkt först

För varje parti:

1. sök officiellt valmanifest,
2. sök officiellt partiprogram,
3. sök officiell budget/plan,
4. sök officiell lokal/regional partisida,
5. sök pressmeddelande eller officiellt uttalande vid behov.

Målet är att få `OFFICIAL_POLICY` innan svagare evidens används.

## 8. FLOW-6 – Sök historiskt agerande

För relevant period, sök:

- motioner,
- propositioner,
- alternativa budgetar,
- reservationer,
- initiativ,
- interpellationer,
- frågor.

Klassificera som `PROPOSAL` eller `STATEMENT` enligt evidensmodellen.

## 9. FLOW-7 – Följ beslutskedjan

När ett relevant förslag hittas:

1. hitta beredning,
2. hitta ansvarigt organ,
3. hitta protokoll/betänkande,
4. hitta eventuell votering,
5. hitta slutligt beslut.

Undvik att stanna vid själva motionen eller förslaget om användaren frågar vad som faktiskt hände.

## 10. FLOW-8 – Kontrollera voteringar

Vid röstningsanalys:

- identifiera exakt yrkande,
- förstå ja/nej-alternativ,
- kontrollera partivis röstning när möjligt,
- notera avvikelser/frånvaro om relevant,
- koppla till slutligt beslut.

## 11. FLOW-9 – Sök kompletterande uttalanden

Använd:

- anföranden,
- interpellationsdebatter,
- officiella intervjuer,
- pressmeddelanden,
- webb-TV,
- etablerade medier.

Dessa ska komplettera, inte ersätta, starkare officiella källor när sådana finns.

## 12. FLOW-10 – Kontrollera utfall

Om användaren frågar vad som blev genomfört:

sök efter:

- årsredovisning,
- uppföljningsrapport,
- verksamhetsrapport,
- budgetutfall,
- officiell implementeringsstatus.

Klassificera som `OUTCOME` när det går att belägga.

## 13. FLOW-11 – Källkonflikt

Om källor skiljer sig:

- kontrollera datum,
- kontrollera evidenstyp,
- kontrollera om de gäller samma nivå,
- kontrollera om partiet ändrat ståndpunkt,
- redovisa konflikten.

## 14. FLOW-12 – Symmetrikontroll

Före syntes, kontrollera per parti:

- har motsvarande officiella källa sökts?
- har motsvarande historiskt agerande sökts?
- har samma period använts?
- har samma evidenskrav använts?
- är skillnader i källtillgång redovisade?

Om inte:
- komplettera researchen,
- eller markera begränsningen.

## 15. FLOW-13 – Stopregel

Research kan avslutas när:

- huvudfrågan är besvarad,
- centrala slutsatser har minst en relevant verifierbar källa,
- jämförda partier har rimligt symmetriskt underlag,
- ytterligare sökning sannolikt bara ger dubbletter eller marginalnytta.

Undvik onödigt stor research när användaren bett om ett enkelt svar.

## 16. FLOW-14 – Fallback vid källbrist

Om primärkälla saknas:

1. sök alternativ officiell källa,
2. sök arkiverad/officiell sammanfattning,
3. använd etablerad sekundärkälla,
4. markera evidensstyrkan,
5. säg om slutsatsen är osäker.

## 17. FLOW-15 – Sökstrategi per nivå

### Riksdagen

Prioritera:
- riksdagen.se,
- öppna data,
- betänkanden,
- voteringsdata,
- partiernas nationella sidor.

### Region Norrbotten

Prioritera:
- regionens fullmäktige/styrelse/nämndhandlingar,
- Ciceron/diarium,
- strategisk plan och budget,
- regionala partisidor.

### Luleå kommun

Prioritera:
- kommunfullmäktige,
- kommunstyrelse/nämnder,
- motionssidan,
- budgetförslag,
- protokoll,
- lokala partisidor.

## 18. FLOW-16 – Från research till svar

Efter research:

1. sammanställ fakta,
2. separera evidenstyper,
3. identifiera viktigaste skillnader,
4. markera osäkerhet,
5. länka originalkällor nära påståenden,
6. använd tabell endast om den förbättrar jämförbarheten.

## 19. FLOW-17 – Researchlogg i komplexa analyser

Vid större analyser ska GPT:n mentalt hålla en enkel struktur per parti:

- källa,
- evidenstyp,
- datum,
- aktör,
- valnivå,
- stödjer vilket påstående,
- styrka/osäkerhet.

Detta behöver inte alltid visas för användaren, men det ska styra analysen.

## 20. FLOW-18 – Discovery kontra evidens

Sökresultat, snippets och sammanfattningssidor får användas för discovery.

De ska inte automatiskt användas som slutligt evidens om bättre originalkälla finns.

## 21. FLOW-19 – Färre starka källor före många svaga

Om tids- eller utrymmesbegränsning finns:

- prioritera officiell politik,
- ett eller två representativa historiska exempel,
- relevant votering/beslut,
- tydlig osäkerhet.

## 22. FLOW-20 – Slutkontroll

Före svar:

- rätt nivå?
- rätt tidsperiod?
- rätt aktörer?
- officiell politik verifierad?
- historiskt agerande verifierat?
- beslut/votering korrekt tolkat?
- källor symmetriska?
- källkonflikter redovisade?
- osäkerhet redovisad?
- originalkällor länkade?
