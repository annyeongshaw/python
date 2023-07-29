"""19.Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m?. À
fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros
cúbicos."""

try:
    Litros = float(input("Informe o volume em litros: "))
    VolumeCubicos = Litros/1000
    print(f"O volume em metros cúbicos  é {VolumeCubicos}")
except:
    print("Informou algo errado.")