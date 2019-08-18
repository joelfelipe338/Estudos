from matriz import Matriz

class Perceptron:

    def __init__(self, neuronios):
        # Declarando Valores Iniciais
        self.neoronios = neuronios
        self.pesos = Matriz(1,neuronios)
        self.bias = -1
        self.taxa = 0.01

    def treino(self,entrada,saidaFinal):
        # Verificando Resultado
        entrada = Matriz.matrizLinha(entrada)
        pesos_t = Matriz.transposta(self.pesos)
        soma = Matriz.mult(entrada,pesos_t)
        soma = Matriz.array(soma)
        soma[0] -= self.bias
        saida = Hebb(soma[0])
        erro = False

        # Atualizando Pesos
        if(saida != saidaFinal):
            taxaErro = saidaFinal - saida
            delta = Matriz.mult_escalar(entrada, self.taxa * taxaErro)
            self.pesos = Matriz.soma(delta,self.pesos)
            self.bias += (taxaErro*self.taxa*-1)
            erro = True
        return erro

    def predict(self,entrada):
        # Retorna saida basiado na entrada
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
