from rply import ParserGenerator
from ast_tn import Divide, Number, Sum, Sub, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['print',
             'if',
             'DIVIDE',
             'PLUS',
             'MINUS',
             'MULT',
             'else if',
             'else',
             'for',
             'while',
             'aadad',
             'string',
             'do_while',
             'LPAREN',
             'RPAREN',
             'COMMA',
             'SEMICOLON',
             'NUMBER',
             'CODE',
             'IDENTIFIER',
             'L_CB',
             'R_CB',
             'AFFECT',
             'COMPARE',
             'DIFFERENT',
             'STRING',
             'TO',
             'FROM'
            ]
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
            elif operator.gettokentype() == 'DIVIDE':
                return Divide(left, right)
        def number(p):
            return Number(p[0].value)   

        @self.pg.production('program : CODE IDENTIFIER L_CB instr R_CB')
        def program_production(p):
            return 0
        @self.pg.production('instr : for IDENTIFIER FROM factor TO factor L_CB instr R_CB')
        def program_production(p):
            return 0
        @self.pg.production('instr : if LPAREN expression COMPARE expression RPAREN L_CB instr R_CB')
        def program_production(p):
            return 0
        @self.pg.production('instr : if LPAREN expression DIFFERENT expression RPAREN L_CB instr R_CB')
        def program_production(p):
            return 0
        @self.pg.production('instr : IDENTIFIER AFFECT expression SEMICOLON')
        def program_production(p):
            return 0
        @self.pg.production('instr : aadad IDENTIFIER SEMICOLON')
        def program_production(p):
            return 0
        @self.pg.production('instr : ')
        def program_production(p):
            return 0
        
        @self.pg.production('instr : aadad IDENTIFIER AFFECT expression SEMICOLON')
        def program_production(p):
            return 0
        @self.pg.production('instr : string IDENTIFIER AFFECT expression SEMICOLON')
        def program_production(p):
            return 0
        @self.pg.production('instr : print LPAREN expression RPAREN SEMICOLON')
        def program_production(p):
            return 0
            
        @self.pg.production('expression : expression PLUS term')
        def expression_production_sum(p):
            return expression(p)

        @self.pg.production('expression : expression MINUS term')
        def expression_production_sub(p):
            return expression(p)
        @self.pg.production('expression : term')
        def term_production(p):
            return 0
        @self.pg.production('term : term MULT factor')
        def term_production(p):
            return 0
        @self.pg.production('term : term DIVIDE factor')
        def term_production(p):
            return 0
        @self.pg.production('term : factor')
        def term_production(p):
            return 0
        @self.pg.production('factor : NUMBER')
        def term_production(p):
            return 0
        @self.pg.production('factor : IDENTIFIER')
        def term_production(p):
            return 0
        @self.pg.production('factor : STRING')
        def term_production(p):
            return 0

        @self.pg.error
        def error_handler(token):
            raise ValueError(token)
