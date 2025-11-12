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
                
            else: self.soma += 10
            
        def contar_ases(self):
            for i in range(self.ases):
                if self.soma > 21: 
                    self.soma -= 10
                    self.ases -= 1
                    
                    
class Jogador(Dealer):
    pass
                    
                   
def mostrar_cartas(objeto):
    if type(objeto) == Dealer:
        print("\nCartas do Dealer:\n")
        for carta in dealer.cartas: 
            print(carta)
        
        print("Total:", dealer.soma)
        
    else: 
        print("\n\033[36m")
        print("Cartas do Jogador:\n")
        
        for carta in jogador.cartas: 
            print(carta)
        
        print(f"Total: {jogador.soma}")
        print("\033[m")
            
 
vitoria = str()             
dealer = Dealer()
jogador = Jogador()
decisao = str()

jogador.pedir()
jogador.pedir()
jogador.contar_ases()
dealer.pedir()
dealer.pedir()
dealer.contar_ases()

mostrar_cartas(jogador)
mostrar_cartas(dealer)

while True:
    if jogador.soma > 21:
        vitoria = "Dealer"
        break
        
    if jogador.soma == 21:
        vitoria = "Jogador"
        break
        
    if dealer.soma == 21:
        vitoria = "Dealer"
        break
        
    print("\n[0] - Parar")
    print("[1] - Continuar")
    decisao = input("O que quer fazer? ")
    
    if decisao == "0": break
    else: 
        jogador.pedir()
        jogador.contar_ases()
        mostrar_cartas(jogador)
        
while dealer.soma < 17:
    if vitoria: break
    dealer.pedir()
    dealer.contar_ases()        
    
if jogador.soma == 21 and dealer.soma == 21:
    vitoria = "Empate"
    
if not vitoria:
    if dealer.soma > 21:
        vitoria = "Jogador"
                        
    elif dealer.soma > jogador.soma: 
        vitoria= "Dealer"
            
    elif dealer.soma < jogador.soma:
        vitoria = "Jogador"
    
    else: vitoria = "Empate"
    
mostrar_cartas(dealer)
print("\nVitória:", vitoria)