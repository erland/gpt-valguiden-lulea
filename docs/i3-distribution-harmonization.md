# I3 – harmonisering av distributioner

Chat- och Custom GPT-distributionerna får skilja sig i format och detaljnivå, men inte i kärnbeteende.

| Kontroll | Chat | Custom GPT |
|---|---|---|
| three_levels | OK | OK |
| evidence_types | OK | OK |
| verification_statuses | OK | OK |
| position_change_labels | OK | OK |
| match_labels | OK | OK |
| confidence_labels | OK | OK |
| ask_level_when_unknown | OK | OK |
| do_not_ask_level_when_clear | OK | OK |
| same_method_neutrality | OK | OK |
| no_normative_vote_advice | OK | OK |
| web_verification | OK | OK |
| original_sources | OK | OK |
| vote_context | OK | OK |
| absence_not_opposite | OK | OK |
| activity_not_influence | OK | OK |

Båda distributionerna följer `distribution-contract.yaml`. Custom GPT-versionen är komprimerad medan Chat-versionen kan bära mer detaljer, men evidensmodell, neutralitet, källkrav, voteringslogik, osäkerhet, kandidatmodell och klassificeringsskalor ska vara semantiskt likvärdiga.
