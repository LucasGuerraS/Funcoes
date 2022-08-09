def it():
    n = float(input("Digite um número: "))
    return n


def maior(n1, n2):
    if n1 > n2:
        r =1
    elif n1 == n2:
        r = 3
    else:
        r =2
    return r


def imp(n1, n2, ct):
    if ct == 1:
        print(f"numero: {n1} maior que {n2}")
    if ct == 2:
        print(f"numero: {n2} maior que {n1}")
    if ct == 3:
        print(f"numero: {n1} igual a {n2}")

#principal
n1 = it()
n2 = it()
q = maior(n1, n2)
imp(n1, n2, q)
