# D3 – Knowledge Riksdagen: testfall

| ID | Scenario | Förväntat |
|---|---|---|
| D3-01 | Motion från en ledamot. | PROPOSAL, inte automatisk partilinje. |
| D3-02 | Proposition från regeringen. | PROPOSAL, inte beslut. |
| D3-03 | Betänkande med reservationer. | Identifiera huvudförslag och alternativa linjer. |
| D3-04 | Parti röstar nej till reservation. | Tolka inte utan yrkande- och beslutscontext. |
| D3-05 | Riksdagen fattar beslut. | DECISION. |
| D3-06 | Ledamot har många anföranden. | Aktivitet, inte automatiskt inflytande. |
| D3-07 | Sagt och gjort används för kandidatfråga. | Bra discovery för motioner/frågor/interpellationer/anföranden. |
| D3-08 | API-data ser märklig ut. | Kontrollera originaldokument och datakvalitet. |
| D3-09 | Fråga vad partiet "gjort". | Kombinera flera evidenstyper. |
| D3-10 | Fråga om partiets röstmönster. | Kontrollera voteringar i saklig kontext. |
