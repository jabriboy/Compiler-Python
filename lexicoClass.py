import re
from tokenClass import Token, TOKEN_TYPES
from tabelaClass import Tabela
from escopoClass import Escopo

class Lexer:
    def __init__(self, rules) -> None:
        self.rules = [(token_type, re.compile(pattern), cod) for token_type, pattern, cod in rules]
        self.tokens = []
        self.tabela = Tabela()
    
    def tokenize(self, text) -> list[object]:
        pos = 0
        lines = 1
        while pos < len(text):
            match = None
            for token_type, pattern, cod in self.rules:
                match = pattern.match(text, pos)
                if match:
                    value = match.group(0)
                    escopo = Escopo(token_type, value)  # lexico organiza escopo
                    esc = escopo.getEscopo()

                    # print(value)
                    if token_type == 'enter':
                        lines += 1
                    if esc == 1 and token_type == 'nomFuncao':
                        esc = 0
                    elif esc == 2 and token_type == 'nomPrograma':
                        esc = 0
                    elif token_type not in ['espaco', 'comentarioLinha', 'comentarioNLinhas', 'desconhecido', 'enter']:  # Ignorando espaços em branco
                        indice = 0
                        trunc = test = value
                        if len(test) > 30:
                            if token_type == 'consCadeia':
                                trunc = value[:31]
                                trunc += '"'
                            else:
                                trunc = value[:30]
                        token = Token(token_type, value, cod, lines, indice, trunc, '---')

                        if not self.tabela.checkTable(token) and cod[0] not in ['A', 'B', 'X', 'D', 'Z']:
                            self.tabela.addTable(token)
                        else:
                            self.tabela.addLine(token)
                        
                        token.indice = self.tabela.getIndice(token) 
                        self.tokens.append(token)
                    pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f'Illegal character at position {pos}, line {lines}')
        return self.tokens, self.tabela.table

# Testando o Lexer
if __name__ == '__main__':
    lexer= Lexer(TOKEN_TYPES)
    code = '''
        programa nomeProg
        funcoes nomeFunc
        variavel
        sub
        "$ cadeia"
        '''
    tokens, tabela = lexer.tokenize(code)
    for token in tokens:
        print(token)

