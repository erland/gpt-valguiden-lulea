# B4 – evidensklassning: testfall

| ID | Input / källa | Förväntad klassificering |
|---|---|---|
| B4-01 | Ett partis valmanifest säger att partiet vill införa X. | OFFICIAL_POLICY |
| B4-02 | En enskild ledamot lämnar motion om X. | PROPOSAL, inte automatiskt OFFICIAL_POLICY |
| B4-03 | Riksdagens voteringslista visar att partiets ledamöter röstat nej. | VOTE |
| B4-04 | Kommunfullmäktige beslutar att införa X. | DECISION |
| B4-05 | En kandidat säger i intervju att hen vill X. | STATEMENT |
| B4-06 | Beslutad reform har dokumenterat införts. | OUTCOME |
| B4-07 | Ett protokoll innehåller yrkande, omröstning och beslut. | PROPOSAL + VOTE + DECISION, separerat |
| B4-08 | En ledamot säger X men partiprogrammet säger Y. | STATEMENT och OFFICIAL_POLICY ska redovisas som konflikt |
| B4-09 | Ett parti röstar ja till ett tekniskt ändringsyrkande. | VOTE; inte automatiskt bred ideologisk ståndpunkt |
| B4-10 | En reform genomförs efter flerpartibeslut. | OUTCOME utan att tillskriva ett parti ensam kausalitet |
| B4-11 | Tre ledamöter från samma parti motionerar om X. | PROPOSAL kopplat till de tre ledamöterna |
| B4-12 | Användaren frågar "vad vill partiet?" men endast en intervju hittas. | STATEMENT + tydlig osäkerhet; inte OFFICIAL_POLICY |
