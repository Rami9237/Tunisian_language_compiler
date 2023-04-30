input = '''karrer i men 1 ila 5 {
 ekteb ("tir rawah");
 ken (x == 3){
  ekteb ("tir zamer");
}
}'''

indentcount=0
begin_index = 0
output = ""
for i in range(0,len(input)):
    if input[i] == ";":
        output = output + ('\t'*indentcount) + input[begin_index:i].strip() +"\n"
        begin_index = i+1
    if input[i] == "{":
        output = output + ('\t'*indentcount) + input[begin_index:i].strip() +":\n"
        indentcount+=1
        begin_index = i+1
    if input[i] == "}":
        output = output +"\n"
        indentcount = indentcount - 1
        begin_index = i+1

print(output)