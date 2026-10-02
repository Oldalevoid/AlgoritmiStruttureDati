# Esercizio 06 — Leggere ed eseguire mentalmente uno pseudocodice

## DESCRIZIONE

L'esercizio richiede di leggere ed eseguire mentalmente un semplice pseudocodice, seguendo passo per passo il valore delle variabili durante un ciclo.

Pseudocodice analizzato:

```text
LEGGI N

CONTA ← 0

PER I DA 1 A N
    SE I > 2
        CONTA ← CONTA + 1
    FINE SE
FINE PER

STAMPA CONTA
```

Con input:

```text
N = 5
```

## SVOLGIMENTO

La variabile `I` assume i valori:

```text
1, 2, 3, 4, 5
```

La condizione `I > 2` è vera per:

```text
3, 4, 5
```

Quindi `CONTA` aumenta tre volte:

```text
0 → 1 → 2 → 3
```

Output finale:

```text
3
```

Durante l'esercizio è stato anche chiarito che nello pseudocodice `PER I DA 1 A N` include il valore `N`, mentre in Python `range(1, n)` esclude `n`. La traduzione corretta è quindi `range(1, n + 1)`.

## IMPLEMENTAZIONE PYTHON

Vedi anche `esercizio_06.py`.

```python
n = 5
conta = 0

for i in range(1, n + 1):
    if i > 2:
        conta = conta + 1

print(conta)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Eseguire mentalmente un semplice pseudocodice con ciclo e condizione.
- Seguire il valore di una variabile che cambia a ogni iterazione.
- Distinguere tra il valore dell'indice del ciclo e il contatore aggiornato dall'algoritmo.
- Comprendere che `PER I DA 1 A N` include `N`.
- Tradurre correttamente un intervallo pseudocodice in `range(1, n + 1)` in Python.
- Verificare l'output di un algoritmo tramite esecuzione manuale.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: pseudocodice, iterazione, selezione ed esecuzione manuale di un algoritmo.

## COMPLESSITÀ

Non ancora analizzata formalmente in questo esercizio.
