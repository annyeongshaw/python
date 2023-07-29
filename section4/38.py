"""38.Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%."""

try:
    salario = float(input("Informe o salário do funcionário: "))
    print(f"O novo salário do funcionário é {salario*1.25}")
except:
    print("Tente novamente")