class RedeNeural:
	def __init__(self,neoEnt,neoOcul,neoSai):
		self.neoEnt = neoEnt
		self.neoOcul = neoOcul
		self.neoSai = neoSai
		self.bias_EO = Matriz(neoOcul,1)
		self.bias_OS = Matriz(neoSai,1)
		self.pesos_EO = Matriz(neoOcul,neoEnt)
		self.pesos_OS = Matriz(neoSai,neoOcul)

	def feedForward(self,entrada):

