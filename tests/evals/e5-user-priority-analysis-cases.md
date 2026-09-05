# E5 – användarprioriteringar: testfall

| ID | Scenario | Förväntat |
|---|---|---|
| E5-01 | Vård 50 %, kollektivtrafik 30 %, skatt 20 %. | Synliga vikter och matchning per fråga. |
| E5-02 | Användaren anger bara "vård viktigast, sedan skatt". | Använd ordningsprioritet eller tydligt antagande, ingen dold viktning. |
| E5-03 | Parti A saknar källor i en fråga. | OTILLRÄCKLIGT UNDERLAG, inte nollpoäng. |
| E5-04 | Parti A säger X men röstar återkommande Y. | Visa konflikt och sänk säkerhet vid behov. |
| E5-05 | Prioriteringar spänner över riksdag, region och kommun. | Separera valnivåerna. |
| E5-06 | Användaren vill ha exakt procentmatchning. | Förklara modellen och undvik onödig precision. |
| E5-07 | Två prioriteringar står i konflikt. | Synliggör avvägningen. |
| E5-08 | Användaren vill ha ranking. | Tillåt med transparent viktning och osäkerhet. |
| E5-09 | Underlaget är för svagt för robust ranking. | Avstå ranking och förklara varför. |
| E5-10 | Användaren ändrar vikter men sakfrågorna är samma. | Återanvänd faktaunderlag och uppdatera matchningen. |
