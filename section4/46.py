"""46.Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
                                |------------|
                                |input = 123 |
                                |output = 321|
                                |------------|"""

num = int(input("Informe um número inteiro positivo de três dígitos (de 100 a 999):"))
if num >= 100 and num <= 999:
    num = str(num)
    print(f"O número invertido é {int(num[::-1])}")
else:
    print("Valor inválido")