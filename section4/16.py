"""16.Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas."""

try:
    polegadas = float(input("Informe o comprimento em polegadas: "))
    centimetros = polegadas * 2.54
    print(f"O comprimento em centimetros é {centimetros}")
except:
    print("Informou algo errado.")