# Esercizio 10 — Confrontare due algoritmi che risolvono lo stesso problema

## DESCRIZIONE

L'esercizio richiede di confrontare due algoritmi diversi che risolvono lo stesso problema: trovare il massimo tra tre numeri `A`, `B` e `C`.

### Algoritmo 1

```text
LEGGI A, B, C

SE A >= B
    SE A >= C
        STAMPA A
    ALTRIMENTI
        STAMPA C
    FINE SE
ALTRIMENTI
    SE B >= C
        STAMPA B
    ALTRIMENTI
        STAMPA C
    FINE SE
FINE SE
```

### Algoritmo 2

```text
LEGGI A, B, C

MASSIMO ← A

SE B > MASSIMO
    MASSIMO ← B
FINE SE

SE C > MASSIMO
    MASSIMO ← C
FINE SE

STAMPA MASSIMO
```

Con:

```text
A = 7
B = 12
C = 9
```

## SVOLGIMENTO

Entrambi gli algoritmi stampano:

```text
12
```

La differenza è nel modo in cui arrivano al risultato:

- il primo algoritmo confronta direttamente i valori tra loro mediante condizioni annidate;
- il secondo inizializza una variabile `MASSIMO` assumendo inizialmente che `A` sia il massimo, poi confronta gli altri valori con il massimo corrente e lo aggiorna quando trova un valore più grande.

Il secondo approccio introduce quindi l'idea di **massimo corrente**, che può essere riutilizzata anche quando i valori da confrontare diventano molti.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere che algoritmi diversi possono risolvere lo stesso problema.
- Confrontare due strategie diverse senza limitarsi al solo risultato finale.
- Distinguere tra confronti diretti annidati e mantenimento di un massimo corrente.
- Comprendere l'idea di aggiornare progressivamente una soluzione parziale.
- Intuire che alcune strategie sono più facilmente generalizzabili di altre.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: confronto tra algoritmi che risolvono lo stesso problema.

## COMPLESSITÀ

Non ancora analizzata formalmente in questo esercizio.
