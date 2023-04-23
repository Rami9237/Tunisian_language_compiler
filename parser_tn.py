from rply import ParserGenerator
from ast_tn import Divide, Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['ekteb',
             'ken',
             'mekenech ken',
             'mekenech',
             'karrer',
             'medem',
             '3dad',
             'jomla',
             '3awed_medem',
             'LPAREN',
             'RPAREN',
             'COMMA',
             'SEMICOLON',
             'PLUS',
             'MINUS',
             'SLASH',
             'NUMBER']
        )

    def get_parser(self):
        return self.pg.build()

    def parse(self):
        def program(p):
            return Print(p[2])
        
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'PLUS':
                return Sum(left, right)
            elif operator.gettokentype() == 'MINUS':
                return Sub(left, right)
            elif operator.gettokentype() == 'SLASH':
                return Divide(left, right)
          
        def number(p):
            return Number(p[0].value)   

        @self.pg.production('program : ekteb LPAREN expression RPAREN SEMICOLON')
        def program_production(p):
            return program(p)

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        def expression_production(p):
            return expression(p)

        @self.pg.production('expression : NUMBER')
        def number_production(p):
            return number(p)

        @self.pg.error
        def error_handler(token):
            raise ValueError(token)
