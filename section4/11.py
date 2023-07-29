"""11.Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
emkm/h e M em m/s."""

try:
    MetrosSegundo = float(input("Informe a velocidade em Km/h: "))
    QuilometrosHora = MetrosSegundo * 3.6
    print(f"A velocidade em Km/h é {QuilometrosHora}")
except:
    print("Informou um valor inválido.")