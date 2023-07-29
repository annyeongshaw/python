"""30.Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares."""

try:
    real = float(input("Informe a quantia em reais: "))
    cotacao = float(input("Informe a cotação atual do dolar: "))
    print(f"A quantia em dolas é {real*cotacao} dolas")
except:
    print("Informou algo errado.")

