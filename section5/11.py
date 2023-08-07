"""11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8(2+5+1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem “Número inválido”."""

"""try:
    num = int(input("Informe um número: "))
    if num > 0:
        num = str(num).replace('',' ').split()
        num = [int(num) for num in num]
        print(f"A soma de todos os seus algarismos é {sum(num)}")
    else:
        print("número inválido")
except:
    print("Tente novamente.")    """



def somaAlgorismos(num=int) -> int:
    """Está função retorna a soma de todos os algorismos do valor dado como parâmetro"""
    soma=0
    num = str(num)
    soma = [soma+int(num) for num in num]
    #for x in num:
    #    soma += int(x)
    return sum(soma)


try:
    num = int(input("Informe um número inteiro: "))
    if num > 0:
        print(f'A soma dos algorismos é {somaAlgorismos(num)}')
    else:
        print(f"Número inválido")
except ValueError:
    print("Tente um número inteiro maior que zero.")