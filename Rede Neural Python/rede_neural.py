import math

from matriz import Matriz


class RedeNeural:
	def __init__(self,neoEnt,neoOcul,neoSai):
		self.neoEnt = neoEnt
		self.neoOcul = neoOcul
		self.neoSai = neoSai
		self.bias_EO = Matriz(neoOcul, 1)
		self.bias_EO.valor(1)
		self.bias_OS = Matriz(neoSai, 1)
		self.bias_OS.valor(1)
		self.pesos_EO = Matriz(neoOcul, neoEnt)
		self.pesos_OS = Matriz(neoSai, neoOcul)
		self.taxa_aprendizado = 0.2

	def treino(self,entrada,saidaFinal):
		# Entrada -> Oculta
		entrada = Matriz.matriz(entrada)
		oculta = Matriz.mult(self.pesos_EO, entrada)
		oculta = Matriz.soma(oculta, self.bias_EO)
		oculta = Matriz.sigmoid(oculta)

		# Oculta -> Saida
		saida = Matriz.mult(self.pesos_OS, oculta)
		saida = Matriz.soma(saida, self.bias_OS)
		saida = Matriz.sigmoid(saida)

		#BACKPROPAGATION

		#Saida -> Oculta
		saidaFinal = Matriz.matriz(saidaFinal)
		saida_error = Matriz.sub(saidaFinal,saida)
		deriv_saida = Matriz.derivadaSigmoid(saida)
		oculta_t = Matriz.transposta(oculta)
		gradient_OS = Matriz.hadamard(deriv_saida,saida_error)
		gradient_OS = Matriz.mult_escalar(gradient_OS,self.taxa_aprendizado)
		delta_pesos_OS = Matriz.mult(gradient_OS,oculta_t)

		#Oculta -> Entrada
		pesos_OS_t = Matriz.transposta(self.pesos_OS)
		oculta_error = Matriz.mult(pesos_OS_t,saida_error)
		deriv_oculta = Matriz.derivadaSigmoid(oculta)
		entrada_t = Matriz.transposta(entrada)
		gradient_EO = Matriz.hadamard(deriv_oculta,oculta_error)
		gradient_EO = Matriz.mult_escalar(gradient_EO,self.taxa_aprendizado)
		delta_pesos_EO = Matriz.mult(gradient_EO,entrada_t)

		#Atualizando Pesos
		self.pesos_OS = Matriz.soma(self.pesos_OS,delta_pesos_OS)
		self.pesos_EO = Matriz.soma(self.pesos_EO,delta_pesos_EO)

	def predict(self,entrada):
		# Entrada -> Oculta
		entrada = Matriz.matriz(entrada)
		oculta = Matriz.mult(self.pesos_EO, entrada)
		oculta = Matriz.soma(oculta, self.bias_EO)
		oculta = Matriz.sigmoid(oculta)

		# Oculta -> Saida
		saida = Matriz.mult(self.pesos_OS, oculta)
		saida = Matriz.soma(saida, self.bias_OS)
		saida = Matriz.sigmoid(saida)
		saida = Matriz.array(saida)
		return saida