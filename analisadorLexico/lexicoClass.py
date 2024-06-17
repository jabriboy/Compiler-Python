import re
from tokenClass import Token, TOKEN_TYPES

class Lexer:
    def __init__(self, rules):
        self.rules = [(token_type, re.compile(pattern), cod) for token_type, pattern, cod in rules]
        self.tokens = []
    
    def tokenize(self, text):
        pos = 0
        while pos < len(text):
            match = None
            for token_type, pattern, cod in self.rules:
                match = pattern.match(text, pos)
                if match:
                    value = match.group(0)
                    if token_type not in ['espaco', 'comentarioLinha', 'comentarioNLinhas']:  # Ignorando espaços em branco
                        token = Token(token_type, value, cod)
                        self.tokens.append(token)
                    pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f'Illegal character at position {pos}')
        return self.tokens

# Testando o Lexer
if __name__ == '__main__':
    lexer = Lexer(TOKEN_TYPES)
    code = '''
        "$conscadeia_."
        'a'
        1.5
        3
        
        // mesma formacao, porém, códigos diferentes
        nomfuncao
        nomprograma

        _variavel
        '''
    tokens = lexer.tokenize(code)
    for token in tokens:
        print(token)
