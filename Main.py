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
              "4", "5", "6", "7",
              "Valete", "Rainha",
              "Rei", "Ás"]
    
    pontos = [None, None, "0", "0",
              "0", "0", "0", "10",
              "3", "2", "4", "11"]

    
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
        i=0
        j=0
        """cont[0] guarda os pontos da maior carta, cont[1] guarda o jogador que a jogou (variável temporária)"""
        cont=[]
        while i!=4:
            if t == rodada[i].naipes[rodada[i].naipe]:
                calcula[i]=rodada[i].pontos[rodada[i].valor]
                i+=1
        if calcula!=[]:
            while j!=4:
                if calcula[j]>cont[0]:
                    cont[0]=calcula[j]
                    cont[1]=calcula[j].cartas.jogador
                    j+=1
        else:
            i=0
            while i!=4:
                if rodada[i].pontos[rodada[i].valor]>cont[0]:
                    cont[0]=rodada[i].pontos[rodada[i].valor]
                    cont[1]=rodada[i].cartas.jogador
                    i+=1
        print(pla1," x ",pla2)
        """Tentativa de chamar a função Winner"""
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
        print("O Trunfo do jogo é ",baralho.cartas[i].naipes[baralho.cartas[i].naipe],".")
        trunfo=baralho.cartas[i].naipes[baralho.cartas[i].naipe]

        """Visualização das mãos dos jogadores"""
        i=0
        while i!=40:
            if i<10:
                print("Jogador 1: ",baralho.cartas[i])
            elif i<20:
                print("Jogador 2: ",baralho.cartas[i])
            elif i<30:
                print("Jogador 3: ",baralho.cartas[i])
            else:
                print("Jogador 4: ",baralho.cartas[i])
            i+=1
            
        """Início dos rounds"""
        y=1
        placar1=0
        placar2=0

        while y!=11:
            print("Round ",y,"! Placar: ",placar1," x ", placar2)
            """Tentativa de chamar função Round_"""
            Jogo.Round_(trunfo,baralho,primeiro,placar1,placar2)
            y+=1

        """Tentativa de chamar função Vencedor"""
        print(Jogo.Vencedor(placar1,placar2))

        nova=input("Deseja jogar novamente? Tecla qualquer tecla exceto q.")
        if nova!="q":

            """Tentativa de chamar função play_game"""
            a= Jogo.play_game()
        

    """"g = ganhador da rodada, r = cartas usadas pelos jogadores na rodada, placar = placar atual do jogo a ser atualizado"""
    def Winner(self, g, r, placar): 
        print("O vencedor da rodada é o Jogador ",g,"!")

        placar[0]=int(r[0].pontos[r[0].valor] + r[2].pontos[r[2].valor])
        placar[1]=int(r[1].pontos[r[1].valor] + r[3].pontos[r[3].valor])
        return placar

    """Mensagem final"""
    def Vencedor(self,p1,p2):
        if p1==p2:
            print("Empate!!")
        elif p1>p2:
            print("A equipe 1 ganhou!")
        else:
            print("A equipe 2 ganhou!")


novojogo= Jogo()
novojogo.play_game()

