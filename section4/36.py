"""36.Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * r²*altura,
onde pi = 3.14"""
from math import pi

def calculaVolumeCilindro(altura=float, raio=float) -> float:
    """Essa função tem o intuito de calcular o volume de um cilindro."""
    volume = pi * (raio**2)*altura
    return volume

try:
    altura = float(input("Informe a altura do cilindro: "))
    raio = float(input("Informe o raio do cilindro: "))
    print(f"O volume do cilíndro é {calculaVolumeCilindro(altura,raio)}")
except:
    print("Tente novamente")