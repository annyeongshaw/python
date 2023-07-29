"""12.Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1,61 * M, sendo K a distância em quilômetros e 1 em milhas."""

try:
    Miles = float(input("Informe a distância em milhas: "))
    Quilometros = 1.61 * Miles
    print(f"A diatância em quilometros é {Quilometros}")
except:
    print("Informou algo errado.")