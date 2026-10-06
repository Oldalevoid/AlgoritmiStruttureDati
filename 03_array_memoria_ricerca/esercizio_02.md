# Esercizio 02 — Array classico vs lista Python

## DESCRIZIONE

L'esercizio confronta l'array classico con la lista Python e consolida:
- accesso tramite indice;
- visita;
- ricerca lineare;
- differenza tra accesso diretto e ricerca di un valore.

## SVOLGIMENTO

Un array classico è una struttura indicizzata che, nel modello tradizionale:
- contiene elementi omogenei;
- ha dimensione tipicamente fissata;
- memorizza gli elementi in posizioni contigue.

Una lista Python è più flessibile:
- può crescere o ridursi dinamicamente;
- può contenere anche elementi di tipi diversi.

Esempio:

```python
dati = [10, "ciao", 3.14]
```

L'accesso tramite indice resta diretto:

```python
numeri = [10, 20, 30, 40]
numeri[2]
```

restituisce `30`.

La complessità dell'accesso diretto per indice è:

```text
Theta(1)
```

Se invece il valore è noto ma non si conosce il suo indice, bisogna cercarlo scorrendo gli elementi uno per uno.

Ricerca lineare:
- caso migliore: il valore è al primo posto;
- caso peggiore: il valore è all'ultimo posto oppure non è presente.

Quindi:

```text
best case  → Theta(1)
worst case → Theta(n)
```

È stato inoltre consolidato che conoscere già l'indice consente accesso diretto anche in una struttura molto grande.

Esempio: accedere direttamente all'elemento in posizione 700 di una lista di 1000 elementi resta:

```text
Theta(1)
```

## COSA HO IMPARATO IN QUESTO ESERCIZIO

- La lista Python è più flessibile di un array classico.
- L'array classico è tipicamente omogeneo e a dimensione fissata.
- L'accesso tramite indice noto è diretto e costa `Theta(1)`.
- Cercare un valore senza conoscerne la posizione richiede una ricerca lineare.
- Nella ricerca lineare il caso migliore è `Theta(1)`.
- Nella ricerca lineare il caso peggiore è `Theta(n)`.
- Accesso diretto e ricerca sono operazioni concettualmente diverse.

## ARGOMENTO D'ESAME

**03 — Array, memoria e ricerca**

- array;
- liste Python;
- accesso tramite indice;
- visita;
- ricerca sequenziale.

## COMPLESSITÀ

```text
accesso tramite indice noto → Theta(1)
ricerca lineare best        → Theta(1)
ricerca lineare worst       → Theta(n)
```
