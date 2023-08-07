"""8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina."""


try:
    media = []
    for i in range(1,3):
        num = int(input(f"Informe a {1}° nota do aluno: "))
        if num >= 0 and num <=10:
            media.append(num)
        else: 
            break


    print(f"A média final do aluno é {sum(media)/2:.2f}")

except:
    print("Tente novamente.")