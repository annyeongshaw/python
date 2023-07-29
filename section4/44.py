"""44.Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo."""

try:
    alturaDegrau, alturaEscada = float(input("Informe a altura do degrau da escada, em centimetros: ")), float(input("Informe a altura da escada, em centimetros: "))
    print(f"A quantidade de degraus é {int(alturaEscada/alturaDegrau)}")
except:
    print("Tente novamente")