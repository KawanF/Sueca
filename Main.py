from random import shuffle

class Jogador:

    def __init__(self,n,i):
        self.nome = n
        self.id = i
        self.mao = []
    
class Carta:
    naipes = ["Espadas", "Copas",
             "Ouros", "Paus"]
    
    valores = [None, None, "2","3",
              "4", "5", "6", "7",
              "Valete", "Rainha",
              "Rei", "Ás"]
    
    pontos = [None, None, "0", "0",
              "0", "0", "0", "10",
              "3", "2", "4", "11"]

    
    def __init__(self, v, n):

        self.valor = v
        self.naipe = n
        self.ganhador = e = 0

    def __ne__(self, c2):
        if self.valor != c2.valor:
            return True
        if self.valor == c2.valor:
            if self.naipe != c2.naipe:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.valores[self.valor] + " de " + self.naipes[self.naipe]
        return v


class Baralho:
    def __init__(self):
        self.cartas = []
        for i in range(2, 12):
            for j in range(4):
                self.cartas.append(Carta(i,j))
        shuffle(self.cartas)




class Jogo:
    def __init__(self):
        name1 = input("Insira o nome do Jogador 1: ")
        name2 = input("Insira o nome do Jogador 2: ")
        name3 = input("Insira o nome do Jogador 3: ")
        name4 = input("Insira o nome do Jogador 4: ")
        self.baralho = Baralho()
        self.p1 = Jogador(name1)
        self.p2 = Jogador(name2)
        self.p3 = Jogador(name3)
        self.p4 = Jogador(name4)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def round_

    def iniciar_rodada(self):
        cartas = self.baralho.cartas
        
    def play_game(self):
        baralho = iniciar+rodada()
        x=0
        while x!=40:
            if x>10:
                y=0
                p1.mao[y]=cartas[x]
            elif x>20:
                y=0
                p2.mao[y]=cartas[x]
            elif x>30:
                y=0
                p3.mao[y]=cartas[x]
            else:
                y=0
                p4.mao[y]=cartas[x]
        x+=1
            
        print("Suecaaaaaa!!")
        for i in range(4):
                print("O Trunfo do jogo é ",cartas.naipe[i],".")

        print("Jogador 1: "', '.join(p1.mao))
        print("Jogador 2: "', '.join(p2.mao))
        print("Jogador 3: "', '.join(p3.mao))
        print("Jogador 4: "', '.join(p4.mao))
        
        x=1
        while x!= 0:
            print("Round ",x,"!")
            
            m = "Tecle 'q' para sair. Qualquer tecla para jogar: "
            response = input(m)
            if response == 'q':
                break
            while x!=11:
                rodada= round_()
            
            





                
            p1 = self.deck.rm_card()
            p2 = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

            x+=1

        win = self.winner(self.p1,
                         self.p2)
        print("War is over.{} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"   


