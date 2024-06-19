# Lexic Compiler - Python
lexic compiler for a made up programming language called *Perpetuum2024.1*, developed to a Compiler class.
## Files:

- ### ==**MeuTeste.241**== is the text document that simulates the code.  
- ### ==__Main.py__== file generates 2 more files: MeuTeste.LEX and MeuTeste.TAB.  
- ### ==tokenClass.py== is the class that create the tokens, also, the file that has the *__TOKEN_TYPES__*
- ### ==lexicoClass.py== is the class that receive the code and separate it into tokens, that later will be put in the *.LEX* or the *.TAB* by the *Main.py** file.
- ### ==tabelaClass.py== is the especial class that handles everything about the table of simbols, and stores the table itself.

### Perpetuum2024.1 code exemple:
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

## Components:
#### Gabriel de Araujo Santos Rocha; gabriel.rocha@aln.senaicimatec.edu.br; +55 (71) 98526-8660
#### Maria Eduarda Benfica Gonçalves; maria.g@aln.senaicimatec.edu.br; +55 (71) 98238-8540
#### Ricardo Alexandre Santos da Silva; ricardo.silva@aln.senaicimatec.edu.br; +55 (71) 99931-9500
