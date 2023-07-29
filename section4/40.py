"""40.Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda."""

try:
    diasTrabalhados = int(input("Informe os dias trabalhos:"))
    dinheiro = (30*diasTrabalhados)*0.92
    print(f"O salário será de {dinheiro}")
except:
    print("Tente novamente.")