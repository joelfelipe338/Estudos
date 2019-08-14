from random import random
class Matriz:

    def __init__(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        self.data = []
        for i in range(self.linha):
            linha = []
            for j in range(self.coluna):
                linha.append(round(random()*100))
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