"""23. Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo:
1988, 1992, 1996"""


def verificaBissexto(ano=int) -> str:
    """Verifica se o ano dado como parâmetro é bissexto."""

    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return "é bissexto."
    else:
        return "não é bissexto."


try:
    year = int(input("Informe o ano que será analisado: "))
    print(f"O ano {year} {verificaBissexto(year)}")
except ValueError:
    print("O ano deve ser um número inteiro.")