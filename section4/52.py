"""52.Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido. formula porcetagemIndividual = (100*investido)/total"""


""" def divisaoPremio(investido=list, total=float) -> list:
    
    '''Essa função recebe como parâmetro o quanto foi investido por cada pessoa e o total do prêmio. Retorna o porcentual de cada investidor'''
    
    porcentualIndidual = []
    for i in range(3):
        p = ((investido[i]*100)/total)/100
        porcentualIndidual.append(p)
    return porcentualIndidual
    

premio = float(input("Informe o prêmio da loteria: "))
pessoas = []
for i in range(1,4):
    pessoas.append(float(input(f"Informe quanto o {i}° amigo investiu: ")))
print(pessoas)
totalInvestido = float(sum(pessoas))
print(totalInvestido)
percentual = divisaoPremio(pessoas, totalInvestido)
print(percentual)
print(f'''
O primeiro amigo investiu R${pessoas[0]} e receberá do prêmio {(percentual[0]*100):.2f}%. O que da o valor de R${premio*percentual[0]:.2f} do prêmio
O segundo amigo investiu R${pessoas[1]} e receberá do prêmio {(percentual[1]*100):.2f}%. O que da o valor de R${premio*percentual[1]:.2f} do prêmio
O terceiro amigo investiu R${pessoas[2]} e receberá do prêmio {(percentual[2]*100):.2f}%. O que da o valor de R${premio*percentual[2]:.2f} do prêmio''') """


def calcular_proporcao(valor_investido, total_investido):
    return valor_investido / total_investido

def calcular_premio_ganhado(proporcao, premio_total):
    return proporcao * premio_total


try:
    investimento_amigo1 = float(input("Digite o valor investido pelo primeiro amigo: "))
    investimento_amigo2 = float(input("Digite o valor investido pelo segundo amigo: "))
    investimento_amigo3 = float(input("Digite o valor investido pelo terceiro amigo: "))
    
    premio_total = float(input("Digite o valor total do prêmio: "))
    
    total_investido = investimento_amigo1 + investimento_amigo2 + investimento_amigo3
    
    proporcao_amigo1 = calcular_proporcao(investimento_amigo1, total_investido)
    proporcao_amigo2 = calcular_proporcao(investimento_amigo2, total_investido)
    proporcao_amigo3 = calcular_proporcao(investimento_amigo3, total_investido)
    
    premio_amigo1 = calcular_premio_ganhado(proporcao_amigo1, premio_total)
    premio_amigo2 = calcular_premio_ganhado(proporcao_amigo2, premio_total)
    premio_amigo3 = calcular_premio_ganhado(proporcao_amigo3, premio_total)
    
    print(f"O primeiro amigo ganharia: R$ {premio_amigo1:.2f}")
    print(f"O segundo amigo ganharia: R$ {premio_amigo2:.2f}")
    print(f"O terceiro amigo ganharia: R$ {premio_amigo3:.2f}")
    
except ValueError:
    print("Entrada inválida. Certifique-se de digitar valores válidos para os investimentos e o prêmio.")

