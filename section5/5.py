"""5. Faça um programa que receba um número inteiro e verifique se este número é par ou
ímpar."""

try:
    def verificador(num=int) -> str:
        """Esta funçao retorna se o parâmento é par ou impar."""
        try:
            if num % 2 == 0:
                return "par"
            else:
                return "impar"
        except:
            print("Tente novamente.")


    num = int(input("Informe um número: "))
    print(f"{num} é {verificador(num)}")
except:
    print("Tente novamente")