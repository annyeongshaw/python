"""6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos."""

num = []

for i in range(2):
    num.append(int(input("Informe um número: ")))
numMax, numMin = max(num), min(num)
if numMax != numMin:
    print(f"O maior número é {numMax}.\nE a difereça entre os dois números é {numMax-numMin}.")
else:
    print("Números iguais.")

    
# vervãos alternativa 
"""if num[0] > num[1]:
    print(f"O maior número é {num[0]}.\nE a difereça entre os dois números é {num[0]-num[1]}.")
elif num[1] > num[0]:
    print(f"O maior número é {num[1]}.\nE a difereça entre os dois números é {num[1]-num[0]}.")
else:
    print("Os números são iguais.")"""
