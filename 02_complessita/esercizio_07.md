# Esercizio 07 — Primo ciclo for scritto autonomamente in C

## DESCRIZIONE

Scrivere un programma C che stampi i numeri da 0 a 9 usando un ciclo `for`.

## SVOLGIMENTO

Soluzione realizzata:

```c
#include <stdio.h>

int main() {

    int n = 10;
    for (int i = 0; i < n; i++) {
        printf("%d\n", i);
    }

    return 0;
}
```

Nel primo tentativo erano presenti soltanto errori di sintassi:
- mancava il punto e virgola dopo `int n = 10`;
- `printf(i)` non era corretto perché `printf` richiede una stringa di formato;
- mancava il punto e virgola dopo `return 0`.

La logica del ciclo era già corretta.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Scrivere autonomamente un ciclo `for` in C.
- Dichiarare una variabile intera con `int`.
- Usare inizializzazione, condizione e incremento nel `for`.
- Usare `printf("%d\n", i)` per stampare un intero.
- Ricordare il punto e virgola al termine delle istruzioni.
- Distinguere errori logici da errori di sintassi.

## ARGOMENTO D'ESAME

**02 — Complessità**

Percorso parallelo C:
- struttura minima di un programma C;
- variabili intere;
- ciclo `for`;
- output con `printf`.

## COMPLESSITÀ

Il ciclo esegue `n` iterazioni:

```text
Theta(n)
```
