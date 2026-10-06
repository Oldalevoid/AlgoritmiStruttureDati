# Esercizio 14 — Costo per livello e numero di livelli

## DESCRIZIONE

L'esercizio introduce la distinzione tra:
- numero di livelli ricorsivi;
- lavoro svolto a ogni livello;
- somma dei costi sui diversi livelli;
- differenza tra operazioni in sequenza e cicli annidati.

## SVOLGIMENTO

Primo caso:

```python
def f(n):
    if n <= 1:
        return

    for i in range(n):
        print(i)

    f(n // 2)
```

Per `n = 8`:

```text
f(8) → 8 operazioni
f(4) → 4 operazioni
f(2) → 2 operazioni
f(1) → caso base
```

Totale:

```text
8 + 4 + 2 = 14
```

In generale:

```text
n + n/2 + n/4 + n/8 + ...
```

La somma resta proporzionale a `n`, quindi:

```text
Theta(n)
```

Secondo caso:

```python
def f(n):
    if n <= 1:
        return

    for i in range(n):
        print(i)

    f(n - 1)
```

Il lavoro totale è:

```text
n + (n-1) + (n-2) + ... + 1
```

che vale:

```text
n(n+1)/2
```

e quindi:

```text
Theta(n^2)
```

È stato chiarito che i costi dei livelli si sommano, non si moltiplicano automaticamente.

Terzo caso: costo costante per livello.

Se ogni livello compie 5 operazioni e ci sono circa `n` livelli:

```text
5 + 5 + 5 + ... + 5 = 5n
```

quindi:

```text
Theta(n)
```

È stato poi consolidato il confronto tra sequenza e annidamento.

Due cicli in sequenza:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Costo:

```text
n + n = 2n
→ Theta(n)
```

Due cicli annidati:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Costo:

```text
n * n = n^2
→ Theta(n^2)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Distinguere il numero di livelli ricorsivi dal lavoro svolto in ogni livello.
- Sommare i costi dei diversi livelli di una ricorsione.
- Riconoscere che `n + n/2 + n/4 + ...` è `Theta(n)`.
- Riconoscere che `n + (n-1) + ... + 1` è `Theta(n^2)`.
- Capire che più cicli in sequenza sommano i propri costi.
- Capire che cicli annidati portano spesso a moltiplicare il numero di iterazioni.
- Riconoscere `Theta(n)`, `Theta(n^2)` e `Theta(n log n)` in semplici combinazioni di lavoro per livello e numero di livelli.

## ARGOMENTO D'ESAME

**02 — Complessità**

- analisi di algoritmi ricorsivi;
- costo per livello;
- numero di livelli;
- somme di costi;
- cicli in sequenza e cicli annidati;
- ordini di crescita.

## COMPLESSITÀ

```text
n + n/2 + n/4 + ...        → Theta(n)
n + (n-1) + ... + 1        → Theta(n^2)
n + n + ... (log n volte)  → Theta(n log n)
n + n                      → Theta(n)
n * n                      → Theta(n^2)
```
