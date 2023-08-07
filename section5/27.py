"""27. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:

Categoria | Idade
Infanti A | 5 a 7
Infantil B| 8 a 10
Juvenil A | 11 a 13
Juvenil B | 14 a 17
Sênior maiores de 18 anos"""


def categoriaNadador(age=int) -> str:
    """Está função retorna a categoria do nadador de acordo com a idade do mesmo."""
    if age >= 5 and age <= 7:
        return "Infantil A"
    elif age >= 8 and age <= 10:
        return "Infantil B"
    elif age >= 11 and age <= 13:
        return "Juvenil A"
    elif age >= 14 and age <= 17:
        return "Juvenil B"
    elif age >= 18:
        return "Sênior"
    else:
        return "Idade inferior a 5 anos."
    


idade = int(input("Informe a idade do nadador: "))
print(f"O nadador se encontra na categoria: {categoriaNadador(idade)}")