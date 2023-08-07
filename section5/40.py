"""40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo
de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao
consumidor.

CUSTO DE FÁBRICA	                  | % comissão DO DISTRIBUIDOR | % DOS IMPOSTOS
até R$12.000,00 	                  | 5 		                   |isento
entre R$12.000,00 e 25.000,00(incluso)| 10		                   | 15
acima de R$25.000,00 	              | 15	                       |20.
"""


def CustoConsumidor(custoFabricar=float):
    if 0 <= custoCarroFabrica <= 12_000:
        return custoCarroFabrica + (custoCarroFabrica*0.05)
    elif 12_000 < custoCarroFabrica <= 25_000:
        return custoCarroFabrica + (custoCarroFabrica*0.1) + (custoCarroFabrica*0.15)
    else:
        return custoCarroFabrica + (custoCarroFabrica*0.15) + (custoCarroFabrica*0.20) 


custoCarroFabrica = float(input("Informe qual foi o custo para fabricação: "))
print(f"Custo final para o consumidor: R$ {CustoConsumidor(custoCarroFabrica):.2f}")
