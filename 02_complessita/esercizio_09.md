# Esercizio 09 — Cicli con limiti non immediati

## DESCRIZIONE

L'esercizio consolida l'analisi di cicli Python in cui il numero di iterazioni non coincide direttamente con `n`.

Sono stati confrontati:
- cicli con passo 2;
- cicli limitati da `n // 2`;
- cicli che dimezzano la variabile a ogni iterazione;
- cicli annidati con un limite `n // 2`.

## SVOLGIMENTO

### 1. Step pari a 2

```python
for i in range(0, n, 2):
    print(i)
```

Il ciclo esegue circa `n/2` iterazioni.

```text
Theta(n/2) = Theta(n)
```

### 2. Range fino a n // 2

```python
for i in range(n // 2):
    print(i)
```

Anche qui il ciclo esegue circa `n/2` iterazioni.

```text
Theta(n)
```

Il simbolo `//` in Python indica la divisione intera.

### 3. Dimezzamento a ogni iterazione

```python
i = n

while i > 1:
    print(i)
    i //= 2
```

Qui la variabile viene dimezzata a ogni passo.

Con `n = 32`:

```text
32 -> 16 -> 8 -> 4 -> 2
```

Il ciclo esegue 5 iterazioni, cioè `log2(32)`.

```text
Theta(log n)
```

### 4. Cicli annidati con n // 2

```python
for i in range(n // 2):
    for j in range(n):
        print(i, j)
```

Il ciclo esterno esegue circa `n/2` iterazioni e quello interno `n`.

```text
(n/2) * n = n^2 / 2
```

Ignorando il fattore costante:

```text
Theta(n^2)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Capire che `range(0, n, 2)` esegue circa `n/2` iterazioni ma resta lineare.
- Capire che `range(n // 2)` resta `Theta(n)`.
- Distinguere tra fare metà delle iterazioni e dimezzare la variabile a ogni iterazione.
- Riconoscere il dimezzamento ripetuto come `Theta(log n)`.
- Analizzare cicli annidati calcolando il numero effettivo di iterazioni di ciascun ciclo.
- Riconoscere `(n/2) * n` come `Theta(n^2)`.

## ARGOMENTO D'ESAME

**02 — Complessità**

- ordini di crescita;
- analisi di cicli;
- fattori costanti;
- cicli annidati;
- crescita logaritmica.

## COMPLESSITÀ

```text
range(0, n, 2)        -> Theta(n)
range(n // 2)         -> Theta(n)
i //= 2               -> Theta(log n)
(n/2) * n             -> Theta(n^2)
```
