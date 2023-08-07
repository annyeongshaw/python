"""31. Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa.

Altura        |Peso

              |Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90
Menor que 1,20| A      |D                          |G
De 1,20 a 1,70| B      |E                          |H
Maior que 1,70| C      |F                          |I
"""


def classifica(altura=float,peso=float):
    if altura < 1.20:
        if peso <= 60:
            return "A"
        elif peso <= 90:
            return "D"
        else:
            return "G"
    elif altura <= 1.70:
        if peso <= 60:
            return "B"
        elif peso <= 90:
            return "E"
        else:
            return "H"
    else:
        if peso <= 60:
            return "C"
        elif peso <= 90:
            return "F"
        else:
            return "I"
        
    

altura, peso = float(input("Informe a altura: ")), float(input("Informe o peso: "))
print(f"Você está na categoría {classifica(altura, peso)}")

