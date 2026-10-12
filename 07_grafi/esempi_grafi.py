"""Esempi introduttivi sui grafi: codice di lettura, non esercizi implementati autonomamente."""
from typing import Dict, List

# Grafo non orientato, liste di adiacenza
grafo: Dict[str, List[str]] = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A"],
}

# Matrice dell'esempio A--B--C
vertici = ["A", "B", "C"]
matrice = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]


def esempio() -> None:
    print(grafo["B"])  # ['A', 'C']
    print(matrice[0][2])  # 0, cioe' nessun arco diretto A--C


if __name__ == "__main__":
    esempio()
