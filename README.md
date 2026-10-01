# Algoritmi e Strutture Dati — Percorso di preparazione all'esame

Questa repository raccoglie un percorso di esercizi progressivi per preparare l'esame di **Algoritmi e Strutture Dati**.

La repository è progettata per essere **completamente autosufficiente**: qualsiasi modello AI deve poter aprirla e continuare il percorso senza avere accesso alle dispense originali, a chat precedenti o a memoria esterna.

Documenti fondamentali:

- [PROGRAMMA_CORSO.md](PROGRAMMA_CORSO.md) — curriculum dettagliato e perimetro degli argomenti;
- [GUIDA_AI.md](GUIDA_AI.md) — regole operative per continuare il percorso;
- questo `README.md` — stato vivo dello studente, progressi e prossimo esercizio.

Le dispense originali non sono necessarie per continuare gli esercizi.

## Obiettivo

L'obiettivo non è soltanto imparare a programmare gli algoritmi, ma saper:

- comprendere il problema risolto da un algoritmo;
- eseguire manualmente l'algoritmo su piccoli input;
- leggere e scrivere pseudocodice;
- tradurre un algoritmo in codice quando utile;
- riconoscere le strutture dati coinvolte;
- analizzare il costo temporale e spaziale;
- distinguere caso ottimo, medio e pessimo quando rilevante;
- usare correttamente la notazione asintotica;
- confrontare algoritmi diversi che risolvono lo stesso problema;
- rispondere a domande concettuali simili a quelle d'esame.

## Metodo didattico

Gli esercizi devono essere **progressivi** e introdurre pochi concetti nuovi alla volta.

L'AI che utilizza questa repository come contesto deve:

1. controllare sempre l'ultimo esercizio completato e il livello raggiunto;
2. non presumere che un argomento sia acquisito solo perché compare nelle dispense;
3. spiegare prima la nuova idea necessaria all'esercizio;
4. lasciare allo studente il compito di scrivere la soluzione;
5. in caso di errore, indicare cosa non funziona e guidare il ragionamento senza fornire immediatamente la soluzione completa, salvo richiesta esplicita;
6. alternare esercizi teorici, esecuzioni manuali, pseudocodice, analisi di complessità e implementazioni;
7. usare **Python** come linguaggio principale per le implementazioni quando il linguaggio non è parte dell'oggetto dell'esercizio;
8. usare **C/C++** quando l'argomento del corso richiede esplicitamente aspetti come memoria, puntatori o una specifica implementazione;
9. non sostituire con Python un esercizio che richiede esplicitamente pseudocodice;
10. mantenere terminologia, perimetro e progressione definiti in `PROGRAMMA_CORSO.md`;
11. leggere e rispettare `GUIDA_AI.md`;
12. non chiedere le dispense originali per poter proseguire il percorso.

## Tipi di esercizio

Non tutti gli esercizi devono essere file Python.

Possono essere utilizzati:

- `.md` → teoria, esecuzioni manuali, pseudocodice, complessità, confronti e domande d'esame;
- `.py` → implementazioni in Python;
- `.cpp` → esercizi in C++ quando utili o richiesti dall'argomento.

Quando ha senso, uno stesso argomento può essere affrontato in più passaggi:

1. intuizione;
2. simulazione manuale;
3. pseudocodice;
4. implementazione;
5. analisi della complessità;
6. confronto con algoritmi alternativi.

## Struttura del percorso

```text
01_fondamenti_algoritmi/
02_complessita/
03_array_memoria_ricerca/
04_ordinamenti/
05_strutture_lineari/
06_alberi/
07_grafi/
08_hashing/
09_programmazione_dinamica/
10_greedy_backtracking/
11_algoritmi_probabilistici/
```

### 01 — Fondamenti degli algoritmi

Argomenti di riferimento:

- introduzione agli algoritmi;
- algoritmo vs programma;
- rappresentazione di un algoritmo;
- flowchart;
- pseudocodice;
- confronto tra algoritmi che risolvono lo stesso problema;
- divide et impera.

### 02 — Complessità

Argomenti di riferimento:

- costo di un algoritmo;
- passi base;
- dimensione dell'input;
- caso ottimo, medio e pessimo;
- notazione asintotica;
- O grande, Omega e Theta;
- complessità degli algoritmi non ricorsivi;
- complessità degli algoritmi ricorsivi.

### 03 — Array, memoria e ricerca

Argomenti di riferimento:

- array;
- accesso tramite indice;
- visita di un array;
- confronto tra array C++ e liste Python;
- gestione della memoria in C++;
- problema della ricerca;
- algoritmi di ricerca e relativa complessità.

### 04 — Ordinamenti

Argomenti di riferimento:

- problema dell'ordinamento;
- stabilità;
- algoritmi in place;
- Selection Sort;
- Insertion Sort;
- Bubble Sort;
- Merge Sort;
- Quick Sort;
- Heap Sort;
- confronto fra complessità temporali e spaziali.

### 05 — Strutture dati lineari

Argomenti di riferimento:

- strutture dati;
- insiemi dinamici;
- puntatori;
- liste;
- stack/pila e principio LIFO;
- queue/coda e principio FIFO;
- operazioni e complessità.

### 06 — Alberi

Argomenti di riferimento:

- alberi e loro proprietà;
- alberi binari;
- DFS ricorsiva e iterativa;
- alberi generici;
- BFS;
- alberi binari di ricerca (BST/ABR);
- ricerca, inserimento e cancellazione;
- alberi rosso-neri.

### 07 — Grafi

Argomenti di riferimento:

- definizione e terminologia dei grafi;
- lista e matrice di adiacenza;
- implementazione;
- BFS;
- DFS;
- alberi di copertura;
- ordinamento topologico;
- componenti connesse;
- cammini minimi;
- teorema di Bellman;
- Dijkstra;
- Bellman-Ford;
- cammini minimi in DAG.

### 08 — Hashing

Argomenti di riferimento:

- dizionari;
- tabelle hash;
- funzioni hash;
- collisioni;
- tecniche di risoluzione delle collisioni;
- differenza fra hashing per strutture dati e hash crittografico;
- complessità delle operazioni.

### 09 — Programmazione dinamica

Argomenti di riferimento:

- sottoproblemi sovrapposti;
- memoization;
- approccio bottom-up;
- confronto con divide et impera;
- problema del domino;
- Fibonacci;
- Hateville;
- problema dello zaino.

### 10 — Greedy e Backtracking

Argomenti di riferimento:

- algoritmi greedy;
- problemi di ottimizzazione;
- scelte localmente ottime;
- insieme indipendente massimale;
- problema del resto;
- backtracking;
- alberi decisionali;
- gioco del 15;
- otto regine;
- Sudoku.

### 11 — Algoritmi probabilistici

Argomenti di riferimento:

- algoritmi deterministici e probabilistici;
- algoritmi Monte Carlo;
- algoritmi Las Vegas;
- randomizzazione;
- Quick Sort randomizzato;
- selezione del mediano.

## Stato iniziale dello studente

Lo studente sta già imparando Python attraverso una repository separata di esercizi progressivi e possiede le basi del linguaggio necessarie per iniziare semplici implementazioni.

Per questa materia, tuttavia, il percorso deve partire dai **fondamenti algoritmici**: non bisogna confondere la capacità di scrivere semplici programmi Python con la padronanza di algoritmi, strutture dati e analisi della complessità.

## Formato dei file completati

Ogni esercizio completato deve indicare chiaramente:

- **DESCRIZIONE** — cosa fa o cosa richiede l'esercizio;
- **COSA HO IMPARATO IN QUESTO ESERCIZIO** — solo ciò che è stato appreso o consolidato in quell'esercizio;
- **ARGOMENTO D'ESAME** — a quale parte del corso si collega;
- **COMPLESSITÀ** — quando pertinente, indicare il risultato dell'analisi svolta dallo studente.

Per i file di codice queste informazioni possono essere commenti iniziali.  
Per i file Markdown possono essere sezioni del documento.

## Regola di sincronizzazione a ogni push

Ogni volta che viene completato e pushato un esercizio, l'AI deve aggiornare anche questo README.

L'aggiornamento deve mantenere sincronizzati almeno:

- **ultimo esercizio completato**;
- **prossimo esercizio da proporre**;
- cartella/argomento corrente;
- concetti già acquisiti;
- eventuali concetti ancora deboli emersi durante gli esercizi;
- livello attuale dello studente, solo quando cambia in modo significativo.

Il push dell'esercizio e l'aggiornamento del README fanno parte della stessa fase di completamento.

## Punto attuale del percorso

**Ultimo esercizio completato: `01_fondamenti_algoritmi/esercizio_05.md`**

Argomento corrente:

**Fondamenti degli algoritmi**

Concetti acquisiti finora:

- distinzione tra input e output;
- algoritmo come sequenza ordinata di istruzioni;
- necessità di istruzioni non ambigue;
- completezza dell'algoritmo rispetto ai casi possibili;
- uso logico di condizioni alternative per distinguere casi diversi;
- proprietà fondamentali di un algoritmo: finito, eseguibile, non ambiguo, generale, deterministico e completo;
- riconoscimento della proprietà violata in esempi concreti;
- riconoscimento degli schemi di sequenza, selezione e iterazione;
- comprensione del fatto che più schemi possono essere combinati e annidati nello stesso algoritmo;
- scrittura autonoma di un algoritmo che combina sequenza, selezione e iterazione;
- descrizione esplicita di un ciclo con un numero definito di ripetizioni;
- traduzione di un algoritmo informale in pseudocodice;
- uso corretto della struttura `SE / ALTRIMENTI SE / ALTRIMENTI`;
- distinzione tra richiesta all'utente, lettura dell'input e produzione dell'output;
- rispetto dell'output richiesto dalla consegna.

Concetti da consolidare nei prossimi esercizi:

- distinzione rapida tra le diverse proprietà formali di un algoritmo;
- precisione formale nella descrizione di input, output e istruzioni;
- lettura ed esecuzione mentale di pseudocodice;
- rappresentazione tramite flowchart.

Prossimo esercizio da proporre:

**Esercizio 06 — Leggere ed eseguire mentalmente un semplice pseudocodice.**

Cartella corrente:

`01_fondamenti_algoritmi/`

## Autosufficienza della repository

Una nuova AI deve poter capire, usando soltanto questa repository:

- il programma specifico dell'esame;
- l'ordine degli argomenti;
- il livello di profondità atteso;
- il metodo con cui proporre gli esercizi;
- cosa è già stato studiato;
- cosa è ancora da consolidare;
- quale esercizio proporre dopo.

Il curriculum stabile è in `PROGRAMMA_CORSO.md`.  
Le regole operative sono in `GUIDA_AI.md`.  
Questo README contiene lo stato aggiornato del percorso.

## Principio guida

La repository è la memoria didattica permanente del percorso: qualsiasi AI che la analizzi deve poter capire **cosa è stato studiato, cosa è stato realmente esercitato, quali difficoltà sono emerse e da quale punto deve continuare**, senza richiedere le dispense originali.
