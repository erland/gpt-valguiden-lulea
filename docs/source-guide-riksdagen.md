# Källguide – Sveriges riksdag

## 1. Syfte

Den här guiden beskriver hur Valguiden ska använda Sveriges riksdags källor för att analysera politik på riksdagsnivå.

Riksdagens öppna data omfattar bland annat:

- dokument,
- ledamöter,
- voteringar,
- anföranden,
- kalenderinformation.

Öppna data finns via API, dataset och rapporter.

## 2. Viktigaste källfamiljer

### 2.1 Dokument

Dokumentkällan används för bland annat:

- propositioner,
- motioner,
- betänkanden,
- riksdagsbeslut,
- protokoll,
- skriftliga frågor,
- interpellationer.

Dokument kan finnas i flera format, exempelvis HTML, text, CSV, XML och JSON.

### 2.2 Ledamöter

Ledamotsdata används för:

- identitet,
- parti,
- valkrets,
- uppdrag,
- historiska uppdrag,
- vad ledamoten sagt och gjort.

Var försiktig med kända datakvalitetsavvikelser i uppdragsperioder.

### 2.3 Sagt och gjort

Datasetet **Sagt och gjort** samlar uppgifter om:

- anföranden,
- skriftliga frågor,
- interpellationer,
- motioner.

Det är särskilt användbart för att analysera en ledamot eller ett partis dokumenterade aktivitet under mandatperioden.

Använd inte aktivitetsmängd som synonym för politiskt inflytande.

### 2.4 Voteringar

Voteringsdata används för att analysera:

- hur en ledamot röstat,
- hur ett parti röstat,
- avvikande röster,
- jämförelser mellan partier,
- omröstningar per riksmöte.

Voteringsdata ska alltid tolkas tillsammans med ärendets sakliga kontext.

### 2.5 Anföranden

Anföranden är tal i kammaren.

Använd dem för:

- dokumenterade argument,
- politiska ståndpunkter,
- retorik,
- förändringar över tid.

Anföranden och repliker ska skiljas åt när det är relevant.

## 3. Dokumenttyper och evidens

### Motion

**Evidensklass:** `PROPOSAL`

En motion visar att en eller flera ledamöter har föreslagit något.

Viktigt:
- en enskild motion är inte automatiskt officiell partipolitik,
- kontrollera vilka ledamöter som står bakom,
- kontrollera om partiet har motsvarande stöd i valmanifest, program eller budget.

### Proposition

**Evidensklass:** `PROPOSAL`

En proposition är regeringens förslag till riksdagen.

För partijämförelse:
- skilj regeringens proposition från enskilt regeringspartis valmanifest,
- notera vilka partier som ingår i regeringen vid tidpunkten,
- kontrollera riksdagens behandling och beslut separat.

### Betänkande

**Evidensklass:** kan innehålla `PROPOSAL`, `VOTE` och `DECISION`

Ett utskottsbetänkande är en central källa för att förstå:

- utskottets förslag,
- reservationer,
- riksdagens beslut,
- sammanfattning av voteringsresultat.

För större frågor är betänkandet ofta bästa ingången till hela beslutskedjan.

### Reservation

**Evidensklass:** `PROPOSAL`

En reservation visar ett alternativt ställningstagande från ledamöter/partier i utskottet.

Kontrollera:
- vilka partier som står bakom reservationen,
- exakt vilket yrkande som görs,
- om reservationen senare blev föremål för votering.

### Riksdagsbeslut

**Evidensklass:** `DECISION`

Riksdagsbeslut visar vad riksdagen faktiskt beslutat.

Skilj beslutet från:
- vad regeringen ursprungligen föreslog,
- vad oppositionen föreslog,
- hur beslutet senare genomfördes.

### Votering

**Evidensklass:** `VOTE`

Voteringen visar hur ledamöter röstat i en konkret omröstning.

Kontrollera alltid:
- vilket yrkande voteringen gällde,
- om voteringen gällde huvudförslag eller reservation,
- om ja betyder stöd för sakförslaget eller för en procedur,
- hur partigrupperna röstade,
- eventuella frånvarande eller avvikande röster.

### Anförande

**Evidensklass:** `STATEMENT`

Anföranden visar vad ledamöter eller ministrar sagt i kammaren.

Använd dem inte automatiskt som officiell partipolitik.

### Skriftlig fråga

**Evidensklass:** normalt `STATEMENT` eller aktivitetsbelägg

En skriftlig fråga visar vilka frågor en ledamot valt att driva eller uppmärksamma.

Den visar inte i sig:
- officiell partipolitik,
- genomförd politik,
- hur partiet skulle rösta.

### Interpellation

**Evidensklass:** normalt `STATEMENT` och aktivitetsbelägg

Interpellationer kan vara särskilt användbara eftersom de ofta leder till mer utvecklade politiska resonemang.

### Protokoll från kammaren

Kan innehålla:
- `STATEMENT`,
- `VOTE`,
- `DECISION`.

Använd protokollet när sammanhang, debatt eller exakt beslutsordning behöver förstås.

## 4. Rekommenderad analyskedja

För en riksdagsfråga:

1. Identifiera sakfrågan.
2. Hitta aktuell officiell partipolitik.
3. Hitta relevanta motioner/propositioner.
4. Hitta relevant betänkande.
5. Identifiera reservationer.
6. Kontrollera voteringar.
7. Kontrollera slutligt beslut.
8. Använd anföranden, frågor och interpellationer för fördjupning.
9. Jämför symmetriskt mellan partier.
10. Redovisa källor och osäkerhet.

## 5. Analys av mandatperioden 2022–2026

För Valguidens huvudperiod ska research normalt omfatta riksmötena:

- 2022/23
- 2023/24
- 2024/25
- 2025/26

Vid historisk jämförelse kan material från tidigare riksmöten användas.

## 6. Partianalys

När ett partis arbete analyseras, undvik att dra slutsats endast från antal dokument.

Bättre dimensioner:

- officiell partipolitik,
- relevanta motioner,
- reservationer,
- voteringsmönster,
- anföranden,
- frågor/interpellationer,
- beslut där partiets linje haft betydelse.

Mängd aktivitet är ett mått på aktivitet, inte automatiskt inflytande eller kvalitet.

## 7. Ledamotsanalys

För en enskild ledamot kan **Sagt och gjort** användas som ingång.

Redovisa exempelvis:

- relevanta motioner,
- anföranden,
- skriftliga frågor,
- interpellationer,
- valkrets,
- parti,
- politiska uppdrag.

Undvik att beskriva en ledamot som "mest engagerad" utan definierat aktivitetsmått.

## 8. Voteringsanalys – särskild kontroll

Före slutsats om hur ett parti "röstat i en fråga":

1. hitta voteringen,
2. hitta relaterat betänkande,
3. identifiera exakt yrkande,
4. förstå vad ja/nej innebar,
5. kontrollera partiets röster,
6. notera avvikelser/frånvaro när relevant,
7. kontrollera beslutet.

Ett parti kan rösta nej till en reservation eftersom det stödjer huvudförslaget, eller tvärtom. Därför räcker inte ett isolerat ja/nej.

## 9. Datakvalitet och avvikelser

Riksdagen publicerar information om kända avvikelser i öppna data.

Valguiden ska därför:

- inte anta att dataset är felfria,
- kontrollera originaldokument vid oväntade uppgifter,
- vara försiktig med historiska luckor,
- särskilt kontrollera kända avvikelser i ledamots- och voteringsdata.

Om datakvaliteten påverkar slutsatsen ska det redovisas.

## 10. API kontra webbsidekällor

### API/dataset lämpar sig för:

- bred analys,
- filtrering,
- jämförelser,
- statistiska sammanställningar,
- många ledamöter eller voteringar.

### Webbside/originaldokument lämpar sig för:

- slutlig källhänvisning,
- läsbar verifiering,
- beslutskontext,
- dokumentets fulla innehåll.

Bra arbetssätt:
- använd strukturerade data för discovery/analys,
- länka helst till läsbart originaldokument i svaret.

## 11. Källor som bör prioriteras

1. Riksdagens dokument och lagar
2. Riksdagens öppna data
3. Riksdagens ledamotsdata och Sagt och gjort
4. Voteringsdata
5. Anföranden
6. Partiernas officiella material för aktuell partipolitik

## 12. Minsta kontroll före påstående

Före formuleringar som:

> Parti X föreslog ...
> Parti X röstade ...
> Riksdagen beslutade ...
> Ledamot Y sade ...

kontrollera:

- rätt dokument,
- rätt datum,
- rätt aktör,
- rätt evidenstyp,
- rätt beslutssteg,
- direkt källa.

## 13. Referenskällor

Guiden bygger på Sveriges riksdags officiella information om:

- Riksdagens öppna data
- Användarstöd
- Dokument
- Ledamöter och Sagt och gjort
- Voteringar
- Anföranden
- Analys av valperioden 2022–2026
- Kända avvikelser i data
