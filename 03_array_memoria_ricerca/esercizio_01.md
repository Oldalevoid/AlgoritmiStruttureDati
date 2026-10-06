# Esercizio 01 — Array/lista Python, accesso per indice e visita lineare

## DESCRIZIONE

L'esercizio introduce l'uso di una lista Python come modello pratico di struttura indicizzata, l'accesso diretto tramite indice, la visita completa degli elementi e una prima introduzione alla ricerca lineare.

## SVOLGIMENTO

Data una lista:

```python
numeri = [10, 20, 30, 40]
```

gli indici sono:

```text
indice:   0   1   2   3
valore:  10  20  30  40
```

L'accesso diretto:

```python
numeri[2]
```

restituisce `30`.

L'accesso a un elemento noto tramite indice è costante:

```text
Theta(1)
```

È stata poi analizzata la visita completa di una lista:

```python
numeri = [5, 10, 15, 20, 25]

for numero in numeri:
    print(numero)
```

Vengono visitati tutti gli elementi. Se la lista contiene `n` elementi:

```text
Theta(n)
```

È stato poi collegato il concetto alla ricerca del massimo e alla ricerca lineare.

Per esempio:

```python
valori = [8, 3, 12, 7, 5]
```

Cercando `7` da sinistra a destra:

```text
8  → 1° confronto
3  → 2°
12 → 3°
7  → 4° confronto, trovato
```

Cercando `5` servono 5 confronti.

Se il valore cercato non è presente, occorre controllare tutti gli `n` elementi.

Quindi, per la ricerca lineare:

```text
caso migliore  → Theta(1)
caso peggiore  → Theta(n)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Gli indici partono da 0.
- Accedere direttamente a un elemento tramite indice costa `Theta(1)`.
- Visitare tutti gli elementi di una lista costa `Theta(n)`.
- Cercare il massimo con una scansione completa costa `Theta(n)`.
- La ricerca lineare controlla gli elementi uno alla volta.
- Se il valore cercato è all'inizio, il costo può essere costante.
- Se il valore è alla fine o assente, servono fino a `n` confronti.

## ARGOMENTO D'ESAME

**03 — Array, memoria e ricerca**

- strutture indicizzate;
- accesso tramite indice;
- visita di un array/lista;
- introduzione alla ricerca sequenziale.

## COMPLESSITÀ

```text
accesso per indice      → Theta(1)
visita completa         → Theta(n)
ricerca lineare best    → Theta(1)
ricerca lineare worst   → Theta(n)
```
