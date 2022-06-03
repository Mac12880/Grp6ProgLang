file = open("D:/School Files/3rd3rd/ProgrammingLanguages/Technical1/Grp6ProgLang/text.txt", "r")

keywords = ["if", "else", "while", ""]
whitespace = [" ", "\n"]
identifier = ["int", "float", "double", "string", "boolean"]
operators = ["+", "-", "*", "/", "%", "=", "<", ">"]
separators = ["{", "}", "[", "]"]

while 1:
    
    char = file.read(1)
    
    if not char:
        break
    
    
    print(char)

file.close