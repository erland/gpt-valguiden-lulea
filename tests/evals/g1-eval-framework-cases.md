# G1 – evalramverk: valideringsfall

| ID | Kontroll | Förväntat |
|---|---|---|
| G1-01 | Ett test saknar severity. | Schemat ska bedömas ofullständigt. |
| G1-02 | Critical test får FAIL. | Release ska blockeras. |
| G1-03 | Ett svar är semantiskt korrekt men ordalydelsen skiljer sig. | Ska kunna PASS om beteendet uppfylls. |
| G1-04 | Live-eval bygger på aktuell politisk data. | Ska kunna märkas data_mode: live. |
| G1-05 | Ett produktionsfel hittas. | Regressionstest ska skapas och behållas. |
| G1-06 | Suite har 95 % PASS men ett critical FAIL. | Suite/release ska FAIL/blockeras. |
| G1-07 | Test testar neutralitet med exakt strängmatchning. | Bedömningen ska kompletteras semantiskt/manual/model-assisted. |
| G1-08 | Samma test byter text men inte beteende. | Test-ID ska vara stabilt. |
