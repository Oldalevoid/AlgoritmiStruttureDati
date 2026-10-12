# Esercizi guidati — sessione 12/10/2026

## DESCRIZIONE
Domande di comprensione sui grafi. Di seguito sono riportate **le risposte date dallo studente**, con l'esito effettivo. Non si dichiarano svolti esercizi non ancora risolti.

| N. | Tema | Risposta dello studente / esito |
|---|---|---|
| 1 | Vicini di B | «3 archi ... C A e D» — corretta |
| 2 | Grado di D | 3 — corretta |
| 3 | Strade a senso unico | Grafo orientato — corretta |
| 4 | Gradi di B | Entrante 3, uscente 1 — corretta |
| 5 | Cammini A→D | A→B→D, A→B→C→D — corretta |
| 6 | Eliminazione C→A | Nessun ciclo residuo — corretta nell'esempio |
| 7 | Cammino minimo semplice | Passare per C costa 7 anziché 10 — corretta |
| 8 | `grafo["B"]` | `['A', 'C']` — corretta |
| 9 | `matrice[0][2]` | 0 — corretta; indica assenza di arco A—C |
| 10 | Memoria, 1.000 vertici e pochi vicini | «Matrice di adiacenza» — **errata**; chiarita la convenienza delle liste |
| 11 | 100 vertici e 120 archi | «Grafo sparso perché ha pochi archi rispetto a quelli possibili» — corretta |
| 12 | 10.000 vertici e 15.000 archi | «Lista di adiacenza perché rappresenta solamente gli effettivi collegamenti» — corretta |
| 13 | Ordine BFS da A | **Non ancora risposto** |

## COSA HO IMPARATO IN QUESTO ESERCIZIO
Definizioni di grafo, archi e vertici; differenza tra orientati e non orientati; gradi entrante/uscente; cammini, cicli, DAG; pesi; accessi a liste e matrici di adiacenza; grafi sparsi/densi e uso della memoria. Iniziale errore sulla scelta della rappresentazione corretto nelle due verifiche successive.

## ARGOMENTO D'ESAME
Grafi: terminologia e rappresentazioni; preliminari a BFS e DFS.

## COMPLESSITÀ
Matrice O(V²) spazio; lista O(V+E) spazio.

## PROSSIMA DOMANDA (aperta)
Nel grafo non orientato con archi A—B, A—C, B—D, B—E, C—F, esegui BFS partendo da A e visitando i vicini **da sinistra verso destra**. Indica l'ordine completo dei vertici. Non anticipare la risposta: chiedere allo studente di eseguirla.
