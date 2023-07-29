"""35.Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = (a²+b²)**0.5. Faça um programa que receba os valores de
 a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação."""

try:
    cateto, cateto2 = float(input("Informe um dos catetos do triângulo: ")), float(input("Informe o outro cateto: "))
    hipotenusa = ((cateto**2) + (cateto2**2))**0.5
    print(f"A hipotenusa desse triângulo é {hipotenusa}")
except:
    print("Tente novamente")
