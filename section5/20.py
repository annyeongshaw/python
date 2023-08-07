"""20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguin-
tes conceitos:

- O comprimento de cada lado de um triângulo é menor do que a soma dos outros
dois lados.

- Chama-se equilátero o triângulo que tem três lados iguais.

- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.

- Recebe o nome de escaleno o triângulo que tem os três lados diferentes."""

def verificaExistencia(ladoA=float, ladoB=float, ladoC=float) -> str:
    if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
        if ladoA == ladoB and ladoA == ladoC:
            return "Triângulo equilátero"
        elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            return "Triânfulo isosceles"
        else:
            return "Triângulo escaleno"
    else:
        raise TypeError("Não é um triângulo.")

A , B, C = float(input("Informe o tramanho do lado A:")), float(input("Informe o tramanho do lado B:")), float(input("Informe o tramanho do lado C:"))
print(verificaExistencia(A, B, C))