from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('print', r'ekteb')
        # if else else if
        self.lexer.add('if',r'ken')
        self.lexer.add('else if',r'mekenech_ken')
        self.lexer.add('else',r'mekenech')
        # for
        self.lexer.add('for',r'KARRER')
        # while
        self.lexer.add('while',r'medem')
        # int
        self.lexer.add('int',r'3DAD')
        # string
        self.lexer.add('string',r'JOMLA')
        # do while
        self.lexer.add('do_while', r'3AWED\s+MEDEM')
        # Number
        self.lexer.add('NUMBER', r'\d+')

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
