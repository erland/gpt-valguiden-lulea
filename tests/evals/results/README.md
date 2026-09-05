# Evalresultat

Den här katalogen används för resultat från evalkörningar.

Rekommenderat resultatformat per körning:

```yaml
run:
  timestamp: ...
  suite: ...
  total: 0
  pass: 0
  partial: 0
  fail: 0
  not_run: 0
  critical_failures: []
  notes: []
```

Resultatfiler ska inte användas som canonical källa för regler.
