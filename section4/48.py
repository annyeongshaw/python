"""48.Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

def converteSeg(tempoSeg=int)->tuple:
    horas = tempoSeg // 3600
    segundos = tempoSeg % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return horas, minutos, segundos

try:
    tempo = int(input("Informe o tempo em segundos: "))
    horas, minutos, segundos = converteSeg(tempo)
    print(f"{tempo} segundos é igual a {horas}h{minutos}min{segundos}s")
except:
    print("Tente novamente")