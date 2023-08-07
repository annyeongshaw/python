"""37. As tarifas de certo parque de estacionamento são as seguintes:

- 1º e 2º hora - R$ 1,00 cada
- 3º e 4º hora - R$ 1,40 cada
- 5º hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida
deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará “dez para a uma da tarde”. Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com
intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior
à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no
dia seguinte ao da chegada."""

def calcular_preco_estacionamento(chegada, partida):
    chegada_minutos = chegada[0] * 60 + chegada[1]
    partida_minutos = partida[0] * 60 + partida[1]
    diferenca_minutos = partida_minutos - chegada_minutos
    numero_horas = -(-diferenca_minutos // 60)  # Técnica para arredondar para cima
    if numero_horas <= 2:
        return numero_horas * 1.00
    elif numero_horas <= 4:
        return 2 * 1.00 + (numero_horas - 2) * 1.40
    else:
        return 2 * 1.00 + 2 * 1.40 + (numero_horas - 4) * 2.00
    

chegadaHora,chegadaMinuto = int(input("Digite a hora de chegada: ")), int(input("Digite o minuto de chegada: "))
partidaHora, partidaMinuto  = int(input("Digite a hora de partida: ")), int(input("Digite o minuto de partida: "))

print(f"O preço cobrado pelo estacionamento é R$ {calcular_preco_estacionamento((chegadaHora, chegadaMinuto), (partidaHora, partidaMinuto)):.2f}")

