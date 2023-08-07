"""22. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são

- Ter pelo menos 65 anos,
- Ou ter trabalhado pelo menos 30 anos,
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos."""


def aposenta(idade=int, tempo=int) -> str:
    """Recebe como parâmetro a idade do trabalhador e o tempo de serviço para anilisar aposentadoria."""

    try:
        if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
            return "Pode se aposentar"
        else:
            return "Não pode se aposentar"
    except:
        print("Valor inválido.\nTente novamente")


try:
    idade, tempoServico = int(input("Informe a idade do trabalhador: ")), int(input("Informe o tempo de serviço, em anos: "))
    print(f"Situação de aposentadoria: {aposenta(idade,tempoServico)}")
except ValueError:
    print("Você deve digitar um número inteiro.\nTente novamente.")
