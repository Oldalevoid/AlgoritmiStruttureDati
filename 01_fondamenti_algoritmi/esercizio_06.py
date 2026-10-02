# DESCRIZIONE
# Implementazione Python dello pseudocodice dell'esercizio 06.
# Conta quanti valori dell'indice, da 1 a N compreso, sono maggiori di 2.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Tradurre "PER I DA 1 A N" in range(1, n + 1)
# - Ricordare che il secondo estremo di range() è escluso
# - Tradurre un semplice pseudocodice con ciclo e condizione in Python

n = 5
conta = 0

for i in range(1, n + 1):
    if i > 2:
        conta = conta + 1

print(conta)
