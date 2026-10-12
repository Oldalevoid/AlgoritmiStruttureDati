# Grafi — appunti ordinati

## 1. Definizione
Un grafo è una coppia **G=(V,E)** con V insieme dei vertici (nodi) ed E insieme degli archi (collegamenti). Esempio: una rete informatica, con computer come vertici e connessioni come archi.

In un grafo **non orientato**, l'arco {A,B} consente di muoversi in entrambi i versi. In uno **orientato**, A→B non implica B→A: utile per strade a senso unico.

## 2. Grado
- Non orientato: grado deg(v) = numero di archi incidenti a v (un cappio conta due volte).
- Orientato: grado entrante deg⁻(v) = numero di archi che arrivano; grado uscente deg⁺(v) = numero di archi che partono.

Esempio: A→B, C→B, D→B, B→C: deg⁻(B)=3 e deg⁺(B)=1.

## 3. Cammini e cicli
Un cammino percorre una sequenza di archi adiacenti; nei grafi orientati ne rispetta il verso. La **lunghezza** di un cammino non pesato è il numero di archi. Un *cammino semplice* non ripete vertici.

Con A→B, B→C, B→D, C→D, i due cammini semplici da A a D sono A→B→D (lunghezza 2) e A→B→C→D (lunghezza 3).

Un **ciclo diretto** torna al vertice di partenza rispettando le frecce (senza ripetere altri vertici). A→B→C→A è un ciclo; eliminando C→A, nel grafo considerato non rimangono cicli. Un grafo diretto aciclico è detto **DAG**.

## 4. Grafi pesati
A ogni arco è associato un peso: distanza, tempo, costo, latenza. Se A—B pesa 10, A—C pesa 4 e C—B pesa 3, passare da C costa 4+3=7, inferiore all'arco diretto di peso 10. Il problema del **cammino minimo** sarà studiato formalmente più avanti (Dijkstra funziona con pesi non negativi).

## 5. Rappresentazioni

### Lista di adiacenza
Ogni vertice contiene i suoi vicini.

```python
grafo = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A"],
}
print(grafo["B"])  # ['A', 'C']
```

Memoria: **O(V+E)** per grafi rappresentati con le liste dei vicini (nel caso non orientato ogni arco compare in due liste).

### Matrice di adiacenza
Una matrice V×V con 1 se un arco esiste e 0 altrimenti. Per gli archi non orientati A—B e B—C, nell'ordine A,B,C:

|   | A | B | C |
|---|---|---|---|
| A | 0 | 1 | 0 |
| B | 1 | 0 | 1 |
| C | 0 | 1 | 0 |

```python
matrice = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
print(matrice[0][2])  # 0: nessun arco diretto A—C
```

Memoria: **O(V²)**, anche se quasi tutti i valori sono zero. Verificare un arco con accesso alla cella richiede O(1), mentre la ricerca di un vicino in una lista tradizionale richiede tempo proporzionale al numero dei vicini, salvo strutture ausiliarie.

## 6. Sparsi e densi
- **Sparso**: relativamente pochi archi rispetto a quelli possibili; generalmente conveniente una lista di adiacenza.
- **Denso**: molti archi rispetto a quelli possibili; una matrice può essere vantaggiosa per i test rapidi di adiacenza.

In un grafo semplice non orientato il massimo è **V(V−1)/2**. Con 100 vertici il massimo è 4.950; 120 archi corrispondono a circa il 2,42%, un grafo sparso. Non esiste una soglia percentuale universale.

Con 10.000 vertici, una matrice contiene 100.000.000 celle, mentre la lista di adiacenza registra solo vertici e archi effettivi (es. 15.000 archi). La quantità di byte dipende dall'implementazione concreta.

## 7. BFS e DFS — solo introduzione
- **BFS**, visita in ampiezza: esplora prima i vertici alla minima distanza in numero di archi dalla sorgente. Tipicamente usa una **coda FIFO**.
- **DFS**, visita in profondità: segue un ramo finché possibile, poi torna indietro. Tipicamente usa ricorsione o una **pila**.

BFS è stata introdotta con l'esempio A–B, A–C, B–D, B–E, C–F. Non è ancora stata eseguita autonomamente una visita completa; non segnare BFS come acquisita.

## Checklist
- [x] Definizioni, gradi, orientamento, cammini, cicli e DAG
- [x] Pesi e confronto di cammini
- [x] Liste vs matrici e grafi sparsi vs densi
- [ ] BFS manuale e coda
- [ ] BFS in Python
- [ ] DFS e confronti
- [ ] Algoritmi avanzati del modulo
