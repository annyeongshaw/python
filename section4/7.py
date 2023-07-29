"""7- Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
AA fórmula de conversão é: C = 5.0 * (F — 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit."""

try: 
    fahrenheit = float(input("Informe a temperatura em Graus Celsius: "))
    Celsius = 5 * ((fahrenheit-32)/9)
    print(f"A temperatura em Celsius é {Celsius}")
except:
    print("Você digitou um valor inválido.")