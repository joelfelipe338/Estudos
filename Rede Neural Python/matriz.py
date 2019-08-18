import math
from random import random


class Matriz:
    def __init__(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        self.data = []
        for i in range(self.linha):
            linha = []
            for j in range(self.coluna):
                linha.append(random())
            self.data.append(linha)

    def print(self):
        for i in range(self.linha):
            for j in range(self.coluna):
                print(f'{self.data[i][j]} ',end='')
            print()

    @staticmethod
    def soma(A,B):
        C = Matriz(A.linha,A.coluna)
        for i in range(A.linha):
            for j in range(B.coluna):
                C.data[i][j] = A.data[i][j] + B.data[i][j]
        return C

    def valor(self,A):

        for i in range(self.linha):
            for j in range(self.coluna):
                self.data[i][j] = A


    @staticmethod
    def sub(A, B):
        C = Matriz(A.linha, A.coluna)
        for i in range(A.linha):
            for j in range(B.coluna):
                C.data[i][j] = A.data[i][j] - B.data[i][j]
        return C

    @staticmethod
    def matrizColuna(A):
        C = Matriz(len(A), 1)
        for i in range(C.linha):
            for j in range(C.coluna):
                C.data[i][j] = A[i]
        return C

    @staticmethod
    def matrizLinha(A):
        C = Matriz(1,len(A))
        for i in range(C.linha):
            for j in range(C.coluna):
                C.data[i][j] = A[j]
        return C

    @staticmethod
    def array(A):
        C = []
        for i in range(A.coluna):
            C.append(A.data[0][i])
        return C

    @staticmethod
    def hadamard(A, B):
        C = Matriz(A.linha, A.coluna)
        for i in range(A.linha):
            for j in range(B.coluna):
                C.data[i][j] = A.data[i][j] * B.data[i][j]
        return C

    @staticmethod
    def mult_escalar(A, B):
        C = Matriz(A.linha, A.coluna)
        for i in range(A.linha):
            for j in range(A.coluna):
                C.data[i][j] = A.data[i][j] * B
        return C

    @staticmethod
    def transposta(A):
        C = Matriz(A.coluna, A.linha)
        for i in range(A.coluna):
            for j in range(A.linha):
                C.data[i][j] = A.data[j][i]
        return C


    @staticmethod
    def mult(A, B):
        soma = 0
        C = Matriz(A.linha, B.coluna)
        for i in range(A.linha):
            for j in range(B.coluna):
                for k in range(B.linha):
                    soma += A.data[i][k] * B.data[k][j]
                C.data[i][j] = soma
                soma = 0
        return C

    @staticmethod
    def sigmoid(A):
        for i in range(A.linha):
            for j in range(A.coluna):
                A.data[i][j] = sigmoid(A.data[i][j])
        return A

    @staticmethod
    def derivadaSigmoid(A):
        for i in range(A.linha):
            for j in range(A.coluna):
                A.data[i][j] = derivadaSigmoid(A.data[i][j])
        return A


def sigmoid(x):
    return 1/(1 + math.exp(-x))

def derivadaSigmoid(x):
    return x*(1 - x)
