# Contributing

## Grundregel

Ändra inte bara distributionerna. Börja i source-of-truth.

## Minsta arbetsflöde

1. Gör ändringen i canonical/policy/Knowledge.
2. Lägg till eller justera eval.
3. Kör:

```bash
python scripts/build_all.py
```

4. Kontrollera:

```bash
git status --short
```

5. Commit endast en konsistent source + generated state.

## Pull requests

PR bör beskriva:
- vilket beteende som ändras,
- varför,
- vilka evals som täcker ändringen,
- om Chat/Custom GPT påverkas,
- om releaseformat eller Knowledge påverkas.

## Regressioner

En bekräftad bugg bör få ett evalfall innan eller samtidigt som fixen.
