def it():
    n = float(input("Digite um número: "))
    return n


def maior(n1, n2):
    if n1 > n2:
        r = f"numero: {n1} maior que {n2}"
    elif n1 == n2:
        r = f"numero: {n1} igual a {n2}"
    else:
        r = f"numero: {n2} maior que {n1}"
    return r


def imp(ct):
    print(ct)

#principal
n1 = it()
n2 = it()
q = maior(n1, n2)
imp(q)
