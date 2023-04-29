from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
<<<<<<< HEAD
        self.lexer.add('print', r'ekteb')
        # if else else if
        self.lexer.add('if',r'ken')
        self.lexer.add('CODE',r'code')
       
        self.lexer.add('L_CB',r'\{')
        self.lexer.add('R_CB',r'\}')
        self.lexer.add('COMPARE',r'==')
        self.lexer.add('AFFECT',r'=')
        self.lexer.add('DIFFERENT',r'!=')
        self.lexer.add('MULT',r'\*')
        self.lexer.add('DIVIDE',r'\/')
      
        # for
        self.lexer.add('FOR',r'karrer')
        # while
        self.lexer.add('while',r'madem')
        # int
        self.lexer.add('aadad',r'aadad')
        # string
        self.lexer.add('string',r'jomla')
        self.lexer.add('STRING', r'"[^"]*"|\'[^\']*\'')
        # do while
        # Number
        self.lexer.add('NUMBER', r'\d+')
=======
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


>>>>>>> main
        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')
        self.lexer.add('SEMICOLON', r'\;')
        self.lexer.add('PLUS',r'\s*\+')
        self.lexer.add('MINUS',r'\s*\-')
        self.lexer.add('FROM',r'men')
        self.lexer.add('TO',r'ila')
        self.lexer.add('IDENTIFIER',r'("_")?[a-zA-Z]+([0-9]|[a-zA-Z])*')
        self.lexer.ignore(r'\s+')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
