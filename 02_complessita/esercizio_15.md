# Esercizio 15 — Verifica mista del modulo 02

## DESCRIZIONE

Verifica di consolidamento sui principali concetti del modulo 02 — Complessità:
- cicli semplici e annidati;
- differenza tra `n/2` iterazioni e dimezzamento ripetuto;
- ricorsioni lineari, logaritmiche ed esponenziali;
- termine dominante;
- confronto tra ordini di crescita.

## SVOLGIMENTO

### 1. Cicli annidati

```python
for i in range(n):
    for j in range(n // 2):
        print(i, j)
```

Il ciclo esterno esegue `n` iterazioni e quello interno `n/2` iterazioni per ogni giro.

```text
n * (n/2) = n^2 / 2
→ Theta(n^2)
```

È stato chiarito che `n/2` iterazioni restano lineari: il fattore costante non rende il costo logaritmico.

### 2. Crescita logaritmica

```python
i = 1

while i < n:
    print(i)
    i *= 2
```

La variabile assume valori:

```text
1 → 2 → 4 → 8 → ...
```

Servono circa `log_2(n)` raddoppi per raggiungere `n`:

```text
Theta(log n)
```

### 3. Ricorsione lineare

```python
def f(n):
    if n <= 1:
        return

    f(n - 1)
```

La catena è:

```text
n → n-1 → n-2 → ... → 1
```

quindi:

```text
Theta(n)
```

### 4. Ricorsione logaritmica

```python
def f(n):
    if n <= 1:
        return

    f(n // 2)
```

La catena è:

```text
n → n/2 → n/4 → n/8 → ... → 1
```

quindi:

```text
Theta(log n)
```

### 5. Ricorsione esponenziale

```python
def f(n):
    if n <= 1:
        return

    f(n - 1)
    f(n - 1)
```

Ogni chiamata genera due nuove chiamate:

```text
Theta(2^n)
```

### 6. Termine dominante

```text
T(n) = 7n^2 + 3n + 20
→ Theta(n^2)

T(n) = 4n + 100
→ Theta(n)

T(n) = 3n log n + 5n
→ Theta(n log n)
```

Il termine che cresce più rapidamente determina la classe asintotica.

### 7. Ordine delle principali classi di crescita

Ordine corretto dalla crescita più lenta alla più veloce:

```text
Theta(1)
<
Theta(log n)
<
Theta(n)
<
Theta(n log n)
<
Theta(n^2)
<
Theta(2^n)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Consolidare la differenza tra `n/2` iterazioni e dimezzamento ripetuto.
- Riconoscere cicli annidati come prodotto del numero di iterazioni quando i limiti lo consentono.
- Riconoscere ricorsioni lineari, logaritmiche ed esponenziali.
- Individuare il termine dominante in una funzione di costo.
- Eliminare fattori costanti e termini di ordine inferiore nell'analisi asintotica.
- Ordinare correttamente le principali classi di complessità.
- Distinguere meglio tra la forma dell'algoritmo e il modo in cui varia la dimensione del problema.

## ARGOMENTO D'ESAME

**02 — Complessità**

- dimensione dell'input;
- funzione di costo;
- notazione asintotica;
- cicli semplici e annidati;
- algoritmi ricorsivi;
- ordini di crescita;
- confronto tra complessità.

## COMPLESSITÀ

```text
Theta(1) < Theta(log n) < Theta(n) < Theta(n log n) < Theta(n^2) < Theta(2^n)
```
