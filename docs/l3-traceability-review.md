# L3 – spårbarhetsgranskning

## Slutsats

Spårbarhetsrisk: **LOW**

Granskningen verifierar att centrala politiska sakpåståenden kan kopplas till evidenstyp, aktör, nivå, tid, källa och verifieringsstatus.

## Kontroller

- [x] evidence_types_present
- [x] source_verification_statuses_present
- [x] actor_required
- [x] level_required
- [x] date_or_time_required
- [x] source_required
- [x] direct_link_or_original_source
- [x] vote_context_required
- [x] decision_context_required
- [x] no_fabricated_source
- [x] claim_support_check
- [x] absence_of_evidence_rule
- [x] decision_not_outcome
- [x] outcome_not_causality
- [x] candidate_evidence_confidence
- [x] priority_match_separate_from_evidence
- [x] canonical_traceability_contract
- [x] canonical_claim_traceability
- [x] traceability_eval_coverage
- [x] source_quality_eval_coverage
- [x] chat_fabrication_prohibition
- [x] custom_fabrication_prohibition
- [x] custom_source_verification
- [x] custom_vote_context
- [x] no_unsupported_claim_language

## Evaltäckning

- Spårbarhets-/källrelaterade evalfall: **100**
- Source quality/conflict/insufficient evidence-fall: **62**
- Explicit fabrication-relaterade evalfall: **13**

## Planräknare

- Tidigare total: 59 (felaktig)
- Korrekt total: **64**
- Klara efter L3: **59/64**

## Bedömning

Inga blockerande spårbarhetsproblem identifierades.

VOTE kräver voteringskontext, DECISION kräver beslutskontext och OUTCOME kräver separat stöd. Källor, dokument, citat, röster, beslut och datum får inte fabriceras.
