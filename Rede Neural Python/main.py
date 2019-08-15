import math

from matriz import Matriz
from rede_neural import RedeNeural
from random import  randint
rede = RedeNeural(2,6,1)
treino = True
liso = 1
irregular = 0
maca = 1
laranja = 0
E = [[140,1],[130,1],[150,0],[160,0]]
S = [[1],[1],[0],[0]]
x = 1
while(treino):
    print("Geração ",x,":")
    print(rede.predict([130,1])[0])
    x += 1
    for i in range(10000):
        index = randint(0,3)
        rede.treino(E[index],S[index])
    if(rede.predict([140,1])[0] > 0.9 and rede.predict([150,0])[0] < 0.1 or x == 40):
        treino = False
        print("!!!!ACABOU, REDE TREINADA!!!!")


peso = float(input("digite o peso"))
tipo = 1
print(rede.predict([peso,tipo])[0])
