"""16. Usando match case, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante."""

def NomeMes(numero):
    match numero:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5:
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11:
            return "Novembro"
        case 12:
            return "Dezembro"
        case _:
            return "Mês inválido"


numeroMes = int(input("Digite um número correspondente ao mês entre 1 e 12: "))

nomeMes = NomeMes(numeroMes)

print(f"O mês correspondente ao número {numeroMes} é: {nomeMes}")
