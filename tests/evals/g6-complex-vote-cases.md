# G6 – evals för komplex votering

Suiten testar att Valguiden inte tolkar en rå ja/nej-röst utan att förstå voteringskontexten.

## Täckning

- ja måste kopplas till rätt yrkande,
- nej kan stödja alternativt förslag,
- reservation kontra huvudförslag,
- flera delvoteringar,
- acklamation utan partivis röstlista,
- avstår,
- frånvaro,
- avvikande ledamot,
- reservation utan röstlista,
- stöd för del men nej till helhet,
- budgetvotering,
- VOTE kontra DECISION,
- kodtolkning i API-data,
- återremiss,
- bordläggning,
- full komplex voteringskedja.

## Kritiska fall

G6-001, G6-002, G6-004, G6-005, G6-011, G6-012, G6-013 och G6-016 är `critical`.
