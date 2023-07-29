"""28.Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos."""

try:
    nums = []
    for i in range(3):
        nums.append(float(input("Informe um número: ")))
    soma = sum([x*x for x in nums])
    print(f"A soma dos quadrados dos valores é {soma}")
except:
    print("Informou algo errado.")