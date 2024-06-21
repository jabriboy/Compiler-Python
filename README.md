# Lexic Analyzer - Python
Lexical Analyzer for a made up programming language called *__Perpetuum2024.1__*, developed for a College Project on Compilers.

## Perpetuum2024.1 code exemple:
```Perpetuum2024.1
programa programa1
funcoes funcoes1(inteiro a, real b){
	real var1 := b
	inteiro var2 := a

	real var3 := var1 + 2.5
	inteiro var4 := var2 * 2

	retorna var4
}

funcoes1(20, 2.5)
```
## Classes
- ### == __Main.py__ == file generates 2 more files: MeuTeste.LEX and MeuTeste.TAB.  
- ### == __tokenClass.py__ == is the class that create the tokens, also, the file that has the *TOKEN_TYPES*
- ### == __lexicoClass.py__ == is the class that receive the code and separate it into tokens, that later will be put in the *.LEX* or the *.TAB* by the *Main.py** file.
- ### == __tabelaClass.py__ == is the especial class that handles everything about the table of simbols, and stores the table itself.
- ### == __escopoClass__ == is the class that changes the scope to diferentiate when the "variable" is variable, nomFuncao or nomPrograma

## Files
- ### == __arquivosFonte__ == is the folder where all the source codes will be placed to eventualy be compiled by the compiler
- ### == __arquivosOutput__ == is the folder where the two report files will be created for each source file compiled

## How to Use
- ### Python 3 installed or above
- ### Create a text file inside the "__arquivoFonte__" folder with the extension __.241__ and write the source code in Perpetuum2024.1 language. <br/>__ex: "MeuTeste.241"__
- ### Run the __Main.py__ file. This will open the terminal and ask for a file name (obs: Dont write the extension). <br/>if the file you created is "MeuTeste.241" you will write "MeuTeste" as the file name
- ### When finished, the terminal will display the lexic report and the table of simbols. These two files will be created at the "__arquivosOutput__" folder

## Exemples

### Source Code in Perpetuum2024.1
```Perpetuum2024.1
inteiro var1 := 10
inteiro var2 := 20

inteiro var3 := var1 + var2

imprime var3
```

### Lexic Report Generated
```
RELATÓRIO DA ANÁLISE LÉXICA. Texto fonte analisado: MeuTeste.241
--------------------------------------------------------------------------
Lexeme: inteiro, Código: A14, Indice na Tab. de Simbolos: None, Linha: 1
---------------------------------------------------------------------------
Lexeme: var1, Código: C07, Indice na Tab. de Simbolos: 1, Linha: 1
---------------------------------------------------------------------------
Lexeme: :=, Código: B06, Indice na Tab. de Simbolos: None, Linha: 1
---------------------------------------------------------------------------
Lexeme: 10, Código: C03, Indice na Tab. de Simbolos: 2, Linha: 1
---------------------------------------------------------------------------
Lexeme: inteiro, Código: A14, Indice na Tab. de Simbolos: None, Linha: 2
---------------------------------------------------------------------------
Lexeme: var2, Código: C07, Indice na Tab. de Simbolos: 3, Linha: 2
---------------------------------------------------------------------------
Lexeme: :=, Código: B06, Indice na Tab. de Simbolos: None, Linha: 2
---------------------------------------------------------------------------
Lexeme: 20, Código: C03, Indice na Tab. de Simbolos: 4, Linha: 2
---------------------------------------------------------------------------
Lexeme: inteiro, Código: A14, Indice na Tab. de Simbolos: None, Linha: 4
---------------------------------------------------------------------------
Lexeme: var3, Código: C07, Indice na Tab. de Simbolos: 5, Linha: 4
---------------------------------------------------------------------------
Lexeme: :=, Código: B06, Indice na Tab. de Simbolos: None, Linha: 4
---------------------------------------------------------------------------
Lexeme: var1, Código: C07, Indice na Tab. de Simbolos: 1, Linha: 4
---------------------------------------------------------------------------
Lexeme: +, Código: B16, Indice na Tab. de Simbolos: None, Linha: 4
---------------------------------------------------------------------------
Lexeme: var2, Código: C07, Indice na Tab. de Simbolos: 3, Linha: 4
---------------------------------------------------------------------------
Lexeme: imprime, Código: A13, Indice na Tab. de Simbolos: None, Linha: 6
---------------------------------------------------------------------------
Lexeme: var3, Código: C07, Indice na Tab. de Simbolos: 5, Linha: 6
---------------------------------------------------------------------------
```

### Table of Simbols

```
RELATÓRIO DA TABELA DE SÍMBOLOS. Texto fonte analisado: MeuTeste.241
---------------------------------------------------------------------------
Entrada: 1, Codigo: C07, Lexeme: var1, 
QntCharAntesTrunc: 4, QntCharDepoisTrunc: 4, 
Tipo Simbolo: VOI, Linhas: [1, 4],
---------------------------------------------------------------------------
Entrada: 1, Codigo: C03, Lexeme: 10, 
QntCharAntesTrunc: 2, QntCharDepoisTrunc: 2, 
Tipo Simbolo: INT, Linhas: [1],
---------------------------------------------------------------------------
Entrada: 1, Codigo: C07, Lexeme: var2, 
QntCharAntesTrunc: 4, QntCharDepoisTrunc: 4, 
Tipo Simbolo: VOI, Linhas: [2, 4],
---------------------------------------------------------------------------
Entrada: 1, Codigo: C03, Lexeme: 20, 
QntCharAntesTrunc: 2, QntCharDepoisTrunc: 2, 
Tipo Simbolo: INT, Linhas: [2],
---------------------------------------------------------------------------
Entrada: 1, Codigo: C07, Lexeme: var3, 
QntCharAntesTrunc: 4, QntCharDepoisTrunc: 4, 
Tipo Simbolo: VOI, Linhas: [4, 6],
---------------------------------------------------------------------------
```

## Components:
#### Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
#### Maria Eduarda Benfica Gonçalves; maria.g@aln.senaicimatec.edu.br; +55 (71) 98238-8540
#### Ricardo Alexandre Santos da Silva; ricardo.silva@aln.senaicimatec.edu.br; +55 (71) 99931-9500
