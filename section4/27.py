"""27.Leia um valor de área em hectares e apresente-o convertido em metros quadrados m?.
AA fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H
a área em hectares."""

try:
    hectares = float(input("Informe a área em hectares:"))
    MetrosQuadrados = hectares * 10000
    print(f"A área em metros quadrados é {MetrosQuadrados}")
except:
    print("Informou algo errado.")