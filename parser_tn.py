from rply import ParserGenerator
from ast_tn import Divide, Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['EKTEB',
             'KEN',
             'MEKENECH_KEN',
             'MEKENECH',
             'KARRER',
             'MEDEM',
             '3DAD',
             'JOMLA',
             '3AWED_MEDEM',
             'LPAREN',
             'RPAREN',
             'COMMA',
             'SEMICOLON',
             'PLUS',
             'MINUS',
             'SLASH',
             'NUMBER',
             'STRING',
             'FOR',
             'IDENTIFIER',
             'FROM',
             'TO',
             'L_CB',
             'R_CB']
        )

    def get_parser(self):
        return self.pg.build()

    def parse(self):
        def print_prod(p):
            print(p.value[0].value)        
        def program(p):
            return Print(p[2])
        def loop_prod(p):
            for p[1].value in range(int(p[3].value),int(p[5].value)+1):
                print_prod(p[7])
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
        @self.pg.production('program : expression')

        @self.pg.production('expression : EKTEB LPAREN expression RPAREN SEMICOLON')
        def program_production(p):
             return program(p)

        @self.pg.production('expression : expression PLUS NUMBER')
        
        def expression_production_sum(p):
            return expression(p)

        @self.pg.production('expression : expression MINUS NUMBER')
        def expression_production_sub(p):
            return expression(p)
        @self.pg.production('expression : NUMBER')
        def number_production(p):
            return number(p)
        @self.pg.production('expression : STRING')
        def string_production(p):
            return p
        @self.pg.production('expression : FOR IDENTIFIER FROM NUMBER TO NUMBER L_CB expression R_CB SEMICOLON')
        def loop_production(p):
            return loop_prod(p)       
        @self.pg.production('expression : ')
        

        @self.pg.error
        def error_handler(token):
            raise ValueError(token)
