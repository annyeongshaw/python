"""29. Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na
tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou."""
import random 

acerto=0
perguntaRespostas = []
for i in range(1,6):
    a, b = random.randint(2,99), random.randint(2,99)
    resposta = int(input(f"{a} + {b} = "))
    if resposta == (a+b):
        acerto+=1
        perguntaRespostas.append(f"{a} + {b} = {a+b}")

print("Pergunta e resposta corretas: ")

for i in perguntaRespostas:
    print (i)

print(f"Você acertou {acerto} pergunta(s) de um total de 5.")