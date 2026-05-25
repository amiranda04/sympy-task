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
    print(f"lim_{variabile}→{punto} ({espressione}) = {risultato}")
    pass

import sympy as sp
def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sp.Expr:
    espressione = espressione.replace("^", "**")
    expr = sp.sympify(espressione)
    var = sp.Symbol(variabile)
    return sp.series(expr, var, punto, ordine + 1).removeO()

if __name__ == "__main__":
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    punto = float(input("Inserisci il punto di sviluppo: "))
    ordine = int(input("Inserisci l'ordine: "))
    risultato = calcola_polinomio_taylor(espressione, variabile, punto, ordine)
    print(f"Serie di Taylor di {espressione} in {variabile} = {punto} (ordine {ordine}):")
    print(risultato)

    pass

import sympy as sp


def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> dict:
    def trasforma(eq):
        eq = eq.replace("^", "**")

        if "=" in eq:
            sx, dx = eq.split("=")
            return sp.sympify(sx) - sp.sympify(dx)
        else:
            return sp.sympify(eq)

    x = sp.Symbol(var1)
    y = sp.Symbol(var2)

    eq1 = trasforma(eq1)
    eq2 = trasforma(eq2)

    return sp.solve((eq1, eq2), (x, y))


# 🔹 INPUT UTENTE
if __name__ == "__main__":
    print("Inserisci due equazioni (puoi usare '=')")

    eq1 = input("Prima equazione: ")
    eq2 = input("Seconda equazione: ")

    var1 = input("Prima variabile (es: x): ")
    var2 = input("Seconda variabile (es: y): ")

    soluzione = risolvi_sistema_lineare(eq1, eq2, var1, var2)

    print("\n✅ Soluzione del sistema:")
    print(f"{var1} = {soluzione[sp.Symbol(var1)]}")
    print(f"{var2} = {soluzione[sp.Symbol(var2)]}")
pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
