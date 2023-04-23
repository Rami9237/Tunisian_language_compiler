from lexer_tn import Lexer
from parser_tn import Parser

text_input = """
5+4
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
for token in tokens:
    print(token)
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()