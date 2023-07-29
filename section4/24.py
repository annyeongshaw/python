"""24.Leia um valor de área em metros quadrados mº e apresente-o convertido em acres. À
fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e À
aárea em acres."""

try:
    metrosQuadrados = float(input("Informe a área em metros quadrados: "))
    Acres = metrosQuadrados * 0.000247
    print(f"A área em acres é {Acres}")
except:
    print("Informou algo errado.")