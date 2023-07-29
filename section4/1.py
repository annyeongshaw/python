"""
1- Faça um programa que leia um número inteiro e o imprima.
"""
try:
   num = int(input("Informe um número inteiro: "))
   print(f"Você digitou {num}")
except:
    print("Você fez alguma coisa errada.\nTente executar o script novamente.")