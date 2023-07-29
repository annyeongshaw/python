"""9- Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. À
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin."""

try:
    Celcius = float(input("Informe a temperatura em Celsius: "))
    kelvins = Celcius + 273.15
    print(f"A temperatura convertida em kelvins é {kelvins}")
except:
    print("Informou um valor inválido") 