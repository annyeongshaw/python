"""21.Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K = L*0,45, sendo K a massa em quilogramas e L. a massa em libras."""

try:
    quilogramas = float(input("Informe a massa em quilos: "))
    Libras = quilogramas/0.45
    print(f"A massa em libras é {Libras}")
except:
    print("Informou algo errado.")