import re
from tokenClass import Token, TOKEN_TYPES
from tabelaClass import Tabela

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
                    if token_type == 'enter':
                        lines += 1
                    if token_type not in ['espaco', 'comentarioLinha', 'comentarioNLinhas', 'desconhecido', 'enter']:  # Ignorando espaços em branco
                        if match.span()[1] - match.span()[0] <= 30:
                            indice = 0
                            token = Token(token_type, value, cod, lines, indice)

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
        var1 var2 var3
        '''
    tokens, tabela = lexer.tokenize(code)
    for token in tokens:
        print(token)

