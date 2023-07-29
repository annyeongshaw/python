"""
3- Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
"""
try:
    nums=[]
    for num in range(3):
        nums.append(int(input("Informe um número inteiro: ")))

    soma = sum(nums)

    print(f"A soma dos números digitados é {soma}")
except:
    print("Você fez alguma coisa errada.\nTente executar o script novamente.")