# Valguiden

Valguiden är en källstyrd och politiskt neutral svensk valguide för:

- **Riksdagen**
- **Region Norrbotten**
- **Luleå kommun**

Syftet är att hjälpa väljare förstå vad partier och kandidater faktiskt säger, föreslår, röstar på, beslutar och åstadkommer – utan att blanda ihop olika typer av politisk evidens.

## Vad Valguiden kan hjälpa till med

Valguiden kan bland annat:

- jämföra partiers officiella politik,
- följa motioner och propositioner till beslut,
- tolka voteringar med rätt yrkandekontext,
- skilja förslag från beslut och beslut från faktiskt utfall,
- analysera om ett parti har ändrat position över tid,
- jämföra kandidaters dokumenterade politiska aktivitet,
- jämföra partier eller kandidater utifrån användarens egna prioriteringar,
- förklara vilken valnivå som faktiskt ansvarar för en fråga.

## Tre valnivåer

### Riksdagen

Valguiden använder i första hand:

- officiella nationella partidokument,
- riksdagen.se,
- Riksdagens öppna data,
- motioner och propositioner,
- betänkanden och reservationer,
- voteringar,
- riksdagsbeslut,
- Sagt och gjort.

### Region Norrbotten

Valguiden använder i första hand:

- regionala partiers officiella material,
- strategisk plan och budget,
- partibudgetar,
- motioner,
- interpellationer och frågor,
- handlingar och protokoll,
- reservationer och voteringar,
- årsredovisning och annan uppföljning.

### Luleå kommun

Valguiden använder i första hand:

- lokala partiers officiella material,
- budgetar och planer,
- kommunens motionsförteckning,
- originalmotioner,
- handlingar och protokoll,
- reservationer och voteringar,
- uppföljning av beslut.

## Evidensmodell

Valguiden skiljer konsekvent mellan:

| Typ | Betydelse |
|---|---|
| `OFFICIAL_POLICY` | Officiell partilinje |
| `PROPOSAL` | Motion, proposition, reservation, yrkande eller annat förslag |
| `VOTE` | Verifierad röst eller votering |
| `DECISION` | Formellt fattat beslut |
| `STATEMENT` | Uttalande, intervju, anförande, fråga eller interpellation |
| `OUTCOME` | Genomförande, uppföljning eller faktiskt resultat |

Det är centralt att inte göra felaktiga uppgraderingar:

- ett förslag är inte automatiskt partiets officiella linje,
- en röst är inte ett beslut,
- ett beslut är inte samma sak som genomförande,
- ett uttalande är inte automatiskt officiell partipolitik,
- ett utfall bevisar inte ensamt kausalitet.

## Politisk neutralitet

Valguidens grundprincip är:

> **Neutralitet = samma metod, inte samma slutsats.**

Det innebär bland annat samma:

- tidsperiod,
- källordning,
- evidenskrav,
- detaljnivå,
- kontroll av stödjande och motsägande evidens.

Valguiden försöker inte skapa falsk balans. Om underlaget är starkare för ett parti eller en slutsats ska det redovisas, men metoden ska vara densamma.

## Användarens prioriteringar

Användarens värderingar och prioriteringar får styra **matchningen**, men inte **faktainsamlingen**.

Exempel:

> Jag prioriterar vård högst, kollektivtrafik därefter och regionskatt sist.

Valguiden samlar först fakta neutralt och visar därefter vilka partier som ligger närmast dessa prioriteringar.

Den ska inte ge normativa uppmaningar som:

> Du borde rösta på parti X.

I stället kan den säga:

> Parti X ligger närmast de prioriteringar du angav, men evidenssäkerheten är lägre i kollektivtrafikfrågan.

## Källor och verifiering

Aktuell politisk fakta ska verifieras via webben vid användning.

Valguiden använder följande verifieringsstatus:

- `VERIFIED`
- `VERIFIED_WITH_LIMITATIONS`
- `DISCOVERY_ONLY`
- `REJECTED`

Den får aldrig hitta på:

- URL:er,
- dokumenttitlar,
- diarienummer,
- datum,
- citat,
- röster,
- beslut.

Om källorna inte räcker ska den säga det.

## Voteringar

Ja och nej får aldrig tolkas utan voteringskontext.

Ett nej kan exempelvis innebära stöd för en reservation eller ett alternativt förslag.

Valguiden skiljer därför mellan:

- ja och nej,
- avstår,
- frånvaro,
- reservation,
- delvotering,
- slutligt beslut,
- acklamation,
- partivis voteringsdata.

## Positionsförändring

Valguiden använder följande skala:

- `I HUVUDSAK OFÖRÄNDRAD`
- `VISS FÖRSKJUTNING`
- `TYDLIG POSITIONSFÖRÄNDRING`
- `MOTSTRIDIG EVIDENS`
- `OTILLRÄCKLIGT UNDERLAG`

En kandidatintervju räcker inte automatiskt för att säga att ett helt parti har ändrat sig.

## Kandidater

Kandidater kan jämföras utifrån offentlig politisk information som:

- motioner,
- frågor och interpellationer,
- anföranden,
- reservationer,
- dokumenterade röster,
- formella roller,
- sakpolitisk profil.

Valguiden skiljer mellan:

> aktivitet ≠ inflytande ≠ kompetens

Nya kandidater ska inte missgynnas för att historisk aktivitetsdata saknas.

## Distributioner

Projektet bygger två distributioner.

### Chat

För användning genom att ladda upp en ZIP i en ChatGPT-konversation.

Byggs med:

```bash
python scripts/build_chat.py
```

### Custom GPT

För konfigurering som en Custom GPT.

Byggs med:

```bash
python scripts/build_custom_gpt.py
```

Custom GPT-versionen använder:

- Web browsing: **på**
- Data Analysis: **på**
- Image generation: **av**
- Custom Actions: **inga i v1.0**

## Bygg och validering

Komplett lokalt bygge:

```bash
python scripts/build_all.py
```

Validering:

```bash
python scripts/validate.py
```

Release-validering:

```bash
python scripts/validate_release.py --tag v1.0.0 --dir dist
```

## CI och release

GitHub Actions innehåller:

- `.github/workflows/ci.yml`
  - körs på PR och relevanta commits,
  - bygger och validerar distributionerna.

- `.github/workflows/release.yml`
  - körs när en GitHub Release publiceras,
  - använder release-taggen som versionskälla,
  - publicerar:
    - `valguiden-chat-<version>.zip`
    - `valguiden-custom-gpt-<version>.zip`

## Projektstruktur

```text
valguiden/
├── assistant/        # kanoniska instruktioner och policies
├── knowledge/        # stabil metodik och ansvarsnivåer
├── docs/             # design- och utvecklingsdokumentation
├── tests/evals/      # evalramverk och suites
├── scripts/          # bygg och validering
├── dist/             # genererade distributioner
├── .github/workflows/
├── distribution-contract.yaml
├── project-status.yaml
└── README.md
```

## Nuvarande utvecklingsstatus

Se `STATUS.md` och `project-status.yaml`.

Projektet byggs stegvis mot en första release `v1.0.0`.
