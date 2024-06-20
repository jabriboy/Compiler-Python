class Escopo:
	def __init__(self, token_type, value) -> None:
		self.token_type = token_type
		self.value = value
		self.escopo = 0
		# escopo = 0 (variável)
		# escopo = 1 (nomFuncao)
		# escopo = 2 (nomPrograma)

	def getEscopo(self) -> int:
		if self.value == 'funcoes':
			self.escopo = 1
		elif self.value == 'programa':
			self.escopo == 2
		return self.escopo