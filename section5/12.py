"""12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número
inválido”. Se o número for positivo, calcular o logaritmo deste numero."""
from math import log


try:
    num = int(input("Informe um número inteiro: "))
    if num > 0:
        print(f"O logaritmo de {num} é igual a {log(num):.2f}")
    else:
        print("Número inválido")
except:
    print("Tente novamente")    