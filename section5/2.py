"""2. Leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""


try:        
    num = int(input("Informe um número inteiro: "))
    if num < 0:
        print("Número inválido.")
    else:
        print(f"O quadrado desse número é {num**(0.5):.3f}")
except:
    print("Tente novamente.")