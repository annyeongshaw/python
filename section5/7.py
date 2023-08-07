"""7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem Números iguais."""

num = []

for i in range(2):
    num.append(int(input("Informe um número: ")))
numMax, numMin = max(num), min(num)
if numMax != numMin:
    print(f"O maior número é {numMax}.\nE a difereça entre os dois números é {numMax-numMin}.")
else:
    print("Números iguais.")