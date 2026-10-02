# Esercizio 07 — Leggere e ricostruire un semplice flowchart

## DESCRIZIONE

L'esercizio richiede di leggere un semplice flowchart e tradurlo in pseudocodice.

Il diagramma rappresenta questa logica:

1. leggere un numero `N`;
2. verificare se `N > 0`;
3. stampare `POSITIVO` se la condizione è vera;
4. stampare `NON POSITIVO` altrimenti;
5. terminare l'algoritmo.

## SOLUZIONE

```text
LEGGI N

SE N > 0
    STAMPA POSITIVO
ALTRIMENTI
    STAMPA NON POSITIVO
FINE SE

FINE
```

Durante lo svolgimento è stato corretto un dettaglio logico importante: nel ramo `ALTRIMENTI` non va scritto `NEGATIVO`, perché anche `N = 0` rende falsa la condizione `N > 0`. Il termine corretto è quindi `NON POSITIVO`.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Tradurre un flowchart in pseudocodice.
- Riconoscere una struttura di selezione a due rami.
- Seguire correttamente il flusso di controllo da una condizione ai due possibili esiti.
- Distinguere tra `NEGATIVO` e `NON POSITIVO`.
- Verificare che l'output del ramo `ALTRIMENTI` copra tutti i casi esclusi dalla condizione principale.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: flowchart, selezione, pseudocodice e completezza dei casi.

## COMPLESSITÀ

Non ancora analizzata formalmente in questo esercizio.
