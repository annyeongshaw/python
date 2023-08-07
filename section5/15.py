"""15. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante."""


def diaSemana(num=int) -> str:
    match num:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7: 
            return "Sábado"
        case _:
            return "dia inválido"
        

num = int(input("""Informe o número correspondente ao dia:
1- Domingo
2- Segunda-feira
3- Terça-feira
4- Quarta-feira
5- Quinta-feira
6- Sexta-feira
7- Sábado
escreva: """))

print(f"{diaSemana(num)}")


