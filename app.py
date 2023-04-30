from flask import Flask,request
from lexer_tn import Lexer
from parser_tn import Parser
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def code_compiler(text_input):
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    return parser.parse(tokens)
   


@app.route('/read_input',methods=['POST'])
def read_input():
    data = request.json 
    print(data.get)
    language_input = data.get('code') # Get the value of the 'code' property from the JSON object
    if language_input:
        result = code_compiler(language_input)
        return result
    else:
        return 'Please enter the code you want to convert.'
@app.route('/read_code',methods=['POST'])
def read_code():
    data = request.json 
    print(data.get)
    language_input = data.get('code') # Get the value of the 'code' property from the JSON object
    if language_input:
        code_py,result = code_compiler(language_input)
        return code_py
    else:
        return 'Please enter the code you want to convert.'
if __name__ == '__main__':
    app.run()

