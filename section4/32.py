"""32.Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro."""

try:
    num = int(input("Informe um número inteiro: "))
    TriploSucessor = (num*30) + 1
    DobroAntecessor = (num*2) - 1
    print(f"""O triplo do número mais o sucessor é :{TriploSucessor}
O dobro do número menos o  antecessor é :{DobroAntecessor}""")
except:
    print("Tente novamente")