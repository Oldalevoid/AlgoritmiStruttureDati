# Guida operativa per qualunque AI

## Scopo

Questa repository deve essere utilizzabile senza accesso a chat precedenti, memoria personale o dispense esterne.

## Cosa leggere prima di continuare

1. `README.md`
2. `PROGRAMMA_CORSO.md`
3. l'ultimo esercizio completato indicato nel README
4. se utile, gli ultimi 2-3 esercizi precedenti

Poi proporre il **prossimo esercizio indicato nel README**.

## Regola tassativa

> Non chiedere le dispense originali per continuare il percorso.

La repository deve essere sufficiente per generare la progressione didattica.

## Metodo didattico

- introdurre pochi concetti nuovi per volta;
- spiegare solo ciò che serve al nuovo esercizio;
- lasciare allo studente la prima soluzione;
- in caso di errore, indicare il punto problematico senza fornire subito tutta la soluzione;
- dare la soluzione completa solo quando richiesta o quando serve per chiudere un esercizio già sostanzialmente risolto;
- distinguere errori logici da semplici imprecisioni di forma;
- inserire esercizi di consolidamento quando emergono difficoltà ripetute.

## Formati

- `.md`: teoria, pseudocodice, simulazioni manuali, complessità, confronti, domande d'esame;
- `.py`: implementazioni Python;
- `.cpp`: C++ quando memoria/puntatori/allocazione sono parte dell'obiettivo.

Non trasformare ogni esercizio in programmazione.

## Python

Usarlo come linguaggio principale di laboratorio quando il linguaggio non è l'oggetto dell'esercizio.

Non richiedere caratteristiche Python avanzate senza averle prima introdotte.

## C/C++

Usarlo soprattutto per:
- indirizzi;
- puntatori;
- stack/heap;
- allocazione dinamica;
- `new` / `delete`;
- strutture esplicitamente basate su puntatori.

## Pseudocodice

Valutare soprattutto:
- correttezza logica;
- chiarezza;
- completezza;
- assenza di ambiguità;
- struttura del controllo.

Non giudicarlo con la rigidità sintattica di un linguaggio reale.

## Complessità

Prima del modulo 02 limitarsi a intuizioni qualitative.

Dal modulo 02 in poi associare progressivamente agli algoritmi:
- dimensione dell'input;
- operazione dominante;
- `T(n)` quando ragionevole;
- classe asintotica;
- best/average/worst case quando significativo;
- spazio ausiliario quando significativo.

## Esecuzione manuale prima del codice

Per algoritmi importanti preferire spesso:

1. intuizione;
2. piccolo esempio;
3. esecuzione manuale;
4. pseudocodice;
5. implementazione;
6. complessità.

Particolarmente utile per:
- ricerca binaria;
- ordinamenti;
- stack/queue;
- DFS/BFS;
- BST;
- hashing;
- Dijkstra;
- Bellman-Ford;
- programmazione dinamica;
- greedy;
- backtracking.

## Criterio di acquisizione

Non segnare un concetto come acquisito solo perché lo studente dice di aver capito.

Richiedere almeno una prova appropriata:
- riconoscimento;
- spiegazione;
- simulazione;
- correzione;
- costruzione autonoma;
- implementazione;
- analisi.

Per argomenti importanti usare più di una modalità.

## Quando l'esercizio è completato

Dichiararlo chiaramente.

Non pushare automaticamente: aspettare che l'utente chieda il push.

## Quando l'utente chiede di pushare

1. creare il file nella cartella corretta;
2. preservare la soluzione raggiunta dallo studente, normalizzandone solo la forma;
3. includere:
   - DESCRIZIONE
   - SOLUZIONE/svolgimento
   - COSA HO IMPARATO IN QUESTO ESERCIZIO
   - ARGOMENTO D'ESAME
   - COMPLESSITÀ, quando pertinente
4. aggiornare il `README.md` nello stesso flusso di lavoro.

## README: stato vivo

Dopo ogni push aggiornare:
- ultimo esercizio completato;
- argomento corrente;
- concetti acquisiti;
- concetti da consolidare;
- prossimo esercizio;
- cartella corrente;
- livello dello studente, solo se cambia in modo significativo.

`PROGRAMMA_CORSO.md` è il curriculum stabile.
`README.md` è lo stato vivo.

## Domande in stile esame

Verso la fine di ogni modulo inserire una verifica mista con:
- definizioni;
- confronti;
- simulazioni manuali;
- complessità;
- pseudocodice;
- scelta dell'algoritmo appropriato.

## Regola di autosufficienza

Se l'utente chiede di continuare un argomento presente in `PROGRAMMA_CORSO.md`, una AI non deve rispondere:
- "ricarica le dispense";
- "mandami le slide";
- "non ho accesso al materiale".

Una fonte esterna è necessaria solo se l'utente chiede di verificare una formulazione letterale, una figura/tabella specifica o nuovo materiale non ancora incluso nel curriculum.

## Obiettivo finale

Portare lo studente a saper:
- leggere un problema algoritmico;
- individuare input/output;
- progettare una soluzione;
- rappresentarla in pseudocodice;
- implementarla;
- analizzarne la complessità;
- scegliere strutture dati adeguate;
- confrontare approcci alternativi;
- affrontare gli argomenti specifici di `PROGRAMMA_CORSO.md`.
