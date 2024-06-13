import re

# Definição dos tipos de tokens
TOKEN_TYPES = [
    ('NUMBER', r'\d+(\.\d*)?'),        # Números inteiros e de ponto flutuante
    ('ASSIGN', r'='),                  # Operador de atribuição
    ('PLUS', r'\+'),                   # Operador de adição
    ('MINUS', r'-'),                   # Operador de subtração
    ('MULT', r'\*'),                   # Operador de multiplicação
    ('DIV', r'/'),                     # Operador de divisão
    ('LPAREN', r'\('),                 # Parêntese esquerdo
    ('RPAREN', r'\)'),                 # Parêntese direito
    ('ID', r'[a-zA-Z_][a-zA-Z_0-9]*'), # Identificadores (variáveis)
    ('WHITESPACE', r'\s+'),            # Espaços em branco (serão ignorados)
    ('UNKNOWN', r'.'),                 # Qualquer outro caractere
]

# Classe que representa um token
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
