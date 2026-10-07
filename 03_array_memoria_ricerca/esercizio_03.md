# Esercizio 03 — Ricerca binaria

## DESCRIZIONE

L'esercizio introduce la ricerca binaria, il requisito dell'ordinamento dei dati e il confronto con la ricerca lineare.

## SVOLGIMENTO

La ricerca binaria funziona su una struttura ordinata.

Esempio:

```text
[2, 5, 8, 12, 16, 21, 30]
```

Per cercare `16`, si controlla l'elemento centrale:

```text
12
```

Poiché `16 > 12`, si scarta tutta la metà sinistra e si continua solo sulla metà destra.

L'idea fondamentale è:

```text
confronta con il centro
→ scarta metà degli elementi
→ ripeti
```

Per questo il numero di passi cresce in modo logaritmico.

Esempi:

```text
32 elementi  → circa 5 dimezzamenti
64 elementi  → circa 6 dimezzamenti
128 elementi → circa 7 dimezzamenti
1024 elementi → circa 10 dimezzamenti
```

Infatti:

```text
log_2(32) = 5
log_2(64) = 6
log_2(128) = 7
log_2(1024) = 10
```

Esempio di simulazione manuale:

```text
[3, 7, 11, 18, 24, 31, 42, 57, 63]
```

Ricerca di `31`:

```text
24 → 42 → 31
```

Ricerca di `7`:

```text
24 → 7
```

Ricerca di `63`:

```text
24 → 42 → 57 → 63
```

Confronto con la ricerca lineare:

```text
ricerca lineare, caso peggiore → Theta(n)
ricerca binaria                → Theta(log n)
```

La ricerca binaria richiede però che i dati siano ordinati.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- La ricerca binaria richiede dati ordinati.
- Si confronta il valore cercato con l'elemento centrale.
- Dopo ogni confronto si può eliminare circa metà dello spazio di ricerca.
- Se il valore cercato è minore del centro si va a sinistra.
- Se è maggiore si va a destra.
- Il numero di passaggi cresce come `log_2(n)`.
- La ricerca binaria ha complessità `Theta(log n)`.
- La ricerca lineare nel caso peggiore ha complessità `Theta(n)`.
- Su strutture ordinate e adatte, la ricerca binaria è molto più efficiente della ricerca lineare per input grandi.

## ARGOMENTO D'ESAME

**03 — Array, memoria e ricerca**

- ricerca sequenziale;
- ricerca binaria;
- prerequisito dell'ordinamento;
- confronto tra i costi;
- riduzione dello spazio di ricerca.

## COMPLESSITÀ

```text
ricerca lineare worst → Theta(n)
ricerca binaria       → Theta(log n)
```
