# Esercizio 04 — Caso migliore, medio e peggiore

## DESCRIZIONE

L'esercizio introduce la distinzione tra **caso migliore, caso medio e caso peggiore** usando come esempio la ricerca lineare in una lista.

Esempio:

```text
[4, 7, 2, 9, 5]
```

La ricerca lineare controlla gli elementi uno alla volta fino a trovare il valore cercato.

### Caso migliore

Il valore cercato si trova nella prima posizione della lista.

```text
[9, 4, 7, 2, 5]
 ↑
 trovato alla prima verifica
```

Numero di verifiche:

```text
1
```

Quindi il costo non dipende da `n`:

```text
O(1)
```

### Caso peggiore

Il valore cercato si trova nell'ultima posizione oppure non è presente.

Numero di verifiche:

```text
n
```

Quindi:

```text
O(n)
```

### Caso medio

Se il valore può trovarsi con uguale probabilità in ogni posizione, mediamente vengono controllati circa metà degli elementi.

Numero medio di verifiche:

```text
(n + 1) / 2
```

Per grandi valori di `n`, questo cresce come `n/2`.

Nella notazione asintotica le costanti moltiplicative vengono ignorate:

```text
O(n/2) = O(n)
```

## RISPOSTA SVOLTA

La ricerca lineare ha quindi:

```text
caso migliore  → 1 verifica      → O(1)
caso medio     → circa n/2       → O(n)
caso peggiore  → n verifiche     → O(n)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Distinguere caso migliore, medio e peggiore dello stesso algoritmo.
- Capire che lo stesso algoritmo può avere costi diversi su input della stessa dimensione.
- Riconoscere che nella ricerca lineare il caso migliore richiede una sola verifica.
- Riconoscere che il caso peggiore richiede fino a `n` verifiche.
- Stimare il caso medio della ricerca lineare in circa `n/2` verifiche.
- Capire introduttivamente che `O(n/2)` si semplifica in `O(n)` perché le costanti non cambiano l'ordine di crescita.

## ARGOMENTO D'ESAME

**02 — Complessità**

Caso ottimo, medio e pessimo di un algoritmo.

## COMPLESSITÀ

Per la ricerca lineare:

```text
caso migliore  → O(1)
caso medio     → O(n)
caso peggiore  → O(n)
```

La notazione `O`, `Ω` e `Θ` verrà approfondita nel prossimo esercizio.
