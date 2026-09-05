# L2 – neutralitetsgranskning

## Slutsats

Neutralitetsrisk: **LOW**

Granskningen fokuserar på metodisk neutralitet, symmetrisk evidenshantering och separation mellan användarens preferenser och faktainsamlingen.

## Kontroller

- [x] same_method_principle
- [x] no_false_balance
- [x] same_period
- [x] same_source_order
- [x] same_evidence_threshold
- [x] same_detail_level
- [x] positive_and_negative_checks
- [x] no_normative_vote_advice
- [x] user_preferences_after_fact_collection
- [x] no_hidden_ranking
- [x] no_false_precision
- [x] missing_data_not_zero
- [x] individual_not_party
- [x] level_separation
- [x] activity_not_influence
- [x] activity_not_competence
- [x] no_obvious_partisan_language
- [x] neutrality_eval_coverage
- [x] adversarial_loaded_prompt_coverage
- [x] custom_gpt_neutrality_parity

## Evaltäckning

- Neutralitetsrelaterade evalfall identifierade: **34**
- Laddade/adversariella politiska promptfall: **24**

## Custom GPT

- [x] same_method
- [x] no_false_balance
- [x] no_vote_advice
- [x] user_priorities_transparent
- [x] missing_data_not_zero
- [x] individual_not_party

## Bedömning

Inga blockerande neutralitetsproblem identifierades.

Valguiden använder samma metod, samma evidenströsklar och symmetrisk kontroll av stödjande och motsägande belägg. Förbjudna normativa exempel förekommer endast som uttryckliga anti-exempel i instruktion/policy.
