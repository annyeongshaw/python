"""8- Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. À
fórmula de conversão é: C = K — 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin."""

try:
    kelvin = float(input("Informe a temperatura atual em kelvins: "))
    Celsius = kelvin - 273.15
    print(f"A temperatura em Celsius é {Celsius}")
except:
    print("Informou um valor inválido.")
    