from lexer_tn import Lexer
from parser_tn import Parser

text_input = "code Bagra {aadad i = 0; karrer i men 1 ila 5 {}}"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)