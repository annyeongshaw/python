"""38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste
se o dia fornecido é um dia válido: dia > O, dia < 28 para o mês de fevereiro (29 se o
ano for bissexto), dia < 30 em abril, junho, setembro e novembro, dia < 31 nos outros
meses. Teste a validade do mês: mês > O e mês < 13. Teste a validade do ano: ano <
ano atual. Imprimir: “data válida” ou “data inválida” no final da execução do programa."""

def verificaBissexto(ano=int) -> bool:
    """Verifica se o ano dado como parâmetro é bissexto."""
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False


def verificaValidadeData(dia=int, mes=int, ano=int) -> str:
    """Verifica se a data é válida."""
    if mes > 0 and mes <= 12:
        if ano < (int(input("Informe o ano atual: "))):
            if mes == 2:
                if verificaBissexto(ano):
                    return 1 <= dia <= 29
                elif not (verificaBissexto(ano)):
                    return 1 <= dia < 29
                else:
                    return False
            elif mes in (4,6,9,11):
                return 1 <= dia <= 30 
            else:
                return 1 <= dia <= 31
        else:
            return False
    else:
        return False


data = int(input("Informe o dia: ")), int(input("Informe o mês: ")), int(input("Informe o ano: "))
if verificaValidadeData(data[0],data[1],data[2]):
    print("Data válida.")
else:
    print("Data inválida.")