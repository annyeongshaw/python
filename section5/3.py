"""3. Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o numero ao quadrado."""

try:
    num = float(input("Informe um número: "))

    if num > 0:
        print(f"Número positivo. Sua raiz quadrada é {num**0.5}")
    else:
        print(f"Número negativo. Seu quadrado é {num*num}")
except:
    print("Tente novamente.")