"""26.Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
AA fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H
a área em hectares."""

try:
    MetrosQuadrados = float(input("Informe a área em metros quadrados: "))
    Hectares = MetrosQuadrados * 0.0001
    print(f"A área em hectares é {Hectares}")
except:
    print("Informou algo errado.")