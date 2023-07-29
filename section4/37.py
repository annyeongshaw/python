"""37.Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%"""

try:
    valorProduto = float(input("Informe o valor do produto para será aplicado o desconto: "))
    desconto = valorProduto*0.12
    print(f"O valor final com desconto será {valorProduto-desconto}")
except:
    print("Tente novamente.")