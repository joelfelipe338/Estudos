from adaline import Adaline
from random import  randint

t1 = Adaline(2)

E = [[1,1],[1,0],[0,1],[0,0]]
S = [1,-1,-1,1]

treino = True
x = 0
while(treino):
    print("Geração : ",x)
    x += 1
    for i in range(len(E)):
        erroAnt = t1.EQM(E,S)
        t1.treino(E[i],S[i])
        erroAtual = t1.EQM(E,S)
        if(t1.testeErro(erroAnt,erroAtual)):
            treino = False
            print("Rede Treinada")
            break


print(t1.predict([1,1]))
print(t1.predict([1,0]))
print(t1.predict([0,1]))
print(t1.predict([0,0]))
