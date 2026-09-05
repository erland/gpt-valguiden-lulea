# G2 – evals för valnivå

Den här suiten testar hur Valguiden väljer, behåller och byter valnivå.

## Täckning

- ingen nivå angiven,
- explicit Riksdagen,
- explicit Region Norrbotten,
- explicit Luleå kommun,
- tydligt implicerad nivå,
- tidigare vald nivå,
- explicit nivåbyte,
- flernivåfråga,
- felaktigt påtvingad nivå,
- geografiskt tvetydig fråga,
- sakfråga som kräver nivåbyte,
- samtidig klassificering av alla tre nivåerna.

## Kritiska fall

G2-009 och G2-011 är `critical` eftersom fel beslutskompetens direkt kan ge vilseledande politisk vägledning.

## Suite-pass

Suiten ska inte kunna PASS om något critical-fall fallerar.
