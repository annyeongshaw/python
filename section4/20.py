"""20.Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = K/0.45, sendo K' a massa em quilogramas e L a massa em libras."""

try:
    quilogramas = float(input("Informe a massa em quilos: "))
    Libras = quilogramas/0.45
    print(f"A massa em libras é {Libras}")
except:
    print("Informou algo errado.")