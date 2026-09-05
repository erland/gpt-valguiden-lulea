# Eval scoring

## Teststatus

- PASS = 1.0
- PARTIAL = 0.5
- FAIL = 0
- NOT_RUN = exkluderas från poäng

## Release-blocker

Oavsett totalscore:

- critical FAIL blockerar release,
- high FAIL i kärnflöde blockerar release candidate tills bedömd/åtgärdad.

## Suite-status

PASS:
- inga critical/high FAIL,
- obligatoriska testfall PASS,
- minst 90 % PASS/PARTIAL.

PARTIAL:
- inga critical FAIL,
- men high FAIL eller för låg täckning finns.

FAIL:
- critical FAIL eller flera centrala high FAIL.
