# Esercizio 08 — Crescita lineare, logaritmica e quadratica in Python

## DESCRIZIONE

L'esercizio consolida il riconoscimento delle principali classi di crescita attraverso semplici frammenti Python e richiede di scrivere autonomamente un ciclo logaritmico.

## SVOLGIMENTO

Sono stati analizzati i seguenti casi.

### A — Ciclo lineare

```python
for i in range(n):
    print(i)
```

Il corpo viene eseguito `n` volte.

```text
Theta(n)
```

### B — Ciclo logaritmico

```python
i = 1

while i < n:
    print(i)
    i *= 2
```

La variabile `i` raddoppia a ogni iterazione.

```text
Theta(log n)
```

### C — Ciclo quadratico

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Il ciclo interno esegue `n` iterazioni per ciascuna delle `n` iterazioni esterne.

```text
Theta(n^2)
```

### Implementazione autonoma in Python

Con:

```python
n = 10
```

è stato scritto autonomamente:

```python
n = 10
i = 1

while i < n:
    print(i)
    i *= 2
```

Output:

```text
1
2
4
8
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere in Python un ciclo lineare, logaritmico e quadratico.
- Collegare `range(n)` a una crescita lineare.
- Collegare `i *= 2` a una crescita logaritmica.
- Collegare due cicli completi annidati a una crescita quadratica.
- Scrivere autonomamente un ciclo `while` logaritmico in Python.
- Usare Python come strumento pratico per implementare concetti di complessità senza cambiare il focus dal corso universitario.

## ARGOMENTO D'ESAME

**02 — Complessità**

- ordini di crescita;
- analisi di cicli semplici;
- analisi di cicli annidati;
- complessità non ricorsiva.

## COMPLESSITÀ

```text
range(n)           -> Theta(n)
i *= 2             -> Theta(log n)
due cicli da n     -> Theta(n^2)
```
