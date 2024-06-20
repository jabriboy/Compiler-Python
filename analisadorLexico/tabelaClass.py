from tokenClass import Token
from typing import Union

class Tabela:
	def __init__(self) -> None:
		self.table = []

	def checkTable(self, lexeme: object) -> bool:
		for lex in self.table:
			if lex.value == lexeme.value:
				return True
		return False
	
	def addLine(self, lexeme: object) -> bool:
		for lex in self.table:
			if lex.value == lexeme.value:
				if len(lex.lines) < 5:
					lex.lines.append(lexeme.lines[0])
					return True
		return False

	def addTable(self, lexeme: object) -> None:
		lex = Token(lexeme.type, lexeme.value, lexeme.cod, lexeme.lines[0], lexeme.indice, lexeme.trunc)
		self.table.append(lex)

	def getIndice(self, lexeme: object) -> Union[int, None]:
		pos = 0
		for lex in self.table:
			pos += 1
			if lex.value == lexeme.value:
				self.table[pos-1].indice = pos
				return pos
		return None

	def getTable(self) -> None:
		pos = 0
		for lex in self.table:
			pos += 1
			print(f'\nindice: {pos}, {lex}\n---------------------------------------------------------------------------------------------')

	def __repr__(self) -> str:
		return f'{self.table}'