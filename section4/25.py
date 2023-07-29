"""25.Leia um valor de área em acres e apresente-o convertido em metros quadrados m?. À
fórmula de conversão é: M = A * 4048,58, sendo M a área em metros quadrados e À a
área em acres."""

try:
    acres = float(input("Informe a área em acres: "))
    MetrosQuadrados = acres * 4048.58
    print(f"A área em metros quadrados é {MetrosQuadrados}")
except:
    print("Informou algo errado.")