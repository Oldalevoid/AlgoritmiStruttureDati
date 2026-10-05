# Esercizio 10 — Ordinare le principali classi di complessità

## DESCRIZIONE

L'esercizio richiede di ordinare alcune delle principali classi di complessità dalla più efficiente alla meno efficiente per valori grandi di `n`.

Classi considerate:

```text
Theta(1)
Theta(log n)
Theta(n)
Theta(n log n)
Theta(n^2)
```

## SVOLGIMENTO

Ordine corretto:

```text
Theta(1)
Theta(log n)
Theta(n)
Theta(n log n)
Theta(n^2)
```

Quindi:

- `Theta(1)` cresce meno di tutte;
- `Theta(log n)` cresce molto lentamente;
- `Theta(n)` cresce linearmente;
- `Theta(n log n)` cresce più della lineare ma meno della quadratica;
- `Theta(n^2)` cresce più rapidamente tra quelle considerate.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Ordinare le principali classi di complessità per ordine di crescita.
- Distinguere tra costante, logaritmica, lineare, quasi-lineare e quadratica.
- Capire che il confronto va fatto pensando a valori grandi di `n`.
- Consolidare la relazione:
  `1 < log n < n < n log n < n^2`.

## ARGOMENTO D'ESAME

**02 — Complessità**

- ordini di crescita;
- confronto tra classi asintotiche.

## COMPLESSITÀ

```text
Theta(1) < Theta(log n) < Theta(n) < Theta(n log n) < Theta(n^2)
```
