"""33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
Calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de
acordo com a segunda tabela).

Preço Antigo        |percentual de aumento
até R$ 50           |     5%    
entre R$ 50 e R$ 100|     10%
acima de R$ 100     |     15%

preço novo                       | mensagem
até R$ 80                        |  barato
entre R$ 80 e R$ 120 (inclusive) | normal
entre R$ 120 e R$ 200 (inclusive)|caro
acima de R$ 200                  | muito caro"""


def mensagem(preco= float):
    if preco <= 80:
        return "barato"
    elif preco <= 120:
        return "normal"
    elif preco <= 200:
        return "caro"
    else:
        return "muito caro" 

def aumento(precoOld=float):
    if precoOld <= 50:
        precoNovo = precoOld*0.05 + precoOld
        return precoNovo, mensagem(precoNovo)
    elif precoOld <= 100:
        precoNovo = precoOld*0.1 + precoOld
        return precoNovo, mensagem(precoNovo)
    else:
        precoNovo = precoOld*0.15 + precoOld
        return precoNovo, mensagem(precoNovo)
    

precoOld = float(input("Informe o preço antigo do produto: "))
print(f"Com o aumento o preço foi para {aumento(precoOld)[0]}. Valor novo é {aumento(precoOld)[1]}")