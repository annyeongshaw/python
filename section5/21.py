"""21. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esco-
lhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção"""


def subtracao(num1,num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1

def soma(num1,num2):
    return num1 + num2

def divisao(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError("Não se pode dividir por zero")
    return num1/num2

def multiplica(num1,num2):
    return num1 * num2

def operacoes(opera = int,num1=float,num2=float) -> float:
    if opera == 2:
        return subtracao(num1,num2)
    elif opera == 1:
        return soma(num1,num2)
    elif opera == 3:
        return multiplica(num1,num2)
    elif opera == 4:
        return divisao(num1,num2)
    else:
        raise ("Operação inválida")

opcao = int(input("""Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção: """))
num1, num2 = float(input("Informe um número: ")), float(input("Informe outro número: "))
print(f"Resultado: {operacoes(opcao,num1,num2):.2f}")