"""17.Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = c/2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas."""

try:
    centimetros = float(input("Informe o comprimento em centimetros: "))
    polegadas = centimetros/2.54
    print(f"O comprimento em polegadas é {polegadas}")
except:
    print("Informou algo errado.")