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

    @staticmethod
    def sub(A, B):
        C = Matriz(A.linha, A.coluna)
        for i in range(A.linha):
            for j in range(B.coluna):
                C.data[i][j] = A.data[i][j] - B.data[i][j]
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
        C = Matriz(A.linha, A.coluna)
        for i in range(A.linha):
            for j in range(A.coluna):
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