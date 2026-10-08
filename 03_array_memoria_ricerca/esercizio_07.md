# Esercizio 07 — Verifica mista del modulo 03

## DESCRIZIONE

Verifica sui concetti principali del modulo 03:
- accesso tramite indice;
- ricerca lineare;
- ricerca binaria;
- stack e heap;
- puntatori;
- indirizzi di memoria;
- dereferenziazione;
- memory leak.

## SVOLGIMENTO

### Ricerca binaria su 256 elementi

```text
2^8 = 256
```

Quindi una ricerca binaria richiede circa 8 dimezzamenti nel caso peggiore:

```text
Theta(log n)
```

### Ricerca lineare

Su 256 elementi, nel caso peggiore possono servire fino a 256 confronti.

In forma asintotica:

```text
Theta(n)
```

### Accesso diretto

Se l'indice è già noto, ad esempio:

```python
lista[200]
```

l'accesso è:

```text
Theta(1)
```

### Stack e heap

Le chiamate ricorsive usano principalmente lo stack delle chiamate.

L'allocazione dinamica con `new` in C++ usa principalmente lo heap.

### Puntatori

Se `p` contiene l'indirizzo di `x`:

```text
p   → indirizzo di x
*p  → valore contenuto all'indirizzo di x
&x  → indirizzo di memoria di x
```

### Memory leak

Se memoria allocata nello heap non viene correttamente liberata, si verifica un:

```text
memory leak
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Consolidare la complessità della ricerca lineare e binaria.
- Riconoscere l'accesso diretto come `Theta(1)`.
- Distinguere stack e heap.
- Collegare ricorsione allo stack.
- Collegare allocazione dinamica allo heap.
- Distinguere `p`, `*p` e `&x`.
- Riconoscere il concetto di memory leak.

## ARGOMENTO D'ESAME

**03 — Array, memoria e ricerca**

- array/lista;
- accesso tramite indice;
- ricerca sequenziale;
- ricerca binaria;
- stack;
- heap;
- puntatori;
- indirizzi;
- dereferenziazione;
- memory leak.

## COMPLESSITÀ

```text
accesso per indice      → Theta(1)
ricerca lineare worst   → Theta(n)
ricerca binaria         → Theta(log n)
```
