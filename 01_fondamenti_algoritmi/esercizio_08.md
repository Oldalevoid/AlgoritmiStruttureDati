# Esercizio 08 — Costruire un flowchart a partire da pseudocodice

## DESCRIZIONE

L'esercizio richiede di trasformare un semplice pseudocodice in un flowchart corretto, usando le forme standard per inizio/fine, input/output e decisione.

Pseudocodice di partenza:

```text
LEGGI N

SE N > 10
    STAMPA "GRANDE"
ALTRIMENTI
    STAMPA "PICCOLO O UGUALE A 10"
FINE SE

FINE
```

## SOLUZIONE

Il flowchart costruito contiene:

1. **INIZIO** — ovale;
2. **LEGGI N** — parallelogramma;
3. **N > 10?** — rombo;
4. ramo **SÌ** → **STAMPA "GRANDE"** — parallelogramma;
5. ramo **NO** → **STAMPA "PICCOLO O UGUALE A 10"** — parallelogramma;
6. ricongiungimento dei due rami;
7. **FINE** — ovale.

Rappresentazione testuale equivalente:

```text
        INIZIO
           |
        LEGGI N
           |
        N > 10?
        /     \
      SÌ       NO
      |         |
STAMPA       STAMPA
"GRANDE"    "PICCOLO O
             UGUALE A 10"
      \         /
          FINE
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Costruire autonomamente un flowchart a partire da pseudocodice.
- Associare correttamente le forme standard alle diverse istruzioni.
- Usare un rombo per una condizione con due rami.
- Usare parallelogrammi per input e output.
- Far convergere correttamente i rami alternativi verso la fine dell'algoritmo.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: flowchart, pseudocodice, selezione e rappresentazione grafica di un algoritmo.

## COMPLESSITÀ

Non ancora analizzata formalmente in questo esercizio.
