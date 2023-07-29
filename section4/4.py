"""
4- Leia um número real e imprima o resultado do quadrado desse número.
"""
try:
    num = float(input("Informe um número: "))
    print(f"O quadrado do número é {num*num}")
except (ValueError, TypeError):
    print("Você fez alguma coisa errada.\nTente executar o script novamente.")
