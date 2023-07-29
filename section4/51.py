"""51.Escreva um programa que leia as coordenadas x e y de pontos no R², plano cartesiano, e calcule sua
distância da origem (0,0). DistânciaDaOrigem(o,0) = ((x)² + (y)²)**0.5"""

try:
    x, y = int(input("Informe a coordenada x: ")), int(input("Informe a coordenada y: "))
    distanciaOrigem = (x**2+y**2)**0.5
    print(f"A distância do ponto ({x}, {y}) à origem (0, 0) é: {distanciaOrigem:.2f}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos para as coordenadas x e y.")
