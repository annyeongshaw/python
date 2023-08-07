"""26. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km /l e escreva uma mensagem de acordo com
a tabela abaixo:

CONSUMO  | (Km/l) | MENSAGEM
menor que|   8    |Venda o carro!
entre    | 8 e 14 | Econômico!
maior que|   12   |Super econômico!"""


def consumoVeiculo(quilometrosLitros = float):
    """Está função retorna o quão econômico é o carro."""
    if quilometrosLitros < 8:
        return "Venda o carro!"
    elif quilometrosLitros < 14:
        return "Econômico!"
    else:
        return "Super econômico"


distance = float(input("Informe a distância em Km: "))
kmL = (distance/(float(input("Informe a quantidade de gasolina consumida no percurso: "))))
print(f"O veículo é :{consumoVeiculo(kmL)}")
