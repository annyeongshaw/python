"""25. Calcule as raízes da equação de 2º grau.
Lembrando que:
x = (-b +- (delta)elevadoaoquadrado)/2a
Onde: 
delta = B² — 4ac
e ax² + bx + c = O representa uma equação de 2º grau.
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não
é equação de segundo grau”.
- Se delta < 0, não existe real. Imprima a mensagem Não existe raiz.
- Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
- Se delta >= 0, imprima as duas raízes reais."""


def raizQuadrada(a=float,b=float,c=float):
    """Calcula a raiz quadrada"""
    delta = (b**2) - (4*a*c)
    x = (-b + (delta)**0.5)/(2*a)
    x2 = (-b - (delta)**0.5)/(2*a)
    if delta < 0:
        return "Não existe raiz!!!"
    elif delta == 0:
        if x > 0:
            return f"A raiz unica é {x}"
        else:
            return f"A raiz única é {x2}"
    else:
        return f"A raizes são {x} e {x2}"


try:
    a, b = float(input("Informe o valor de (a) da equação de 2 grau: ")),float(input("Informe o valor de (b) da equação de 2 grau: "))
    c = float(input("Informe o valor de (c) da equação de 2 grau: "))
    if a == 0:
        print("(a) Não pode ser zero.")
    else:
        print(f"{raizQuadrada(a,b,c)}")
except ValueError as ve:
    print(f"Valor inválido: {ve}.")