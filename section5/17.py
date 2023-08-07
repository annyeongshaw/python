"""17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

A = ((basemaior + basemenor) * altura)/2

Lembre-se a base maior e a base menor devem ser números maiores que zero."""


def areaTrapezio(baseM = float, baseMe=float, altura=float) -> float:
    """Calcula  a área de um trapézio"""
    return ((baseM + baseMe)*altura)/2


baseMaior, baseMenor = float(input("Informe a base maior do trapézio: ")), float(input("Informe a base menor do trapézio: ")) 
altura = float(input("Informe a altura do trapézio: "))
if baseMaior > 0 and baseMenor > 0:
    print(f"A área do trapézio é {areaTrapezio(baseMaior,baseMenor,altura):.2f}")
else:
    raise ValueError("As bases devem ser números maiores que zero.")