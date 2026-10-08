# Esercizio 02 — Bubble Sort: simulazione, pseudocodice e Python

## DESCRIZIONE

Consolidamento del Bubble Sort attraverso:
- simulazione manuale;
- numero massimo di passate;
- confronti adiacenti;
- flag booleano per arresto anticipato;
- riduzione progressiva del ciclo interno;
- implementazione Python.

## SIMULAZIONE

Lista iniziale:

```text
[5, 1, 4, 2]
```

Prima passata:

```text
5 e 1 → scambio → [1, 5, 4, 2]
5 e 4 → scambio → [1, 4, 5, 2]
5 e 2 → scambio → [1, 4, 2, 5]
```

Seconda passata:

```text
1 e 4 → nessuno scambio
4 e 2 → scambio → [1, 2, 4, 5]
```

## NUMERO DI PASSATE

Con `n` elementi servono al massimo:

```text
n - 1 passate
```

Esempi:

```text
n = 4  → massimo 3 passate
n = 10 → massimo 9 passate
```

## CONFRONTI ADIACENTI

Con `n` elementi, nella prima passata ci sono al massimo:

```text
n - 1 confronti
```

Con 4 elementi:

```text
indici validi: 0, 1, 2, 3

confronti:
0-1
1-2
2-3
```

Il ciclo interno non deve arrivare a `i = 3`, perché il confronto usa anche `i + 1` e quindi tenterebbe di accedere a un indice inesistente.

## FLAG BOOLEANO

All'inizio di ogni passata:

```python
scambiato = False
```

Quando avviene almeno uno scambio:

```python
scambiato = True
```

Alla fine della passata:

```python
if not scambiato:
    break
```

Il flag non conta gli scambi: ricorda soltanto se nella passata ne è avvenuto almeno uno.

## RIDUZIONE DEL CICLO INTERNO

Dopo ogni passata, un elemento finale è già nella sua posizione corretta.

Per questo il ciclo interno può accorciarsi:

```python
for i in range(len(numeri) - 1 - passata):
```

Esempio con 5 elementi:

```text
passata = 0 → 4 confronti
passata = 1 → 3 confronti
passata = 2 → 2 confronti
passata = 3 → 1 confronto
```

## IMPLEMENTAZIONE PYTHON

```python
numeri = [5, 1, 4, 2]

for passata in range(len(numeri) - 1):
    scambiato = False

    for i in range(len(numeri) - 1 - passata):
        if numeri[i] > numeri[i + 1]:
            numeri[i], numeri[i + 1] = numeri[i + 1], numeri[i]
            scambiato = True

    if not scambiato:
        break

print(numeri)
```

Output:

```text
[1, 2, 4, 5]
```

## COMPLESSITÀ

```text
Worst case → O(n²)
Best case con arresto anticipato → O(n)
Spazio aggiuntivo → O(1)
```

Bubble Sort è quindi:
- in-place;
- stabile nella versione classica;
- quadratico nel caso peggiore.

## COSA HO IMPARATO

- Con `n` elementi ci sono al massimo `n - 1` passate.
- Nella prima passata ci sono `n - 1` confronti adiacenti.
- Il ciclo interno deve evitare l'out of range su `i + 1`.
- `scambiato` è un flag booleano.
- Se una passata non produce scambi, l'algoritmo può terminare.
- Il ciclo interno si accorcia dopo ogni passata.
- Ho costruito passo passo il Bubble Sort ottimizzato in Python.
