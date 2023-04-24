from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('EKTEB', r'ekteb')
        # if else else if
        self.lexer.add('KEN',r'ken')
        self.lexer.add('MEKENECH_KEN',r'mekenech\s+ken')
        self.lexer.add('MEKENECH',r'mekenech')
        # for
        self.lexer.add('KARRER',r'karrer')
        # while
        self.lexer.add('WHILE',r'while')
        # int
        self.lexer.add('3DAD',r'3dad')
        # string
        self.lexer.add('JOMLA',r'jomla')
        # do while
        self.lexer.add('3AWED_MEDEM', r'do\s+while')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('STRING', r'"[^"]*"|\'[^\']*\'')


        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('SEMICOLON', r'\;')
        self.lexer.add('PLUS',r'\s*\+')
        self.lexer.add('MINUS',r'\s*\-')
        self.lexer.add('SLASH',r'\s*\/')
        
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
