"""22.Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento
em metros."""

try:
    Jardas = float(input("Informe o comprimento em jardas: "))
    Metros = 0.91 * Jardas
    print(f"O comprimento em metros é {Metros}")
except:
    print("Informou algo errado.")