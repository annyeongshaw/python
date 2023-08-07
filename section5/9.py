"""9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: Empréstimo não concedido, Caso
contrário imprima: Empréstimo concedido."""


try:
    salarioTrabalhador = float(input("Informe o salário do trabalhador: "))
    emprestimo = float(input("Informe quanto você deseja de emprestimo: "))
    prestacao = salarioTrabalhador*0.2

    if emprestimo > prestacao:
        print("Empréstimo não concedido.")
    else:
        print("Emprestimo concedido.")
except:
    print("Tente novamente.")