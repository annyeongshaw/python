"""28. Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

(a) Geométrica: raizcúbica(x*y*z)
(b) Ponderada: (x+2*y+3*z)6
(c) Harmônica: (1) / ((1/x) + (1/y) + (1/z))
(d) Aritmética: (x+y+z)/3"""

def geometrica(x=int, y=int, z=int):
    return (x*y*z) ** (1/3)


def ponderada(x=int, y=int, z=int):
    return (x+(2*y)+(3*z))/6


def harmonica(x=int, y=int, z=int):
    return (1) / ((1/x) + (1/y) + (1/z))


def aritmetica(x=int, y=int, z=int):
    return (x+y+z)/3



num, num2, num3 = int(input("Informe um número inteiro(x):")), int(input("Informe outro número inteiro(y):")), int(input("Informe outro número inteiro(z):"))
opcao = int(input("""
1- Geometrica
2- Ponderada
3- Harmônica
4- Aritmetica
Escolha uma das opções acima. Informando o número correspondente: """))
match opcao:
    case 1:
        print(f"Geometrica: {geometrica(num,num2,num3):.2f}")
    case 2:
        print(f"Ponderada: {ponderada(num,num2,num3):.2f}")
    case 3:
        print(f"Harmônica: {harmonica(num,num2,num3):.2f}")
    case 4:
        print(f"Aritmetica: {aritmetica(num,num2,num3):.2f}")
    case _:
        print("Opção inválida.")
    