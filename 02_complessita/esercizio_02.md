# Esercizio 02 — Costo temporale e costo spaziale

## DESCRIZIONE

L'esercizio distingue il costo temporale dal costo spaziale osservando due algoritmi semplici.

Primo caso:

```text
ALGORITMO Somma(A, n)

somma ← 0

PER i ← 0 FINO A n-1
    somma ← somma + A[i]

RESTITUISCI somma
```

L'istruzione principale viene eseguita una volta per ogni elemento dell'input.

```text
T(n) = n
```

La memoria aggiuntiva usata dall'algoritmo resta invece sostanzialmente costante, perché vengono create solo poche variabili indipendentemente da `n`.

```text
S(n) = costante
```

Secondo caso:

```text
ALGORITMO Copia(A, n)

CREA B di dimensione n

PER i ← 0 FINO A n-1
    B[i] ← A[i]

RESTITUISCI B
```

Per `n = 5`, l'istruzione:

```text
B[i] ← A[i]
```

viene eseguita 5 volte.

In generale:

```text
T(n) = n
```

La nuova struttura `B` contiene `n` elementi, quindi anche la memoria aggiuntiva cresce con la dimensione dell'input:

```text
S(n) = n
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Distinguere il costo temporale dal costo spaziale.
- Capire che il costo temporale descrive quante operazioni vengono eseguite al crescere di `n`.
- Capire che il costo spaziale descrive quanta memoria aggiuntiva viene usata al crescere di `n`.
- Riconoscere che due algoritmi possono avere lo stesso `T(n)` ma un diverso `S(n)`.
- Riconoscere che poche variabili producono uno spazio aggiuntivo costante.
- Riconoscere che creare una nuova struttura di dimensione `n` produce un costo spaziale che cresce con `n`.

## ARGOMENTO D'ESAME

**02 — Complessità**

Costo temporale e costo spaziale di un algoritmo.

## COMPLESSITÀ

Per l'algoritmo di somma:

```text
T(n) = n
S(n) = costante
```

Per l'algoritmo di copia:

```text
T(n) = n
S(n) = n
```

In questa fase non viene ancora usata la notazione asintotica `O`, `Ω` o `Θ`.
