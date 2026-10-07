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
7. usare **Python come unico linguaggio pratico di accompagnamento** al corso, introducendo progressivamente anche la sintassi Python necessaria;
8. usare Python per implementare gli stessi concetti algoritmici affrontati nel programma universitario, senza trasformare il percorso in un corso di programmazione separato;
9. non introdurre C o C++ come secondo percorso parallelo, salvo futura richiesta esplicita dello studente o necessità strettamente legata al programma;
10. non sostituire con Python un esercizio che richiede esplicitamente pseudocodice;
11. mantenere terminologia, perimetro e progressione definiti in `PROGRAMMA_CORSO.md`;
12. leggere e rispettare `GUIDA_AI.md`;
13. non chiedere le dispense originali per poter proseguire il percorso;
14. al completamento di ogni esercizio, **pusharlo automaticamente** e aggiornare contestualmente questo README.

## Tipi di esercizio

Non tutti gli esercizi devono essere file Python.

Possono essere utilizzati:

- `.md` → teoria, esecuzioni manuali, pseudocodice, complessità, confronti e domande d'esame;
- `.py` → implementazioni in Python collegate direttamente agli argomenti del corso.

C e C++ non fanno parte del percorso pratico corrente e non devono essere introdotti automaticamente.

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

Da questo punto il percorso ha anche un secondo obiettivo pratico: **rafforzare progressivamente Python attraverso gli stessi esercizi di Algoritmi e Strutture Dati**. Python deve restare uno strumento al servizio del corso universitario: teoria, pseudocodice, correttezza e complessità rimangono prioritari. La sintassi Python va introdotta solo quando serve a implementare i concetti del programma, evitando un secondo percorso separato di programmazione.

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

**Ultimo esercizio completato: `03_array_memoria_ricerca/esercizio_04.py`**

Argomento corrente:

**03 — Array, memoria e ricerca**

Stato dei moduli precedenti:

**01 — Fondamenti degli algoritmi: completato.**

**02 — Complessità: completato.**

Concetti acquisiti nel modulo 01:

- distinzione tra problema generale, istanza e soluzione;
- distinzione tra algoritmo e programma;
- distinzione tra input e output;
- algoritmo come sequenza ordinata, finita e non ambigua di istruzioni;
- proprietà fondamentali di un algoritmo: finito, eseguibile, non ambiguo, generale, deterministico e completo;
- riconoscimento di difetti e proprietà violate;
- uso di sequenza, selezione, iterazione e assegnazione;
- comprensione del principio di Böhm-Jacopini a livello introduttivo;
- scrittura e lettura di pseudocodice semplice;
- lettura e costruzione di flowchart;
- esecuzione manuale di pseudocodice con cicli e condizioni;
- tracciamento delle variabili durante l'esecuzione;
- confronto tra algoritmi diversi che risolvono lo stesso problema;
- comprensione del principio divide et impera;
- riconoscimento delle fasi dividere, risolvere e combinare;
- distinzione tra decomposizione top-down e ricomposizione bottom-up.

Concetti acquisiti finora nel modulo 02:

- `n` come dimensione dell'input;
- scelta di un'operazione elementare da contare;
- significato della funzione di costo `T(n)`;
- calcolo di un caso concreto, ad esempio `T(5) = 5`;
- passaggio dal caso concreto alla forma generale `T(n) = n`;
- distinzione tra costo temporale `T(n)` e costo spaziale `S(n)`;
- riconoscimento di spazio aggiuntivo costante quando il numero di variabili non cresce con `n`;
- riconoscimento di spazio crescente quando viene creata una struttura di dimensione `n`;
- confronto tra algoritmi con stesso costo temporale ma diverso costo spaziale;
- conteggio di più operazioni elementari nello stesso algoritmo;
- costruzione di funzioni di costo come `T(n) = 3n`, `T(n) = 2n + 1` e `T(n) = 3n + 3`;
- distinzione tra termini che dipendono da `n` e termini costanti;
- distinzione tra caso migliore, medio e peggiore;
- analisi dei tre casi nella ricerca lineare;
- riconoscimento del caso migliore come costo costante;
- riconoscimento del caso medio e peggiore come crescita lineare;
- comprensione introduttiva del fatto che fattori costanti come `1/2` non cambiano l'ordine di crescita;
- distinzione operativa tra `O`, `Ω` e `Θ`;
- riconoscimento di `Θ(n)` come ordine stretto per funzioni lineari come `5n + 10`;
- riconoscimento di cicli lineari `Θ(n)`;
- riconoscimento di cicli con indice moltiplicato per 2 come `Θ(log n)`;
- riconoscimento di due cicli completi annidati come `Θ(n²)`;
- riconoscimento di cicli annidati con crescita mista `Θ(n log n)`;
- esperienza introduttiva pregressa con un semplice ciclo `for` in C, utile solo come confronto storico;
- decisione successiva di usare **Python come unico linguaggio pratico** per evitare confusione tra più linguaggi mentre si studiano gli algoritmi;
- riconoscimento in Python di cicli `Theta(n)`, `Theta(log n)` e `Theta(n^2)`;
- scrittura autonoma di un ciclo `while` logaritmico con `i *= 2`;
- distinzione tra `n/2` iterazioni, che restano lineari, e dimezzamento ripetuto, che è logaritmico;
- analisi di cicli annidati con limiti `n // 2` e `n` come `Theta(n^2)`;
- ordinamento corretto delle classi `Theta(1)`, `Theta(log n)`, `Theta(n)`, `Theta(n log n)` e `Theta(n^2)`;
- riconoscimento della crescita esponenziale `Theta(2^n)` come peggiore della crescita quadratica;
- comprensione introduttiva della ricorsione come funzione che richiama sé stessa;
- riconoscimento del caso base e della chiamata ricorsiva;
- comprensione della pila delle chiamate: una chiamata resta in pausa mentre viene eseguita quella successiva e riprende al ritorno;
- riconoscimento di `T(n) = T(n - 1) + 1` come `Theta(n)`;
- riconoscimento di `T(n) = T(n / 2) + 1` come `Theta(log n)`;
- comprensione introduttiva di `T(n) = 2T(n - 1) + 1` come crescita esponenziale `Theta(2^n)`;
- consolidamento della pila delle chiamate e della distinzione tra discesa e risalita;
- comprensione del fatto che, in risalita, vengono eseguite solo le istruzioni poste dopo la chiamata ricorsiva;
- riconoscimento autonomo di ricorsioni `Theta(n)`, `Theta(log n)` e `Theta(2^n)`;
- distinzione tra numero di livelli ricorsivi e costo del lavoro svolto a ogni livello;
- comprensione della somma geometrica `n + n/2 + n/4 + ...` come `Theta(n)`;
- riconoscimento della somma `n + (n-1) + ... + 1` come `Theta(n^2)`;
- consolidamento della differenza tra cicli in sequenza, i cui costi si sommano, e cicli annidati, i cui costi spesso si moltiplicano;
- verifica mista superata sui concetti fondamentali del modulo 02;
- riconoscimento del termine dominante in funzioni come `7n^2 + 3n + 20`, `4n + 100` e `3n log n + 5n`;
- ordinamento corretto delle principali classi: `Theta(1) < Theta(log n) < Theta(n) < Theta(n log n) < Theta(n^2) < Theta(2^n)`.

Concetti acquisiti finora nel modulo 03:

- consolidare il confronto tra diversi ordini di crescita;
- consolidare il confronto tra `Θ(n)`, `Θ(log n)`, `Θ(n log n)` e `Θ(n²)`;
- accesso tramite indice in una lista Python come operazione `Theta(1)`;
- visita completa di una lista come operazione `Theta(n)`;
- ricerca del massimo tramite scansione lineare come `Theta(n)`;
- introduzione alla ricerca lineare;
- riconoscimento del caso migliore `Theta(1)` e del caso peggiore `Theta(n)` nella ricerca lineare;
- distinzione tra array classico e lista Python;
- comprensione della maggiore flessibilità della lista Python rispetto all'array classico;
- consolidamento della differenza tra accesso diretto tramite indice e ricerca sequenziale di un valore;
- comprensione del requisito dell'ordinamento per la ricerca binaria;
- simulazione manuale della ricerca binaria scegliendo la metà sinistra o destra;
- riconoscimento della ricerca binaria come `Theta(log n)`;
- confronto tra ricerca lineare `Theta(n)` nel caso peggiore e ricerca binaria `Theta(log n)`;
- implementazione autonoma in Python di una ricerca lineare;
- comprensione della differenza tra valore e indice in un ciclo `for`;
- implementazione guidata e poi corretta autonomamente della ricerca binaria con `sinistra`, `destra` e `centro`;
- comprensione del ricalcolo del centro a ogni iterazione e dell'aggiornamento dei confini di ricerca.

Concetti da acquisire o consolidare nel modulo 03:

- consolidare ulteriormente la ricerca binaria con esecuzione manuale e casi limite;
- introdurre memoria, stack, heap e puntatori a livello previsto dal corso;
- collegare accesso, visita e ricerca alle rispettive complessità.
- consolidare la traduzione degli algoritmi in Python;
- usare Python per esercitare cicli, condizioni, funzioni e strutture dati solo quando collegati agli argomenti del corso.

Punti emersi da ricordare:

- l'istanza è lo specifico input del problema, non un'operazione effettuata su quell'input;
- nelle condizioni e nei flowchart va mantenuto con precisione il verso dei confronti;
- nei cicli va rispettato l'ordine tra operazione, aggiornamento della variabile e nuova verifica;
- nella complessità bisogna dichiarare chiaramente quale operazione elementare si sta contando;
- un ciclo annidato non è automaticamente quadratico: bisogna analizzare quante iterazioni compie ciascun ciclo;
- distinguere con attenzione i simboli `O`, `Ω` e `Θ`;
- nella ricorsione, ricordare che una chiamata precedente non scompare: resta sospesa e riprende dopo il ritorno della chiamata più interna.

Prossimo esercizio da proporre:

**03_array_memoria_ricerca/esercizio_05.md — Consolidare la ricerca binaria con casi limite e introdurre il collegamento con la memoria.**

Cartella corrente:

`03_array_memoria_ricerca/`

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

