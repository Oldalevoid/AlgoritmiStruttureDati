# Esercizio 01 — Introduzione agli algoritmi di ordinamento

## DESCRIZIONE

Introduzione ai concetti fondamentali degli algoritmi di ordinamento:
- confronto;
- scambio;
- algoritmo in-place;
- stabilità;
- prime passate di Bubble Sort;
- complessità del Bubble Sort.

## CONCETTI

### Confronto e scambio

Un algoritmo di ordinamento confronta elementi e, quando necessario, li scambia.

Esempio:

```text
[5, 2, 8]
5 e 2 → scambio
[2, 5, 8]
```

Un confronto è utile anche quando non produce uno scambio: serve a verificare se gli elementi sono già nell'ordine corretto.

### In-place

Un algoritmo è in-place quando riordina direttamente la struttura originale usando poca memoria aggiuntiva.

Non crea una seconda struttura grande quanto l'input.

### Stabilità

Un algoritmo stabile mantiene l'ordine relativo degli elementi che hanno la stessa chiave di ordinamento.

Esempio ordinando per età:

```text
Marco 20
Luca  18
Anna  20
```

Un ordinamento stabile produce:

```text
Luca  18
Marco 20
Anna  20
```

Marco resta prima di Anna.

## INTRODUZIONE AL BUBBLE SORT

Bubble Sort confronta elementi adiacenti e li scambia quando sono nell'ordine sbagliato.

Esempio:

```text
[4, 2, 7, 1]

4 e 2 → [2, 4, 7, 1]
4 e 7 → nessuno scambio
7 e 1 → [2, 4, 1, 7]
```

Dopo una passata completa, un elemento grande tende a raggiungere la sua posizione finale verso destra.

Una passata non garantisce sempre che tutta la lista sia già ordinata.

Esempio:

```text
[2, 3, 1]
→ [2, 1, 3]
→ [1, 2, 3]
```

## COMPLESSITÀ

Nel caso peggiore Bubble Sort esegue circa:

```text
(n-1) + (n-2) + ... + 1
```

quindi:

```text
O(n²)
```

Nella versione ottimizzata, se durante una passata non avviene alcuno scambio, l'algoritmo può terminare.

Per una lista già ordinata il best case è quindi:

```text
O(n)
```

## PROPRIETÀ DEL BUBBLE SORT

```text
Worst case → O(n²)
Best case ottimizzato → O(n)
In-place → sì
Stabile → sì
```

## COSA HO IMPARATO

- Il confronto verifica l'ordine di due elementi.
- Lo scambio modifica la loro posizione.
- In-place riguarda l'uso della memoria.
- La stabilità riguarda l'ordine relativo degli elementi con la stessa chiave.
- Bubble Sort confronta coppie adiacenti.
- Una passata non sempre ordina tutta la lista.
- Bubble Sort è in-place e stabile.
- Il worst case di Bubble Sort è O(n²).
