"""42.Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base."""

try:
    SalarioBase = float(input("Informe o salário base do funcionário:"))
    gratificacao = SalarioBase*0.05
    imposto = SalarioBase*0.07
    print(f"O salário do funcionário é {SalarioBase+gratificacao-imposto}")
except:
    print("Tente novamente")