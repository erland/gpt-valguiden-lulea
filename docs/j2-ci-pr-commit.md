# J2 – CI för PR och commit

## Workflow

`.github/workflows/ci.yml`

## När den körs

- pull requests,
- push till:
  - `main`,
  - `master`,
  - `develop`,
  - `feature/**`,
  - `fix/**`.

## Jobb

`build-and-validate`:

1. checkar ut repot,
2. installerar Python 3.12,
3. installerar `pyyaml`,
4. kör `python scripts/build_all.py`,
5. kör `python scripts/validate.py`,
6. verifierar att bygget inte lämnar ocommittade förändringar.

## Syfte

CI ska stoppa ändringar som:
- bryter distributionsbygget,
- gör Chat och Custom GPT semantiskt osynkade,
- överskrider Custom GPT-gränserna,
- tappar obligatoriska eval-sviter eller kärnfiler,
- kräver manuellt genererade filer för att repot ska vara konsistent.

Release-publicering ingår inte här; det kommer i J3.
