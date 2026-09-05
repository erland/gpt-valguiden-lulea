# Källguide – Luleå kommun

## 1. Syfte

Den här guiden beskriver hur Valguiden ska använda Luleå kommuns officiella källor för analys av kommunal politik.

Luleå kommun publicerar bland annat:

- kommunfullmäktiges ledamöter och mandatfördelning,
- mötesdatum,
- kallelser,
- protokoll,
- nämndhandlingar,
- motioner,
- beslut på motioner,
- partiernas budgetförslag,
- beslutad plan och budget,
- webbsändningar av kommunfullmäktige.

## 2. Viktigaste källfamiljer

### 2.1 Kommunfullmäktige

Kommunfullmäktige är kommunens högsta beslutande instans.

Använd källorna för att analysera:

- mål och riktlinjer,
- budget,
- skatt, taxor och avgifter,
- större organisationsfrågor,
- motioner,
- principiellt viktiga beslut,
- mandatfördelning,
- ledamöter och ersättare.

Fullmäktigehandlingar bör vara huvudkälla för kommunövergripande politiska beslut.

### 2.2 Möten, handlingar och protokoll

Kommunens sida för möten, handlingar och protokoll samlar material från:

- kommunfullmäktige,
- kommunstyrelsen,
- nämnder,
- råd och kommittéer.

Använd:

- kallelser för att se vilka ärenden som ska behandlas,
- handlingar för beredning och beslutsunderlag,
- protokoll för vad som faktiskt beslutades.

Kommunen anger att kallelser/ärenden normalt publiceras omkring en vecka före sammanträdet.

### 2.3 Kommunstyrelsen

Kommunstyrelsen bereder många ärenden till kommunfullmäktige och fattar även egna beslut inom sitt mandat.

Skilj alltid mellan:

- kommunstyrelsens eget beslut,
- kommunstyrelsens förslag till fullmäktige,
- kommunfullmäktiges slutliga beslut.

### 2.4 Nämnder

Exempel på relevanta nämnder:

- barn- och utbildningsnämnden,
- socialnämnden,
- miljö- och byggnadsnämnden,
- kultur- och fritidsnämnden,
- arbetsmarknads- och gymnasienämnden,
- infrastruktur- och servicenämnden.

För varje fråga:
- identifiera rätt nämnd,
- kontrollera om nämnden beslutar slutligt,
- kontrollera om ärendet går vidare till kommunstyrelse/fullmäktige.

## 3. Motioner – särskilt stark lokal källa

Luleå kommun har en särskild motionssida för mandatperioden 2022–2026.

Den innehåller bland annat:

- ärendenummer,
- datum,
- förslagsställare,
- partitillhörighet,
- länk till motion,
- senare beslut när sådant finns.

Detta gör sidan särskilt användbar för att följa:

förslag
→ beredning
→ beslut.

### Motion

**Evidensklass:** `PROPOSAL`

En motion visar att en eller flera ledamöter föreslagit något.

Kontrollera:

- vilka personer som står bakom,
- vilket eller vilka partier de representerar,
- om motionen är gemensam mellan partier,
- om motionen senare bifallits, avslagits, besvarats eller delvis bifallits,
- datum för beslutet.

Skriv inte att hela partiet "vill" något om enda belägget är en motion från en enskild ledamot.

## 4. Beslut på motioner

När motionssidan länkar ett beslut ska detta användas som `DECISION`.

Exempel på beslutskategorier som kan förekomma:

- bifall,
- avslag,
- besvarad,
- delvis bifall,
- delvis avslag,
- kombinationer av dessa.

Var noga med formuleringen.

"Besvarad" är inte samma sak som bifall.

"Delvis bifall" betyder inte att hela motionen antogs.

## 5. Budgetförslag

Luleå kommun publicerar partiernas förslag till plan och budget.

Detta är en mycket stark källa för jämförelse mellan partier.

### Majoritetens budget

Kan fungera som:

- `OFFICIAL_POLICY`,
- `PROPOSAL`,
- efter fullmäktigebeslut även `DECISION` för den antagna planen.

### Oppositionens budgetförslag

Kan fungera som:

- `OFFICIAL_POLICY`,
- `PROPOSAL`.

Det ska inte beskrivas som beslutad kommunpolitik om det inte antagits.

### Jämförelseregel

Vid budgetjämförelse:

- använd samma budgetperiod,
- jämför motsvarande poster och mål,
- skilj majoritetsförslag från beslutad budget,
- skilj oppositionsförslag från beslut,
- redovisa gemensamma budgetförslag mellan flera partier korrekt.

## 6. Protokoll

**Evidensklass:** kan innehålla `PROPOSAL`, `VOTE`, `DECISION`, `STATEMENT`

Protokoll ska användas för att fastställa:

- vilket beslut som fattades,
- vilket organ som fattade beslutet,
- eventuella yrkanden,
- reservationer,
- omröstningar,
- särskilda yttranden när de redovisas.

För centrala slutsatser väger protokollet tyngre än en kort sammanfattande webbsida.

## 7. Kallelser och möteshandlingar

Kallelser är främst `PROPOSAL`- och discovery-källor.

De visar:

- vilka ärenden som ska tas upp,
- beslutsförslag,
- underlag,
- bilagor.

De visar inte automatiskt vad som senare beslutades.

Följ därför ärendet till protokollet.

## 8. Voteringar

**Evidensklass:** `VOTE`

Om protokollet redovisar votering ska GPT:n kontrollera:

- vad omröstningen gällde,
- vilka förslag som stod mot varandra,
- eventuella röstsiffror,
- om partivis eller individuell röstning går att fastställa,
- slutligt beslut.

Om endast beslutet framgår men inte hur partierna röstat:
- dra inte slutsats om partiernas röstning.

## 9. Reservationer och särskilda yttranden

### Reservation

**Evidensklass:** `PROPOSAL`/`STATEMENT`

Reservation kan ge starkt stöd för oppositionens alternativa linje.

### Särskilt yttrande

**Evidensklass:** `STATEMENT`

Kan visa nyanser eller invändningar, men är inte samma sak som ett alternativt formellt yrkande.

## 10. Kommunfullmäktiges webbsändningar

Kommunfullmäktiges möten webbsänds.

Använd sändningar som kompletterande källa för:

- vad en ledamot sagt,
- debattargument,
- förklaringar av yrkanden.

Sändningarna är autotextade och textningen kan innehålla fel.

Därför:
- använd inte automattext som ensam grund för viktiga exakta citat,
- verifiera med protokoll eller annan säkrare källa när möjligt.

## 11. Rekommenderad analyskedja

För en kommunal sakfråga:

1. Identifiera sakfrågan.
2. Identifiera ansvarig nämnd/organ.
3. Hitta aktuell plan/budget.
4. Hitta partiernas alternativa budgetförslag.
5. Sök relevanta motioner.
6. Läs kallelse och beslutsunderlag.
7. Följ ärendet till kommunstyrelse/fullmäktige.
8. Kontrollera protokoll.
9. Kontrollera eventuell votering/reservation.
10. Kontrollera senare genomförande/uppföljning när möjligt.
11. Presentera jämförelsen symmetriskt.

## 12. Mandatperioden 2022–2026

För mandatperiodsanalys ska GPT:n särskilt använda:

- motionssidan för mandatperioden,
- kommunfullmäktiges protokoll,
- nämndprotokoll,
- budgetförslag per år,
- beslutad plan och budget,
- relevanta årsredovisningar och uppföljningar.

Motionssidan är särskilt värdefull eftersom den knyter ihop motion och senare beslut.

## 13. Partianalys

För varje parti kan följande dimensioner användas:

- officiellt lokalt valprogram,
- budgetförslag,
- motioner,
- reservationer,
- voteringar,
- kommunfullmäktige-/nämndbeslut,
- dokumenterat genomförande.

Antal motioner är ett aktivitetsmått, inte ett mått på kvalitet eller inflytande.

## 14. Kandidat- och ledamotsanalys

Kommunfullmäktiges sida innehåller ledamöter och ersättare med partitillhörighet.

För en ledamot kan GPT:n kombinera:

- uppdrag,
- motioner,
- debattuttalanden,
- eventuella reservationer,
- dokumenterade röster.

Undvik ranking som "mest engagerad" utan definierat kriterium.

## 15. Besluts- och genomförandekedja

För större kommunala frågor, försök följa:

idé/förslag
→ nämnd/beredning
→ kommunstyrelse
→ kommunfullmäktige
→ beslut
→ genomförande
→ uppföljning

Alla steg finns inte i varje ärende.

## 16. Källprioritet

För kommunal analys:

1. fullständigt protokoll,
2. beslutsunderlag/möteshandling,
3. beslutad plan och budget,
4. partiernas budgetförslag,
5. motionssidan + originalmotion,
6. reservation/särskilt yttrande,
7. nämndhandlingar,
8. webbsändning som kompletterande uttalandekälla.

## 17. Minsta kontroll före påstående

Före formuleringar som:

> Parti X föreslog ...
> Parti X röstade ...
> Kommunfullmäktige beslutade ...
> Kommunstyrelsen beslutade ...
> Motionen bifölls ...

kontrollera:

- rätt organ,
- rätt datum,
- rätt förslagsställare,
- rätt parti,
- rätt beslutstyp,
- om beslutet var slutligt,
- om partivis röstmönster faktiskt går att belägga.

## 18. Källbrist

Om ett protokoll inte visar hur partierna röstat:
- säg det,
- använd inte antaganden.

Om en motion saknar beslut:
- beskriv den som ännu inte verifierat avgjord utifrån tillgänglig källa.

Om lokalt valmanifest saknas:
- använd budget och andra officiella partiställningstaganden,
- redovisa att manifestunderlag saknas.

## 19. Referenskällor

Guiden bygger på Luleå kommuns officiella information om:

- kommunfullmäktige,
- möten, handlingar och protokoll,
- motioner mandatperioden 2022–2026,
- partiernas budgetförslag,
- beslutad plan och budget,
- ledamöter och ersättare,
- webbsändningar från kommunfullmäktige.
