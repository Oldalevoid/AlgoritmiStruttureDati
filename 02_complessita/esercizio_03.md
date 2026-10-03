# Esercizio 03 — Contare più operazioni elementari

## DESCRIZIONE

L'esercizio mostra come costruire la funzione di costo temporale quando, dentro lo stesso algoritmo, vengono eseguite più operazioni elementari.

Esempio 1:

```text
ALGORITMO Esempio(A, n)

PER i ← 0 FINO A n-1
    x ← A[i]
    y ← x * 2
    stampa y
```

Se contiamo come operazioni elementari:

```text
x ← A[i]
y ← x * 2
stampa y
```

per ogni iterazione del ciclo vengono eseguite 3 operazioni.

Per `n = 4`:

```text
T(4) = 3 × 4 = 12
```

In generale:

```text
T(n) = 3n
```

Esempio 2:

```text
x ← 0

PER i ← 0 FINO A n-1
    x ← x + 1
    stampa x
```

Se contiamo anche l'assegnazione iniziale `x ← 0`, abbiamo:

- 1 operazione iniziale;
- 2 operazioni per ogni iterazione del ciclo.

Quindi:

```text
T(n) = 2n + 1
```

Esempio 3:

```text
ALGORITMO Test(A, n)

x ← 0
y ← 1

PER i ← 0 FINO A n-1
    x ← x + A[i]
    y ← y + 1
    stampa x

RESTITUISCI y
```

Contando come operazioni elementari:

```text
x ← 0
y ← 1
x ← x + A[i]
y ← y + 1
stampa x
RESTITUISCI y
```

otteniamo:

- 2 operazioni iniziali;
- 3n operazioni nel ciclo;
- 1 operazione finale di restituzione.

Quindi:

```text
T(n) = 3n + 3
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Contare più operazioni elementari nello stesso ciclo.
- Costruire funzioni di costo come `T(n) = 3n`.
- Aggiungere termini costanti per le operazioni fuori dal ciclo.
- Distinguere tra parte variabile e parte costante della funzione di costo.
- Capire che il costo totale è la somma delle operazioni dentro e fuori dal ciclo.

## ARGOMENTO D'ESAME

**02 — Complessità**

Conteggio di più operazioni elementari nello stesso algoritmo.

## COMPLESSITÀ

Esempi studiati:

```text
T(n) = 3n
T(n) = 2n + 1
T(n) = 3n + 3
```

In questa fase non viene ancora usata la notazione asintotica `O`, `Ω` o `Θ`.
