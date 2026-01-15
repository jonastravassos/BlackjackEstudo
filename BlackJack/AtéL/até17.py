from random import randrange
from time import perf_counter
# from pandas import DataFrame

n = 1_000_000
n_vitorias = 0
n_derrotas = 0
n_empates = 0
'''import matplotlib.pyplot as plt

x = [i for i in range(1, n+1)]
y = []'''


class Carta:
    # Esta classe representa uma carta de baralho.
    def __init__(self, naipe: str, valor: str):
        """
        naipe: representa o naipe da carta. O naipe é irrelevante para o blackjacks, mas pode ser útil caso o projeto
        seja expandido e o naipe tenha significado em outro jogo de cartas.

        valor: representa o valor da carta, sendo um número natural de 2 a 10 ou as letras do baralho (A, J, Q, K).
        """
        self.naipe = naipe
        self.valor = valor
        if self.valor.isnumeric(): self.valor_num = int(self.valor)
        elif self.valor == 'A': self.valor_num = 11
        else: self.valor_num = 10

    def __repr__(self):
        return f"Naipe: {self.naipe} | Valor: {self.valor}"


# Registra a carta do dealer nas vitórias, derrotas e empates.
melhor_decisao = {
    "4H": {'A': 0, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "5H": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "6H": {'A': 1, '2': 1, '3': 1, '4': 0, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "7H": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "8H": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "9H": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "10H": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "11H": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "12H": {'A': 1, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "13H": {'A': 1, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "14H": {'A': 1, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "15H": {'A': 1, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "16H": {'A': 1, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "17H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12S": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "13S": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "14S": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "15S": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "16S": {'A': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, 'J': 1, 'Q': 1, 'K': 1},
    "17S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "21S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
}

vitorias = {
    "4H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "5H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "6H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "7H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "8H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "9H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "10H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "11H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "13H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "14H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "15H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "16H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "17H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "13S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "14S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "15S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "16S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "17S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "21S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
}

derrotas = {
    "4H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "5H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "6H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "7H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "8H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "9H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "10H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "11H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "13H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "14H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "15H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "16H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "17H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "13S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "14S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "15S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "16S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "17S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "21S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
}

empates = {
    "4H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "5H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "6H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "7H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "8H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "9H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "10H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "11H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "13H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "14H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "15H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "16H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "17H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20H": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "12S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "13S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "14S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "15S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "16S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "17S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "18S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "19S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "20S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0},
    "21S": {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
}

baralho = [
    Carta("Copas", "A"), Carta("Copas", "2"),
    Carta("Copas", "3"), Carta("Copas", "4"),
    Carta("Copas", "5"), Carta("Copas", "6"),
    Carta("Copas", "7"), Carta("Copas", "8"),
    Carta("Copas", "9"), Carta("Copas", "10"),
    Carta("Copas", "J"), Carta("Copas", "Q"),
    Carta("Copas", "K"), Carta("Ouros", "A"),
    Carta("Ouros", "2"), Carta("Ouros", "3"),
    Carta("Ouros", "4"), Carta("Ouros", "5"),
    Carta("Ouros", "6"), Carta("Ouros", "7"),
    Carta("Ouros", "8"), Carta("Ouros", "9"),
    Carta("Ouros", "10"), Carta("Ouros", "J"),
    Carta("Ouros", "Q"), Carta("Ouros", "K"),
    Carta("Espada", "A"), Carta("Espada", "2"),
    Carta("Espada", "3"), Carta("Espada", "4"),
    Carta("Espada", "5"), Carta("Espada", "6"),
    Carta("Espada", "7"), Carta("Espada", "8"),
    Carta("Espada", "9"), Carta("Espada", "10"),
    Carta("Espada", "J"), Carta("Espada", "Q"),
    Carta("Espada", "K"), Carta("Paus", "A"),
    Carta("Paus", "2"), Carta("Paus", "3"),
    Carta("Paus", "4"), Carta("Paus", "5"),
    Carta("Paus", "6"), Carta("Paus", "7"),
    Carta("Paus", "8"), Carta("Paus", "9"),
    Carta("Paus", "10"), Carta("Paus", "J"),
    Carta("Paus", "Q"), Carta("Paus", "K"),
] * 6


class Dealer:
    # Esta classe representa o dealer.
    def __init__(self):
        """
        cartas: é a mão do portador, o conjunto de cartas (deck).

        ases: às é uma carta especial que muda seu valor conforme for vantajoso ao portador, então contar a quantidade
        de ases na mão é necessário.

        soma: é soma total do valor das cartas, representando a pontuação do indivíduo.
        """
        self.cartas = list()
        self.ases = 0
        self.soma = 0
        self.busts = 0 # Quando ultrapassa 21.
        self.blackjacks = 0 # Vitória por blackjacks.

    def pedir(self):
        """
        Representa um pedido de carta. Quando o portador pede uma carta, a carta que vem é escolhida aleatoriamente
        através da função randrange(), essa carta é removida do baralho e depois é contabilizada na soma. Cartas
        númericas tem seu valor nominal, cartas não numéricas valem 10, exceto ás que a princípio vale 11.
        """
        esc = randrange(len(baralho))
        baralho[esc], baralho[-1] = baralho[-1], baralho[esc]
        top = baralho.pop()

        self.cartas.append(top)
        self.soma += top.valor_num

        if top.valor_num == 11: self.ases += 1
        self.contar_ases()

    def contar_ases(self):
        """
        Apesar da função se chamar contar_ases(), o que ela faz na verdade é contabilizar ases ('contar' surgiu porque é
        uma palavra mais curta). Ela diminue a soma em 10 caso ela seja maior 21 para cada ás contido na mão, assim,
        cada ás que atender a essas condições vale 1.
        """
        for i in range(self.ases):
            if self.soma > 21:
                self.soma -= 10
                self.ases -= 1

    def mostrar(self):
        # Mostra as cartas do dealer quando o jogador para.
        print("Cartas do Dealer:\n")
        for carta in self.cartas: print(carta)
        print("Total:", self.soma)

    def ver_carta(self):
        # Mostra apenas uma carta do dealer no ínicio de cada rodada, mostrando apenas a soma parcial.
        print("Cartas do Dealer:\n")
        print("Naipe: ??? | Valor: ???")
        print(self.cartas[0])

        if self.cartas[0].valor.isnumeric(): print("Total:", self.cartas[0])
        elif self.cartas[0].valor != "A": print("Total: 10")
        else: print("1 / 11")
        print("\n", end='')

    def resetar(self):
        # Reseta os atributos de rodada, útil para jogar o jogo novamente dentro da mesma execução.
        self.cartas.clear()
        self.ases = 0
        self.soma = 0


class Jogador(Dealer):
    # Esta classe representa o jogador.
    def __init__(self):
        super().__init__()
        self.vencedor = str()
        self.decisao = 1
        self.saldo = 0
        self.aposta = 1

    def mostrar(self):
        print("\033[36m")
        print("Cartas do Jogador:\n")

        for carta in jogador.cartas:
            print(carta)

        print(f"Total: {jogador.soma}")
        print("\033[m")

    def resetar(self):
        super().resetar()
        self.vencedor = str()
        self.decisao = 1
        self.aposta = 1

    def soft_hard(self):
        return f"{self.soma}{'S' if self.ases > 0 else 'H'}"

    def dobrar(self):
        self.aposta *= 2
        self.pedir()
        self.decisao = 0
        self.contar_ases()


def ver_dados():
    print('\n', end='')
    for k, v in vitorias.items():
        print(f"{k}: {v}")

    print('\n', end='')
    for k, v in derrotas.items():
        print(f"{k}: {v}")

    print('\n', end='')
    for k, v in empates.items():
        print(f"{k}: {v}")


def iniciar(dealer: Dealer, jogador: Jogador):
    # Função que inicia cada rodada. É chamada antes da função jogar().
    for i in range(2):
        jogador.pedir()
        dealer.pedir()

    # jogador.mostrar()
    # dealer.ver_carta()


def jogar(baralho: list, dealer: Dealer, jogador: Jogador):
    global n_vitorias
    global n_derrotas
    global n_empates
    pontos = jogador.soft_hard()
    pre_total = pontos

    while True:
        if jogador.soma > 21:
            jogador.vencedor = "Dealer"
            n_derrotas += 1
            jogador.busts += 1
            jogador.saldo -= jogador.aposta
            break

        if jogador.soma == 21:
            if len(jogador.cartas) == 2:
                jogador.blackjacks += 1

                if dealer.soma == 21:
                    if len(dealer.cartas) == 2: dealer.blackjacks += 1
                    jogador.vencedor = "Empate"
                    n_empates += 1
                    break

                jogador.saldo += jogador.aposta * 0.5
                jogador.vencedor = "Jogador"
                n_vitorias += 1
                break

            break

        if dealer.soma == 21:
            if len(dealer.cartas) == 2: dealer.blackjacks += 1
            jogador.vencedor = "Dealer"
            jogador.saldo -= jogador.aposta
            n_derrotas += 1
            break

        if melhor_decisao[pre_total][dealer.cartas[0].valor] == 0 or jogador.soma > 16: break
        while jogador.soma < 17:
            pre_total = jogador.soft_hard()
            if melhor_decisao[pre_total][dealer.cartas[0].valor] == 1: jogador.pedir()
            else: break
            # jogador.mostrar()

    while dealer.soma < 17:
        if jogador.vencedor: break
        dealer.pedir()

    if not jogador.vencedor:
        if dealer.soma > 21:
            jogador.vencedor = "Jogador"
            n_vitorias += 1
            jogador.saldo += jogador.aposta
            dealer.busts += 1

        elif dealer.soma > jogador.soma:
            jogador.vencedor = "Dealer"
            jogador.saldo -= jogador.aposta
            n_derrotas += 1

        elif dealer.soma < jogador.soma:
            jogador.vencedor = "Jogador"
            jogador.saldo += jogador.aposta
            n_vitorias += 1

        else:
            jogador.vencedor = "Empate"
            n_empates += 1

    # dealer.mostrar()
    # print("\nVencedor:", jogador.vencedor)
    # print(f"Seu saldo R$ {jogador.saldo:.2f}")

    # y.append(jogador.saldo)
    if jogador.vencedor == "Jogador": vitorias[pontos][dealer.cartas[0].valor] += 1
    elif jogador.vencedor == "Dealer": derrotas[pontos][dealer.cartas[0].valor] += 1
    else: empates[pontos][dealer.cartas[0].valor] += 1

    baralho += dealer.cartas
    baralho += jogador.cartas
    jogador.resetar()
    dealer.resetar()


def monte_carlo(simulacoes):
    for i in range(simulacoes):
        iniciar(dealer, jogador)
        jogar(baralho, dealer, jogador)


dealer = Dealer()
jogador = Jogador()
t0 = perf_counter()
monte_carlo(n)
t = perf_counter()

'''plt.title("Evolução do saldo do jogador")
plt.xlabel("Número de rodadas")
plt.ylabel("Saldo do jogador (R$)")
plt.plot(x, y)
plt.show()'''

print("="*120)
print(f"Vitórias: {n_vitorias}\nDerrotas: {n_derrotas}\nEmpates: {n_empates}")
print(f"Busts do jogador: {jogador.busts}\nBlackjacks do jogador: {jogador.blackjacks}")
print(f"Busts do dealer: {dealer.busts}\nBlackjacks do dealer: {dealer.blackjacks}")
print(f"Saldo: R$ {jogador.saldo:.2f}")
ver_dados()
print("Tempo gasto:", t-t0)
print("="*120)
'''wins_df = DataFrame(vitorias).T.to_csv("wins_df.csv", sep=";")
losses_df = DataFrame(derrotas).T.to_csv("losses_df.csv", sep=";")
ties_df = DataFrame(empates).T.to_csv("ties_df.csv", sep=";")'''
