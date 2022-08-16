import random

def tamanho():
    """
    @description: Função que recebe um numero que corresponde ao tamanho de array que irá ser criado
    @params: None
    @return: n -> numero inputado pelo usuário
    """
    n = int(input("digite o tamanho da lista: "))
    return n

def create_list(t: int):
    """
    @description: Função que cria um array de inteiros aleatórios com base num tamanho recebido por parâmetro
    @params: t -> int número que corresponde ao tamanho do array
    @return: lista -> list[] criada pela função com números aleatóroios
    """
    lista = []
    i = 1
    while i <= t:
        lista.append(random.randint(0, 100))
        i += 1
    return lista

def percorre(lista: list):
    """
    @description: Função que percorre e imprime um array
    @params: lista -> array de números
    @return: None
    """
    i = 0
    while i < len(lista):
        print(f" elemento {i + 1} - {lista[i]}")
        i += 1

def pares(lista: list): 
    """
    @description: Função que percorre um array e cria um array novo com os números pares sortados
    @params: lista -> lista[] que deseja sortar
    @return: pares -> array[] com os números pares somente
    """
    pares = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        i += 1
    return pares

def impares(lista: list): 
    """
    @description: Função que percorre um array e cria um array novo com os números impares sortados
    @params: lista -> lista[] que deseja sortar
    @return: impares -> array[] com os números imapares somente
    """
    impares = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            impares.append(lista[i])
        i += 1
    return impares

def numero():
    """
    @description: Função que recebe um numero que corresponde ao número buscado no array
    @params: None
    @return: n -> int, numero inputado pelo usuário
    """
    n = int(input("digite um numero para ver se o mesmo se encontra na lista: "))
    return n


def contido(lista: list, n: int):
    """
    @description: Percorre um array passado por parâmetro em busca do número passado também por parâmetro e retorna se tal número se encontra no array
    @params: 
    lista -> array[] que deseja saber se x número está presente 
    n -> int, número que deseja saber se está presente dentro do array
    @return: str dizendo se o número se encontra ou não no array
    """
    x = None
    i = 0
    while i < len(lista):
        if n == lista[i]:
           x=(f"{n} contido na lista")
        i+=1
    if x == None:
        return f"{n} não contido na lista"
    else: 
        return x

def main():
    """
    @description: Função responsável pela execução do programa
    """
    t = tamanho()
    lista = create_list(t)
    percorre(lista)
    print("-------------------------")
    print("lista de pares")
    par = pares(lista)
    percorre(par)
    print("-------------------------")
    print("lista de impares")
    impar = impares(lista)
    percorre(impar)
    print("-------------------------")
    print("numero contido")
    t2 = tamanho()
    lista2 = create_list(t2)
    n = numero()
    percorre(lista2)
    presente = contido(lista2, n)
    print(presente)

main()
