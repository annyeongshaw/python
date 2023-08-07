"""14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de O até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre O e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias."""


def verificaSituacao(nota1=float, nota2=float, nota3=float) -> float:
    peso1, peso2, peso3 = 2, 3, 5
    nota1, nota2, nota3 = nota1*peso1, nota2*peso2, nota3*peso3
    mediaPonderada = (nota1 + nota2 + nota3) / 10
    if mediaPonderada >= 5 and mediaPonderada <= 10:
        return (f"A média do aluno é: {mediaPonderada:.2f}\nSituação do aluno: Aprovado")
    elif mediaPonderada < 5 and mediaPonderada > 3:
        return (f"A média do aluno é: {mediaPonderada:.2f}\nSituação do aluno: Recuperação")
    else:
        return (f"A média do aluno é: {mediaPonderada:.2f}\nSituação do aluno: Reprovado")
        

notaLab = float(input("Informe a nota tirada do trabalho de laboratório: "))
notaSemestre = float(input("Informe a nota tirada na avaliação semestral: "))
notaExameFinal = float(input("Informe a nota tirada no exame final: "))
print(verificaSituacao(notaLab,notaSemestre,notaExameFinal))