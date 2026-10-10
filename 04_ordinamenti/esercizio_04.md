# Esercizio 04 — Insertion Sort

## DESCRIZIONE

Introduzione e consolidamento di Insertion Sort:
- parte già ordinata;
- variabile chiave;
- spostamento verso destra;
- uso di j per scorrere verso sinistra;
- inserimento finale della chiave;
- stabilità;
- complessità;
- confronto con Bubble Sort e Selection Sort;
- implementazione Python.

## IDEA DI BASE

Insertion Sort lavora come quando si ordinano delle carte in mano: considera una parte iniziale già ordinata e inserisce ogni nuovo elemento nella posizione corretta.

Esempio:

```text
[5, 2, 4, 6]
```

Prima si considera `5` già ordinato.

Poi si inserisce `2`:

```text
[2, 5, 4, 6]
```

Poi si inserisce `4` tra `2` e `5`:

```text
[2, 4, 5, 6]
```

## CHIAVE

La variabile `chiave` contiene il valore da inserire nella parte già ordinata.

Esempio:

```python
chiave = numeri[i]
```

`chiave` contiene un valore, non un indice.

## SCORRIMENTO VERSO SINISTRA

L'indice `j` parte dall'elemento immediatamente a sinistra della chiave:

```python
j = i - 1
```

Il ciclo continua finché l'elemento a sinistra è maggiore della chiave:

```python
while j >= 0 and numeri[j] > chiave:
```

Gli elementi più grandi vengono spostati di una posizione verso destra:

```python
numeri[j + 1] = numeri[j]
j -= 1
```

Quando il ciclo termina, la chiave viene inserita nella posizione corretta:

```python
numeri[j + 1] = chiave
```

## ESEMPIO

Partiamo da:

```text
[1, 2, 5, 3]
```

Salviamo:

```text
chiave = 3
```

Poiché `5 > 3`, il 5 viene spostato a destra:

```text
[1, 2, 5, 5]
```

Poi `2 < 3`, quindi ci fermiamo e inseriamo la chiave:

```text
[1, 2, 3, 5]
```

## IMPLEMENTAZIONE PYTHON

```python
numeri = [5, 2, 4, 6, 1, 3]

for i in range(1, len(numeri)):
    chiave = numeri[i]
    j = i - 1

    while j >= 0 and numeri[j] > chiave:
        numeri[j + 1] = numeri[j]
        j -= 1

    numeri[j + 1] = chiave

print(numeri)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

## PERCHÉ IL CICLO PARTE DA 1

Il primo elemento, da solo, è già una parte ordinata di lunghezza 1.

Per questo il ciclo esterno parte da:

```python
range(1, len(numeri))
```

## COMPLESSITÀ

Lista già ordinata:

```text
Best case → O(n)
```

Lista ordinata al contrario:

```text
Worst case → O(n²)
```

Spazio aggiuntivo:

```text
O(1)
```

## STABILITÀ E MEMORIA

Insertion Sort classico:
- è in-place;
- è stabile.

È stabile perché sposta soltanto gli elementi strettamente maggiori della chiave:

```python
numeri[j] > chiave
```

Gli elementi uguali non si scavalcano tra loro.

## CONFRONTO CON GLI ALGORITMI PRECEDENTI

```text
Bubble Sort
- stabile
- in-place
- best O(n) nella versione ottimizzata
- worst O(n²)

Selection Sort
- non stabile
- in-place
- best O(n²)
- worst O(n²)
- tende a fare pochi swap

Insertion Sort
- stabile
- in-place
- best O(n)
- worst O(n²)
- particolarmente adatto a dati quasi ordinati
```

## COSA HO IMPARATO

- Insertion Sort costruisce progressivamente una parte ordinata.
- La chiave è il valore da inserire, non un indice.
- j scorre verso sinistra.
- Gli elementi maggiori della chiave vengono spostati verso destra.
- La chiave viene inserita in `j + 1`.
- Se j arriva a -1, la chiave viene inserita all'indice 0.
- Insertion Sort non usa swap ripetuti nella versione classica: usa spostamenti e un inserimento finale.
- È in-place e stabile.
- Ha best case O(n) e worst case O(n²).
- È particolarmente efficace su liste già quasi ordinate.
