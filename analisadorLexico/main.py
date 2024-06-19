from lexicoClass import Lexer
from tabelaClass import Tabela
from tokenClass import Token, TOKEN_TYPES

nome = input('Nome do arquivo que deseja compilar: ')

with open(f'{nome}.241', 'r') as arquivoFonte:
	code = arquivoFonte.read()

lexer = Lexer(TOKEN_TYPES)
lex, tab = lexer.tokenize(code)


def createLex(lex: list[object]) -> None:
	# Criação e Escrita do Arquivo .LEX
	with open(f'{nome}.LEX', 'w') as arquivoLex:
		arquivoLex.write(
f'''Código da Equipe: 08
Componentes:
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660

RELATÓRIO DA ANÁLISE LÉXICA. Texto fonte analisado: {nome}.241
----------------------------------------------------------------------------------------------''')
		
		for i in lex:
			arquivoLex.write(f'\n{i}\n---------------------------------------------------------------------------------------------')
	

	# Leitura do Arquivo .LEX
	with open(f'{nome}.LEX', 'r') as arquivoLex:
			arqLex = arquivoLex.read()

			print(arqLex)


def createTab(tab: list[object]) -> None:
	# Criação e Escrita do Arquivo .LEX
	with open(f'{nome}.TAB', 'w') as arquivoTab:
		arquivoTab.write(
f'''Código da Equipe: 08
Componentes:
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660

RELATÓRIO DA TABELA DE SÍMBOLOS. Texto fonte analisado: {nome}.241
----------------------------------------------------------------------------------------------''')
	

		for i in tab:
			arquivoTab.write(f'\nEntrada: 1, Tipo Simbolo: "---", {i}\n---------------------------------------------------------------------------------------------')
	

	# Leitura do Arquivo .LEX
	with open(f'{nome}.TAB', 'r') as arquivoTab:
			arqTab = arquivoTab.read()

			print(arqTab)

if __name__ == "__main__":
	createLex(lex)
	createTab(tab)