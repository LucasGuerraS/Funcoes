def it():
    """
    Função que pede um número e retorna o número

    @parameters: none
    @return: número (float)
    """
    n = float(input("Digite um número: "))
    return n

def maior(n1: float, n2: float):
    """
    Função que retorna o maior número entre dois números

    @parameters: n1 (float), n2 (float)
    @return: texto do maior numero (str)
    """
    if n1 > n2:
        r = f"numero: {n1} maior que {n2}"
    elif n1 == n2:
        r = f"numero: {n1} igual a {n2}"
    else:
        r = f"numero: {n2} maior que {n1}"
    return r

def imp(ct):
    """
    Função que imprime o parametro passado

    @parameters: ct (any) - qualquer coisa que deseje imprimir
    @return: none
    """
    print(ct)

def main():
    """
    Função principal de execução do programa
    """
    n1 = it()
    n2 = it()
    r = maior(n1, n2)
    imp(r)

# principal
main()
