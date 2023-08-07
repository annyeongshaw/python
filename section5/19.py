"""19. Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou
5, mas não simultaneamente pelos dois."""

num = int(input("Informe um número inteiro: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} é divisível por 3 e 5 simultaneamente")
elif num % 3 == 0:
    print(f"{num} é um número divisível por 3.")
elif num % 5 == 0:
    print(f"{num} é um número divisível por 5.")
else:
    print(f"{num} não é divisível nem por 3 nem por 5")