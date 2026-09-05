# Kandidatpost – logisk struktur

```yaml
candidate:
  name: string
  party: string
  election_level: RIKSDAGEN | REGION_NORRBOTTEN | LULEA_KOMMUN
  geography: string | null
  current_role: string | null
  period:
    from: date | null
    to: date | null
  evidence:
    proposals: []
    votes: []
    statements: []
    roles: []
  topic_profile: []
  activity_metrics: {}
  evidence_confidence: HIGH | MEDIUM | LOW | INSUFFICIENT
  limitations: []
```

Strukturen är konceptuell och behöver inte exponeras för användaren.


## Rekommenderade aktivitetsmått

```yaml
activity_metrics:
  lead_motion_count: integer | null
  co_signed_motion_count: integer | null
  interpellation_count: integer | null
  question_count: integer | null
  speech_count: integer | null
  reservation_count: integer | null
  special_statement_count: integer | null
  documented_vote_count: integer | null
  topic_count: integer | null
  active_years: number | null
  activity_per_active_year: number | null
  data_coverage: HIGH | MEDIUM | LOW | UNKNOWN
```

Råmåtten ska hållas separata. Ett sammanvägt index är inte standard.
