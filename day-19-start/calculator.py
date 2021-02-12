def add(n1, n2):
    return n1 + n2


def subst(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# calculator는 higher order function이다.
def calculator(n1, n2, func):
    print(func(n1, n2))


calculator(1, 2, add)
calculator(1, 2, subst)
calculator(1, 2, divide)
calculator(1, 2, multiply)
