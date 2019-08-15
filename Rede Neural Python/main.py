import math

from matriz import Matriz
from rede_neural import RedeNeural
from random import  randint
rede = RedeNeural(2,3,1)
treino = True
E = [[40,40],[77,53],[15,1],[2,2]]
S = [[0],[1],[1],[0]]
x = 1
while(treino):
    print("Geração ",x,":")
    print(rede.predict([40,40])[0])
    x += 1
    for i in range(10000):
        index = randint(0,3)
        rede.treino(E[index],S[index])
    if(rede.predict([40,40])[0] < 0.1 and rede.predict([77,53])[0] > 0.9):
        treino = False
        print("!!!!ACABOU, REDE TREINADA!!!!")
        print(rede.predict([15,15])[0])
        print(rede.predict([24,42])[0])
        print(rede.predict([64,64])[0])
        print(rede.predict([67,1])[0])

