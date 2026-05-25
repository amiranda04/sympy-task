import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

import sympy as sp
def calcola_derivata(espressione: str, variabile: str) -> sp.Expr:
    espressione = espressione.replace("^", "**")  # fix semplice
    expr = sp.sympify(espressione)
    var = sp.Symbol(variabile)
    return sp.diff(expr, var)


if __name__ == "__main__":
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")

    print("Derivata:", calcola_derivata(espressione, variabile))

pass

import sympy as sp

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sp.Expr:
    espressione = espressione.replace("^", "**")
    expr = sp.sympify(espressione)
    var = sp.Symbol(variabile)
    return sp.integrate(expr, (var, estremo_inf, estremo_sup))


# Input utente
if __name__ == "__main__":
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    estremo_inf = float(input("Estremo inferiore: "))
    estremo_sup = float(input("Estremo superiore: "))

    risultato = calcola_integrale_definito(espressione, variabile, estremo_inf, estremo_sup)
    print("Integrale definito:", risultato)

    pass

import sympy as sp

def calcola_limite(espressione: str, variabile: str, punto: str) -> sp.Expr:
    espressione = espressione.replace("^", "**")
    expr = sp.sympify(espressione)
    var = sp.Symbol(variabile)
    p = sp.sympify(punto)
    return sp.limit(expr, var, p)


if __name__ == "__main__":
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    punto = input("Inserisci il punto: ")

    risultato = calcola_limite(espressione, variabile, punto)

    # ✅ Stampa elegante
    print(f"lim_{variabile}→{punto} ({espressione}) = {risultato}")
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
