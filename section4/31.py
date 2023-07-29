"""31.Leia um número inteiro e imprima o seu antecessor e o seu sucessor."""

try:
    num = int(input("Informe um número inteiro: "))
    print(f"O antecessor desse número é {num-1} e o seu sucessor é {num+1}")
except:
    print("Tente novamente")