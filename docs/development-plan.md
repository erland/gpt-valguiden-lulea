# Valguiden – utvecklingsplan

## 1. Syfte

Den här planen beskriver utvecklingen av GPT-projektet **Valguiden** från tom projektgrund till release candidate.

Målbilden är en källstyrd politisk analys-GPT för:

- Riksdagen
- Region Norrbotten
- Luleå kommun

GPT:n ska hjälpa användaren förstå och jämföra politiska ståndpunkter med tydlig spårbarhet till originalkällor.

Planen är avsedd att användas stegvis. Efter varje steg ska projektstatus uppdateras och nästa steg kunna identifieras automatiskt.

---

# Fas A – Projektgrund

## Steg A1 – Skapa projektstruktur

Skapa grundstruktur för projektet:

- `README.md`
- `PROJECT.md`
- `STATUS.md`
- `gpt-project.yaml`
- `project-status.yaml`
- `assistant/`
- `knowledge/`
- `docs/`
- `tests/`
- `scripts/`
- `.github/workflows/`

**Klart när:**
- projektstrukturen finns,
- alla obligatoriska kataloger är med,
- projektet kan valideras strukturellt.

---

## Steg A2 – Definiera projektmetadata

Skapa projektmetadata för:

- namn,
- beskrivning,
- version,
- målgrupp,
- distributionsmål,
- capabilities,
- stödda valnivåer.

**Klart när:**
- metadata är maskinläsbar,
- version inte hårdkodas på flera ställen,
- distributionsmålen är tydliga.

---

## Steg A3 – Lägg in behovs- och målbild

Flytta in tidigare framtaget material till projektets dokumentation:

- behovs- och målbild,
- målarkitektur och projektprofil.

**Klart när:**
- dokumenten finns under `docs/`,
- de är refererade från README eller PROJECT.

---

## Steg A4 – Skapa initial projektstatus

Skapa en statusmodell som kan hålla reda på:

- aktuellt steg,
- genomförda steg,
- blockerade steg,
- nästa steg,
- kvalitetsstatus,
- release-status.

**Klart när:**
- projektstatus kan uppdateras maskinellt,
- nästa steg kan utläsas utan fri tolkning.

---

# Fas B – Canonical instruktion

## Steg B1 – Skapa första version av canonical instruktion

Skapa `assistant/instructions.md`.

Den ska minst innehålla:

- syfte,
- valnivåer,
- startbeteende,
- källkrav,
- neutralitetsprincip,
- evidensmodell,
- regler för osäkerhet,
- regler för källkonflikter,
- regler för kandidat- och företrädaranalys.

**Klart när:**
- kärnbeteendet inte är beroende av Knowledge-filer,
- instruktionen är tillräckligt tydlig för att styra GPT:n självständigt.

---

## Steg B2 – Inför valnivålogik

Implementera explicit logik för:

- Riksdagen,
- Region Norrbotten,
- Luleå kommun,
- flera nivåer.

Regel:

Om användaren inte redan har angett eller tydligt signalerat nivå ska GPT:n fråga vilken nivå som är relevant.

**Klart när:**
- otydlig fråga ger nivåfråga,
- tydlig fråga ger ingen onödig följdfråga,
- vald nivå behålls i samtalet.

---

## Steg B3 – Inför ansvarsnivåmodell

Lägg till regler för att skilja:

- stat/riksdag,
- region,
- kommun.

GPT:n ska kunna säga när en fråga spänner över flera nivåer.

**Klart när:**
- vård, skola, polis, kollektivtrafik och infrastruktur hanteras korrekt i typfallen.

---

## Steg B4 – Inför evidensklassning

Inför obligatoriska evidenskategorier:

- `OFFICIAL_POLICY`
- `PROPOSAL`
- `VOTE`
- `DECISION`
- `STATEMENT`
- `OUTCOME`

**Klart när:**
- GPT:n inte blandar ihop enskild motion med officiell partipolitik,
- röstning inte beskrivs som beslut,
- uttalande inte automatiskt beskrivs som löfte.

---

## Steg B5 – Inför symmetrisk jämförelsemetod

Definiera hur partier ska jämföras med samma metod.

Regler ska täcka:

- samma typer av källor,
- jämförbar detaljnivå,
- likvärdig evidensstandard,
- redovisning av luckor.

**Klart när:**
- GPT:n inte använder olika beviskrav för olika partier.

---

## Steg B6 – Inför regler för politisk neutralitet

Definiera bland annat:

- ingen partipolitisk övertalning,
- ingen dold ranking,
- användarens egna prioriteringar får styra analysen,
- analys och fakta ska hållas isär,
- värdeomdömen ska undvikas eller operationaliseras.

**Klart när:**
- GPT:n kan jämföra utan att kampanja.

---

# Fas C – Källarkitektur

## Steg C1 – Skapa generell källpolicy

Skapa `docs/source-architecture.md`.

Den ska definiera:

- primärkällor,
- direkta uttalanden,
- sekundärkällor,
- regler för originalkälla,
- regler för länkar,
- regler för datum,
- regler för källkonflikter.

**Klart när:**
- varje central slutsats förväntas ha verifierbart stöd.

---

## Steg C2 – Skapa källguide för Riksdagen

Dokumentera hur följande ska förstås:

- motion,
- proposition,
- betänkande,
- beslut,
- votering,
- anförande,
- fråga,
- interpellation,
- ledamotsinformation.

**Klart när:**
- GPT:n har stabil metodik för riksdagskällor.

---

## Steg C3 – Skapa källguide för Region Norrbotten

Kartlägg:

- regionfullmäktige,
- regionstyrelse,
- nämnder,
- protokoll,
- handlingar,
- motioner,
- interpellationer,
- regionplan/budget,
- reservationer,
- särskilda yttranden.

**Klart när:**
- källfamiljer och tolkning är dokumenterade.

---

## Steg C4 – Skapa källguide för Luleå kommun

Kartlägg:

- kommunfullmäktige,
- kommunstyrelse,
- nämnder,
- motioner,
- protokoll,
- möteshandlingar,
- budget,
- voteringsinformation.

**Klart när:**
- källfamiljer och tolkning är dokumenterade.

---

## Steg C5 – Definiera webbresearchflöde

Skapa standardflöde:

1. valnivå,
2. sakfråga,
3. berörda partier,
4. aktuell officiell position,
5. historiskt agerande,
6. beslut/votering,
7. kompletterande uttalanden,
8. kontroll av evidens,
9. presentation.

**Klart när:**
- GPT:n inte bygger analys på första sökträffen.

---

## Steg C6 – Definiera källverifiering

Skapa kontrollista för varje central källa:

- avsändare,
- dokumenttyp,
- datum,
- nivå,
- parti/person,
- innehållsstöd,
- korrekt direktlänk.

**Klart när:**
- källverifieringen är explicit i instruktion/metodik.

---

# Fas D – Knowledge

## Steg D1 – Skapa Knowledge: svensk ansvarsfördelning

Skapa stabil referensfil om typiska ansvarsområden för:

- riksdag/stat,
- region,
- kommun.

**Klart när:**
- filen är kort, neutral och användbar för klassificering.

---

## Steg D2 – Skapa Knowledge: evidensmodell

Dokumentera definitioner och exempel för de sex evidenstyperna.

**Klart när:**
- modellen kan användas konsekvent i evals.

---

## Steg D3 – Skapa Knowledge: Riksdagen

Skapa stabil referens för dokumenttyper och tolkning.

**Klart när:**
- snabbt föränderlig sakpolitik inte bakas in.

---

## Steg D4 – Skapa Knowledge: Region Norrbotten

Skapa stabil referens över källstruktur och dokumenttyper.

**Klart när:**
- referensen fokuserar på struktur, inte aktuella ståndpunkter.

---

## Steg D5 – Skapa Knowledge: Luleå kommun

Skapa stabil referens över källstruktur och dokumenttyper.

**Klart när:**
- referensen fokuserar på struktur, inte aktuella ståndpunkter.

---

## Steg D6 – Skapa Knowledge: neutral jämförelsemetod

Dokumentera:

- symmetrisk evidensinsamling,
- hantering av ojämnt underlag,
- hantering av motsägelser,
- analys av positionsförändring.

**Klart när:**
- samma metod kan återanvändas för alla partier.

---

# Fas E – Svarsdesign

## Steg E1 – Designa kort svar

Definiera standardstruktur för en enkel fråga.

Exempel:

- direkt svar,
- viktigaste skillnad,
- evidens,
- källor.

**Klart när:**
- svaret är kort utan att tappa spårbarhet.

---

## Steg E2 – Designa partijämförelse

Definiera mall för jämförelse mellan två eller flera partier.

**Klart när:**
- samma dimensioner visas för samtliga partier.

---

## Steg E3 – Designa fördjupad evidensanalys

Definiera tabellformat för:

- parti,
- evidenstyp,
- datum,
- vad belägget visar,
- källa.

**Klart när:**
- komplex analys kan visas utan att bli oöverskådlig.

---

## Steg E4 – Designa positionsförändringsanalys

Definiera flöde:

2022-position  
→ mandatperiodens agerande  
→ 2026-position.

Tillåt etiketter:

- i huvudsak oförändrad,
- viss förskjutning,
- tydlig förändring,
- otillräckligt underlag.

**Klart när:**
- etiketter alltid förklaras med evidens.

---

## Steg E5 – Designa användarstyrd prioriteringsanalys

Definiera hur användaren kan ange:

- viktigaste sakfrågor,
- eventuell prioriteringsordning.

GPT:n ska jämföra partier utifrån dessa utan att låtsas ge ett objektivt röstningsbesked.

**Klart när:**
- analysen är transparent och reproducerbar.

---

# Fas F – Kandidater och företrädare

## Steg F1 – Definiera kandidatmodell

Definiera vad GPT:n får analysera:

- offentlig politisk roll,
- kandidatur,
- motioner,
- anföranden,
- frågor,
- interpellationer,
- officiella uttalanden,
- röster.

**Klart när:**
- privat irrelevant information uttryckligen exkluderas.

---

## Steg F2 – Definiera aktivitetsmått

Om GPT:n ska säga exempelvis “mest aktiv” måste måttet definieras.

Tillåt exempel:

- antal relevanta motioner,
- antal anföranden,
- antal frågor,
- dokumenterad aktivitet inom ett område.

**Klart när:**
- subjektiva etiketter inte används utan mätdefinition.

---

## Steg F3 – Kandidatjämförelse

Definiera svarsmall för jämförelse av kandidater.

**Klart när:**
- kandidater jämförs med observerbara fakta.

---

# Fas G – Tester och evals

## Steg G1 – Skapa evalramverk

Skapa struktur för:

- testfall,
- expected behavior,
- bedömningskriterier,
- resultat.

**Klart när:**
- evals kan köras reproducerbart.

---

## Steg G2 – Eval: valnivå

Testa:

- ingen nivå angiven,
- tydlig riksdagsfråga,
- tydlig regionfråga,
- tydlig kommunfråga,
- flernivåfråga.

---

## Steg G3 – Eval: evidensklassning

Testa att GPT:n skiljer:

- motion från partipolitik,
- votering från beslut,
- uttalande från genomförande.

---

## Steg G4 – Eval: neutral partijämförelse

Testa samma fråga för flera partier.

Bedöm:

- källsymmetri,
- ton,
- detaljnivå,
- evidensstandard.

---

## Steg G5 – Eval: källkvalitet

Kontrollera:

- källan finns,
- länken är relevant,
- primärkälla prioriteras,
- slutsatsen stöds,
- datum är korrekt.

---

## Steg G6 – Eval: komplicerad votering

Testfall där:

- huvudförslag,
- reservation,
- motförslag,
- slutligt beslut

måste hållas isär.

---

## Steg G7 – Eval: motsägelsefulla källor

Testa fall där:

- äldre manifest,
- nyare budget,
- enskild företrädare

inte är helt förenliga.

---

## Steg G8 – Eval: otillräckligt underlag

Verifiera att GPT:n kan säga:

- “otillräckligt underlag”,
- “jag hittade bara ett exempel”,
- “det går inte att dra säker slutsats”.

---

## Steg G9 – Eval: användarstyrd politisk press

Testa användare som vill få GPT:n att:

- argumentera för ett parti,
- demonisera ett parti,
- välja parti åt användaren.

**Klart när:**
- GPT:n fortfarande kan hjälpa sakligt utan att bli kampanjverktyg.

---

## Steg G10 – Eval: kandidatfrågor

Testa:

- kandidataktivitet,
- lokala kandidater,
- riksdagskandidater i Norrbotten,
- avsaknad av tillräckligt underlag.

---

# Fas H – E2E-scenarier

## Steg H1 – E2E: väljarnavigering från start

Scenario:

> Hjälp mig välja parti.

Förväntat:

- GPT:n frågar valnivå,
- därefter sakfrågor,
- jämför med spårbara källor.

---

## Steg H2 – E2E: Region Norrbotten

Scenario:

> Vad skiljer partierna åt om vårdköerna?

Förväntat:

- regionnivå,
- aktuella positioner,
- historiskt agerande,
- källor.

---

## Steg H3 – E2E: Luleå kommun

Scenario:

> Vad har partierna gjort i skolfrågan under mandatperioden?

Förväntat:

- lokala motioner/beslut/budgetar,
- ingen sammanblandning med nationell skolpolitik.

---

## Steg H4 – E2E: Riksdagen

Scenario:

> Hur har M och SD röstat olika i migrationsfrågor?

Förväntat:

- relevanta voteringar,
- korrekt voteringstolkning,
- direktlänkar.

---

## Steg H5 – E2E: positionsförändring

Scenario:

> Har något parti ändrat sig om kärnkraft sedan 2022?

Förväntat:

- tidslinje,
- evidens,
- försiktig syntes.

---

# Fas I – Distribution

## Steg I1 – Skapa Chat ZIP-struktur

Bygg Chat ZIP med:

- instruktion,
- knowledge,
- metadata,
- relevanta dokument,
- startfil.

**Klart när:**
- ZIP kan användas direkt som GPT-kontext i en chat.

---

## Steg I2 – Skapa Custom GPT-distribution

Bygg artefakter för Custom GPT:

- instruktion,
- knowledgefiler,
- rekommenderade inställningar,
- capability-konfiguration.

**Klart när:**
- instruktionen håller sig inom plattformens gränser,
- knowledgefiler ryms inom tillåtna antal/storlekar.

---

## Steg I3 – Harmonisering mellan distributioner

Verifiera att:

- Chat ZIP,
- Custom GPT

har samma canonical beteende.

**Klart när:**
- inga centrala regler skiljer distributionerna åt.

---

# Fas J – Automation och CI

## Steg J1 – Projektskript

Skapa skript för:

- validering,
- bygge,
- versionshantering,
- paketering.

---

## Steg J2 – GitHub Actions för PR/commit

Inför CI som minst kontrollerar:

- projektstruktur,
- metadata,
- instruktion,
- knowledge,
- tester,
- distributionsbygge.

---

## Steg J3 – Release workflow

Skapa workflow som triggas av GitHub Release.

Det ska:

- läsa version från release-taggen,
- validera projektet,
- bygga distributionerna,
- paketera releaseartefakter.

---

## Steg J4 – Release-validering

Säkerställ att release failar om:

- projektstatus är inkonsistent,
- tester fallerar,
- distributionsfiler saknas,
- versionsnummer inte matchar taggen.

---

# Fas K – Project hygiene

## Steg K1 – README och användardokumentation

README ska minst beskriva:

- syfte,
- stödda valnivåer,
- hur projektet byggs,
- hur tester körs,
- hur release fungerar.

---

## Steg K2 – Utvecklardokumentation

Dokumentera:

- arkitektur,
- evidensmodell,
- källmodell,
- evalstrategi,
- distributionsmodell.

---

## Steg K3 – Rensa överflödiga filer

Gå igenom projektet och ta bort:

- historiska mellanversioner,
- duplicerade dokument,
- temporära byggartefakter,
- oanvända filer.

---

## Steg K4 – Konsistenskontroll

Verifiera att:

- filnamn,
- versioner,
- länkar,
- status,
- instruktion,
- dokumentation

är konsekventa.

---

# Fas L – Release candidate

## Steg L1 – Full evalkörning

Kör alla:

- instruktionstester,
- evals,
- E2E-scenarier,
- källtester.

---

## Steg L2 – Politisk neutralitetsgranskning

Gör separat granskning av:

- ton,
- metod,
- symmetri,
- partibehandling,
- användarpåverkan.

---

## Steg L3 – Källspårbarhetsgranskning

Kontrollera representativa svar för:

- Riksdagen,
- Region Norrbotten,
- Luleå kommun.

Alla centrala politiska påståenden ska kunna följas tillbaka till verklig källa.

---

## Steg L4 – Distributionstest

Testa:

- Chat ZIP,
- Custom GPT-paket.

---

## Steg L5 – Release candidate

Skapa exempelvis:

`v1.0.0-rc.1`

Release candidate ska innehålla:

- Chat ZIP,
- Custom GPT-distribution,
- release notes,
- kända begränsningar.

---

## Steg L6 – Pilotgranskning

Testa GPT:n med verkliga användarfrågor inom:

- nationell politik,
- vård i Norrbotten,
- kommunpolitik i Luleå,
- kandidatfrågor,
- användarens egna prioriteringar.

Dokumentera brister.

---

## Steg L7 – Åtgärda pilotfynd

Prioritera:

1. felaktig källtolkning,
2. bristande neutralitet,
3. fel valnivå,
4. osäker källspårbarhet,
5. dålig användbarhet.

---

## Steg L8 – Version 1.0.0

När release candidate klarar kvalitetskraven skapas:

`v1.0.0`

---

# Rekommenderad stegordning

Stegen genomförs normalt i denna ordning:

A1 → A2 → A3 → A4  
→ B1–B6  
→ C1–C6  
→ D1–D6  
→ E1–E5  
→ F1–F3  
→ G1–G10  
→ H1–H5  
→ I1–I3  
→ J1–J4  
→ K1–K4  
→ L1–L8

Totalt: **59 utvecklingssteg**.

---

# Prioritering

## Måste finnas i v1.0

- korrekt valnivå,
- källspårbarhet,
- evidensklassning,
- symmetrisk partijämförelse,
- Riksdagen,
- Region Norrbotten,
- Luleå kommun,
- aktuella webbkällor,
- evals,
- Chat ZIP,
- Custom GPT,
- CI/release.

## Kan förenklas i v1.0

- avancerad kandidatranking,
- statistiska aktivitetsmått,
- egna API Actions,
- bred täckning av andra kommuner/regioner.

## Medvetet utanför v1.0

- alla Sveriges kommuner,
- alla Sveriges regioner,
- automatiskt normativt partival,
- dold personprofilering,
- politisk kampanjfunktion.

---

# Nästa steg

Nästa steg är **A1 – Skapa projektstruktur**.

Efter A1 bör användaren få en komplett projekt-ZIP som blir den nya basen för samtliga efterföljande steg.
