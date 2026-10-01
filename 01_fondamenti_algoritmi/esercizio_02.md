# Esercizio 02 — Proprietà di un algoritmo

## DESCRIZIONE

L'esercizio richiede di riconoscere quale proprietà fondamentale di un algoritmo viene violata da una serie di istruzioni problematiche.

Le proprietà considerate sono:

- finito;
- eseguibile;
- non ambiguo;
- generale;
- deterministico;
- completo.

## ESERCIZIO

1. "Aggiungi un po' di acqua."
2. "Continua a sommare 1 per sempre."
3. "Vola fino alla Luna e prendi una roccia."
4. Se il numero è maggiore di 10, stampa "grande". Se è minore di 10, stampa "piccolo".
5. Dato il numero 7, stampa 14.
6. Lancia una moneta: se esce testa stampa 1, se esce croce stampa 2.

## SOLUZIONE

### 1. Non ambiguo

"Aggiungi un po' di acqua" non specifica una quantità precisa e può quindi essere interpretato in modi diversi.

### 2. Finito

L'istruzione "per sempre" implica che l'esecuzione non terminerà mai. Un algoritmo deve terminare dopo un numero finito di passi.

### 3. Eseguibile

"Vola fino alla Luna e prendi una roccia" non rappresenta un'istruzione materialmente eseguibile dal normale esecutore considerato.

### 4. Completo

Manca il caso in cui il numero sia esattamente uguale a 10.

### 5. Generale

L'istruzione è costruita esclusivamente sul caso particolare del numero 7. Un algoritmo generale deve essere applicabile a una classe di problemi.

### 6. Deterministico

Il lancio della moneta può produrre risultati diversi pur partendo dalla stessa situazione iniziale, quindi non garantisce sempre lo stesso risultato finale.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere le principali proprietà richieste a un algoritmo.
- Distinguere tra ambiguità, non terminazione, non eseguibilità e incompletezza.
- Capire che un algoritmo deve essere generale e non limitato a una singola istanza.
- Comprendere il significato di determinismo nella definizione introduttiva del corso.
- Associare un difetto concreto alla proprietà algoritmica violata.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: proprietà di un algoritmo.

## COMPLESSITÀ

Non pertinente in questo esercizio.
