"""29.Leia quatro notas, calcule a média aritmética e imprima o resultado."""

try:
    notas = []
    for i in range(4):
        notas.append(float(input("Informe um número: ")))
    print(f"A média aritmética é {sum(notas)/len(notas)}")
except:
    print("Informou algo errado.")
