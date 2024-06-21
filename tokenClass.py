# Definição dos tipos de tokens
TOKEN_TYPES = [
    # CÓDIGO X
    ('enter', r'\r?\n|\r', 'X00'),
    ('comentarioLinha', r'//.*', 'X01'),
    ('comentarioNLinhas', r'/\*[\s\S]*?\*/', 'X02'),
    ('espaco', r'\s+', 'X03'),

    # CÓDIGO A (palavras reservadas)
    ('cadeia', r'cadeia(?![\w_])', 'A01'),
    ('caracter', r'caracter(?![\w_])', 'A02'),
    ('declaracoes', r'declaracoes(?![\w_])', 'A03'),
    ('enquanto', r'enquanto(?![\w_])', 'A04'),
    ('false', r'false(?![\w_])', 'A05'),
    ('fimDeclaracoes', r'fimDeclaracoes(?![\w_])', 'A06'),
    ('fimEnquanto', r'fimEnquanto(?![\w_])', 'A07'),
    ('fimFunc', r'fimFunc(?![\w_])', 'A08'),
    ('fimFuncoes', r'fimFuncoes(?![\w_])', 'A09'),
    ('fimPrograma', r'fimPrograma(?![\w_])', 'A10'),
    ('fimSe', r'fimSe(?![\w_])', 'A11'),
    ('funcoes', r'funcoes(?![\w_])', 'A12'),
    ('imprime', r'imprime(?![\w_])', 'A13'),
    ('inteiro', r'inteiro(?![\w_])', 'A14'),
    ('logico', r'logico(?![\w_])', 'A15'),
    ('pausa', r'pausa(?![\w_])', 'A16'),
    ('programa', r'programa(?![\w_])', 'A17'),
    ('real', r'real(?![\w_])', 'A18'),
    ('retorna', r'retorna(?![\w_])', 'A19'),
    ('se', r'se(?![\w_])', 'A20'),
    ('senao', r'senao(?![\w_])', 'A21'),
    ('tipoFunc', r'tipoFunc(?![\w_])', 'A22'),
    ('tipoParam', r'tipoParam(?![\w_])', 'A23'),
    ('tipoVar', r'tipoVar(?![\w_])', 'A24'),
    ('true', r'true(?![\w_])', 'A25'),
    ('vazio', r'vazio(?![\w_])', 'A26'),

    # CÓDIGO B (simbolos reservados)
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

    # CÓDIGO C (Identificadores)
    ('consCadeia', r'"[^"]*"', 'C01'),
    ('consCaracter', r'\'[a-zA-Z]\'', 'C02'),
    ('consReal', r'\d*\.\d+|\d+\.\d*', 'C04'),
    ('consInteiro', r'\d+', 'C03'),
    ('variavel', r'[a-zA-Z_][a-zA-Z_0-9]*', 'C07'),
    ('nomFuncao', r'[a-zA-Z][a-zA-Z0-9]*', 'C05'),
    ('nomPrograma', r'[a-zA-Z][a-zA-Z0-9]*', 'C06'),

    # CÓDIGO D
    # ('subMaquina1', r'sub', 'D01'),
    # ('subMaquina2', r'sub', 'D02'),
    # ('subMaquina3', r'sub', 'D03'),

    # CÓDIGO Z (caracteres não reconhecido ex: ç, á, ô...)
    ('desconhecido', r'.', 'Z01'),
]

# Classe que representa um token
class Token:
    def __init__(self, type, value, cod, line, indice, trunc, tipo) -> None:
        self.type = type
        self.value = value
        self.cod = cod
        self.lines = [line]
        self.indice = indice
        self.trunc = trunc
        self.tipo = tipo

    def __repr__(self) -> str:
        return f'Lexeme: {self.trunc}, Código: {self.cod}, Indice na Tab. de Simbolos: {self.indice}, Linha: {self.lines[0]}'
