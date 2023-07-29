"""23.Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J = M/0.91, sendo J o comprimento em jardas e M o comprimento em
metros."""

try:
    Metros = float(input("Informe o comprimento em metros: "))
    Jardas = Metros/0.91
    print(f"O comprimento em jardas é {Jardas}")
except:
    print("Informou algo errado.")