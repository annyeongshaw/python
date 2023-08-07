"""13. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos."""
    
    
try:
    prova = []
    for i in range(1,4):
        prova.append(float(input(f"Informe a {i}° nota: ")))

    sumPonderada = ((prova[0] + prova[1]) + 2*prova[2])/3
    if sumPonderada >= 60 and sumPonderada <=100:
        print(f"A média do aluno é: {sumPonderada:.2f}")
        print(f"Situação do aluno: Aprovado")
    elif sumPonderada < 0 and sumPonderada >100:
        print("Error. Tente novamente.")
    else: 
        print(f"A média do aluno é: {sumPonderada:.2f}")
        print(f"Situação do aluno: Reprovado")
except:
    print("Tente novamente")