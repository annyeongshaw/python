"""18.Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. À
fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos."""

try:
    VolumeCubicos = float(input("Informe o volume em metros cúbicos: "))
    Litros = VolumeCubicos * 1000
    print(f"O volume em litros é {Litros}")
except:
    print("Informou algo errado.")