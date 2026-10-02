# Esercizio 01 — Dimensione dell'input, operazione elementare e funzione di costo

## DESCRIZIONE

L'esercizio introduce i concetti base dell'analisi della complessità:

- dimensione dell'input `n`;
- operazione elementare;
- funzione di costo `T(n)`.

Pseudocodice analizzato:

```text
LEGGI N

SOMMA ← 0

PER I DA 1 A N
    SOMMA ← SOMMA + 2
FINE PER

STAMPA SOMMA
```

## SVOLGIMENTO

La dimensione dell'input è:

```text
n
```

Come operazione elementare scegliamo:

```text
SOMMA ← SOMMA + 2
```

Se:

```text
N = 5
```

il ciclo esegue l'operazione elementare 5 volte.

Quindi:

```text
T(5) = 5
```

In generale, se l'input ha dimensione `n`:

```text
T(n) = n
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere `n` come dimensione dell'input.
- Individuare una possibile operazione elementare da contare.
- Comprendere che `T(n)` rappresenta quante volte viene eseguita l'operazione scelta.
- Calcolare un semplice valore concreto come `T(5)`.
- Passare dal caso concreto `T(5) = 5` alla forma generale `T(n) = n`.

## ARGOMENTO D'ESAME

Complessità: dimensione dell'input, operazione elementare e funzione di costo.

## COMPLESSITÀ

La funzione di costo dell'operazione scelta è:

```text
T(n) = n
```

La notazione asintotica non è ancora stata introdotta formalmente in questo esercizio.
