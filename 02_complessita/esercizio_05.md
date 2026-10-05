# Esercizio 05 — Notazione asintotica e primi cicli in C

## DESCRIZIONE

L'esercizio consolida la distinzione tra **O grande**, **Ω (Omega)** e **Θ (Theta)** e collega gli ordini di crescita alla lettura di semplici cicli `for` in C.

Sono stati analizzati:

- limiti superiori, inferiori e stretti;
- crescita lineare;
- crescita logaritmica;
- crescita quadratica;
- effetto dell'aggiornamento della variabile di controllo di un ciclo;
- primi elementi di sintassi C utili all'analisi algoritmica.

## SVOLGIMENTO

### 1. O, Ω e Θ

Data:

```text
T(n) = 5n + 10
```

sono vere:

```text
T(n) ∈ O(n)
T(n) ∈ O(n²)
T(n) ∈ Ω(n)
T(n) ∈ Ω(1)
T(n) ∈ Θ(n)
```

mentre è falsa:

```text
T(n) ∈ Θ(n²)
```

Il punto importante è che `O` esprime un limite superiore, `Ω` un limite inferiore e `Θ` un limite asintotico stretto. Per `5n + 10`, la descrizione più precisa dell'ordine di crescita è quindi `Θ(n)`.

### 2. Primo ciclo lineare in C

```c
#include <stdio.h>

int main() {
    int n = 5;

    for (int i = 0; i < n; i++) {
        printf("Ciao\n");
    }

    return 0;
}
```

Con `n = 8`, `printf` viene eseguito 8 volte.

Il ciclo compie `n` iterazioni, quindi:

```text
Θ(n)
```

Sono stati introdotti a livello di lettura:

- `#include <stdio.h>`;
- `int main()`;
- `int`;
- `printf`;
- struttura del `for`: inizializzazione, condizione, aggiornamento;
- `i++`.

### 3. Incremento di 2

Se l'aggiornamento diventa:

```c
i = i + 2
```

il ciclo esegue circa `n/2` iterazioni.

Il fattore costante `1/2` non cambia l'ordine asintotico:

```text
Θ(n/2) = Θ(n)
```

### 4. Raddoppio della variabile: crescita logaritmica

Considerato:

```c
for (int i = 1; i < n; i = i * 2) {
    printf("Ciao\n");
}
```

i valori di `i` crescono come:

```text
1, 2, 4, 8, 16, 32, ...
```

Dopo `k` iterazioni, `i` è circa `2^k`. Per raggiungere `n`:

```text
2^k ≈ n
k ≈ log₂(n)
```

quindi la complessità è:

```text
Θ(log n)
```

Per:

```c
for (int i = 1; i < 32; i = i * 2) {
    printf("Ciao\n");
}
```

`printf` viene eseguito 5 volte, per `i = 1, 2, 4, 8, 16`.

### 5. Cicli annidati

Considerato:

```c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        printf("Ciao\n");
    }
}
```

il ciclo esterno esegue `n` iterazioni e quello interno `n` iterazioni per ciascuna iterazione esterna:

```text
n × n = n²
```

quindi:

```text
Θ(n²)
```

Con `n = 4`, `printf` viene eseguito 16 volte.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Distinguere `O`, `Ω` e `Θ`.
- Capire che `Θ` descrive in modo più preciso l'ordine di crescita quando limite superiore e inferiore coincidono.
- Riconoscere un ciclo lineare `Θ(n)`.
- Capire che aumentare l'indice di 2 dimezza circa il numero di iterazioni ma lascia la complessità `Θ(n)`.
- Riconoscere che un indice moltiplicato per una costante a ogni iterazione produce tipicamente una crescita logaritmica.
- Collegare `i = i * 2` a `Θ(log n)`.
- Riconoscere due cicli completi annidati come `Θ(n²)`.
- Leggere la struttura fondamentale di un ciclo `for` in C.
- Leggere semplici istruzioni C come `int`, `printf`, `i++`, `i = i + 2` e `i = i * 2`.

## ARGOMENTO D'ESAME

**02 — Complessità**

- notazione asintotica;
- ordini di crescita;
- analisi di cicli semplici;
- introduzione ai cicli annidati.

Percorso parallelo di C:

- struttura minima di un programma;
- ciclo `for`;
- variabili intere;
- aggiornamento della variabile di controllo.

## COMPLESSITÀ

```text
i++       → Θ(n)
i += 2    → Θ(n)
i *= 2    → Θ(log n)
n × n     → Θ(n²)
```

## PUNTO DA CONSOLIDARE

Non assumere che ogni ciclo annidato sia automaticamente `Θ(n²)`: bisogna analizzare il numero di iterazioni effettive di ciascun ciclo.
