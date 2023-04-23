from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('ekteb', r'print')
        # if else else if
        self.lexer.add('ken',r'if')
        self.lexer.add('mekenech ken',r'else if')
        self.lexer.add('mekenech',r'else')
        # for
        self.lexer.add('karrer',r'for')
        # while
        self.lexer.add('medem',r'while')
        # int
        self.lexer.add('3dad',r'int')
        # string
        self.lexer.add('jomla',r'string')
        # do while
        self.lexer.add('3awed_medem', r'do\s+while')
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
