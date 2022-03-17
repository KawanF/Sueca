from random import shuffle

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
        self.p1.nome = Jogador(name1)
        self.p2.nome = Jogador(name2)
        self.p3.nome = Jogador(name3)
        self.p4.nome = Jogador(name4)

    """t=trunfo, b=baralho"""
    def Round_(self, t, b, primeiro, placar):
        """rodada=cartas jogadas pelos jogadores, calcula=array auxiliar de 'rodada'"""
        rodada=[]
        calcula=[]
        x=0
        p=primeiro
        """Introdução das cartas a array 'rodada'. O primeiro a jogar guarda a carta na posição 0"""
        while x!=4:
            if p==3:
                mesa=int(input("Jogador ",p," digite a carta que deseja jogar(1-10): "))
                if mesa<1 or mesa>10 or b[(mesa-1)+(p*10)]==None:
                    return False
                else:      
                    rodada[x]=b[(mesa-1)+(p*10)]
                    print(b[(mesa-1)+(p*10)])
                    b[(mesa-1)+(p*10)]=None
                p=0
                x+=1
            else:
                mesa=int(input("Jogador ",p," digite a carta que deseja jogar(1-10): "))
                if mesa<1 or mesa>10 or b[(mesa-1)+(p*10)]==None:
                  return False
                else:      
                    rodada[x]=b[(mesa-1)+(p*10)]
                    print(b[(mesa-1)+(p*10)])
                    b[(mesa-1)+(p*10)]=None
                p+=1
                x+=1

        """Decisão do vencedor da rodada"""
        i=0
        j=0

        """cont[0] guarda os pontos da maior carta, cont[1] guarda o jogador que a jogou (variável temporária)"""
        cont=[]
        while i!=4:
            if t in rodada[i].naipe:
                calcula[i]=int(rodada[i].pontos[rodada[i].valor])
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
        p=cont[1]
        
        """Tentativa de chamar a função Winner"""
        return Winner(p,rodada,placar)
             
        
    def play_game(self,p1,p2,p3,p4):
        baralho = Baralho()
        x=0
        primeiro=1

        """Divisão das cartas para fins visuais"""
        while x!=40:
            if x>10:
                p1.mao[x]=baralho.cartas[x]
                baralho.cartas.jogador=1
            elif x>20:
                p2.mao[x%10]=baralho.cartas[x]
                baralho.cartas.jogador=2
            elif x>30:
                p3.mao[x%20]=baralho.cartas[x]
                baralho.cartas.jogador=3
            else:
                p4.mao[x%30]=baralho.cartas[x]
                baralho.cartas.jogador=4
            x+=1
            
        print("Suecaaaaaa!!")
        for i in range(4):
            print("O Trunfo do jogo é ",baralho.cartas.naipe[i],".")
            trunfo=baralho.cartas.naipe[i]

        """Visualização das mãos dos jogadores"""
        print("Jogador 1: "', '.join(p1.mao))
        print("Jogador 2: "', '.join(p2.mao))
        print("Jogador 3: "', '.join(p3.mao))
        print("Jogador 4: "', '.join(p4.mao))
        
        """Início dos rounds"""
        y=1
        placar=[0,0]
        while y!=11:
            print("Round ",y,"! Placar: ",placar)
            """Tentativa de chamar função Round_"""
            placar= Round_(trunfo,baralho,primeiro,placar)
            y+=1

        """Tentativa de chamar função Vencedor"""
        print(Vencedor(placar))

        nova=input("Deseja jogar novamente? Tecla qualquer tecla exceto q.")
        if nova!="q":

            """Tentativa de chamar função play_game"""
            a= play_game()
        

    """"g = ganhador da rodada, r = cartas usadas pelos jogadores na rodada, placar = placar atual do jogo a ser atualizado"""
    def Winner(self, g, r, placar): 
        print("O vencedor da rodada é o Jogador ",g,"!")

        placar[0]=int(r[0].pontos[r[0].valor] + r[2].pontos[r[2].valor])
        placar[1]=int(r[1].pontos[r[1].valor] + r[3].pontos[r[3].valor])
        return placar

    """Mensagem final"""
    def Vencedor(self,p):
        if p[0]==p[1]:
            print("Empate!!")
        elif p[0]>p[1]:
            print("A equipe 1 ganhou!")
        else:
            print("A equipe 2 ganhou!")




