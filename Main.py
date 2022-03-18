from random import Random, shuffle
from re import A
import random

class Jogador:

    def __init__(self,n):
        self.nome = n
        self.mao = []
    


class Carta:
    naipes = ["Espadas", "Copas",
             "Ouros", "Paus"]
    
    valores = [None, None, "2","3",
              "4", "5", "6",
              "Valete", "Rainha",
              "Rei","7", "Ás"]
    
    pontos = [None, None, "0", "0",
              "0", "0", "0",
              "3", "2", "4","10", "11"]

    
    def __init__(self, v, n):

        self.valor = v
        self.naipe = n
        self.jogador = 0

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
        self.p1 = Jogador(name1)
        self.p2 = Jogador(name2)
        self.p3 = Jogador(name3)
        self.p4 = Jogador(name4)

    """t=trunfo, b=baralho"""

    def Round_(t, b, primeiro, pla1, pla2):
        """rodada=cartas jogadas pelos jogadores, calcula=array auxiliar de 'rodada'"""
        rodada=[0,0,0,0]
        calcula=[0,0,0,0]
        x=0
        p=primeiro

        print("O Trunfo do jogo é ",t,".")
        """Introdução das cartas a array 'rodada'. O primeiro a jogar guarda a carta na posição 0"""
        while x!=4:
            if p==4:
                mesa=int(input(f"Jogador {p} digite a carta que deseja jogar(1-10): "))
                i=(mesa-1)+((p-1)*10)
                if mesa<1 or mesa>10 or b.cartas[i]==None:
                    return False
                else:      
                    rodada[x]=b.cartas[i]
                    print(b.cartas[i])
                    b.cartas[i]=None
                p=1
                x+=1
            else:
                mesa=int(input(f"Jogador {p} digite a carta que deseja jogar(1-10): "))
                i=(mesa-1)+((p-1)*10)
                if mesa<1 or mesa>10 or b.cartas[i]==None:
                  return False
                else:      
                    rodada[x]=b.cartas[i]
                    print(b.cartas[i])
                    b.cartas[i]=None
                p+=1
                x+=1
    
        """Decisão do vencedor da rodada"""
        """cont[0] guarda os pontos da maior carta, cont[1] guarda o jogador que a jogou (variável temporária)"""
        cont=[0,0]
        j=0

        for i in range(4):

            if t == rodada[i].naipes[rodada[i].naipe]: 
                calcula[i]=rodada[i].valor
                int(calcula[i])
                j+=1

        if j==0:
            for i in range(4):
                calcula[i]=rodada[i].valor

            for i in range(4):
                if calcula[i]>cont[0]:
                    cont[0]=calcula[i]
                    cont[1]=rodada[i].jogador

        else:
            for i in range(4):
                if calcula[i]>cont[0]:
                    cont[0]=calcula[i]
                    cont[1]=rodada[i].jogador

        """Retorna a função Winner"""
        return Jogo.Winner(cont[1],rodada,pla1,pla2)
             
        
    def play_game(self):
        baralho = Baralho()
        x=0
        primeiro = random.choice([1,2,3,4])
        print("O primeiro a jogar é o Jogador ",primeiro,"!")

        """Divisão das cartas para fins visuais"""
        while x!=40:
            if x<10:
                self.p1.mao.append(baralho.cartas[x])
                baralho.cartas[x].jogador=1
            elif x<20:
                self.p2.mao.append(baralho.cartas[x])
                baralho.cartas[x].jogador=2
            elif x<30:
                self.p3.mao.append(baralho.cartas[x])
                baralho.cartas[x].jogador=3
            else:
                self.p4.mao.append(baralho.cartas[x])
                baralho.cartas[x].jogador=4
            x+=1
            
        print("Suecaaaaaa!!")
        i=random.choice([1,2,3,4])
        trunfo=baralho.cartas[i].naipes[baralho.cartas[i].naipe]

        """Visualização das mãos dos jogadores"""
        for i in range(40):
            if i<10:
                print("Jogador 1 (",i+1,"): ",baralho.cartas[i])
            elif i<20:
                print("Jogador 2 (",i%10+1,"): ",baralho.cartas[i])
            elif i<30:
                print("Jogador 3 (",i%20+1,"): ",baralho.cartas[i])
            else:
                print("Jogador 4 (",i%30+1,"): ",baralho.cartas[i])
            
            
        """Início dos rounds"""
        y=1
        placar1=0
        placar2=0

        while y!=11:
            if y!=1:
                for i in range(40):
                    if baralho.cartas[i]==None:
                        baralho.cartas[i]=' '

                    if i<10:
                        print("Jogador 1 (",i+1,"): ",baralho.cartas[i])
                    elif i<20:
                        print("Jogador 2 (",i%10+1,"): ",baralho.cartas[i])
                    elif i<30:
                        print("Jogador 3 (",i%20+1,"): ",baralho.cartas[i])
                    else:
                        print("Jogador 4 (",i%30+1,"): ",baralho.cartas[i])

            print("Round ",y,"! Placar: ",placar1," x ", placar2)
            """Tentativa de chamar função Round_"""
            placar1, placar2, primeiro=Jogo.Round_(trunfo,baralho,primeiro,placar1,placar2)
            sair=input("Para sair digite 'q', para continuar qualquer outra tecla:  ")
            if sair=='q':
                break
            y+=1

        """Tentativa de chamar função Vencedor"""
        Jogo.Vencedor(placar1,placar2)

        nova=input("Deseja jogar novamente? Tecla qualquer tecla exceto q: ")
        if nova!="q":

            """Tentativa de chamar função play_game"""
            Jogo.play_game(self)
        

    """"g = ganhador da rodada, r = cartas usadas pelos jogadores na rodada, placar = placar atual do jogo a ser atualizado"""
    def Winner(g, r, placar1,placar2): 
        print("O vencedor da rodada é o Jogador ",g,"!")

        for i in range(1,5):
            if g%2==0:
                placar2+=int(r[i-1].pontos[r[i-1].valor])
            else:
                placar1+=int(r[i-1].pontos[r[i-1].valor])

        return placar1, placar2, g
    """Retorna os placares atualizados e o primeiro jogador a jogar o proximo round"""

    """Mensagem final"""
    def Vencedor(p1,p2):
        if p1==p2:
            print("Empate!!")
        elif p1>p2:
            print("A equipe 1 ganhou!")
        else:
            print("A equipe 2 ganhou!")


novojogo= Jogo()
novojogo.play_game()

