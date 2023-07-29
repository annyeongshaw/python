"""47.Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""

num = int(input("Informe um número de quatro dígitos (de 1000 a 9999): "))
if num >= 1000 and num <= 9999:
    num = str(num)
    num = [x for x in num]
    for i in num:
        print(int(i))
else:
    print("Valor inválido")