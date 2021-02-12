from sympy import *

from metodos_iterativos.bisseccao import bisseccao
from metodos_iterativos.falsa_posicao import falsa_posicao
from metodos_iterativos.newton import newton
from metodos_iterativos.secante import secante


def get_f(equation):
    equation = equation.replace("^", "**")
    equation = sympify(equation)
    x = symbols("x")

    def f(value):
        fx = equation.subs(x, value)
        return round(fx.evalf(), 4)

    def d(value):
        dx = diff(equation, x).subs(x, value)
        return round(dx.evalf(), 4)

    return f, d


def menu(x, f, d):
    return {
        "bisseccao": lambda a, b: bisseccao(f, d, a, b, 0.001, 5),
        "falsa posição": lambda a, b: falsa_posicao(f, d, a, b, 0.001, 5),
        "newton": lambda a, b: newton(f, d, a, b, 0.001, 5),
        "secante": lambda a, b: secante(f, d, a, b, 0.001, 5)
    }[x](float(input("a: ")), float(input("b: ")))


def main():
    alg = "x ** 3 - 9 * x + 3"
    f, d = get_f(alg)

    menu("secante", f, d)


if __name__ == '__main__':
    main()
