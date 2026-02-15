# cython: boundscheck=False, wraparound=False
from libc.stdint cimport uint64_t, UINT64_MAX

cdef uint64_t seed_global
cdef int baralho[312]
cdef int decisao[27][10]
baralho = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
]
decisao = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 2, 2, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 2, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 0, 0], [0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

cdef struct Jogador:
    int pontos
    int ases
    int busts
    int blackjacks
    int cartas_pedidas
    int resultado
    int upercard
    int aposta
    double saldo

cdef uint64_t xorshift64():
    global seed_global
    seed_global ^= seed_global << 26
    seed_global ^= seed_global >> 34
    seed_global ^= seed_global << 10
    return seed_global

cdef int randint(int min, int max):
    cdef uint64_t intervalo = max - min + 1
    cdef uint64_t limite = UINT64_MAX - (UINT64_MAX % intervalo)
    cdef uint64_t rand

    while True:
        rand = xorshift64()
        if rand < limite: return rand % intervalo + min

def gerar_seed_global(uint64_t seed_nova):
    global seed_global
    if seed_nova == 0: seed_nova = 32767
    seed_global = seed_nova

cdef void init_stats(Jogador* jogador):
    jogador.busts = 0
    jogador.blackjacks = 0
    jogador.saldo = 0.0

cdef void init_jogador(Jogador* jogador, int pontos, int ases):
    jogador.pontos = pontos
    jogador.ases = ases
    jogador.aposta = 1
    jogador.cartas_pedidas = 0
    jogador.resultado = 2
    jogador.upercard = 0

cdef void contar_ases(Jogador* jogador):
    while jogador.ases > 0 and jogador.pontos > 21:
        jogador.pontos -= 10
        jogador.ases -= 1

cdef void pedir(Jogador* jogador, int* tamanho):
    cdef int esc = randint(0, tamanho[0] - 1)
    cdef int temp = baralho[esc]

    if temp == 14:
        jogador.pontos += 11
        jogador.ases += 1
    elif temp > 10: jogador.pontos += 10
    else: jogador.pontos += temp
    jogador.cartas_pedidas += 1
    contar_ases(jogador)

    baralho[esc] = baralho[tamanho[0] - 1]
    baralho[tamanho[0] - 1] = temp
    tamanho[0] -= 1

cdef void dobrar(Jogador* jogador, int* tamanho):
    jogador.aposta *= 2
    pedir(jogador, tamanho)

cdef int soft_hard(Jogador* jogador):
    if jogador.ases == 0: return jogador.pontos - 4
    else: return jogador.pontos + 5

cdef void jogar(Jogador* jogador, Jogador* dealer, int[:, :, :] resultados, int pontos, int ases):
    cdef int pts
    cdef int pts_copy
    cdef int tamanho = 312
    cdef bint parou = False

    init_jogador(jogador, pontos, ases)
    init_jogador(dealer, 0, 0)

    pedir(jogador, &tamanho)
    pedir(jogador, &tamanho)
    pedir(dealer, &tamanho)
    dealer.upercard = dealer.pontos - 2
    pedir(dealer, &tamanho)
    pts = soft_hard(jogador)
    pts_copy = pts

    while True:
        if jogador.pontos > 21:
            jogador.resultado = -1
            jogador.busts += 1
            jogador.saldo += jogador.aposta * jogador.resultado
            break

        if jogador.pontos == 21:
            if jogador.cartas_pedidas == 2:
                jogador.blackjacks += 1

                if dealer.pontos == 21:
                    dealer.blackjacks += 1
                    jogador.resultado = 0
                    break

                jogador.resultado = 1
                jogador.saldo += jogador.aposta * 0.5
                break

            break

        if dealer.pontos == 21:
            dealer.blackjacks += 1
            jogador.resultado = -1
            jogador.saldo += jogador.aposta * jogador.resultado
            break

        if parou: break
        while jogador.pontos < 21:
            if decisao[pts_copy][dealer.upercard] == 0:
                parou = True
                break
            elif decisao[pts_copy][dealer.upercard] == 1:
                pedir(jogador, &tamanho)
                pts_copy = soft_hard(jogador)
            else:
                dobrar(jogador, &tamanho)
                parou = True
                break

    while dealer.pontos < 17 and jogador.resultado == 2: pedir(dealer, &tamanho)

    if jogador.resultado == 2:
        if dealer.pontos > 21:
            jogador.resultado = 1
            dealer.busts += 1

        elif dealer.pontos > jogador.pontos:
            jogador.resultado = -1

        elif dealer.pontos < jogador.pontos:
            jogador.resultado = 1

        else:
            jogador.resultado = 0

        jogador.saldo += jogador.aposta * jogador.resultado

    jogador.aposta = 1
    if jogador.resultado == 1: resultados[pts][0][dealer.upercard] += 1
    elif jogador.resultado == -1: resultados[pts][1][dealer.upercard] += 1
    else: resultados[pts][2][dealer.upercard] += 1

def monte_carlo(int[:, :, :] resultados, int n, int pontuacao, int ases):
    cdef Jogador jogador
    cdef Jogador dealer
    init_stats(&jogador)
    init_stats(&dealer)
    cdef int i
    for i in range(n): jogar(&jogador, &dealer, resultados, pontuacao, ases)
    dealer.saldo = -jogador.saldo
    return jogador.busts, jogador.blackjacks, jogador.saldo, dealer.busts, dealer.blackjacks, dealer.saldo