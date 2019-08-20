from matriz import Matriz

class Adaline:
    def __init__(self,neuronios):
        self.neuronios = neuronios
        self.pesos = Matriz(1, neuronios)
        self.bias = -1
        self.taxa = 0.0025
        self.precisao = 0.0000001

    def treino(self,entrada,saida):
        # Verificando e Atualizando pesos
        entrada = Matriz.matrizLinha(entrada)
        pesos_t = Matriz.transposta(self.pesos)
        soma = Matriz.mult(pesos_t,entrada)
        soma = Matriz.array(soma)
        soma[0] -= self.bias
        erro = saida - soma[0]
        delta = erro * self.taxa
        self.bias += (delta * -1)
        delta = Matriz.mult_escalar(entrada,delta)
        self.pesos = Matriz.soma(self.pesos,delta)

    def EQM(self,entrada,saida):
        eqm = 0
        pesos_t = Matriz.transposta(self.pesos)
        for i in range(len(entrada)):
            entrada_m = Matriz.matrizLinha(entrada[i])
            u = Matriz.mult(entrada_m,pesos_t)
            u = Matriz.array(u)
            u[0] -= self.bias
            eqm += (saida[i] - u[0])**2
        eqm = eqm/len(entrada)
        return eqm

    def testeErro(self,eqm_ant,eqm_atual):
        mod = eqm_atual - eqm_ant
        if(mod < 0):
            mod = mod * -1
        if(mod < self.precisao):
            return True
        return False

    def predict(self,entrada):
        entrada = Matriz.matrizLinha(entrada)
        pesos_t = Matriz.transposta(self.pesos)
        soma = Matriz.mult(entrada, pesos_t)
        soma = Matriz.array(soma)
        soma[0] -= self.bias
        saida = Hebb(soma[0])
        return saida

def Hebb(x):
    if(x < 0):
        return -1
    else:
        return 1



