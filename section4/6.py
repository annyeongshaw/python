"""
6- Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
Afórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

try: 
    celsius = float(input("Informe a temperatura em Graus Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32
    print(f"A temperatura em fahrenheit é {fahrenheit}")
except:
    print("Você digitou um valor inválido.")