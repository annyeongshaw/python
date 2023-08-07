"""18. Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-
temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro-
grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e
saindo."""
  

def subtracao(num1,num2):
    return num1 - num2

def soma(num1,num2):
    return num1 + num2

def divisao(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError("Não se pode dividir por zero")
    return num1/num2

def multiplica(num1,num2):
    return num1 * num2

def operacoes(opera = str) -> float:
    if opera == "-":
        return subtracao(num1,num2)
    elif opera == "+":
        return soma(num1,num2)
    elif opera == "*":
        return multiplica(num1,num2)
    elif opera == "/":
        return divisao(num1,num2)
    else:
        raise ("Operação inválida")


option = input("""Escolha uma das opções::
Soma: +
Subtração: -
Divisão: /
Multiplicação: *
Escolha através do simbolo correspondente: """)
num1, num2 = float(input("Informe o primeiro número: ")), float(input("Informe o segundo número: "))

print(f"Resultado: {operacoes(option)}")
