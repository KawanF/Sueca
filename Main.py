from random import Random, shuffle
from re import A
import random
from traceback import print_tb

class Jogador:

    def __init__(self,n):
        self.nome = n
        self.mao = []
        self.pontos = 0
    


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

    def embaralhar(b):
        for x in range(40):
            y=random.randint(0,40)
            b.cartas[x], b.cartas[y] = b.cartas[y], b.cartas[x]
        return b

    """Verifica se a mão do jogador tem carta do primeiro naipe jogado"""
    def verifica_naipe(b, player, n):
        for i in range(10):
            if b.cartas[i+((player-1)*10)]!=None:
                if b.cartas[i+((player-1)*10)].naipes[b.cartas[i+((player-1)*10)].naipe]== n:
                    return True
        return False

    """t=trunfo, b=baralho"""
    def Round_(t, b, primeiro, pla1, pla2):
        """rodada=cartas jogadas pelos jogadores, calcula=array auxiliar de 'rodada'"""
        rodada=[0,0,0,0]
        calcula=[0,0,0,0]
        x=0
        p=primeiro

        print("O Trunfo do jogo é ",t,".")
        """Primeira jogado, irá guardar o naipe da rodada"""
        while True:                   
            mesa=int(input(f"Jogador {p} digite a carta que deseja jogar(1-10): "))
            i=(mesa-1)+((p-1)*10)
            if mesa<1 or mesa>10:
                print("Número inválido!")
            elif b.cartas[i]==None:
                print("Carta já usada!")
            else:      
                rodada[0]=b.cartas[i]
                print(b.cartas[i])
                naipePrimeiro=b.cartas[i].naipes[b.cartas[i].naipe]
                b.cartas[i]=None
                if p ==4:
                    p=1
                else:
                    p+=1
                break

        """Introdução das cartas a array 'rodada'. O primeiro a jogar guarda a carta na posição 0"""
        for x in range(1,4):
            if p==4:
                while True:                   
                    mesa=int(input(f"Jogador {p} digite a carta que deseja jogar(1-10): "))
                    i=(mesa-1)+((p-1)*10)
                    if mesa<1 or mesa>10:
                        print("Número inválido!")
                    elif b.cartas[i]==None:
                        print("Carta já usada!")
                    elif Jogo.verifica_naipe(b,p,naipePrimeiro) == True:  
                        if b.cartas[i].naipes[b.cartas[i].naipe]==naipePrimeiro or b.cartas[i].naipes[b.cartas[i].naipe]==t:
                            rodada[x]=b.cartas[i]
                            print(b.cartas[i])
                            b.cartas[i]=None
                            p=1
                            break
                        else:
                            print("Naipe da carta inválido!")

                    else:      
                        rodada[x]=b.cartas[i]
                        print(b.cartas[i])
                        b.cartas[i]=None
                        p=1
                        break

            else:
                while True:
                    mesa=int(input(f"Jogador {p} digite a carta que deseja jogar(1-10): "))
                    i=(mesa-1)+((p-1)*10)
                    if mesa<1 or mesa>10:
                        print("Número inválido!")
                    elif b.cartas[i]==None:
                        print("Carta já usada!")
                    elif Jogo.verifica_naipe(b,p,naipePrimeiro) == True:  
                        if b.cartas[i].naipes[b.cartas[i].naipe]==naipePrimeiro or b.cartas[i].naipes[b.cartas[i].naipe]==t:
                            rodada[x]=b.cartas[i]
                            print(b.cartas[i])
                            b.cartas[i]=None
                            p+=1
                            break
                        else:
                            print("Naipe da carta inválido!")
                    
                    else:      
                        rodada[x]=b.cartas[i]
                        print(b.cartas[i])
                        b.cartas[i]=None
                        p+=1
                        break

    
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
        for i in range(4):
            if i<1:
                print("Jogador 1: ",self.p1.mao)
            elif i<2:
                print("Jogador 2: ",self.p2.mao)
            elif i<3:
                print("Jogador 3: ",self.p3.mao)
            else:
                print("Jogador 4: ",self.p4.mao)
            
            
        """Início dos rounds"""
        y=1
        placar1=0
        placar2=0

        while y!=11:
            if y!=1:
                for i in range(40):
                    if baralho.cartas[i]==None:
                        if i<10:
                            self.p1.mao[i]=' '
                        elif i<20:
                            self.p2.mao[i%10]=' '
                        elif i<30:
                            self.p3.mao[i%20]=' '
                        else:
                            self.p4.mao[i%30]=' '

                for i in range(4):
                    if i<1:
                        print("Jogador 1: ",self.p1.mao)
                    elif i<2:
                        print("Jogador 2: ",self.p2.mao)
                    elif i<3:
                        print("Jogador 3: ",self.p3.mao)
                    else:
                        print("Jogador 4: ",self.p4.mao)

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
            baralho=Baralho()
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

