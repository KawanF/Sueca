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
    
    equipe = [1,2]
    
    def __init__(self, v, n):

        self.valor = v
        self.naipe = n

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

from random import shuffle

class Baralho:
    def __init__(self):
        self.cartas = []
        for i in range(2, 12):
            for j in range(4):
                self.cartas.append(Carta(i,j))
        shuffle(self.cartas)

    def rm_card(self):
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()


teste=Baralho()
x=0
while x!=40:
    print(teste.cartas[x], teste.cartas[x].pontos[teste.cartas[x].valor])
    x+=1
