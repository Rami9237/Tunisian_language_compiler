from lexer_tn import Lexer
from parser_tn import Parser

text_input = "code Bagra {aadad x=3;aadad y=5;aadad q=1;aadad z=8;aadad i = 0;karrer i men x ila y { ken(x!=z+y){ekteb(x+y*z/q);}}}"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
# for token in tokens:
#     print (token)
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)