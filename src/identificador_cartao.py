import re


def validar_cartao(numero_cartao):
    """
    Valida o número do cartão usando o algoritmo de Luhn.
    """
    numero = str(numero_cartao).replace(" ", "")
    if not numero.isdigit():
        return False

    soma = 0
    inverso = numero[::-1]
    for i, digito in enumerate(inverso):
        n = int(digito)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        soma += n

    return soma % 10 == 0


def identificar_bandeira(numero_cartao):
    """Identifica a bandeira do cartão de crédito."""
    numero = str(numero_cartao)
    numero = re.sub(r"\s+", "", numero)  # Remove todos os espaços

    if not validar_cartao(numero):
        print("Número de cartão inválido.")
        return

    bandeiras = [
        (r"^4\d{12}(\d{3})?$", "Visa"),
        (
            r"^(5[1-5]\d{14}|2("
            r"2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$",
            "Mastercard",
        ),
        (r"^3[47]\d{13}$", "American Express"),
        (r"^6(?:011\d{12}|5\d{14}|4[4-9]\d{13})$", "Discover"),
        (r"^35\d{14}$", "JCB"),
        (r"^3(?:6\d{12}|8\d{12})$", "Diners Club"),
        (r"^(606282\d{10}(\d{3})?|3841\d{15})$", "Hipercard"),
        (r"^50\d{14,17}$", "Aura"),
        (r"^(2014|2149)\d{11}$", "EnRoute"),
        (r"^(7088|8699)\d{10,12}$", "Voyager"),
    ]

    for padrao, nome in bandeiras:
        if re.match(padrao, numero):
            print(nome)
            return

    print("Bandeira desconhecida")


if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    identificar_bandeira(numero)
