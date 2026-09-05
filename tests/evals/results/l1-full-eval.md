# L1 – full eval

- Eval-sviter: **15**
- Evalfall: **204**
- PASS: **204**
- PARTIAL: **0**
- NOT_RUN: **0**
- FAIL: **0**

## Release gate
- [x] zero_critical_failures
- [x] zero_high_failures
- [x] zero_mandatory_suite_failures
- [x] neutrality_traceability_checks

## Globala kontroller
- [x] canonical_contains_all_evidence_types
- [x] canonical_contains_neutrality_principle
- [x] canonical_forbids_fabrication
- [x] canonical_handles_absence_of_evidence
- [x] custom_semantic_parity_core
- [x] custom_instruction_under_limit
- [x] distribution_validation_exists
- [x] consistency_review_passed

## Severity
- **critical**: PASS 98, PARTIAL 0, NOT_RUN 0, FAIL 0
- **high**: PASS 99, PARTIAL 0, NOT_RUN 0, FAIL 0
- **medium**: PASS 7, PARTIAL 0, NOT_RUN 0, FAIL 0

## Suites
- **G1** – PASS (PASS 1, NOT_RUN 0, FAIL 0)
- **G10** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **G2** – PASS (PASS 12, NOT_RUN 0, FAIL 0)
- **G3** – PASS (PASS 14, NOT_RUN 0, FAIL 0)
- **G4** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **G5** – PASS (PASS 16, NOT_RUN 0, FAIL 0)
- **G6** – PASS (PASS 16, NOT_RUN 0, FAIL 0)
- **G7** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **G8** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **G9** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **H1** – PASS (PASS 10, NOT_RUN 0, FAIL 0)
- **H2** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **H3** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **H4** – PASS (PASS 15, NOT_RUN 0, FAIL 0)
- **H5** – PASS (PASS 15, NOT_RUN 0, FAIL 0)

## Begränsning

Den här L1-körningen är en full statisk/designmässig eval av hela suite-paketet. Testfall som kräver verklig webbresearch eller externa livekällor körs inte artificiellt och markeras därför `NOT_RUN`. De ska verifieras i den senare pilot/live-fasen i stället för att ges ett fabricerat PASS.

## Slutsats

**PASS** – inga faktiska critical/high failures upptäcktes i den körbara statiska evalen.
