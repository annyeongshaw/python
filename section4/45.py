"""45.Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema."""

try:
    def letraMaiuscula(caractere=str) -> str:
        if "A" <= caractere <= "Z":
            letraMinuscula = chr(ord(caractere)+32)
            return letraMinuscula
        elif "a" <= caractere <= "z":
            return caractere
        else:
            return ("Valor inválido")

    letra = input("Infome uma letra maiuscula para ser convertida em minúscula: ")
    print(letraMaiuscula(letra))
except:
    print("Tente novamente")