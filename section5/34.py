"""34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

NOTA |CONCEITO (ATE 20 FALTAS)| CONCEITO (MAIS DE 20 FALTAS)
9.0 até 10.0| A               | B
7.5 até 8.9 | B               | C
5.0 até 7.4 | C               | D
4.0 até 4.9 | D               | E
0.0 até 3.9 | E               | E"""


def situacao(nota=float,faltas=int):
    if nota <= 3.9:
        if faltas <=20:
            return "E"
        else:
            return "E"
    elif nota <= 4.9:
        if faltas <=20:
            return "D"
        else:
            return "E"
    elif nota <= 7.4:
        if faltas <=20:
            return "C"
        else:
            return "D"
    elif nota <= 8.9:
        if faltas <=20:
            return "B"
        else:
            return "C"
    else:
        if faltas <=20:
            return "A"
        else:
            return "B"


nota, faltas = float(input("Informe a nota do aluno: ")), int(input("Informe a quantidade de faltas: "))
print(f"Conceito: {situacao(nota,faltas)}")
