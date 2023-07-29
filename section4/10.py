"""10- Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s."""

try:
    QuilometrosHora = float(input("Informe a velocidade em Km/h: "))
    MetrosSegundo = QuilometrosHora/3.6
    print(f"A velocidade em m/s é {MetrosSegundo}")
except:
    print("Informou um valor inválido.")