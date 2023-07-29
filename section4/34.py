"""34.Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do círculo é pi * r², considere pi = 3.141592."""

from math import pi

try:
    RaioDoCirculo = float(input("Informe o raio do circulo: "))
    AreaDoCirculo = pi * (RaioDoCirculo**2)
    print(f"A área do circulo é {AreaDoCirculo}")
except:
    print("Tente novamente")