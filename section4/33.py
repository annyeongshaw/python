"""33.Leia o tamanho do lado de um quadrado e imprima como resultado a sua área."""

try:
    side = float(input("Informe o tamanho do lado do quadrado: "))
    print(f"O lado do quadrado é igual a {side**2}")
except:
    print("Tente novamente")
