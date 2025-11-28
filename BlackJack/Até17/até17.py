from random import randrange
from time import perf_counter
from pandas import DataFrame


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
vitorias = {
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
    Carta("Copas", "K"), Carta("Ouro", "A"),
    Carta("Ouro", "2"), Carta("Ouro", "3"),
    Carta("Ouro", "4"), Carta("Ouro", "5"),
    Carta("Ouro", "6"), Carta("Ouro", "7"),
    Carta("Ouro", "8"), Carta("Ouro", "9"),
    Carta("Ouro", "10"), Carta("Ouro", "J"),
    Carta("Ouro", "Q"), Carta("Ouro", "K"),
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
        carta = baralho.pop()

        self.cartas.append(carta)
        self.soma += carta.valor_num

        if carta.valor_num == 11: self.ases += 1

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
        for carta in self.cartas:
            print(carta)

        print("Total:", self.soma)

    def ver_carta(self):
        # Mostra apenas uma carta do dealer no ínicio de cada rodada, mostrando apenas a soma parcial.
        print("Cartas do Dealer:\n")
        print("Naipe: ??? | Valor: ???")
        print(self.cartas[1])

        if self.cartas[1].valor.isnumeric():
            print("Total:", self.cartas[1])

        elif self.cartas[1].valor != "A":
            print("Total: 10")

        else:
            print("1 / 11")

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
        self.decisao = int()
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.cartas_iniciais = 0

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
        self.decisao = int()

    def soft_hard(self):
        return f"{self.soma}{'S' if self.ases > 0 else 'H'}"


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

     jogador.contar_ases()
     dealer.contar_ases()
     jogador.mostrar()
     dealer.ver_carta()


def jogar(baralho: list, dealer: Dealer, jogador: Jogador, parou: int):
    pre_total = jogador.soft_hard()

    while True:
        if jogador.soma > 21:
            jogador.vencedor = "Dealer"
            jogador.derrotas += 1
            jogador.busts += 1
            break

        if jogador.soma == 21:
            if len(jogador.cartas) == 2: jogador.blackjacks += 1
            if dealer.soma == 21:
                if len(dealer.cartas) == 2: dealer.blackjacks += 1
                jogador.vencedor = "Empate"
                jogador.empates += 1
                break

            jogador.vencedor = "Jogador"
            jogador.vitorias += 1
            break

        if dealer.soma == 21:
            if len(dealer.cartas) == 2: dealer.blackjacks += 1
            jogador.vencedor = "Dealer"
            jogador.derrotas += 1
            break

        if jogador.soma >= parou: break

        # Enquanto o jogador não atingir uma pontuação, ele não para de pedir, semelhante ao dealer.
        while jogador.soma < parou:
            pre_total = jogador.soft_hard()
            jogador.pedir()
            jogador.mostrar()
            jogador.contar_ases()

    while dealer.soma < 17:
        if jogador.vencedor: break
        dealer.pedir()
        dealer.contar_ases()

    if not jogador.vencedor:
        if dealer.soma > 21:
            jogador.vencedor = "Jogador"
            jogador.vitorias += 1
            dealer.busts += 1

        elif dealer.soma > jogador.soma:
            jogador.vencedor = "Dealer"
            jogador.derrotas += 1

        elif dealer.soma < jogador.soma:
            jogador.vencedor = "Jogador"
            jogador.vitorias += 1

        else:
            jogador.vencedor = "Empate"
            jogador.empates += 1

    dealer.mostrar()
    print("\nVencedor:", jogador.vencedor)

    if jogador.vencedor == "Jogador":
        vitorias[pre_total][dealer.cartas[1].valor] += 1

    elif jogador.vencedor == "Dealer":
        derrotas[pre_total][dealer.cartas[1].valor] += 1

    else:
        empates[pre_total][dealer.cartas[1].valor] += 1

    baralho += dealer.cartas
    baralho += jogador.cartas
    jogador.resetar()
    dealer.resetar()


def monte_carlo(n, parou):
    for i in range(n):
        iniciar(dealer, jogador)
        jogar(baralho, dealer, jogador, parou)


dealer = Dealer()
jogador = Jogador()
t0 = perf_counter()
monte_carlo(1000000, 17)
t = perf_counter()

print("="*120)
print(f"Vitórias: {jogador.vitorias}\nDerrotas: {jogador.derrotas}\nEmpates: {jogador.empates}")
print(f"Busts do jogador: {jogador.busts}\nBlackjacks do jogador: {jogador.blackjacks}")
print(f"Busts do dealer: {dealer.busts}\nBlackjacks do dealer: {dealer.blackjacks}")
ver_dados()
print("Tempo gasto:", t-t0)
print("="*120)
wins_df = DataFrame(vitorias).T.to_csv("wins_df.csv", sep=";")
losses_df = DataFrame(derrotas).T.to_csv("losses_df.csv", sep=";")
ties_df = DataFrame(empates).T.to_csv("ties_df.csv", sep=";")
