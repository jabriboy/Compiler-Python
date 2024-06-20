from lexicoClass import Lexer
from tokenClass import TOKEN_TYPES

nome = input('Nome do arquivo que deseja compilar: ')

with open(f'./arquivosFonte/{nome}.241', 'r') as arquivoFonte:
	code = arquivoFonte.read()

lexer = Lexer(TOKEN_TYPES)
lex, tab = lexer.tokenize(code)


def createLex(lex: list[object]) -> None:
	# Criação e Escrita do Arquivo .LEX
	with open(f'./arquivosOutput/{nome}.LEX', 'w') as arquivoLex:
		arquivoLex.write(
f'''Código da Equipe: 08
Componentes:
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
	Maria Eduarda Benfica Gonçalves; maria.g@aln.senaicimatec.edu.br; +55 (71) 98238-8540
	Ricardo Alexandre Santos da Silva; ricardo.silva@aln.senaicimatec.edu.br; +55 (71) 99931-9500

RELATÓRIO DA ANÁLISE LÉXICA. Texto fonte analisado: {nome}.241
----------------------------------------------------------------------------------------------''')
		
		for i in lex:
			arquivoLex.write(f'\n{i}\n---------------------------------------------------------------------------------------------')
	

	# Leitura do Arquivo .LEX
	with open(f'./arquivosOutput/{nome}.LEX', 'r') as arquivoLex:
			arqLex = arquivoLex.read()

			print(arqLex)


def createTab(tab: list[object]) -> None:
	# Criação e Escrita do Arquivo .LEX
	with open(f'./arquivosOutput/{nome}.TAB', 'w') as arquivoTab:
		arquivoTab.write(
f'''Código da Equipe: 08
Componentes:
	Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
	Maria Eduarda Benfica Gonçalves; maria.g@aln.senaicimatec.edu.br; +55 (71) 98238-8540
	Ricardo Alexandre Santos da Silva; ricardo.silva@aln.senaicimatec.edu.br; +55 (71) 99931-9500

RELATÓRIO DA TABELA DE SÍMBOLOS. Texto fonte analisado: {nome}.241
------------------------------------------------------------------------------------------------------''')
	

		for i in tab:
			value = i.value.replace('"', '')
			trunc = i.trunc.replace('"', '')
			arquivoTab.write(f'\nEntrada: 1, Codigo: {i.cod}, Lexeme: {i.trunc}, \nQntCharAntesTrunc: {len(value)}, QntCharDepoisTrunc: {len(trunc)}, \nTipo Simbolo: ---, Linhas: {i.lines},\n------------------------------------------------------------------------------------------------------')
	

	# Leitura do Arquivo .LEX
	with open(f'./arquivosOutput/{nome}.TAB', 'r') as arquivoTab:
			arqTab = arquivoTab.read()

			print(arqTab)



if __name__ == "__main__":
	createLex(lex)
	createTab(tab)