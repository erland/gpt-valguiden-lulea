# Projektstatusmodell

`project-status.yaml` är projektets maskinläsbara sanningskälla för utvecklingsstatus.

## Fält

### `phase`
Aktuell utvecklingsfas och dess status.

### `current_step`
Det senast genomförda eller pågående steget.

### `next_step`
Nästa explicita steg som ska utföras.

### `completed_steps`
Lista över genomförda steg.

### `blocked_steps`
Steg som inte kan genomföras och orsaken till det.

### `quality`
Status för instruktionstester, evals, E2E, källvalidering och neutralitetsgranskning.

### `distribution`
Status för Chat ZIP och Custom GPT.

### `release`
Releaseberedskap, målversion och blockerande orsaker.

### `progress`
Total mängd steg, antal genomförda och procentuell framdrift.

## Regler

1. `project-status.yaml` är sanningskälla.
2. `STATUS.md` är mänskligt läsbar spegling.
3. Båda uppdateras efter varje steg.
4. Nästa steg ska alltid vara explicit.
5. Blockerare ska registreras innan arbetet går vidare.
6. Release får inte markeras som redo så länge blockerande orsaker finns.
