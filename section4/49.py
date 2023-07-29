"""49.Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma."""


def converteSeg(tempoSeg=int)->tuple:
    horas = tempoSeg // 3600
    segundos = tempoSeg % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return horas, minutos, segundos


try:
    hora, minuto, segundo = int(input("Informe a hora:")), int(input("Agora informe os minutos:")),int(input("agora informe os segundos:"))
    duracao = int(input("Informe a duração do experimento, em segundos: "))
    horas, minutos, segundos = converteSeg(duracao)
    horas, minutos, segundos = hora+horas, minutos+minuto, segundos+segundo
    print(f"O experimento durou cerca de {horas-hora}h{minutos-minuto}min{segundos-segundo}seg")
except:
    print("Tente novamente")



