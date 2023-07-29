"""
2- Faça um programa que leia um número real e o imprima.
"""

try:
   num = float(input("Informe um número: "))
   print(f"Você digitou {num}")
except:
    print("Você fez alguma coisa errada.\nTente executar o script novamente.")
