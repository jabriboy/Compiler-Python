import re
from tokenClass import Token, TOKEN_TYPES

class Lexer:
    def __init__(self, rules):
        self.rules = [(token_type, re.compile(pattern)) for token_type, pattern in rules]
        self.tokens = []
    
    def tokenize(self, text):
        pos = 0
        while pos < len(text):
            match = None
            for token_type, pattern in self.rules:
                match = pattern.match(text, pos)
                if match:
                    value = match.group(0)
                    if token_type != 'WHITESPACE':  # Ignorando espaços em branco
                        token = Token(token_type, value)
                        self.tokens.append(token)
                    pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f'Illegal character at position {pos}')
        return self.tokens

# Testando o Lexer
if __name__ == '__main__':
    lexer = Lexer(TOKEN_TYPES)
    code = 'a = 3 + 4 * (2 - 1)'
    tokens = lexer.tokenize(code)
    for token in tokens:
        print(token)
