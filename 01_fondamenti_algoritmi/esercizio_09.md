# Esercizio 09 — Rappresentare un ciclo semplice tramite flowchart

## DESCRIZIONE

L'esercizio richiede di trasformare in flowchart un semplice ciclo che stampa i numeri da 1 a `N`.

Pseudocodice di partenza:

```text
LEGGI N

I ← 1

FINCHÉ I <= N
    STAMPA I
    I ← I + 1
FINE FINCHÉ

FINE
```

## SOLUZIONE

Il flowchart corretto segue questa sequenza:

1. **INIZIO**;
2. **LEGGI N**;
3. assegnazione **I ← 1**;
4. decisione **I <= N?**;
5. se **SÌ**:
   - **STAMPA I**;
   - **I ← I + 1**;
   - ritorno alla condizione **I <= N?**;
6. se **NO**:
   - **FINE**.

Rappresentazione testuale equivalente:

```text
        INIZIO
           |
        LEGGI N
           |
         I ← 1
           |
        I <= N ?
        /      \
      SÌ        NO
      |          |
   STAMPA I     FINE
      |
   I ← I + 1
      |
      └────── torna a I <= N ?
```

Durante lo svolgimento sono stati corretti due dettagli:
- la condizione deve essere `I <= N`, non `N <= I`;
- il flusso deve andare da `STAMPA I` a `I ← I + 1`, e solo dopo tornare alla condizione.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Rappresentare un ciclo tramite flowchart.
- Usare un rombo come condizione di permanenza nel ciclo.
- Rappresentare il ritorno alla condizione con una freccia all'indietro.
- Mantenere corretto l'ordine tra stampa, aggiornamento della variabile e nuova verifica.
- Distinguere correttamente `I <= N` da `N <= I`.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: flowchart, iterazione, pseudocodice e flusso di controllo.

## COMPLESSITÀ

Non ancora analizzata formalmente in questo esercizio.
