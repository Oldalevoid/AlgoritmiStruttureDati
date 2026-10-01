# Esercizio 03 — Sequenza, selezione e iterazione

## DESCRIZIONE

L'esercizio richiede di riconoscere i tre principali schemi di composizione di un algoritmo:

- sequenza;
- selezione/condizione;
- iterazione.

Nella seconda parte, l'obiettivo è riconoscere come più schemi possano comparire e combinarsi all'interno dello stesso algoritmo.

## PARTE 1 — RICONOSCIMENTO DEGLI SCHEMI

### 1

```text
Prendi un numero
Moltiplicalo per 2
Stampa il risultato
```

**Risposta:** Sequenza.

### 2

```text
Prendi l'età
SE età >= 18
    Stampa "Maggiorenne"
ALTRIMENTI
    Stampa "Minorenne"
```

**Risposta:** Selezione/condizione.

### 3

```text
Ripeti 10 volte:
    Stampa "Ciao"
```

**Risposta:** Iterazione.

### 4

```text
Prendi un numero
Aggiungi 5
Moltiplica il risultato per 3
Stampa il risultato
```

**Risposta:** Sequenza.

### 5

```text
FINCHÉ il numero è minore di 100:
    Aggiungi 10 al numero
```

**Risposta:** Iterazione.

### 6

```text
SE temperatura > 30
    Stampa "Fa caldo"
ALTRIMENTI
    Stampa "Non fa caldo"
```

**Risposta:** Selezione/condizione.

## PARTE 2 — COMBINAZIONE DEGLI SCHEMI

Algoritmo analizzato:

```text
Prendi un numero

SE numero < 0
    Stampa "Numero negativo"
ALTRIMENTI
    RIPETI 3 VOLTE
        Stampa il numero
    Stampa "Fine"
```

Schemi riconosciuti:

- **Sequenza:** l'algoritmo nel suo complesso segue un ordine di istruzioni.
- **Selezione:** il blocco `SE numero < 0 ... ALTRIMENTI ...`.
- **Iterazione:** il blocco `RIPETI 3 VOLTE`.
- L'iterazione è contenuta all'interno del ramo `ALTRIMENTI`, mostrando che gli schemi possono essere combinati e annidati.

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- Riconoscere una sequenza di istruzioni.
- Riconoscere una selezione basata su una condizione.
- Riconoscere un'iterazione.
- Capire che sequenza, selezione e iterazione possono comparire nello stesso algoritmo.
- Capire che uno schema può essere annidato all'interno di un altro.

## ARGOMENTO D'ESAME

Fondamenti degli algoritmi: schemi di composizione di un algoritmo.

## COMPLESSITÀ

Non ancora analizzata in questo esercizio.
