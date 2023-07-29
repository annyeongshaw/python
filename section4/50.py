"""50.Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual."""

try:
    ano, idade = int(input("Informe o ano atual: ")), int(input("Informe sua idade atual: "))
    print(f"O ano de nascimento é {ano-idade}")
except:
    print("Tente novamente.")