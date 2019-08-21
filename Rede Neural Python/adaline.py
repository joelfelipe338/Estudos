from matriz import Matriz
from random import random
class Adaline:
    def __init__(self,neuronios):
        self.neuronios = neuronios
        self.pesos = Matriz(1, neuronios)
        self.bias = random()
        self.taxa = 0.0025
        self.precisao = 0.0000001

    def treino(self, entrada, saida):
        entrada = Matriz.matrizLinha(entrada)
        pesos_t = Matriz.transposta(self.pesos)
        soma = Matriz.mult(entrada, pesos_t)
        soma.data[0][0] -= self.bias;
        erro = saida - soma.data[0][0]
        delta = erro * self.taxa
        self.bias = delta * -1
        delta = Matriz.mult_escalar(entrada,delta)
        self.pesos = Matriz.soma(self.pesos,delta)

    def EQM(self,padroes,entrada,saida):
        eqm = 0
        x = 0
        pesos_t = Matriz.transposta(self.pesos)
        for i in entrada:
            i = Matriz.matrizLinha(i)
            u = Matriz.mult(i,pesos_t)
            u = u.data[0][0] - self.bias
            erro = saida[x] - u
            x += 1
            eqm += erro**2
        eqm = eqm/padroes
        return eqm

        eqm = soma/padroes
        return eqm

    def testeErro(self,eqm_ant,eqm_atual):
        mod = eqm_atual - eqm_ant
        if(mod < 0):
            mod = mod * -1
        if(mod <= self.precisao):
            return True
        return False

    def predict(self,entrada):
        entrada = Matriz.matrizLinha(entrada)
        pesos_t = Matriz.transposta(self.pesos)
        soma = Matriz.mult(entrada,pesos_t)
        soma.data[0][0] -= self.bias;
        return Hebb(soma.data[0][0])

def Hebb(x):
    if(x < 0):
        return -1
    else:
        return 1



