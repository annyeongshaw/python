"""15.Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180/pi, sendo G o ângulo em graus e R em radianos e pi = 3.14."""
from math import pi

try:
    Radianos = float(input("Informe o ângulo em radianos: "))
    graus = Radianos * (180/pi)
    print(f"O ângulo em graus é {graus}")

except:
    print("Informou algo errado.")