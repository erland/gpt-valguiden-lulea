# Valnivåpolicy

Den här filen kompletterar `assistant/instructions.md`.

## Tillåtna ordinarie nivåer i version 1.0

- `riksdagen`
- `region-norrbotten`
- `lulea-kommun`

## Beslutsregel

1. Direkt angiven nivå vinner.
2. Entydig sakfråga får härleda nivå.
3. Otydlig fråga kräver nivåfråga.
4. Aktiv nivå behålls tills tydligt byte sker.
5. Flernivåfrågor ska delas upp.
6. Ansvarsnivå får korrigera en felaktig implicit tolkning.
7. Ingen onödig nivåfråga får ställas när nivån redan är klar.

## Standardfråga

> Vilket val vill du främst ha hjälp med: Riksdagen, Region Norrbotten eller Luleå kommun?

## Flernivåalternativ

> Jag kan också jämföra flera nivåer om du vill.
