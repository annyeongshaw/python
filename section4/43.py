"""43-Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

- o total a pagar com desconto de 10%;
- o valor de cada parcela, no parcelamento de 3x sem juros;

- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des-
conto)

- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)"""

try:
    ValorTotal = float(input("Informe o valor total: "))
    print(f"""
    O total a pagar com 10%: R${ValorTotal*0.9}
    Parcelando em 3x sem juros. Cada parcela fica por: {ValorTotal/3}
    Comissão do vendedor para pagamento a vista: {(ValorTotal*0.9)*0.05}
    comissão do vendedor para pagamento parcelado {ValorTotal*0.05}""")
except:
    print("Tente novamente")