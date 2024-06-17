# Definição dos tipos de tokens
TOKEN_TYPES = [
    # CÓDIGO X
    ('comentarioLinha', r'//.*', 'X01'),
    ('comentarioNLinhas', r'/\*[\s\S]*?\*/', 'X02'),
    ('espaco', r'\s+', 'X03'),

    # CÓDIGO A
    ('cadeia', r'cadeia', 'A01'),
    ('caracter', r'caracter', 'A02'),
    ('declaracoes', r'declaracoes', 'A03'),
    ('enquanto', r'enquanto', 'A04'),
    ('false', r'false', 'A05'),
    ('fimDeclaracoes', r'fimDeclaracoes', 'A06'),
    ('fimEnquanto', r'fimEnquanto', 'A07'),
    ('fimFunc', r'fimFunc', 'A08'),
    ('fimFuncoes', r'fimFuncoes', 'A09'),
    ('fimPrograma', r'fimPrograma', 'A10'),
    ('fimSe', r'fimSe', 'A11'),
    ('funcoes', r'funcoes', 'A12'),
    ('imprime', r'imprime', 'A13'),
    ('inteiro', r'inteiro', 'A14'),
    ('logico', r'logico', 'A15'),
    ('pausa', r'pausa', 'A16'),
    ('programa', r'programa', 'A17'),
    ('real', r'real', 'A18'),
    ('retorna', r'retorna', 'A19'),
    ('se', r'se', 'A20'),
    ('senao', r'senao', 'A21'),
    ('tipoFunc', r'tipoFunc', 'A22'),
    ('tipoParam', r'tipoParam', 'A23'),
    ('tipoVar', r'tipoVar', 'A24'),
    ('true', r'true', 'A25'),
    ('vazio', r'vazio', 'A26'),

    # CÓDIGO B

    ('%', r'%', 'B01'),
    ('(', r'\(', 'B02'),
    (')', r'\)', 'B03'),
    (',', r',', 'B04'),
    (':=', r':=', 'B06'),
    (':', r':', 'B05'),
    (';', r';', 'B07'),
    ('?', r'\?', 'B08'),
    ('[', r'\[', 'B09'),
    (']', r'\]', 'B10'),
    ('{', r'\{', 'B11'),
    ('}', r'\}', 'B12'),
    ('-', r'-', 'B13'),
    ('*', r'\*', 'B14'),
    ('/', r'/', 'B15'),
    ('+', r'\+', 'B16'),
    ('!=', r'!=', 'B17'),
    ('#', r'#', 'B17'),
    ('<=', r'<=', 'B19'),
    ('<', r'<', 'B18'),
    ('==', r'==', 'B20'),
    ('>=', r'>=', 'B22'),
    ('>', r'>', 'B21'),

    # CÓDIGO C

    ('consCadeia', r'\"[a-zA-Z\s\S$_.0-9]*\"', 'C01'),
    ('consCaracter', r'\'[a-zA-Z]\'', 'C02'),
    ('consReal', r'\d*\.\d+|\d+\.\d*', 'C04'),
    ('consInteiro', r'\d+', 'C03'),
    ('nomFuncao', r'[a-zA-Z][a-zA-Z0-9]*', 'C05'),
    ('nomPrograma', r'[a-zA-Z][a-zA-Z0-9]*', 'C06'),
    ('variavel', r'[a-zA-Z_][a-zA-Z_0-9]*', 'C07'),

    # CÓDIGO D

    ('subMaquina1', r'sub', 'D01'),
    ('subMaquina2', r'sub', 'D02'),
    ('subMaquina3', r'sub', 'D03'),

    # CÓDIGO Z

    ('desconhecido', r'.', 'Z01'),
]

# Classe que representa um token
class Token:
    def __init__(self, type, value, cod):
        self.type = type
        self.value = value
        self.cod = cod

    def __repr__(self):
        return f'Token(Átomo: {self.type}, Valor: {self.value}, Código: {self.cod})'
