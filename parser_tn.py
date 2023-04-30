from rply import ParserGenerator
from ast_tn import Divide, Number, Sum, Sub, Print,Token,Instruction
import re
import io,sys

class Parser():
    def __init__(self,code):
        self.code = code
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['print',
             'if',
             'DIVIDE',
             'PLUS',
             'MINUS',
             'MULT',
             'FOR',
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
            ],
            
        )   
        self.declarations = []
        self.instructions = []
        self.denom = []
        self.vartypes = {}
        self.operations = []
    def get_parser(self):

        return self.pg.build()
    def checkTypes(self,types,operators):
        if (types.count(types[0]) == len(types)):
            if types[0] == 'STRING':
                if (len(operators) == 0 or (operators.count(operators[0]) == len(operators) and operators[0]=='+')):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False    
    def indent_code(self,code):
            indentcount=0
            begin_index = 0
            output = ""
            for i in range(0,len(code)):
                if code[i] == ";":
                    output = output + ('\t'*indentcount) + code[begin_index:i].strip() +"\n"
                    begin_index = i+1
                if code[i] == "{":
                    output = output + ('\t'*indentcount) + code[begin_index:i].strip() +":\n"
                    indentcount+=1
                    begin_index = i+1
                if code[i] == "}":
                    output = output +"\n"
                    indentcount = indentcount - 1
                    begin_index = i + 1
            return output    
    def checkDiv(self,instructions,denom):
        for instruction in reversed(instructions):
            if (instruction.itype == 'decl'):
                exec(instruction.value)      
        for item in denom:
            if (eval(item) == 0):
                err = "'Dividing By 0 is not allowed'"
                return None,None,err
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
            if (len(self.declarations) != 0):
                c = ','.join(self.declarations)
                err = 'These variables are undeclared : '+ c
                return "","",err
            else:
                patternType = r'"[^"]*"|[a-zA-Z_]\w*|\d+'
                patternOperation = r'[-+*/]'
                while (self.operations != []):
                    x = self.operations.pop()
                    patternType = r'"[^"]*"|[a-zA-Z_]\w*|\d+'
                    matchesType = re.findall(patternType, x)
                    matchesOperation = re.findall(patternOperation,x)
                    print(matchesType)
                    for k in range(0,len(matchesType)):
                        if (matchesType[k][0] == "\""):
                            matchesType.pop(k)
                    print(matchesType)
                    if (len(matchesType) > 0):
                        for i in range(0,len(matchesType)):
                            matchesType[i] = self.vartypes[matchesType[i]]
                        check = self.checkTypes(matchesType,matchesOperation)
                        if (not(check)):
                            err = "TypeMismatch for expression " + x
                            return "","",err
                self.checkDiv(self.instructions,self.denom)
                s2 = "{"
                self.code = self.code.replace('aadad','')
                self.code = self.code.replace('jomla','')
                self.code = self.code.replace('ken','if')
                self.code = self.code.replace('karrer','for')
                self.code = self.code.replace('men','in range(')
                self.code = self.code.replace('ila',',')
                self.code = self.code.replace('ekteb','print')
                print(self.code)
                self.code = self.code[self.code.index(s2) + len(s2) :]
                match = True
                while(match):
                    match = re.search(r"range\(\s*\w*\s*,\s*\w*\s*[\{]", self.code)
                    if match:
                        index = match.end()
                        self.code = self.code[:index-1] + ')' + self.code[index-1:] 
                        print (self.code)
                output = io.StringIO()
                sys.stdout = output
                indented_code = self.indent_code(self.code)
                exec(indented_code)
                result = output.getvalue()

                return indented_code,result,""
                
        @self.pg.production('instr : FOR IDENTIFIER FROM factor TO factor L_CB instr R_CB instr_ext')
        def program_production(p):
                expCombine = p[1].value + '+' + p[3].value + '+' + p[5].value
                pattern = r'_?[a-zA-Z]+[0-9a-zA-Z]*'
                matches = re.findall(pattern,expCombine) # expression1 identifiers
                variables = set(matches)
                for variable in variables:
                    if(not(exists(self.declarations,variable))):
                        self.declarations.insert(0,variable)
                self.instructions.append(Instruction("for " + p[1].value + " in range("+p[3].value+","+p[5].value+"):","ref"))
        @self.pg.production('instr : if LPAREN expression COMPARE expression RPAREN L_CB instr R_CB instr_ext')
        def program_production(p):
            self.operations.append(p[2].value)
            self.operations.append(p[4].value)
            expCombine = p[2].value + '+' + p[4].value
            pattern = r'_?[a-zA-Z]+[0-9a-zA-Z]*'
            matches = re.findall(pattern,expCombine) # expression1 identifiers
            variables = set(matches)
            for variable in variables:
                if(not(exists(self.declarations,variable))):
                    self.declarations.insert(0,variable)
            self.instructions.append(Instruction("if (" + p[2].value + "==" + p[4].value + "):","ref"))
        @self.pg.production('instr : if LPAREN expression DIFFERENT expression RPAREN L_CB instr R_CB instr_ext')
        def program_production(p):
            self.operations.append(p[2])
            self.operations.append(p[4])
            expCombine = p[2].value + '+' + p[4].value
            pattern = r'_?[a-zA-Z]+[0-9a-zA-Z]*'
            matches = re.findall(pattern,expCombine) # expression1 identifiers
            variables = set(matches)
            for variable in variables:
                if(not(exists(self.declarations,variable))):
                    self.declarations.insert(0,variable)
            self.instructions.append(Instruction("if (" + p[2].value + "!=" + p[4].value + "):","ref"))
        @self.pg.production('instr : if LPAREN STRINGS COMPARE STRINGS RPAREN L_CB instr R_CB instr_ext')
        def program_production(p):
            self.instructions.append(Instruction("if (" + p[2].value + "==" + p[4].value + "):","ref"))
        @self.pg.production('instr : if LPAREN STRINGS DIFFERENT STRINGS RPAREN L_CB instr R_CB instr_ext')
        def program_production(p):
            self.instructions.append(Instruction("if (" + p[2].value + "!=" + p[4].value + "):","ref"))
        @self.pg.production('instr : IDENTIFIER AFFECT expression SEMICOLON instr')
        def program_production(p):
            exp = p[2].value
            self.operations.append(p[2].value)
            pattern = r'_?[a-zA-Z]+[0-9a-zA-Z]*'
            matches = re.findall(pattern,exp) # expression1 identifiers
            variables = set(matches)
            for variable in variables:
                if(not(exists(self.declarations,variable))):
                    self.declarations.insert(0,variable)
            if(not(exists(self.declarations,p[0].value))):
                self.declarations.insert(0,p[0].value)
            self.instructions.append(Instruction(p[0].value + "=" + p[2].value,"decl"))
        @self.pg.production('instr : aadad IDENTIFIER SEMICOLON instr')
        def program_production(p):
            self.vartypes[p[1].value] = 'INTEGER'
            if(exists(self.declarations,p[1].value)):
                self.declarations.remove(p[1].value)
            self.instructions.append(Instruction(p[1].value + "= 0","decl"))
        @self.pg.production('instr : ')
        def program_production(p):
            return None
        @self.pg.production('instr : aadad IDENTIFIER AFFECT expression SEMICOLON instr')
        def program_production(p):
            exp = p[3].value
            self.operations.append(p[3].value)
            self.vartypes[p[1].value] = 'INTEGER'
            pattern = r'_?[a-zA-Z]+[0-9a-zA-Z]*'
            matches = re.findall(pattern,exp) # expression1 identifiers
            variables = set(matches)
            for variable in variables:
                if (not(exists(self.declarations,variable))):
                    self.declarations.insert(0,variable)
            if(exists(self.declarations,p[1].value)):
                self.declarations.remove(p[1].value)        
            self.instructions.append(Instruction(p[1].value + "=" + p[3].value,"decl")) 
        @self.pg.production('instr : string IDENTIFIER AFFECT expression1 SEMICOLON instr')
        def program_production(p):
            exp = p[3].value
            self.operations.append(p[3].value)
            self.vartypes[p[1].value] = 'STRING'
            variables = list(exp.split("+"));
            for variable in variables:
                if (variable[0] == '\"'):
                    variables.remove(variable)
            for variable in variables:
                if (not(exists(self.declarations,variable))):
                    self.declarations.insert(0,variable)
            if(exists(self.declarations,p[1].value)):
                self.declarations.remove(p[1].value)   
            self.instructions.append(Instruction(p[1].value + "=" + p[3].value,"decl"))
        @self.pg.production('expression1 : expression1 PLUS str')
        def expression_production_sum(p):
            return Token(p[0].value + '+' + p[2].value)
        @self.pg.production('expression1 : str')
        def expression_production_sum(p):
            return Token(p[0].value)
        @self.pg.production('str : STRING')
        def expression_production_sum(p):
            self.vartypes[p[0].value] = 'STRING'
            return Token(p[0].value)
        @self.pg.production('str : IDENTIFIER')
        def expression_production_sum(p):
            return Token(p[0].value)
        @self.pg.production('instr : print LPAREN expression RPAREN SEMICOLON instr')
        def program_production(p):
            self.operations.append(p[2].value)
            self.instructions.append(Instruction("print("+p[2].value+")","ref"))
            return None
        @self.pg.production('expression : expression PLUS term')
        def expression_production_sum(p):
            return Token(p[0].value + '+' + p[2].value)
        @self.pg.production('expression : expression MINUS term')
        def expression_production_sub(p):
            return Token(p[0].value + '-' + p[2].value)
        @self.pg.production('expression : term')
        def term_production(p):
            return Token(p[0].value)
        @self.pg.production('term : term MULT factor')
        def term_production(p):
            return Token(p[0].value + '*' + p[2].value)
        @self.pg.production('term : term DIVIDE factor')
        def term_production(p):
                self.denom.append(p[2].value)
                return Token(p[0].value + '/' + p[2].value)
        @self.pg.production('term : factor')
        def term_production(p):
            return Token(p[0].value)
        @self.pg.production('factor : NUMBER')
        def term_production(p):
            self.vartypes[p[0].value] = 'INTEGER'
            return Token(p[0].value)
        @self.pg.production('factor : IDENTIFIER')
        def term_production(p):
            return Token(p[0].value)
        @self.pg.production('factor : MINUS factor' )
        def term_production(p):
            return  Token(p[0].value + p[1].value)
        @self.pg.production('factor : LPAREN expression RPAREN')
        def term_production(p):
            return Token('(' + p[1].value + ')')
        @self.pg.production('instr : print LPAREN STRINGS RPAREN SEMICOLON instr')
        def program_production(p):
            self.operations.append(p[2].value)
            self.instructions.append(Instruction("print("+p[2].value+")","ref"))
            return None
        @self.pg.production('STRINGS : STRING PLUS STRINGS')
        def program_production(p):
            return Token(p[0].value + "+" + p[2].value)
        @self.pg.production('STRINGS : STRING')
        def program_production(p):
            return Token(p[0].value)
        @self.pg.production('instr_ext : instr')
        def program_production(p):
            return None
        @self.pg.error
        def error_handler(token):
            raise ValueError("Erreur : token "+token.getstr() + " à la ligne " + str(token.source_pos.lineno)+ " col "+str(token.source_pos.colno))