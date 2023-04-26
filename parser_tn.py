from rply import ParserGenerator
from ast_tn import Divide, Number, Sum, Sub, Print,Tabulations


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
             'FOR',
             'while',
             'aadad',
             'string',
             'LPAREN',
             'RPAREN',
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
        self.arr = []
        self.counter = 0
        self.instructions = []

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
        def exists(arr,val):
            for elm in arr:
                if (val == elm):
                    return True
            return False
        @self.pg.production('program : CODE IDENTIFIER L_CB instr R_CB')
        def program_production(p):
            print(self.instructions)
            if (len(self.arr) != 0):
                    c = ','.join(self.arr) 
                    raise ValueError('Les variables suivantes doivent être déclarées :',c)
            else:
                c = 0
                code = ""
                tabs = ""
                while (len(self.instructions) != 0 ):
                    x = self.instructions.pop()
                    code = code + tabs + x + "\n"
                    li = list(x.split(" "))
                    if (li[0] == "for" or li[0] == "if"):
                        tabs = tabs + " \t "
                exec(code)

        @self.pg.production('instr : FOR IDENTIFIER FROM factor TO factor L_CB instr R_CB')
        def program_production(p):
                print("IDENTIFIER is", p[1].value)
                e = exists(self.arr,p[1].value)
                if (e == False):
                    self.arr.append(p[1].value)
                e = exists(self.arr,p[3].value)
                if (e == False and p[3].gettokentype() == 'IDENTIFIER'):
                    self.arr.append(p[3].value)
                e = exists(self.arr,p[5].value)
                if (e == False and p[5].gettokentype() == 'IDENTIFIER'):
                    self.arr.append(p[5].value)
                self.instructions.append("for " + p[1].value + " in range("+p[3].value+","+p[5].value+"):")

        @self.pg.production('instr : if LPAREN expression COMPARE expression RPAREN L_CB instr R_CB')
        def program_production(p):
            print(p[2])
            if (p[2].gettokentype() == 'IDENTIFIER'):
                c = p[2].value
            else:
                c = p[2] 
            print(p[4])
            self.instructions.append("if (" + c + "==" + p[4] + "):")
        @self.pg.production('instr : if LPAREN expression DIFFERENT expression RPAREN L_CB instr R_CB')
        def program_production(p):
            if (p[2].gettokentype() == 'IDENTIFIER'):
                c = p[2].value
            else:
                c = p[2] 
            print(p[4])
            self.instructions.append("if (" + c + "!=" + p[4] + "):")
        @self.pg.production('instr : IDENTIFIER AFFECT expression SEMICOLON instr')
        def program_production(p):
            self.instructions.append(p[0].value + "=" + p[2])
        @self.pg.production('instr : aadad IDENTIFIER SEMICOLON instr')
        def program_production(p):
            self.arr.remove(p[1].value)
            self.instructions.append(p[1].value + "= None")
        @self.pg.production('instr : ')
        def program_production(p):
            return None
        @self.pg.production('instr : aadad IDENTIFIER AFFECT expression SEMICOLON instr')
        def program_production(p):
            self.instructions.append(p[1].value + "=" + p[3].value)

            self.arr.remove(p[1].value)
        @self.pg.production('instr : string IDENTIFIER AFFECT expression SEMICOLON instr')
        def program_production(p):
            self.instructions.append(p[1].value + "=" + p[3])
            self.arr.pop(p[1].value)
        @self.pg.production('instr : print LPAREN expression RPAREN SEMICOLON instr')
        def program_production(p):
            if(isinstance(p[2],str)):
                self.instructions.append("print("+p[2]+")")
            else:
                self.instructions.append("print("+p[2].value+")")
        @self.pg.production('expression : expression PLUS term')
        def expression_production_sum(p):
            if (isinstance(p[0],str)):
                return p[0] + '+' + p[2].value
            elif (isinstance(p[0],str) and (isinstance(p[2],str))):
                return p[0] + '+' + p[2]
            elif (isinstance(p[2],str)):
                return p[0].value + '+' + p[2]
            else:
                return p[0].value + '+' + p[2].value
        @self.pg.production('expression : expression MINUS term')
        def expression_production_sub(p):
            if (isinstance(p[0],str)):
                return p[0] + '-' + p[2].value
            elif (isinstance(p[0],str) and (isinstance(p[2],str))):
                return p[0] + '-' + p[2]
            elif (isinstance(p[2],str)):
                return p[0].value + '-' + p[2]
            else:
                return p[0].value + '-' + p[2].value
        @self.pg.production('expression : term')
        def term_production(p):
            return p[0]
        @self.pg.production('term : term MULT factor')
        def term_production(p):
            if (isinstance(p[0],str)):
                return p[0] + '*' + p[2].value
            elif (isinstance(p[0],str) and (isinstance(p[2],str))):
                return p[0] + '*' + p[2]
            elif (isinstance(p[2],str)):
                return p[0].value + '*' + p[2]
            else:
                return p[0].value + '*' + p[2].value
        @self.pg.production('term : term DIVIDE factor')
        def term_production(p):
            if (isinstance(p[0],str)):
                return p[0] + '/' + p[2].value
            elif (isinstance(p[0],str) and (isinstance(p[2],str))):
                return p[0] + '/' + p[2]
            elif (isinstance(p[2],str)):
                return p[0].value + '/' + p[2]
            else:
                return p[0].value + '/' + p[2].value
        @self.pg.production('term : factor')
        def term_production(p):
            return p[0]
        @self.pg.production('factor : NUMBER')
        def term_production(p):
            return p[0]
        @self.pg.production('factor : IDENTIFIER')
        def term_production(p):
            e = exists(self.arr,p[0].value)
            if (e == False):
                self.arr.append(p[0].value)
            return p[0]
        @self.pg.production('factor : STRING')
        def term_production(p):
            return p[0]
        @self.pg.error
        def error_handler(token):
            raise ValueError(token)
