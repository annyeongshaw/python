"""24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS
8%). Faça um programa em que o usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem
de erro."""

def tax(valor=float, estado=str) -> float:
    if estado == "MG":
        return (valor*0.07) + valor
    elif estado == "SP":
        return (valor*0.12) + valor
    elif estado == "RJ":
        return (valor*0.15) + valor
    elif estado == "Ms":
        return (valor*0.08) + valor
    else:
        raise ("Error.")


valorProduto = float(input("Informe o valor do produto: "))
estado = str(input("""Escolha uma das opções:
Minas Gerais: MG
São Paulo: SP
Rio de Janeiro:RJ
Mato Grosso do Sul:MS
Escolha o estado pela sigla: """).upper())
if estado in ("MG","SP","RJ","MS"):
    print(f"O valor final é R${tax(valorProduto,estado):.2f}")
else:
    print("Error. Estado inválido.\nTente novamente.")