"""39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários
com menor salário terão um aumento proporcionalmente maior do que os funcionários
com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá
receber um bônus adicional de salário. Faça um programa que leia:

- o valor do salário atual do funcionário;
- o tempo de serviço desse funcionário na empresa (número de anos de trabalho na
empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o
valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito
a nenhum aumento.

Salário Atual	 | Reajuste(%)  | Tempo de Serviço    | Bônus
Até 500,00  	 | 25%		    | Abaixo de 1 ano     |  Sem bônus
Até 1000,00  	 | 20%		    | De 1 a 3 anos       | 100,00
Até 1500,00      | 15%	    	| De 4 a 6 anos	      | 200,00
Até 2000,00      | 10%		    | De 7 a 10 anos      | 300,00
Acima de 2000,00 | Sem reajuste | Mais de 10 anos     |500,00"""


def aumento(salario=float, tempo=int):
    """Reajuste de salário atual dos funcionários, de acordo com o tempo de serviço."""
    if 0 < salario <= 500:
        if tempo < 1:
            return salario + (salario*0.25)
        elif 1 <= tempo <= 3:
            return salario + (salario*0.25) + 100
        elif 4 <= tempo <= 6:
            return salario + (salario*0.25) + 200 
        elif 7 <= tempo <= 10:
            return salario + (salario*0.25) + 300
        else:
            return salario + (salario*0.25) + 500
    elif salario <= 1000:
        if tempo < 1:
            return salario + (salario*0.20)
        elif 1 <= tempo <= 3:
            return salario + (salario*0.20) + 100
        elif 4 <= tempo <= 6:
            return salario + (salario*0.20) + 200 
        elif 7 <= tempo <= 10:
            return salario + (salario*0.20) + 300
        else:
            return salario + (salario*0.20) + 500
    elif salario <= 1500:
        if tempo < 1:
            return salario + (salario*0.15)
        elif 1 <= tempo <= 3:
            return salario + (salario*0.15) + 100
        elif 4 <= tempo <= 6:
            return salario + (salario*0.15) + 200 
        elif 7 <= tempo <= 10:
            return salario + (salario*0.15) + 300
        else:
            return salario + (salario*0.15) + 500
    elif salario <= 2000:
        if tempo < 1:
            return salario + (salario*0.10)
        elif 1 <= tempo <= 3:
            return salario + (salario*0.10) + 100
        elif 4 <= tempo <= 6:
            return salario + (salario*0.10) + 200 
        elif 7 <= tempo <= 10:
            return salario + (salario*0.10) + 300
        else:
            return salario + (salario*0.10) + 500
    else:
        if tempo < 1:
            return salario
        elif 1 <= tempo <= 3:
            return salario + 100
        elif 4 <= tempo <= 6:
            return salario +  200 
        elif 7 <= tempo <= 10:
            return salario + 300
        else:
            return salario +  500

salarioAtual, tempoServico = float(input("Informe o salário atual: ")), int(input("Informe quanto tempo, o funcionário, tem de serviço:"))
print(f"O seu novo salário será : {aumento(salarioAtual,tempoServico)}")
