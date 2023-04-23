from lexer_tn import Lexer
from parser_tn import Parser

text_input = "ekteb(6-4);"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()