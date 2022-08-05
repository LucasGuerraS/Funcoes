# Calculadora simples
# Contem adicao, subtracao, multiplicacao e divisao

# menu()
# entrada_de_dados()
# adicao()
# subtracao()
# multiplicacao()
# divisao()
# imprimir()
# controlador()
# Funcao Menu()
def menu():
    print("*- Menu *-")
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    op = int(input("Digite a opcao desejada: "))
    return op
# -----------------------------------------------------------------------------------------------------------------------
# Funcao entrada_de_dados()
def entrada_de_dados():
    print("*- Entrada de dados *-")
    num = int(input("Numero: "))
    return num
# -----------------------------------------------------------------------------------------------------------------------
# Funcao adicao()
def adicao(n1, n2):
    print("*- Adicao *-")
    result = n1 + n2
    return result
# -----------------------------------------------------------------------------------------------------------------------
# Funcao subtracao()
def subtracao(n1, n2):
    print("*- Subtracao *-")
    result = n1 - n2
    return result
# -----------------------------------------------------------------------------------------------------------------------
# Funcao multiplicacao()
def multiplicacao(n1, n2):
    print("*- Multiplicacao *-")
    result = n1 * n2
    return result
# -----------------------------------------------------------------------------------------------------------------------
# Funcao divisao()
def divisao(n1, n2):
    print("*- Divisao *-")
    if n2 == 0:
        return print("Nao e possivel dividir por 0")
    result = n1 / n2
    return result
# -----------------------------------------------------------------------------------------------------------------------
# Funcao imprimir()
def imprimir(result):
    print("*- Resultado *-")
    print("Resultado: ", result)
# -----------------------------------------------------------------------------------------------------------------------
# Funcao controlador()
def controlador(n1, n2, op):
    print("*- Controlador-*")
    if op == 1:
       result = adicao(n1, n2)
    elif op == 2:
       result = subtracao(n1, n2)
    elif op == 3:
        result = multiplicacao(n1, n2)
    elif op == 4:
        result = divisao(n1, n2)
    else:
        result = "Opcao invalida"
    return result
# -----------------------------------------------------------------------------------------------------------------------
# Programa principal
print("***- Calculadora simples ***-")
op = menu()
n1 = entrada_de_dados()
n2 = entrada_de_dados()
result = controlador(n1, n2, op)
imprimir(result)

