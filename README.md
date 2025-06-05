# Credit Card Brand Identifier

Este projeto tem como objetivo identificar a bandeira de um cartão de crédito a partir do número informado pelo usuário. O programa utiliza o algoritmo de Luhn para validar o número do cartão e, em seguida, identifica a bandeira com base em padrões conhecidos.

## Funcionalidades

- **Validação do número do cartão:** Utiliza o algoritmo de Luhn para verificar se o número informado é válido.
- **Identificação da bandeira:** Reconhece as principais bandeiras de cartão de crédito, incluindo:
  - Visa
  - Mastercard
  - American Express
  - Discover
  - JCB
  - Diners Club
  - Hipercard
  - Aura
  - EnRoute
  - Voyager
- **Mensagem para cartões inválidos ou bandeiras desconhecidas.**

## Como usar

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Clone este repositório ou baixe os arquivos.
3. No terminal, navegue até a pasta do projeto.
4. Execute o arquivo identificador_cartao.py
5. Digite o número do cartão quando solicitado.

## Exemplo de uso

Digite o número do cartão: 4111111111111111 Visa
Digite o número do cartão: 6011111111111117 Discover
Digite o número do cartão: 1234567890123456 Número de cartão inválido.

## Estrutura do Projeto
. ├── README.md └── src └── identificador_cartao.py

O arquivo principal é [`src/identificador_cartao.py`](src/identificador_cartao.py), que contém duas funções principais:

- [`validar_cartao`](src/identificador_cartao.py): Valida o número do cartão usando o algoritmo de Luhn.
- [`identificar_bandeira`](src/identificador_cartao.py): Identifica a bandeira do cartão com base em expressões regulares.
