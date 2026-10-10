# Esercizio 03 — Selection Sort

## DESCRIZIONE

Introduzione e consolidamento del Selection Sort:
- ricerca del minimo;
- distinzione tra indice e valore;
- parte ordinata e parte non ordinata;
- uso di due cicli;
- swap finale;
- stabilità;
- complessità;
- confronto con Bubble Sort;
- implementazione Python.

## IDEA DI BASE

Selection Sort cerca il valore minimo nella parte non ancora ordinata della lista e lo porta nella prima posizione libera.

Esempio:

```text
[7, 4, 9, 2]
```

Il minimo è `2`, quindi:

```text
[2, 4, 9, 7]
```

Poi si lavora sulla parte restante:

```text
[4, 9, 7]
```

## SIMULAZIONE

Lista:

```text
[8, 5, 3, 7]
```

Prima passata:

```text
indice_minimo = 0   → valore 8
trovo 5             → indice_minimo = 1
trovo 3             → indice_minimo = 2
7 non è più piccolo → indice_minimo resta 2
```

Alla fine scambio gli indici 0 e 2:

```text
[8, 5, 3, 7]
→ [3, 5, 8, 7]
```

Seconda passata:

```text
indice_minimo = 1
5 resta il minimo
nessuno swap necessario
```

Terza passata:

```text
indice_minimo = 2
7 < 8 → indice_minimo = 3
swap tra indice 2 e indice 3
```

Risultato:

```text
[3, 5, 7, 8]
```

## INDICE VS VALORE

`indice_minimo` contiene la posizione del minimo corrente, non il valore.

Esempio:

```python
indice_minimo = 2
```

significa che il minimo corrente si trova in posizione 2.

Il suo valore è:

```python
numeri[indice_minimo]
```

## STRUTTURA DEL CICLO

Il ciclo esterno identifica la prima posizione della parte ancora da ordinare:

```python
for i in range(len(numeri) - 1):
    indice_minimo = i
```

Il ciclo interno parte da `i + 1`, perché `i` è già il minimo provvisorio:

```python
for j in range(i + 1, len(numeri)):
```

Se trova un valore più piccolo:

```python
if numeri[j] < numeri[indice_minimo]:
    indice_minimo = j
```

Lo swap viene eseguito solo dopo che il ciclo interno ha terminato la ricerca del minimo:

```python
if indice_minimo != i:
    numeri[i], numeri[indice_minimo] = numeri[indice_minimo], numeri[i]
```

## IMPLEMENTAZIONE PYTHON

```python
numeri = [8, 5, 3, 7]

for i in range(len(numeri) - 1):
    indice_minimo = i

    for j in range(i + 1, len(numeri)):
        if numeri[j] < numeri[indice_minimo]:
            indice_minimo = j

    if indice_minimo != i:
        numeri[i], numeri[indice_minimo] = numeri[indice_minimo], numeri[i]

print(numeri)
```

Output:

```text
[3, 5, 7, 8]
```

## COMPLESSITÀ

Selection Sort deve cercare il minimo nella parte restante anche quando la lista è già ordinata.

Quindi:

```text
Best case  → O(n²)
Worst case → O(n²)
Spazio     → O(1)
```

## STABILITÀ E MEMORIA

Selection Sort classico:
- è in-place;
- non è stabile.

Esempio di perdita di stabilità:

```text
[4A, 4B, 2]
→ swap 4A con 2
[2, 4B, 4A]
```

L'ordine relativo tra `4A` e `4B` cambia.

## CONFRONTO CON BUBBLE SORT

```text
Bubble Sort ottimizzato
- best case: O(n)
- worst case: O(n²)
- stabile: sì
- in-place: sì
- può fare molti swap

Selection Sort
- best case: O(n²)
- worst case: O(n²)
- stabile: no
- in-place: sì
- fa al massimo circa n - 1 swap
```

Selection Sort può essere utile quando gli swap sono costosi e conviene ridurne il numero.

## COSA HO IMPARATO

- Selection Sort cerca il minimo della parte non ordinata.
- `indice_minimo` memorizza un indice, non un valore.
- Il ciclo interno serve a cercare l'indice del minimo.
- Lo swap si esegue dopo il ciclo interno.
- Se `indice_minimo == i`, lo swap può essere evitato.
- Selection Sort resta O(n²) anche nel caso migliore.
- È in-place ma non stabile.
- Tende a fare meno swap del Bubble Sort.
