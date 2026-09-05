# J1 – bygg- och valideringsscripts

## Scripts

- `scripts/build_chat.py` – bygger Chat-distributionen.
- `scripts/build_custom_gpt.py` – bygger om Knowledge-delen och paketerar Custom GPT-distributionen.
- `scripts/validate.py` – kontrollerar distributionsparitet, instruktionsgräns, Knowledge-gräns och grundstruktur.
- `scripts/build_all.py` – kör båda byggena och valideringen.
- `scripts/build.sh` – shell-wrapper för komplett bygge.
- `scripts/validate.sh` – shell-wrapper för validering.
- `scripts/common.py` – gemensamma hjälpfunktioner.

## Avsikt

Scripten ska vara den lokala grund som GitHub Actions i J2/J3 använder. Byggen ska vara reproducerbara från repots source-of-truth-filer och inte kräva manuell paketering.
