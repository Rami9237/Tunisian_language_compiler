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
        self.lexer.add('CODE',r'code')
        self.lexer.add('IDENTIFIER',r'("_")?[a-zA-Z]+([0-9]|[a-zA-Z])*')
        self.lexer.add('L_CB',r'\{')
        self.lexer.add('R_CB',r'\}')
        self.lexer.add('AFFECT',r'=')
        self.lexer.add('COMPARE',r'==')
        self.lexer.add('DIFFERENT',r'!=')
        self.lexer.add('MULT',r'\*')
        self.lexer.add('DIVIDE',r'\/')
      
        # for
        self.lexer.add('for',r'karrer')
        # while
        self.lexer.add('while',r'madem')
        # int
        self.lexer.add('aadad',r'aadad')
        # string
        self.lexer.add('string',r'jomla')
        self.lexer.add('STRING', r'"[^"]*"|\'[^\']*\'')
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
        self.lexer.add('FROM',r'men')
        self.lexer.add('TO',r'ila')
        self.lexer.ignore(r'\s+')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
