# Esercizio 11 — Crescita esponenziale

## DESCRIZIONE

L'esercizio introduce la complessità esponenziale `Theta(2^n)` e la confronta con le principali classi di crescita già studiate.

## SVOLGIMENTO

Confronto tra crescita quadratica ed esponenziale:

```text
n = 5   -> n^2 = 25      ; 2^n = 32
n = 10  -> n^2 = 100     ; 2^n = 1024
n = 20  -> n^2 = 400     ; 2^n = 1.048.576
```

La crescita esponenziale diventa rapidamente molto più grande della crescita quadratica.

Ordine dalla più efficiente alla meno efficiente:

```text
Theta(1)
Theta(log n)
Theta(n)
Theta(n log n)
Theta(n^2)
Theta(2^n)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere la crescita esponenziale `Theta(2^n)`.
- Capire che `2^n` cresce molto più rapidamente di `n^2`.
- Inserire correttamente la crescita esponenziale nell'ordine delle principali classi di complessità.
- Consolidare il confronto tra costante, logaritmica, lineare, quasi-lineare, quadratica ed esponenziale.

## ARGOMENTO D'ESAME

**02 — Complessità**

- ordini di crescita;
- confronto tra classi asintotiche;
- crescita esponenziale.

## COMPLESSITÀ

```text
Theta(1) < Theta(log n) < Theta(n) < Theta(n log n) < Theta(n^2) < Theta(2^n)
```
