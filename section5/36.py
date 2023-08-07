"""36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

Venda mensal                                          | Comissão
Maior ou igual a R$100.000,00                         | R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00 | R$650,00 +14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00  | R$600,00 +14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00  | R$550,00 +14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00  | R$500,00 +14% das vendas
Menor que R$20.000,00                                 |R$400,00 +14% das vendas"""

def comissao(vendaMensal= float):
    """Retorna a comissão do vendedor."""
    if vendaMensal >= 100_000:
        return 700 + (vendaMensal*0.16)
    
    elif 100_000 > vendaMensal >= 80_000:
        return 650 + (vendaMensal*0.14)
    
    elif 80_000 > vendaMensal >=60_000:
        return 600 + (vendaMensal*0.14)
    
    elif 60_000 > vendaMensal >= 40_000:
        return 550 + (vendaMensal*0.14)
    
    elif 40_000 > vendaMensal >= 20_000:
        return 500 + (vendaMensal*0.14)
    
    elif 20_000 > vendaMensal >= 0:
        return 400 + (vendaMensal*0.14)
    
    else:
        return 0



VendasMes = float(input("Quanto foi vendido pelo vendedor: "))
print(f"A comissão do vendedor é {comissao(VendasMes)}")