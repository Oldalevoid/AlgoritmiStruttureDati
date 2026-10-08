# Esercizio 05 — Casi limite della ricerca binaria, stack, heap e puntatori

## DESCRIZIONE

L'esercizio consolida i casi limite della ricerca binaria e introduce i concetti di stack, heap, puntatori, indirizzo di memoria, dereferenziazione, allocazione dinamica e memory leak.

## SVOLGIMENTO

### Ricerca binaria — casi limite

Lista:

```text
[4, 9, 15, 22, 31]
```

Con:

```text
sinistra = 0
destra = 4
```

il centro è:

```text
(0 + 4) // 2 = 2
```

Se il valore cercato è minore del valore centrale, si aggiorna:

```python
destra = centro - 1
```

Se il valore cercato è maggiore del valore centrale, si aggiorna:

```python
sinistra = centro + 1
```

È stato consolidato anche il caso in cui rimane un solo elemento:

```text
sinistra = destra
```

Per questo la condizione corretta è:

```python
while sinistra <= destra:
```

Se invece i limiti si incrociano:

```text
sinistra > destra
```

la ricerca termina e il valore non è presente.

### Stack e heap

Lo stack è associato soprattutto alle chiamate di funzione e al loro stato locale.

Nella ricorsione, le chiamate si accumulano nello stack:

```text
f(3)
f(2)
f(1)
```

e vengono completate in ordine inverso.

Lo heap è associato alla memoria dinamica e a oggetti/dati con durata più flessibile.

### Puntatori

Un puntatore contiene un indirizzo di memoria.

Esempio concettuale:

```text
indirizzo 1000 → valore 10
p → 1000
*p → 10
```

In C/C++:

```cpp
int x = 10;
int *p = &x;
```

Significati:

```text
x   → valore 10
&x  → indirizzo di x
p   → contiene l'indirizzo di x
*p  → valore contenuto all'indirizzo puntato
```

Quindi:

```text
& → ottieni l'indirizzo
* → dereferenzia il puntatore e accedi al valore
```

### Allocazione dinamica

In C++:

```cpp
int *p = new int;
```

`new int` alloca spazio nello heap e restituisce l'indirizzo dello spazio allocato.

Successivamente:

```cpp
*p = 10;
```

scrive il valore 10 nella zona di memoria puntata da `p`.

Per liberare quella memoria:

```cpp
delete p;
```

`delete p` libera la memoria nello heap a cui `p` punta.

Se la memoria allocata dinamicamente non viene liberata quando necessario, si può verificare un memory leak.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Consolidare i casi limite della ricerca binaria.
- Capire perché il ciclo usa `sinistra <= destra`.
- Riconoscere quando una ricerca binaria termina senza trovare il valore.
- Distinguere stack e heap.
- Collegare lo stack alle chiamate di funzione e alla ricorsione.
- Collegare lo heap alla memoria dinamica.
- Capire che un puntatore contiene un indirizzo di memoria.
- Distinguere `p`, `&x` e `*p`.
- Comprendere la dereferenziazione.
- Comprendere a livello introduttivo `new` e `delete`.
- Comprendere il concetto di memory leak.

## ARGOMENTO D'ESAME

**03 — Array, memoria e ricerca**

- ricerca binaria;
- stack;
- heap;
- indirizzi;
- puntatori;
- operatore di indirizzo;
- dereferenziazione;
- allocazione dinamica;
- `new`;
- `delete`;
- memory leak.

## COMPLESSITÀ

```text
ricerca binaria → Theta(log n)
```
