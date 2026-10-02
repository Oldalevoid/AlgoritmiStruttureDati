# Esercizio 11 — Comprendere il divide et impera

## DESCRIZIONE

L'esercizio introduce l'idea di **divide et impera** applicata al problema di trovare il massimo in una lista.

Lista di partenza:

```text
[7, 2, 9, 4, 6, 1, 8, 3]
```

La strategia consiste nel dividere progressivamente il problema in sottoproblemi più piccoli, risolverli e poi combinare i risultati.

Prima divisione:

```text
[7, 2, 9, 4]     [6, 1, 8, 3]
```

Seconda divisione:

```text
[7, 2] [9, 4]     [6, 1] [8, 3]
```

## SVOLGIMENTO

I quattro sottoproblemi da due elementi producono:

```text
max(7, 2) = 7
max(9, 4) = 9
max(6, 1) = 6
max(8, 3) = 8
```

I risultati vengono poi combinati:

```text
max(7, 9) = 9
max(6, 8) = 8
max(9, 8) = 9
```

Il massimo finale è quindi:

```text
9
```

Il metodo è un esempio di **divide et impera** perché il problema viene scomposto in sottoproblemi sempre più piccoli, risolti separatamente e poi ricomposti fino a ottenere la soluzione finale.

La decomposizione procede in modo **top-down**, mentre la combinazione dei risultati avviene risalendo **bottom-up**.

Schema concettuale:

```text
problema grande
↓
sottoproblemi
↓
sottoproblemi più piccoli
↓
soluzioni
↑
combinazione
↑
soluzione finale
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Comprendere il principio del divide et impera.
- Riconoscere le tre fasi fondamentali: dividere, risolvere e combinare.
- Comprendere la decomposizione top-down del problema.
- Comprendere la ricomposizione bottom-up delle soluzioni.
- Applicare intuitivamente divide et impera alla ricerca del massimo.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: strategia divide et impera.

## COMPLESSITÀ

Non ancora analizzata formalmente in questo esercizio.
