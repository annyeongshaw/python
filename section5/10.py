"""10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):

- Homens: (72.7*h) — 58
- Mulheres: (62,1 *h) — 44,7"""

altura, sexo = float(input("Informe a sua altura:")), input("Informe seu genero com M para masculino e F para feminino: ").upper()

if sexo == "M":
    print(f"Seu peso ideal é {(71.7*altura) - 58:.2f}")
elif sexo == "F":
    print(f"Seu peso ideal é {(61.1*altura) - 44,7:.2f}")
else:
    print("Tente novamente.")