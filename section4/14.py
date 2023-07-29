"""14.Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * pi/180, sendo G o ângulo em graus e R em radianos e pi = 3.14."""
from math import pi

try:
    graus = float(input("Informe o ângulo em graus: "))
    Radianos = graus * (pi/180)
    print(f"O ângulo em radianos é {Radianos}")

except:
    print("Informou algo errado.")