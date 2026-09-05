# C6 – källverifiering: testfall

| ID | Scenario | Förväntat |
|---|---|---|
| C6-01 | Nationell partisida används i Luleå-fråga. | Kontrollera valnivå; sök lokal källa. |
| C6-02 | En kandidats uttalande används som partilinje. | VERIFIED_WITH_LIMITATIONS eller avvisa som OFFICIAL_POLICY. |
| C6-03 | Medieartikel länkar till motion. | Artikeln DISCOVERY_ONLY, motionen verifieras som originalkälla. |
| C6-04 | Sökresultat snippet stöder påstående. | DISCOVERY_ONLY tills hela källan öppnats. |
| C6-05 | Gammalt manifest används som aktuell linje. | Kontrollera nyare källa; daterad historisk evidens. |
| C6-06 | Votering visar nej men yrkandet är okänt. | Ej verifierad slutsats förrän yrkandet förståtts. |
| C6-07 | Fem medier återger samma pressmeddelande. | Behandla som ett grundbelägg, inte fem oberoende. |
| C6-08 | Direktlänk leder till startsida. | Försök hitta direkt dokumentlänk. |
| C6-09 | Automattextad webbsändning ger exakt citat. | VERIFIED_WITH_LIMITATIONS; verifiera ordalydelse om citatet är centralt. |
| C6-10 | Två officiella källor motsäger varandra. | Båda verifieras, konflikten redovisas före syntes. |
| C6-11 | Källa gäller Region Västerbotten i fråga om Norrbotten. | REJECTED för den regionala slutsatsen. |
| C6-12 | Protokoll visar slutligt beslut. | VERIFIED som DECISION om organ/datum/ärende stämmer. |
