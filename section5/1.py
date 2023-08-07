"""1. Faça um programa que receba dois números e mostre qual deles é o maior."""


try:
    num = []
    for i in range(2):
        num.append(float(input("Informe um número: ")))
    if num[0] == num[1]:
        print(f"Os dois números possuem o mesmo valor. Que é {num[0]}")
    else:
        print(f"O maior número é {max(num)}")
except:
    print("Tente novamente.")


# Versão alternativa 

"""num1 = float(input("Informe um número: "))
num2 = float(input("Informe um número: "))
if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else: 
    print(f"Os dois números possuem o mesmo valor. Que é {num2}")"""