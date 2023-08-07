"""35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28
dias em anos não bissextos."""


def verificaBissexto(ano=int) -> bool:
    """Verifica se o ano dado como parâmetro é bissexto."""
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False


def verificaValidadeData(dia=int, mes=int, ano=int) -> str:
    """Verifica se a data é válida."""
    if mes > 0 and mes <= 12:
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


data = int(input("Informe o dia: ")), int(input("Informe o mês: ")), int(input("Informe o ano: "))
if verificaValidadeData(data[0],data[1],data[2]):
    print("Data válida.")
else:
    print("Data inválida.")