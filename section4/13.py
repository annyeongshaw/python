"""13.Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = k/1.61 sendo K a distância em quilômetros e M em milhas."""

try:
    Quilometros = float(input("Informe a distância em milhas: "))
    Miles = Quilometros/1.61
    print(f"A diatância em milhas é {Miles}")
except:
    print("Informou algo errado.")