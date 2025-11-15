from random import randrange


class Carta:
    # Esta classe representa uma carta de baralho.
    def __init__(self, naipe, valor):
        """
        naipe: representa o naipe da carta. O naipe é irrelevante para o blackjack, mas pode ser útil caso o projeto
        seja expandido e o naipe tenha significado em outro jogo de cartas.

        valor: representa o valor da carta, sendo um número natural de 2 a 10 ou as letras do baralho (A, J, Q, K).
        """
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f"Naipe: {self.naipe} | Valor: {self.valor}"

    def valor_num(self):
        if self.valor.isnumeric(): return int(self.valor)
        elif self.valor == 'A': return self.valor
        else: return 10


soma_vitorias = []
soma_derrotas = []
soma_empates = []
carta2_vitorias = []
carta2_derrotas = []
carta2_empates = []

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
        self.bust = 0 # Quando ultrapassa 21.
        self.blackjack = 0 # Vitória por blackjack.

    def pedir(self):
        """
        Representa um pedido de carta. Quando o portador pede uma carta, a carta que vem é escolhida aleatoriamente
        atarvés da função choice(), essa carta é removida do baralho e depois é contabilizada na soma. Cartas númericas
        tem seu valor nominal, cartas não numéricas valem 10, exceto ás que a princípio vale 11.
        """
        esc = randrange(len(baralho))
        baralho[esc], baralho[-1] = baralho[-1], baralho[esc]
        carta = baralho.pop()
        self.cartas.append(carta)

        if carta.valor.isnumeric():
            self.soma += int(carta.valor)

        elif carta.valor == 'A':
            self.ases += 1
            self.soma += 11

        else:
            self.soma += 10

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

        print("\n")

    def resetar(self):
        # Reseta os atributos do portador, útil para jogar o jogo novamente dentro da mesma execução.
        self.cartas.clear()
        self.ases = 0
        self.soma = 0


class Jogador(Dealer):
    # Esta classe representa o jogador. Ela poderá ser expandida para pôr mais funcionalidades do blackjack.
    def __init__(self):
        super().__init__()
        self.vencedor = str()
        self.decisao = str()
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0

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


def iniciar(dealer: Dealer, jogador: Jogador):
    # Função que inicia cada rodada. É chamada antes da função jogar().
    for i in range(2):
        jogador.pedir()
        dealer.pedir()

    jogador.contar_ases()
    dealer.contar_ases()
    jogador.mostrar()
    dealer.ver_carta()


def jogar(baralho: list, dealer: Dealer, jogador: Jogador):
    # Função que contém toda a lógica do jogo e determina o vencedor de uma rodada.
    while True:
        if jogador.soma > 21:
            jogador.vencedor = "Dealer"
            jogador.derrotas += 1
            jogador.bust += 1
            break

        if jogador.soma == 21:
            jogador.vencedor = "Jogador"
            jogador.vitorias += 1
            jogador.blackjack += 1
            break

        if dealer.soma == 21:
            jogador.vencedor = "Dealer"
            jogador.derrotas += 1
            dealer.blackjack += 1
            break

        '''print("[0] - Parar")
        print("[1] - Pedir")
        jogador.decisao = input("O que quer fazer? ")'''
        jogador.decisao = "0"

        if jogador.decisao == "0":
            break
        else:
            jogador.pedir()
            jogador.contar_ases()
            jogador.mostrar()

    while dealer.soma < 17:
        if jogador.vencedor: break
        dealer.pedir()
        dealer.contar_ases()

    if jogador.soma == 21 and dealer.soma == 21:
        jogador.vencedor = "Empate"
        jogador.empates += 1

    if not jogador.vencedor:
        if dealer.soma > 21:
            jogador.vencedor = "Jogador"
            jogador.vitorias += 1
            dealer.bust += 1

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
        soma_vitorias.append(jogador.soma)
        carta2_vitorias.append(dealer.cartas[1].valor_num())

    elif jogador.vencedor == "Dealer":
        soma_derrotas.append(jogador.soma)
        carta2_derrotas.append(dealer.cartas[1].valor_num())
    else:
        soma_empates.append(jogador.soma)
        carta2_empates.append(dealer.cartas[1].valor_num())

    baralho += dealer.cartas
    baralho += jogador.cartas
    jogador.resetar()
    dealer.resetar()


dealer = Dealer()
jogador = Jogador()

for i in range(10):
    iniciar(dealer, jogador)
    jogar(baralho, dealer, jogador)

print("="*60)
print(f"Vitórias: {jogador.vitorias}\nDerrotas: {jogador.derrotas}\nEmpates: {jogador.empates}")
print(f"Busts do jogador: {jogador.bust}\nBlackjacks do jogador: {jogador.blackjack}")
print(f"Busts do dealer: {dealer.bust}\nBlackjacks do dealer: {dealer.blackjack}")
print(f"Soma das vitórias: {soma_vitorias}\nSoma das derrotas: {soma_derrotas}\nSoma dos empates:{soma_empates}")
print(f"Carta do dealer em:\nVitórias: {carta2_vitorias}\nDerrotas: {carta2_derrotas}\nEmpates: {carta2_empates}")
print("="*60)
