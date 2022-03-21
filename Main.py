from random import Random, shuffle
import random
"""\/Não lembro pq coloquei esse"""
from re import A 
"""Nem esse\/"""
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

class Turma:
    def __init__(self,p1,p2,p3,p4):
        self.jogadores = [p1,p2,p3,p4]
        

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
        self.turma= Turma(self.p1,self.p2,self.p3,self.p4)

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

    """t=trunfo, b=baralho, pla=placar"""
    def Round_(t, b, primeiro, pla1, pla2,turma):
        """rodada=cartas jogadas pelos jogadores, calcula=array auxiliar de 'rodada'"""
        rodada=[0,0,0,0]
        calcula=[0,0,0,0]
        x=0
        p=primeiro

        print("O Trunfo do jogo é ",t,".")
        """Primeira jogado, irá guardar o naipe da rodada"""
        while True:                   
            mesa=input(f"{turma.jogadores[p-1].nome} digite a carta que deseja jogar(1-10): ")
            if mesa=='':
                print("Número inválido")
            else:
                mesa=int(mesa)
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
                    if p==4:
                        p=1
                    else:
                        p+=1
                    break

        """Jogada dos outros 3 jogadores"""
        for x in range(1,4):
            if p==4:
                while True:                   
                    mesa=input(f"{turma.jogadores[p-1].nome} digite a carta que deseja jogar(1-10): ")
                    if mesa=='':
                        print("Número inválido")
                    else:
                        mesa=int(mesa)
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
                    mesa=input(f"{turma.jogadores[p-1].nome} digite a carta que deseja jogar(1-10): ")
                    if mesa=='':
                        print("Número inválido")
                    else:
                        mesa=int(mesa)
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
                if calcula[i]>=cont[0]:
                    cont[0]=calcula[i]
                    cont[1]=rodada[i].jogador

        """Retorna a função Winner"""
        return Jogo.Winner(cont[1],rodada,pla1,pla2,turma)
             
        
    def play_game(self):
        baralho = Baralho()
        x=0
        primeiro = random.choice([1,2,3,4])
        print(f"{self.turma.jogadores[primeiro-1].nome} é o(a) primeiro(a) a jogar!")

        """Divisão das cartas para fins visuais"""
        self.p1.mao=[]
        self.p2.mao=[]
        self.p3.mao=[]
        self.p4.mao=[]

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
                print(self.p1.nome,": ",self.p1.mao)
            elif i<2:
                print(self.p2.nome,": ",self.p2.mao)
            elif i<3:
                print(self.p3.nome,": ",self.p3.mao)
            else:
                print(self.p4.nome,": ",self.p4.mao)
                      
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
                        print(self.p1.nome,": ",self.p1.mao)
                    elif i<2:
                        print(self.p2.nome,": ",self.p2.mao)
                    elif i<3:
                        print(self.p3.nome,": ",self.p3.mao)
                    else:
                        print(self.p4.nome,": ",self.p4.mao)

            print("Round ",y,"! Placar: ",placar1," x ", placar2)
            """Função Round_"""
            placar1, placar2, primeiro=Jogo.Round_(trunfo,baralho,primeiro,placar1,placar2,self.turma)
            sair=input("Para sair digite 'q', para continuar qualquer outra tecla:  ")
            if sair=='q':
                break
            y+=1

        """Chamar função Vencedor"""
        Jogo.Vencedor(placar1,placar2,self.turma)

        nova=input("Deseja jogar novamente? Tecla qualquer tecla exceto q: ")
        if nova!="q":

            """Chamar função play_game para iniciar outro """
            baralho=Baralho()
            Jogo.play_game(self)
        

    """"g = ganhador da rodada, r = cartas usadas pelos jogadores na rodada, placar = placar atual do jogo a ser atualizado"""
    def Winner(g, r, placar1,placar2,turma): 
        print(f"O vencedor da rodada é o(a) {turma.jogadores[g-1].nome}!")
        for i in range(1,5):
            if g%2==0:
                placar2+=int(r[i-1].pontos[r[i-1].valor])
                turma.jogadores[g-1].pontos+=int(r[i-1].pontos[r[i-1].valor])
            else:
                turma.jogadores[g-1].pontos+=int(r[i-1].pontos[r[i-1].valor])
                placar1+=int(r[i-1].pontos[r[i-1].valor])

        return placar1, placar2, g
    """Retorna os placares atualizados e o primeiro jogador a jogar o proximo round"""

    """Mensagem final"""
    def Vencedor(p1,p2,turma):
        if p1==p2:
            print("!!!!!!Empate!!!!!!")
        elif p1>p2:
            print(f"{turma.jogadores[0].nome} e {turma.jogadores[2].nome} ganharam a partida!")
            print(f"{turma.jogadores[0].nome} fez {turma.jogadores[0].pontos} pontos, e {turma.jogadores[2].nome} fez {turma.jogadores[2].pontos} pontos!")
        else:
            print(f"{turma.jogadores[1].nome} e {turma.jogadores[3].nome} ganharam a partida!")
            print(f"{turma.jogadores[1].nome} fez {turma.jogadores[1].pontos} pontos, e {turma.jogadores[3].nome} fez {turma.jogadores[3].pontos} pontos!")

novojogo= Jogo()
novojogo.play_game()

