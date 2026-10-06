# Esercizio 12 — Prime ricorrenze e complessità degli algoritmi ricorsivi

## DESCRIZIONE

L'esercizio introduce il funzionamento della ricorsione, il ruolo del caso base, la pila delle chiamate e il collegamento tra la forma della chiamata ricorsiva e la complessità.

## SVOLGIMENTO

È stato analizzato prima un caso ricorsivo lineare:

```python
def conto(n):
    if n == 0:
        return

    conto(n - 1)
```

Per `conto(4)` la catena delle chiamate è:

```text
conto(4)
→ conto(3)
→ conto(2)
→ conto(1)
→ conto(0)
```

Ogni chiamata riduce `n` di 1, quindi servono circa `n` chiamate per raggiungere il caso base:

```text
T(n) = T(n - 1) + 1
→ Theta(n)
```

È stato poi chiarito il comportamento della pila delle chiamate: una funzione che effettua una chiamata ricorsiva resta in pausa fino al termine della chiamata più interna, quindi riprende dalla riga successiva.

Esempio:

```python
def conto(n):
    if n == 0:
        return

    conto(n - 1)
    print(n)
```

Con `conto(3)`, la discesa è:

```text
conto(3)
→ conto(2)
→ conto(1)
→ conto(0)
```

Poi le chiamate riprendono in ordine inverso e stampano:

```text
1
2
3
```

È stato analizzato anche il caso in cui il problema viene dimezzato:

```python
def dimezza(n):
    if n <= 1:
        return

    dimezza(n // 2)
```

Per `n = 16`:

```text
16 → 8 → 4 → 2 → 1
```

La ricorrenza è:

```text
T(n) = T(n / 2) + 1
→ Theta(log n)
```

Infine è stato introdotto un caso con due chiamate ricorsive:

```python
def doppia(n):
    if n <= 1:
        return

    doppia(n - 1)
    doppia(n - 1)
```

Per `n = 3` l'albero delle chiamate è:

```text
doppia(3)
├─ doppia(2)
│  ├─ doppia(1)
│  └─ doppia(1)
└─ doppia(2)
   ├─ doppia(1)
   └─ doppia(1)
```

La ricorrenza è:

```text
T(n) = 2T(n - 1) + 1
→ Theta(2^n)
```

Verifica finale svolta correttamente:

```python
def f(n):
    if n <= 1:
        return

    f(n - 1)
```

Lo studente ha riconosciuto autonomamente la complessità `Theta(n)`.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Capire che una funzione ricorsiva richiama sé stessa.
- Riconoscere il caso base come condizione che interrompe la ricorsione.
- Capire che ogni chiamata ha il proprio stato e che le chiamate precedenti restano in pausa.
- Comprendere la discesa e la successiva risalita della pila delle chiamate.
- Riconoscere `T(n) = T(n - 1) + 1` come crescita lineare `Theta(n)`.
- Riconoscere `T(n) = T(n / 2) + 1` come crescita logaritmica `Theta(log n)`.
- Comprendere in modo introduttivo che due chiamate ricorsive per livello possono generare una crescita esponenziale.
- Distinguere una riduzione di `n` di una unità da un dimezzamento ripetuto del problema.

## ARGOMENTO D'ESAME

**02 — Complessità**

- algoritmi ricorsivi;
- caso base;
- chiamata ricorsiva;
- numero di chiamate;
- semplici relazioni di ricorrenza;
- complessità lineare, logaritmica ed esponenziale.

## COMPLESSITÀ

```text
T(n) = T(n - 1) + 1   → Theta(n)
T(n) = T(n / 2) + 1   → Theta(log n)
T(n) = 2T(n - 1) + 1  → Theta(2^n)
```
