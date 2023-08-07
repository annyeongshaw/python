"""4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:

- O número digitado ao quadrado
- A raiz quadrada do número digitado"""

try:
    num = int(input("Informe um número: "))
    if num > 0:
        print(f"O quadrado de {num} é {num**2}")
        print(f"A raiz quadrada de {num} é {num**0.5:.3f}")
    else:
        print("Valor negativo. Tente novamente!!!")
except:
    print("Tente novamente")       