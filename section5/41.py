"""41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de
acordo com a tabela abaixo:
peso / (altura)**2
IMC 	         | Classificação
imc<18        | Abaixo do Peso
de 18 ate 25 (excluso) | Saudável
de 25,0 ate 30 (excluso) | Peso em excesso
de 30,0 ate 35 (excluso) | Obesidade Grau I
de 35,0 ate 40 (incluso) | Obesidade Grau II(severa)
imc > 40,0	     | Obesidade Grau III(mórbida)"""

def imc(peso=float, altura=float) -> str:
    calImc = peso/((altura)**2)
    if 0 < calImc < 18:
        return calImc, "Abaixo do peso"
    elif calImc < 25:
        return calImc, "Saudável"
    elif calImc < 30:
        return calImc, "Peso em excesso"
    elif calImc < 35:
        return calImc, "Obesidade grau I"
    elif calImc <= 40:
        return calImc, "Obesidade grau II (severa)"
    else:
        return calImc, "Obesidade grau III (mórbida)"


peso, altura = float(input("Informe o peso: ")), float(input("Informe a altura: "))
print(f"IMC:{imc(peso,altura)[0]:.2f}\nClassificação: {imc(peso,altura)[1]}")