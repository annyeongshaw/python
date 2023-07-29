"""53.Faça um programa para ler as dimensões de um terreno (comprimento c e largura L),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.
"""

def calculaCustoCercamento(comprimento=float, largura=float, precoTela=float) -> float:
    perimetroTerreno = (comprimento+largura)*2
    return perimetroTerreno*precoTela

try:
    comprimento, largura = float(input("Informe o comprimento do terreno, em metros: ")), float(input("Informe a largura do terreno, em metros: "))
    precoCercarTela = float(input("Informe o preço por metro da tela: "))
    custoTotal = calculaCustoCercamento(comprimento, largura, precoCercarTela)
    print(f"O custo para cercar o terreno: R${custoTotal:.2f}")
except:
    print("Entrada inválida. Certifique-se de digitar valores válidos para as dimensões do terreno e o preço da tela.") 

""" def calcular_custo_cercamento(comprimento, largura, preco_tela):
    perimetro = 2 * (comprimento + largura)
    custo_cercamento = perimetro * preco_tela
    return custo_cercamento


try:
    comprimento = float(input("Digite o comprimento do terreno (em metros): "))
    largura = float(input("Digite a largura do terreno (em metros): "))
    preco_tela = float(input("Digite o preço do metro de tela (em reais): "))
    
    custo_total = calcular_custo_cercamento(comprimento, largura, preco_tela)
    print(f"O custo para cercar o terreno é de R$ {custo_total:.2f}")
    
except ValueError:
    print("Entrada inválida. Certifique-se de digitar valores válidos para as dimensões do terreno e o preço da tela.") """

