def it():
    """
    Função que pede um número e retorna o número

    @parameters: none
    @return: número (float)
    """
    n = float(input("Digite um número: "))
    return n

def dobro(n: float):
    """
    Função que retorna o dobro de um número
    
    @parameters: n (float)
    @return: dobro (float)
    """
    r = n * 2
    return r

def imp(n: float):
    """
    Função que imprime o dobro de um número

    @parameters: n (float)
    @return: none
    """
    print(f"numero: {n/2} \n dobro: {n}")

def main():
    """
    Função principal de execução do programa
    """
    n = it()
    r = dobro(n)
    imp(r)
    n = it()
    r = dobro(n)
    imp(r)

# Principal
main()
