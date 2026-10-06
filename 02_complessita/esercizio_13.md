# Esercizio 13 — Consolidamento della pila delle chiamate e delle ricorrenze

## DESCRIZIONE

Esercizio di consolidamento sulla ricorsione: esecuzione manuale della pila delle chiamate, distinzione tra discesa e risalita e riconoscimento delle complessità lineare, logaritmica ed esponenziale.

## SVOLGIMENTO

È stata analizzata una funzione con stampa prima e dopo la chiamata ricorsiva:

```python
def f(n):
    if n == 0:
        return

    print("A", n)
    f(n - 1)
    print("B", n)
```

Per `f(2)`, l'ordine corretto è:

```text
A 2
A 1
B 1
B 2
```

Questo mostra la distinzione tra:
- discesa nelle chiamate ricorsive;
- risalita dopo il raggiungimento del caso base.

È stato poi analizzato il caso:

```python
def f(n):
    if n <= 1:
        return

    print(n)
    f(n // 2)
```

Per `f(8)` vengono stampati:

```text
8 4 2
```

Durante la risalita non viene stampato nulla perché non ci sono istruzioni dopo la chiamata ricorsiva.

Con invece:

```python
def f(n):
    if n <= 1:
        return

    print("A", n)
    f(n // 2)
    print("B", n)
```

per `f(8)` l'ordine è:

```text
A 8
A 4
A 2
B 2
B 4
B 8
```

La complessità è `Theta(log n)` perché il problema viene dimezzato a ogni chiamata.

È stata poi riconosciuta correttamente la ricorsione lineare:

```python
def f(n):
    if n == 0:
        return

    f(n - 1)
```

con complessità:

```text
Theta(n)
```

Infine è stata riconosciuta correttamente la ricorsione con due chiamate per livello:

```python
def f(n):
    if n <= 1:
        return

    f(n - 1)
    f(n - 1)
```

con complessità:

```text
Theta(2^n)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Consolidare il concetto di pila delle chiamate.
- Distinguere chiaramente discesa e risalita nella ricorsione.
- Capire che durante la risalita vengono eseguite solo le istruzioni presenti dopo la chiamata ricorsiva.
- Riconoscere una ricorsione lineare `Theta(n)`.
- Riconoscere una ricorsione logaritmica `Theta(log n)`.
- Riconoscere una ricorsione esponenziale `Theta(2^n)`.
- Collegare la forma della riduzione del problema al numero di chiamate.

## ARGOMENTO D'ESAME

**02 — Complessità**

- algoritmi ricorsivi;
- caso base;
- pila delle chiamate;
- relazioni di ricorrenza elementari;
- complessità lineare, logaritmica ed esponenziale.

## COMPLESSITÀ

```text
T(n) = T(n - 1) + 1   → Theta(n)
T(n) = T(n / 2) + 1   → Theta(log n)
T(n) = 2T(n - 1) + 1  → Theta(2^n)
```
