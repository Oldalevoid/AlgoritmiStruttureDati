# DESCRIZIONE
# Implementazione in Python della ricerca lineare e della ricerca binaria.
# L'esercizio consolida la differenza tra ricerca sequenziale e ricerca su lista ordinata.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - In un ciclo "for numero in numeri", la variabile "numero" contiene direttamente il valore.
# - La ricerca lineare controlla gli elementi uno alla volta.
# - Il messaggio "non trovato" va dato solo dopo aver esaurito il ciclo.
# - Nella ricerca binaria si mantengono due limiti: sinistra e destra.
# - Il centro si ricalcola a ogni iterazione.
# - Se il valore cercato è maggiore del valore centrale, si sposta sinistra a centro + 1.
# - Se il valore cercato è minore del valore centrale, si sposta destra a centro - 1.
# - Il ciclo continua finché sinistra <= destra.
#
# ARGOMENTO D'ESAME
# 03 — Array, memoria e ricerca
#
# COMPLESSITÀ
# Ricerca lineare: best Theta(1), worst Theta(n)
# Ricerca binaria: Theta(log n)

# Ricerca lineare

numeri = [4, 9, 15, 22, 31]

def trovanumero(numeri, cercato):
    for numero in numeri:
        if numero == cercato:
            print("Trovato")
            return

    print("Numero non in lista")

trovanumero(numeri, 15)


# Ricerca binaria

numeri = [4, 9, 15, 22, 31]
cercato = 22

sinistra = 0
destra = len(numeri) - 1

while sinistra <= destra:
    centro = (sinistra + destra) // 2

    if numeri[centro] == cercato:
        print("Trovato")
        break

    elif cercato > numeri[centro]:
        sinistra = centro + 1

    else:
        destra = centro - 1
