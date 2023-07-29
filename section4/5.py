"""
5- Leia um número real e imprima a quinta parte deste número.
"""
try:
    num = float(input("Informe um número: "))
    print(f"A quinta parte desse número é {num/5}")
except:
    print("Você fez alguma coisa errada.\nTente executar o script novamente.")