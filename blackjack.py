from random import choice


class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f"Naipe: {self.naipe} | Valor: {self.valor}"


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
]


class Dealer:
    def __init__(self):
        self.cartas = list()
        self.ases = 0
        self.soma = 0

    def pedir(self):
        esc = choice(baralho)
        self.cartas.append(esc)
        baralho.remove(esc)

        if esc.valor.isnumeric():
            self.soma += int(esc.valor)

        elif esc.valor == "A":
            self.ases += 1
            self.soma += 11

        else:
            self.soma += 10

    def contar_ases(self):
        for i in range(self.ases):
            if self.soma > 21:
                self.soma -= 10
                self.ases -= 1

    def mostrar(self):
        print("Cartas do Dealer:\n")
        for carta in self.cartas:
            print(carta)

        print("Total:", self.soma)

    def ver_carta(self):
        print("Cartas do Dealer:\n")
        print("Naipe: ??? | Valor: ???")
        print(self.cartas[1])

        if self.cartas[1].valor.isnumeric():
            print("Total:", self.cartas[1])

        elif self.cartas[1].valor != "A":
            print("Total: 10")

        else:
            print("1 / 11")

        print("\n")

    def resetar(self):
        self.cartas.clear()
        self.ases = 0
        self.soma = 0


class Jogador(Dealer):
    def __init__(self):
        super().__init__()
        self.vencedor = str()
        self.decisao = str()

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
        self.decisao = str()


def jogar(baralho: list, dealer: Dealer, jogador: Jogador):
    while True:
        if jogador.soma > 21:
            jogador.vencedor = "Dealer"
            break

        if jogador.soma == 21:
            jogador.vencedor = "Jogador"
            break

        if dealer.soma == 21:
            jogador.vencedor = "Dealer"
            break

        print("[0] - Parar")
        print("[1] - Continuar")
        jogador.decisao = input("O que quer fazer? ")

        if jogador.decisao == "0":
            break
        else:
            jogador.pedir()
            jogador.contar_ases()
            jogador.mostrar()

    while dealer.soma < 17:
        if jogador.vencedor:
            break
        dealer.pedir()
        dealer.contar_ases()

    if jogador.soma == 21 and dealer.soma == 21:
        jogador.vencedor = "Empate"

    if not jogador.vencedor:
        if dealer.soma > 21:
            jogador.vencedor = "Jogador"

        elif dealer.soma > jogador.soma:
            jogador.vencedor = "Dealer"

        elif dealer.soma < jogador.soma:
            jogador.vencedor = "Jogador"

        else:
            jogador.vencedor = "Empate"

    dealer.mostrar()
    print("\nVencedor:", jogador.vencedor)

    baralho += dealer.cartas
    baralho += jogador.cartas
    jogador.resetar()
    dealer.resetar()


def iniciar(dealer: Dealer, jogador: Jogador):
    jogador.pedir()
    jogador.pedir()
    jogador.contar_ases()
    dealer.pedir()
    dealer.pedir()
    dealer.contar_ases()
    jogador.mostrar()
    dealer.ver_carta()


dealer = Dealer()
jogador = Jogador()

for i in range(3):
    iniciar(dealer, jogador)
    jogar(baralho, dealer, jogador)
