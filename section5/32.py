"""32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lan-
Chonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lan-
Chonete segue o padrão abaixo:

Especificação   |Código | Preço
Cachorro Quente | 100   | 1.20
Bauru Simples   | 101   | 1.30
Bauru com Ovo   | 102   | 1.50
Hamburguer      | 103   | 1.20
Cheeseburguer   | 104   | 1.70
[Suco           | 105   | 2.20
Refrigerante    | 106   | 1.00"""


def valorFinal(codigoProduto= int, quantidadeProduto= int):
    if codigoProduto == 100:
        return 1.2 * quantidadeProduto
    elif codigoProduto == 101:
        return 1.3 * quantidadeProduto
    elif codigoProduto == 102:
        return 1.5 * quantidadeProduto
    elif codigoProduto == 103:
        return 1.2 * quantidadeProduto
    elif codigoProduto == 104:
        return 1.7 * quantidadeProduto
    elif codigoProduto == 105:
        return 2.2 * quantidadeProduto
    elif codigoProduto == 106:
        return 1 * quantidadeProduto
    else:
        return "código inválido."



print("""|________________________________
|Especificação   |Código | Preço |
|----------------|-------|-------|
|Cachorro Quente | 100   | 1.20  |
|----------------|-------|-------|
|Bauru Simples   | 101   | 1.30  |
|----------------|-------|-------|
|Bauru com Ovo   | 102   | 1.50  |
|----------------|-------|-------|
|Hamburguer      | 103   | 1.20  |
|----------------|-------|-------|
|Cheeseburguer   | 104   | 1.70  |
|----------------|-------|-------|
|Suco            | 105   | 2.20  |
|----------------|-------|-------|
|Refrigerante    | 106   | 1.00  |
|________________|_______|_______|""")

codigo, quantidade = int(input("Informe o código: ")), int(input("Informe a quantidade do produto: "))
print(f"Preço final R$ {valorFinal(codigo,quantidade):.2f}")
