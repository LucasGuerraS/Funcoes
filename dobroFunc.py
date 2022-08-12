def it():
    n = float(input("Digite um número: "))
    return n


def dobro(n):
    r = n * 2
    return r


def imp(n):
    print(f"numero: {n/2} \n dobro: {n}")

def main():
    n = it()
    r = dobro(n)
    imp(r)

# Principal
main()
