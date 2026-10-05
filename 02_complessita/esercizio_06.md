# Esercizio 06 — Cicli annidati con crescita mista

## DESCRIZIONE

L'esercizio mostra che due cicli annidati non producono automaticamente complessità quadratica. Se il ciclo esterno è lineare e quello interno è logaritmico, le crescite si moltiplicano.

## SVOLGIMENTO

```c
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j = j * 2) {
        printf("Ciao\n");
    }
}
```

Il ciclo esterno esegue `n` iterazioni. Il ciclo interno esegue circa `log2(n)` iterazioni per ogni iterazione esterna.

Quindi il numero totale di esecuzioni e' circa:

```text
n * log2(n)
```

La complessita' e':

```text
Theta(n log n)
```

Con `n = 8`, il ciclo esterno gira 8 volte e quello interno 3 volte, quindi `printf` viene eseguito `8 * 3 = 24` volte.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere un ciclo annidato con crescite diverse.
- Capire che, quando il ciclo interno viene rieseguito per ogni iterazione esterna, i costi si moltiplicano.
- Riconoscere `n * log n`.
- Distinguere una crescita `Theta(n log n)` da una crescita quadratica.
- Calcolare manualmente il numero di iterazioni in un caso concreto.

## ARGOMENTO D'ESAME

02 — Complessita': analisi di cicli annidati e ordini di crescita.

Percorso parallelo C: lettura di cicli `for` annidati e aggiornamento moltiplicativo della variabile di controllo.

## COMPLESSITA'

```text
ciclo esterno: Theta(n)
ciclo interno: Theta(log n)
totale: Theta(n log n)
```
