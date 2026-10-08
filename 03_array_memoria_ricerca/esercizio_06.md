# Esercizio 06 — Consolidamento di stack, heap e puntatori

## DESCRIZIONE

L'esercizio consolida i concetti di stack, heap, puntatori, indirizzi di memoria, dereferenziazione, allocazione dinamica e memory leak.

## SVOLGIMENTO

### Stack e heap

Lo stack è associato soprattutto a:
- chiamate di funzione;
- stato locale delle funzioni;
- ricorsione;
- comportamento LIFO.

Lo heap è associato soprattutto a:
- memoria dinamica;
- oggetti e dati allocati durante l'esecuzione;
- allocazione e liberazione esplicita della memoria nei linguaggi come C++.

### Puntatori

Se una variabile `x` contiene un valore:

```text
x = 25
```

e un puntatore `p` contiene il suo indirizzo:

```text
p = indirizzo di x
```

allora:

```text
p   → indirizzo
*p  → valore contenuto a quell'indirizzo
&x  → indirizzo di x
```

È stato consolidato che:

```text
p = &y
```

cambia il punto a cui `p` fa riferimento, mentre:

```text
*p = 50
```

cambia il valore memorizzato nell'area puntata.

Esempio:

```text
x = 10
y = 20
p punta a x
p viene poi fatto puntare a y
*p = 50
```

Risultato:

```text
x = 10
y = 50
*p = 50
```

### Allocazione dinamica

A livello concettuale:

```text
new     → richiede memoria nello heap
delete  → libera la memoria
```

Dopo che una zona di memoria è stata liberata, non va più usato il vecchio puntatore per leggere o scrivere quel contenuto.

### Memory leak

Un memory leak si verifica quando memoria allocata dinamicamente non viene correttamente liberata e resta inutilmente occupata.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Distinguere stack e heap.
- Collegare lo stack alle chiamate di funzione e alla ricorsione.
- Collegare lo heap alla memoria dinamica.
- Capire che `p` contiene un indirizzo.
- Capire che `*p` accede al valore memorizzato all'indirizzo puntato.
- Capire che `&x` rappresenta l'indirizzo di memoria di `x`.
- Distinguere il cambio del puntatore dal cambio del valore puntato.
- Comprendere il significato concettuale di `new` e `delete`.
- Riconoscere il concetto di memory leak.

## ARGOMENTO D'ESAME

**03 — Array, memoria e ricerca**

- stack;
- heap;
- indirizzi;
- puntatori;
- dereferenziazione;
- allocazione dinamica;
- new;
- delete;
- memory leak.

## COMPLESSITÀ

Non è il focus principale dell'esercizio.
