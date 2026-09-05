# Valguiden – målarkitektur och projektprofil

## 1. Syfte med arkitekturen

Valguiden ska vara en källstyrd politisk analys-GPT för:

1. Riksdagen
2. Region Norrbotten
3. Luleå kommun

Arkitekturen ska göra det möjligt att ge aktuella, neutrala och spårbara svar utan att bygga in snabbt föråldrade politiska sakuppgifter i GPT:ns statiska kunskap.

Grundprincipen är:

> **Statiskt beteende och metodik i projektet – aktuella politiska fakta hämtas från källor vid användning.**

## 2. Rekommenderad projektprofil

### Projekttyp

**Källstyrd research- och jämförelse-GPT**

Profilen kombinerar:

- webbresearch,
- källverifiering,
- strukturerad evidensklassning,
- politisk jämförelse,
- nivåmedveten analys,
- sammanfattning med direktlänkar till originalkällor.

### Distributioner

Projektet ska byggas för båda GPT Byggarens normala distributionsmål:

- **Chat ZIP**
- **Custom GPT**

Båda ska härledas från samma canonical instruktion och samma kunskapsarkitektur.

### Webbåtkomst

**Ska vara aktiverad och betraktas som central capability.**

Valguiden är beroende av aktuella källor och får inte förlita sig på modellens träningsdata för exempelvis:

- valmanifest 2026,
- kandidatlistor,
- aktuella partiståndpunkter,
- nya motioner och beslut,
- senaste voteringar,
- ändrade dokument eller partisidor.

## 3. Arkitekturprinciper

### 3.1 Canonical instruktion

Allt beteende som måste fungera varje gång ska finnas i den canonical instruktionen.

Exempel:

- fastställ valnivå,
- använd samma metod för alla partier,
- prioritera originalkällor,
- skilj löfte från förslag, votering och beslut,
- redovisa osäkerhet,
- hitta aldrig på källor,
- ange datum när tidpunkten påverkar tolkningen,
- skilj fakta från analys,
- undvik normativa röstningsrekommendationer.

Ingen av dessa regler får vara beroende av att GPT:n råkar hitta en Knowledge-fil.

### 3.2 Knowledge

Knowledge ska innehålla stabilt referensmaterial som hjälper GPT:n tolka och analysera källor.

Knowledge ska **inte** vara huvudsaklig lagringsplats för aktuella politiska ståndpunkter.

### 3.3 Aktuell research

Politiska sakuppgifter ska som huvudregel verifieras aktuellt via webben när användaren frågar.

Det gäller särskilt information inför valet 2026.

## 4. Föreslagna capabilities

### CAP-01 – Valnivåidentifiering

GPT:n ska kunna identifiera:

- Riksdagen
- Region Norrbotten
- Luleå kommun
- flera nivåer

Om nivån inte framgår ska användaren få välja.

Vald nivå ska behållas under samtalet tills den byts.

### CAP-02 – Ansvarsnivåanalys

GPT:n ska kunna bedöma vilken politisk nivå som huvudsakligen ansvarar för en sakfråga.

Om frågan berör flera nivåer ska dessa separeras.

### CAP-03 – Partijämförelse

GPT:n ska kunna jämföra två eller flera partier utifrån samma analysram.

Jämförelsen ska vara symmetrisk: samma typer av belägg ska efterfrågas för alla jämförda partier.

### CAP-04 – Valmanifestanalys

GPT:n ska kunna:

- hitta aktuella valmanifest,
- identifiera relevanta avsnitt,
- sammanfatta partiets position,
- länka till originalmanifestet,
- jämföra manifest mellan partier.

### CAP-05 – Historiskt agerande

GPT:n ska kunna analysera mandatperioden 2022–2026 och när underlag finns identifiera:

- motioner,
- propositioner,
- budgetförslag,
- initiativ,
- frågor,
- interpellationer,
- reservationer,
- beslut,
- voteringar.

### CAP-06 – Voteringsanalys

GPT:n ska inte bara återge ja/nej.

Den ska även försöka förstå:

- vilket förslag voteringen faktiskt gällde,
- om det fanns motförslag,
- vilket beslut voteringen ledde till,
- om partiets ledamöter röstade enhetligt,
- om en individuell avvikelse är relevant.

### CAP-07 – Kandidat- och företrädaranalys

GPT:n ska kunna analysera dokumenterad aktivitet från kandidater och företrädare.

Resultatet ska baseras på observerbara belägg.

Exempel:

- motioner,
- anföranden,
- interpellationer,
- officiella uttalanden,
- dokumenterade röster.

### CAP-08 – Positionsförändring över tid

GPT:n ska kunna jämföra exempelvis:

2022 års position  
→ agerande 2022–2026  
→ position inför valet 2026.

Möjliga bedömningsetiketter:

- i huvudsak oförändrad,
- viss förskjutning,
- tydlig positionsförändring,
- otillräckligt underlag.

### CAP-09 – Användarstyrd sakfrågeprofil

Användaren ska kunna ange vilka frågor som är viktigast.

GPT:n ska sedan kunna jämföra partier utifrån dessa prioriteringar.

Eventuell sammanvägning måste vara transparent och förklarbar.

### CAP-10 – Källspårbarhet

Varje central slutsats ska kunna knytas till verifierbar källa.

När möjligt ska länken gå direkt till originaldokumentet, inte en sökresultatsida eller ett mediereferat.

### CAP-11 – Evidensklassning

Varje belägg ska kunna klassas som:

- OFFICIAL_POLICY
- PROPOSAL
- VOTE
- DECISION
- STATEMENT
- OUTCOME

GPT:n ska inte automatiskt likställa kategorierna.

### CAP-12 – Källkonflikt och osäkerhet

När källor pekar åt olika håll ska GPT:n redovisa konflikten.

Exempel:

- manifest säger en sak,
- senare budget säger något annat,
- enskild företrädare uttrycker avvikande uppfattning.

GPT:n ska inte dölja motsägelsen genom att välja den källa som passar bäst.

## 5. Källarkitektur

### 5.1 Riksdagen

Primärt:

- Sveriges riksdag
- Riksdagens öppna data
- dokument och lagar
- motioner
- propositioner
- betänkanden
- voteringar
- anföranden
- frågor och interpellationer
- ledamotsinformation

Kompletterande:

- partiernas officiella nationella webbplatser
- officiella valmanifest och partiprogram
- Valmyndigheten
- Regeringen/Regeringskansliet när relevant

### 5.2 Region Norrbotten

Primärt:

- Region Norrbottens officiella webbplats
- regionfullmäktige
- regionstyrelse
- nämnder
- protokoll
- handlingar
- motioner
- interpellationer
- budget/regionplan
- reservationer och särskilda yttranden när publicerade

Kompletterande:

- partiernas officiella regionala organisationer
- Valmyndigheten
- etablerade medier när originalkälla saknas eller för uttalanden.

### 5.3 Luleå kommun

Primärt:

- Luleå kommuns officiella webbplats
- kommunfullmäktige
- kommunstyrelse
- nämnder
- motioner
- möteshandlingar
- protokoll
- budget och strategiska planer
- voteringsresultat när publicerade

Kompletterande:

- partiernas officiella lokala organisationer
- Valmyndigheten
- etablerade lokala medier när originalkälla saknas eller för uttalanden.

## 6. Sökstrategi

GPT:n ska inte göra en enda bred webbsökning och sedan sammanfatta de första resultaten.

Rekommenderad arbetsordning:

1. Identifiera valnivå.
2. Identifiera sakfråga och tidsperiod.
3. Identifiera vilka partier/kandidater som ska analyseras.
4. Sök först efter officiell partiposition.
5. Sök därefter efter historiskt agerande.
6. Sök efter relevant beslut/votering som kontext.
7. Använd sekundärkällor för komplettering.
8. Kontrollera att centrala slutsatser har stöd.
9. Presentera resultatet med källor.

## 7. Källverifieringsregler

För varje central källa ska GPT:n, när möjligt, kontrollera:

- avsändare,
- dokumenttyp,
- datum,
- valnivå,
- vilket parti eller vilken företrädare dokumentet gäller,
- att dokumentet verkligen stöder slutsatsen,
- att länken går till rätt material.

För voteringar ska även beslutsärendets sammanhang verifieras.

## 8. Statisk Knowledge

Följande lämpar sig som statisk Knowledge.

### K-01 – Svensk ansvarsfördelning

Kort neutral referens över typiska ansvarsområden för:

- stat/riksdag,
- region,
- kommun.

Syfte: hjälpa GPT:n klassificera frågor rätt.

### K-02 – Politisk evidensmodell

Definitioner och exempel för:

- officiell politik,
- förslag,
- votering,
- beslut,
- uttalande,
- utfall.

### K-03 – Källguide Riksdagen

Praktisk guide över riksdagens dokumenttyper och hur de ska tolkas.

### K-04 – Källguide Region Norrbotten

Kända officiella källfamiljer, dokumenttyper och sökvägar.

### K-05 – Källguide Luleå kommun

Kända officiella källfamiljer, dokumenttyper och sökvägar.

### K-06 – Neutralitets- och jämförelsemetod

Referensmaterial med symmetrisk metod för partijämförelse och hantering av osäkerhet.

## 9. Information som inte bör lagras statiskt

Följande ska normalt hämtas aktuellt:

- valmanifest 2026,
- kandidatlistor 2026,
- deltagande partier,
- aktuella partisidor,
- senaste motioner,
- senaste voteringar,
- aktuella budgetförslag,
- senaste uttalanden,
- pågående politiska frågor.

Skälet är risken för föråldrad information.

## 10. Svarsarkitektur

### 10.1 Kort fråga

Vid en enkel fråga ska GPT:n svara kort men källbelagt.

Exempelstruktur:

1. direkt svar,
2. viktigaste skillnaden,
3. 2–5 relevanta belägg,
4. originalkällor.

### 10.2 Partijämförelse

Rekommenderad struktur:

- valnivå och fråga,
- jämförelsetabell,
- partiernas aktuella positioner,
- agerande under mandatperioden,
- viktigaste skillnader,
- osäkerheter,
- originalkällor.

### 10.3 Fördjupad evidensanalys

För större frågor:

| Parti | Evidenstyp | Datum | Vad belägget visar | Källa |
|---|---|---|---|---|

Därefter analytisk syntes.

## 11. Neutralitetsarkitektur

Neutralitet ska inte bygga på vaga instruktioner som ”var balanserad”.

Den ska implementeras metodiskt.

GPT:n ska:

1. använda samma frågor för alla partier,
2. söka motsvarande källtyper för alla,
3. skilja belägg från tolkning,
4. ge ungefär jämförbar detaljnivå,
5. redovisa positiva och negativa evidens på samma sätt,
6. inte förstärka en källa för att den passar användarens uppfattning,
7. redovisa informationsluckor.

## 12. Hantering av personuppgifter och kandidater

GPT:n ska i normalfallet endast använda offentligt relevanta uppgifter om politiska kandidater och företrädare.

Fokus ska ligga på deras offentliga politiska roll och aktivitet.

Privata förhållanden som saknar tydlig relevans för det offentliga uppdraget ska inte samlas in eller presenteras.

## 13. Rekommenderade projektartefakter

Projektet bör minst innehålla:

- `README.md`
- `PROJECT.md`
- `STATUS.md`
- `gpt-project.yaml`
- `project-status.yaml`
- `assistant/instructions.md`
- `assistant/policies/`
- `knowledge/`
- `docs/development-plan.md`
- `docs/source-architecture.md`
- `docs/evidence-model.md`
- `tests/evals/`
- `tests/e2e/`
- `scripts/`
- `.github/workflows/`

## 14. Teststrategi

### 14.1 Instruktionstester

Verifiera bland annat:

- frågar efter valnivå när den saknas,
- frågar inte när nivån redan är tydlig,
- behåller vald nivå,
- blandar inte kommun/region/riksdag,
- hittar inte på källor,
- skiljer ledamotsmotion från officiell partipolitik.

### 14.2 Evals

Minst följande typer bör finnas:

1. enkel sakfråga,
2. partijämförelse,
3. otydlig valnivå,
4. flernivåfråga,
5. kandidatfråga,
6. historisk jämförelse,
7. konflikt mellan källor,
8. otillräckligt underlag,
9. votering med komplicerad beslutsstruktur,
10. användare som försöker få GPT:n att argumentera partipolitiskt.

### 14.3 Källtest

Evals ska kontrollera att:

- källor faktiskt finns,
- länkar är relevanta,
- primärkälla används när sådan hittas,
- påståendet stöds av källan,
- datum och dokumenttyp tolkas rätt.

## 15. GitHub och releaseprofil

Standard enligt GPT Byggaren:

- GitHub Actions CI aktiveras.
- Pull requests och relevanta commits validerar projektet.
- GitHub Release bygger distributionsartefakter.
- Release-taggen styr versionsnumret.
- Chat ZIP och Custom GPT byggs från samma canonical source.
- Distributionerna valideras före release.

## 16. Rekommenderade Custom GPT-inställningar

### Web Search

**På**

Kritisk capability.

### Code Interpreter / Data Analysis

**På**

Kan vara användbart för större tabeller, strukturerade jämförelser och analyser av nedladdade öppna data.

### Image generation

**Av som standard**

Tillför inget centralt värde för kärnuppgiften.

### Actions

**Inte nödvändigt i version 1.0**

Webbsökning kan bära första versionen.

En framtida version kan överväga egna API-integrationer, särskilt mot Riksdagens öppna data, om det visar sig ge väsentligt bättre precision eller prestanda.

## 17. Arkitekturbeslut för version 1.0

Följande rekommenderas som fastställda beslut:

- [x] Webbresearch är central runtime-capability.
- [x] Aktuella politiska fakta hämtas dynamiskt.
- [x] Knowledge används för stabil metodik och källförståelse.
- [x] Riksdagen, Region Norrbotten och Luleå kommun är de enda ordinarie valnivåerna i v1.0.
- [x] Evidensklassning är obligatorisk i analyslogiken.
- [x] Originalkällor prioriteras.
- [x] Neutralitet implementeras som symmetrisk metod, inte enbart som ton.
- [x] Custom Actions behövs inte för v1.0.
- [x] Data Analysis aktiveras.
- [x] Image generation är inte nödvändig.
- [x] Chat ZIP och Custom GPT ska byggas parallellt.
- [x] GitHub Actions används för CI och release.
- [x] Release-taggen styr versionsnummer.

## 18. Nästa steg

Nästa steg är att skapa en **nedladdningsbar utvecklingsplan** för hela GPT-projektet.

Planen bör bryta ned arbetet i hanterbara steg från projektgrund, canonical instruktion och Knowledge till evals, distributionsbygge, CI, project hygiene och release candidate.
