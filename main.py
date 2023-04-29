from lexer_tn import Lexer
from parser_tn import Parser
text_input = "code Bagra {aadad x1=1;aadad x=-3;jomla y1=\"test\";jomla y2=\"test\";jomla y3=\"Hello\";jomla y=y1;aadad z=8;aadad q=-2;aadad i = 0;karrer i men x ila x1 { ken(x1==1){ekteb(y1 + y3);}}}"
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
# for token in tokens:
#     print (token)
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)
