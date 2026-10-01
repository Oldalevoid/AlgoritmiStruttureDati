# Programma canonico del corso — Algoritmi e Strutture Dati

## Scopo

Questo documento è la **fonte canonica del programma** della repository. È una sintesi autonoma del corso e permette a qualunque AI di continuare il percorso senza accesso alle dispense originali.

Usarlo insieme al `README.md`, che contiene lo stato corrente dello studente.

---

# 01 — Fondamenti degli algoritmi

## Problema, istanza, soluzione
- problema: classe generale di situazioni da risolvere;
- istanza: specifico input del problema;
- soluzione: output associato all'istanza.

## Algoritmo
Un algoritmo è una procedura ordinata di istruzioni per risolvere un problema.

Proprietà introduttive:
- finito;
- eseguibile;
- non ambiguo;
- generale;
- deterministico;
- completo.

## Algoritmo vs programma
L'algoritmo è la procedura logica; il programma è una sua implementazione in un linguaggio.

## Schemi fondamentali
- sequenza;
- selezione/condizione;
- iterazione;
- assegnazione.

## Böhm-Jacopini
Comprendere che un algoritmo strutturato può essere costruito combinando sequenza, selezione e iterazione.

## Rappresentazione
### Flowchart
Saper interpretare:
- inizio/fine;
- input/output;
- operazione;
- condizione;
- flusso di controllo.

### Pseudocodice
Deve essere comprensibile, coerente e non ambiguo, senza dipendere da un linguaggio reale.

Progressione:
1. problema in linguaggio naturale;
2. algoritmo informale;
3. pseudocodice;
4. eventuale implementazione.

## Confronto tra algoritmi
Comprendere che più algoritmi possono risolvere lo stesso problema con costi diversi.

## Divide et impera
- divisione in sottoproblemi;
- risoluzione dei sottoproblemi;
- combinazione delle soluzioni;
- ricorsione;
- distinzione dalla programmazione dinamica.

### Criterio di uscita
Saper identificare input/output, scrivere algoritmi semplici e completi, riconoscere difetti, usare sequenza/selezione/iterazione, leggere e scrivere pseudocodice semplice, leggere flowchart e comprendere divide et impera.

---

# 02 — Complessità

## Concetti
- dimensione dell'input `n`;
- operazione elementare;
- funzione di costo `T(n)`;
- costo temporale e, quando pertinente, spaziale.

## Casi
- migliore;
- medio;
- peggiore.

## Notazione asintotica
- `O(...)`: limite superiore;
- `Ω(...)`: limite inferiore;
- `Θ(...)`: limite stretto.

Ordini di crescita da riconoscere:
- costante;
- logaritmico;
- lineare;
- `n log n`;
- quadratico;
- cubico;
- esponenziale quando compare.

## Algoritmi non ricorsivi
Analizzare:
- sequenze;
- cicli semplici;
- cicli annidati;
- condizioni.

## Algoritmi ricorsivi
Comprendere:
- caso base;
- chiamata ricorsiva;
- numero di chiamate;
- semplici relazioni di ricorrenza.

### Criterio di uscita
Saper contare operazioni, ricavare semplici `T(n)`, classificare la crescita e analizzare cicli e ricorsioni elementari.

---

# 03 — Array, memoria e ricerca

## Array
- struttura indicizzata;
- celle contigue;
- elementi omogenei nel modello classico;
- dimensione normalmente fissata;
- indice da 0 nelle implementazioni trattate;
- accesso diretto per indice.

## C++ array vs Python list
- array C++ omogeneo;
- lista Python più flessibile;
- accesso per indice efficiente;
- differenze nella gestione dei limiti.

## Visita
Attraversare tutti gli elementi e riconoscere il costo lineare.

## Memoria in C++
Studiare:
- stack;
- heap;
- indirizzi;
- puntatori;
- operatore di indirizzo;
- dereferenziazione;
- allocazione dinamica;
- `new`;
- `delete`;
- memory leak;
- gestione automatica vs manuale.

## Ricerca
- ricerca sequenziale;
- ricerca binaria;
- prerequisito dell'ordinamento;
- confronto dei costi;
- collegamento della ricerca binaria con la riduzione dello spazio di ricerca.

### Criterio di uscita
Saper distinguere array/lista Python, visitare un array, scrivere ricerca sequenziale, simulare ricerca binaria e spiegare stack/heap/puntatori a livello introduttivo.

---

# 04 — Ordinamenti

## Concetti generali
- ordinamento;
- confronto e scambio;
- stabilità;
- in-place;
- costo temporale;
- costo spaziale.

## Selection Sort
Idea: trovare il minimo nella parte non ordinata e portarlo nella posizione corretta.
- best/average/worst: `Θ(n²)`;
- memoria: `Θ(1)`;
- non stabile nella forma standard;
- in place.

## Insertion Sort
Idea: mantenere una parte iniziale ordinata e inserire progressivamente il nuovo elemento.
- best: `Θ(n)`;
- average/worst: `Θ(n²)`;
- memoria: `Θ(1)`;
- stabile;
- in place.

## Bubble Sort
Idea: confrontare elementi adiacenti e scambiarli.
- best con ottimizzazione: `Θ(n)`;
- average/worst: `Θ(n²)`;
- memoria: `Θ(1)`;
- stabile;
- in place.

## Merge Sort
Idea: dividere, ordinare ricorsivamente e fondere.
- best/average/worst: `Θ(n log n)`;
- memoria: `O(n)`;
- stabile;
- non in place nell'implementazione standard trattata.

## Quick Sort
Idea: pivot, partizionamento, ricorsione.
- best/average: `Θ(n log n)`;
- worst: `O(n²)`;
- non stabile;
- trattato come in place;
- memoria indicata nel materiale del corso come `O(n)`.

## Heap Sort
Idea: usare un heap e mantenere la proprietà di heap.
- `O(n log n)`;
- memoria: `Θ(1)`;
- non stabile;
- in place.

### Confronto obbligatorio
Confrontare Selection, Insertion, Bubble, Merge, Quick e Heap per:
- idea;
- best/average/worst;
- memoria;
- stabilità;
- in-place.

### Criterio di uscita
Per ogni algoritmo: spiegarlo, simularlo, leggere/scrivere pseudocodice, implementarlo quando richiesto, indicarne la complessità e confrontarlo con gli altri.

---

# 05 — Strutture dati lineari

## Struttura dati
Distinguere:
- statica vs dinamica;
- compatta vs sparsa;
- basata o non basata sull'ordinamento;
- lineare vs non lineare.

## Insiemi dinamici
Comprendere inserimento, ricerca e cancellazione.

## Liste
- nodi;
- valore;
- riferimenti;
- lista semplicemente collegata;
- lista doppiamente collegata quando prevista;
- inserimento;
- rimozione;
- ricerca;
- attraversamento.

## Stack / pila
Principio **LIFO**.
Operazioni:
- `push`;
- `pop`;
- `peek`.

## Queue / coda
Principio **FIFO**.
Operazioni:
- `enqueue`;
- `dequeue`;
- `front`.

Comprendere perché una implementazione ingenua con array può causare spostamenti inefficienti.

### Criterio di uscita
Saper distinguere array/lista, manipolare una lista semplice, simulare stack e queue, riconoscere LIFO/FIFO e ragionare sui costi.

---

# 06 — Alberi

## Terminologia
Nodo, arco, radice, padre, figlio, foglia, sottoalbero, cammino, livello/profondità, altezza quando usata, grado.

## Albero binario
Ogni nodo ha al massimo due figli: sinistro e destro.

## Visite
### DFS
- ricorsiva;
- iterativa;
- collegamento con lo stack.

### Albero generico e BFS
- numero variabile di figli;
- visita per livelli;
- uso della coda.

## BST / ABR
Proprietà:
- chiavi a sinistra inferiori;
- chiavi a destra superiori;
- proprietà ricorsiva.

Operazioni:
- ricerca;
- inserimento;
- cancellazione.

## Alberi rosso-neri
Scopo: mantenere il BST sufficientemente bilanciato.
Conoscere:
- nodi rossi/neri;
- radice nera;
- foglie NIL nere;
- vincoli di colorazione;
- relazione tra bilanciamento e prestazioni.

### Criterio di uscita
Saper leggere/disegnare alberi, eseguire DFS/BFS, lavorare con BST e riconoscere le proprietà essenziali di un rosso-nero.

---

# 07 — Grafi

## Concetti
- vertici `V`;
- archi `E`;
- orientato/non orientato;
- ponderato/non ponderato;
- adiacenza;
- grado;
- cammino;
- ciclo;
- connessione.

## Rappresentazioni
### Matrice di adiacenza
- struttura `|V| × |V|`;
- costo in memoria;
- accesso diretto alla presenza di un arco.

### Lista di adiacenza
- per ogni nodo si memorizzano i vicini;
- vantaggiosa sui grafi sparsi.

## BFS
- visita in ampiezza;
- coda;
- livelli/distanze nei grafi non pesati;
- BFS-tree;
- esempio applicativo: numero di Erdős.

## DFS
- visita in profondità;
- ricorsione o stack;
- albero di copertura DFS.

## Ordinamento topologico
- applicabile ai DAG;
- prerequisito: aciclicità;
- interpretazione come ordinamento delle dipendenze;
- collegamento con DFS.

## Componenti connesse
Individuazione tramite visite.

## Cammini minimi
### Principio di Bellman
Comprendere rilassamento e struttura ottima dei cammini.

### Dijkstra
Usare con pesi non negativi/positivi secondo l'impostazione del corso.
Saper:
- inizializzare distanze;
- scegliere progressivamente il nodo;
- rilassare archi;
- ricostruire tramite padri.
Applicazione citata: OSPF.

### Bellman-Ford
- rilassamenti ripetuti;
- pesi negativi;
- costo maggiore rispetto a Dijkstra;
- cicli negativi quando introdotti.

### Cammini minimi in DAG
Collegare ordinamento topologico e rilassamento.

### Criterio di uscita
Saper rappresentare grafi, convertire lista/matrice, simulare BFS/DFS, produrre ordinamento topologico, trovare componenti ed eseguire Dijkstra/Bellman-Ford su piccoli grafi.

---

# 08 — Hashing

## Dizionario
Associazione chiave → valore/dato satellite.
Operazioni:
- lookup;
- inserimento;
- cancellazione.

## Tabella hash
Una funzione hash trasforma una chiave in un indice.

## Collisioni
Chiavi differenti possono produrre lo stesso slot.

## Chaining
- lista di trabocco per slot;
- fattore di carico;
- impatto della lunghezza delle catene.

## Indirizzamento aperto
Tecniche del corso:
- probing lineare;
- probing quadratico;
- doppio hashing/probing doppio.

Comprendere:
- ricerca di slot alternativi;
- clustering;
- fattore di carico e prestazioni.

## Hash vs hash crittografico
Distinguere hashing per strutture dati e hashing crittografico.

## Python
Il `dict` è un esempio pratico di struttura basata su hashing.

### Criterio di uscita
Saper individuare collisioni, simulare chaining/probing, interpretare il fattore di carico e distinguere hashing strutturale da crittografico.

---

# 09 — Programmazione dinamica

## Idea
Applicare quando i sottoproblemi si sovrappongono e conviene memorizzare risultati già calcolati.

## Concetti
- sottoproblemi sovrapposti;
- struttura ottima;
- memoization;
- tabella delle soluzioni;
- top-down con memoria;
- bottom-up.

## Processo
1. caratterizzare la soluzione ottima;
2. definire i sottoproblemi;
3. evitare ricalcoli;
4. memorizzare risultati;
5. ricostruire eventualmente la soluzione.

## Problemi del corso
- domino;
- Fibonacci;
- Hateville;
- problema dello zaino.

### Criterio di uscita
Riconoscere sottoproblemi ripetuti, usare memoization e bottom-up, risolvere piccole istanze dei problemi del corso e confrontare dinamica con divide et impera.

---

# 10 — Greedy e Backtracking

## Greedy
Costruire progressivamente una soluzione scegliendo ogni volta una opzione localmente conveniente.

Concetti:
- scelta locale;
- obiettivo globale;
- sottostruttura ottima;
- una scelta greedy non è automaticamente ottima per ogni problema.

Problemi del corso:
- insieme indipendente massimale di intervalli;
- problema del resto.

Confrontare greedy e programmazione dinamica.

## Backtracking
Costruire una soluzione per tentativi:
1. fare una scelta;
2. verificare i vincoli;
3. se fallisce, annullare;
4. provare un'alternativa.

Concetti:
- albero decisionale;
- soluzione parziale;
- vincoli;
- ricorsione;
- potatura.

Problemi del corso:
- gioco del 15;
- otto regine;
- Sudoku.

### Criterio di uscita
Riconoscere strategie greedy, comprenderne i limiti, costruire piccoli alberi di backtracking e risolvere versioni ridotte di problemi a vincoli.

---

# 11 — Algoritmi probabilistici

## Obiettivo
Comprendere algoritmi che introducono casualità nel processo di calcolo.

## Monte Carlo
- tempo/costo controllabile;
- il risultato può avere probabilità di errore o essere approssimato.

## Las Vegas
- risultato corretto;
- tempo di esecuzione influenzato dalle scelte casuali.

## Quick Sort randomizzato
Collegare la scelta casuale del pivot alla riduzione della dipendenza da configurazioni sfavorevoli sistematiche.

## Selezione del mediano
Studiare il problema di selezione collegato alla randomizzazione.

### Criterio di uscita
Distinguere deterministico/probabilistico, Monte Carlo/Las Vegas e collegare randomizzazione a Quick Sort e selezione.

---

# Ordine didattico obbligatorio

1. Fondamenti
2. Complessità
3. Array, memoria e ricerca
4. Ordinamenti
5. Strutture lineari
6. Alberi
7. Grafi
8. Hashing
9. Programmazione dinamica
10. Greedy e Backtracking
11. Algoritmi probabilistici

# Tipi di esercizio da alternare

Quando pertinente:
1. riconoscimento concettuale;
2. esecuzione manuale;
3. correzione di algoritmo errato;
4. scrittura informale;
5. pseudocodice;
6. implementazione;
7. analisi della complessità;
8. confronto tra alternative;
9. domanda in stile esame.

Un modulo non va considerato acquisito soltanto perché lo studente ha risposto a una domanda teorica.

# Regola sui contenuti esterni

Questo documento definisce il perimetro del corso. Conoscenze esterne possono essere usate per spiegare meglio, ma:
- non devono sostituire il syllabus;
- non vanno presentate come se facessero parte del corso;
- eventuali approfondimenti vanno indicati come tali;
- gli esercizi principali devono restare centrati sugli argomenti qui elencati.
