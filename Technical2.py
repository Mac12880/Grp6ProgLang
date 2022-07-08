import re
import tkinter
from tkinter import *
from tkinter import filedialog
from turtle import clear

def getTxt():
    tkinter.Tk().withdraw()
    filepath = filedialog.askopenfilename(initialdir="N:\Schoolworks\Prog Languages\PL Final Proj",
                                          title="Select Text File",
                                          filetypes= (("text files","*.txt"), ("python files","*.py"),
                                          ("all files","*.*")))
    global file
    global fileName
    file = open(filepath,'r+')
    fileName = file.name
    
    if file == "":
        print("\n==No File Uploaded==")
    else:
        print("\n==File Uploaded==")

def keepTxt():
    global keptFile
    keptFile = ""
    fileNameList = []
    for char in fileName:
        fileNameList.append(char)

    for item in fileNameList:
        if item == "/":
            keptFile += "\\"
        else:
            keptFile += item

def reopenTxt():
    global file
    file = open(keptFile, 'r+')

def viewLexemes():
    tempString = ""
    prevTemp = ""
    nextLine = "\n"
    tempKey = []
    prevKey = ""
    temp = []
    strstatus = False #If true, then the next following characters are probably a whole string.
    quot = False #True - Double quotation. | False - Single quotation.
    prevValue = 0
    curValue = 0

    lexemeCount = 0
    totalLexemes = 0

    print("=== View Lexemes/Tokens ===")
    for word in file: #read per line
        comstatus = False
        for char in word: #read per character
            if strstatus == True and char != '"': #if an iteration of " is found this will not proceed
                temp.append(char)

            elif comstatus == True and char != word[-1]:
                temp.append(char)

            elif char == "\n": #proceed here if newline is encountered
                for item in temp: #list per character per word
                    tempString += item #combined characters to string
                temp.clear()

                if tempString == "": #so empty newlines dont get printed
                    pass
                elif char == word[-1] and comstatus == True:
                    print(tempString, "-> comment")
                    comstatus = False
                elif prevValue != curValue: #to check if an occurence of a string was observed
                    print(tempString, "-> string")
                    prevValue = curValue
                elif tempString in arithmetics or tempString in assignments or tempString in comparisons or tempString in logicals or tempString in identifiers or tempString in memberships or tempString in bitwise:
                    print(tempString, "-> operator")
                elif tempString in keyCharacters:
                    print(tempString, "-> key character")
                elif tempString in keywords:
                    print(tempString, "-> keyword")
                elif tempString in datatype:
                    print(tempString, "-> datatype")
                elif re.match("[0-9]+", tempString):
                    print(tempString, "-> integer")
                else:
                    print(tempString, "-> variable")
                tempString = ""
                lexemeCount += 1

            elif char != " ": #proceed here if not space and newline
                if char not in keyCharacters:
                    temp.append(char)
                    if char == "#" and comstatus == False:
                        comstatus = True
                    elif char == word[-1] and comstatus == True:
                        for item in temp:
                            tempString += item
                        temp.clear()
                        print(tempString, "-> comment")
                        tempString = ""
                        lexemeCount += 1
                        comstatus = False
                else: 
                    if char == '"' and strstatus == False: #used to manage strstatus and curValue
                        curValue = curValue + 1
                        strstatus = True
                    elif char == '"' and strstatus == True:
                        strstatus = False

                    if not temp: #Pag walang laman si temp, aappend niya yung keyCharacter sa tempKey list
                        tempString += char
                        print(tempString, "-> key character")
                        tempString = ""
                        lexemeCount += 1
                    else:
                        for item in temp:
                            tempString += item
                        temp.clear()
                        if tempString == "":
                            pass
                        elif prevValue != curValue:
                            print(tempString, "-> string")
                            prevValue = curValue   
                        elif tempString in arithmetics or tempString in assignments or tempString in comparisons or tempString in logicals or tempString in identifiers or tempString in memberships or tempString in bitwise:
                            print(tempString, "-> operator")
                        elif tempString in keyCharacters:
                            print(tempString, "-> key character")
                        elif tempString in keywords:
                            print(tempString, "-> keyword")
                        elif tempString in datatype:
                            print(tempString, "-> datatype")
                        elif re.match("[0-9]+", tempString):
                            print(tempString, "-> integer")
                        else:
                            print(tempString, "-> variable")
                        tempString = ""
                        tempKey.append(char)
                        lexemeCount += 1
                        for item in tempKey:
                            tempString += item
                        tempKey.clear()
                        print(tempString, "-> key character")
                        tempString = ""
                        lexemeCount += 1

            else: #proceed here if space
                for item in temp:
                    tempString += item
                temp.clear()
                if tempString == "":
                    pass
                elif prevValue != curValue:
                    print(tempString, "-> string")
                    prevValue = curValue
                elif tempString in arithmetics or tempString in assignments or tempString in comparisons or tempString in logicals or tempString in identifiers or tempString in memberships or tempString in bitwise:
                    print(tempString, "-> operator")
                elif tempString in keyCharacters:
                    print(tempString, "-> key character")
                elif tempString in keywords:
                    print(tempString, "-> keyword")
                elif tempString in datatype:
                    print(tempString, "-> datatype")
                elif re.match("[0-9]+", tempString):
                    print(tempString, "-> integer")
                else:
                    print(tempString, "-> variable")
                tempString = ""
                lexemeCount += 1
    print("Total Lexemes: ", lexemeCount)
    
def viewLexicalError():
    lineCount = 1
    print("=== View Lexical Error ===")
    for line in file:
        words = line.split()
        if words == [] or words[0] not in datatype:
            pass
        elif words[0] == "num":
            if len(words) < 3:
                pass
            elif (int(words[3]) > 2147483647 or int(words[3]) < -2147483648):
                print("== line ", lineCount, " ==")
                print("Limit of num reached -> Lexical Error")
            elif re.match("\A[^a-z]", words[1][0]): #Does not accept any special character EVEN underscore
                    print("== line ", lineCount, " ==")
                    print("Invalid variable declaration -> Lexical Error")
            else:
                pass
        elif words[0] in datatype:
            if re.match("\A[^a-z]", words[1][0]): #Does not accept any special character EVEN underscore
                    print("== line ", lineCount, " ==")
                    print("Invalid variable declaration -> Lexical Error")
            else:
                pass
        else:
            pass
        lineCount = lineCount + 1

def viewSyntaxError():
    operator = ""
    lineCount = 1
    print("=== View Syntax Error ===")
    for line in file:
        words = line.split()
        for i in words:
            if i == "==":
                operator = "=="
            elif i == "=":
                operator = "="
        if words == []:
            pass
        elif re.match("\A[^a-z]", words[0][0]): #Does not accept any special character EVEN underscore
            if words[1] == "=":
                if re.match("[a-z]", words[2][0]):
                    print("== line ", lineCount, " ==")
                    print("Inverted assigning of value -> Syntax Error")
        elif words[0] == "if" or words[0] == "ei" or words[0] == "while":
            if operator == "=":
                print("== line ", lineCount, " ==")
                print("Wrong use of = operator -> Syntax Error")
            else:
                pass

        elif words[0] != "if" or words[0] != "ei" or words[0] != "while":
            if operator == "==":
                print("== line ", lineCount, " ==")
                print("Wrong use of == operator -> Syntax Error")
            else:
                pass

        operator = ""
        lineCount = lineCount + 1

def viewSemanticError():
    print("=== View Semantic Error ===")
    varList = []
    lineCount = 1
    for line in file:
        words = line.split()
        if words == []:
            pass
        elif words[0] not in datatype or words[0] not in keywords:
            if len(words) < 2:
                pass
            elif words[1] == "=" and words[0] not in varList and re.match("[^0-9]", words[0]):
                print("== line ", lineCount, " ==")
                print("Assigning to undefined variable -> Semantic Error") 
            else:
                pass
        elif words[0] in datatype:
            if words[1] in varList:
                print("== line ", lineCount, " ==")
                print("Redefining Variable -> Semantic Error")
            else:
                varList.append(words[1])
        else:
            pass
        
        lineCount = lineCount + 1

def mainMenu():
        
    print("\n===== Main Menu =====")
    print("[1] Upload Text File")
    print("[2] View Lexemes/Tokens")
    print("[3] View Lexical Error")
    print("[4] View Syntax Error")
    print("[5] View Semantic Error")
    print("[6] Exit")
    print("Enter Choice: ", end='')

    ch = int(input())
    print("")

    #Upload Text File
    if ch == 1:
        
        print("=== Upload Text File ===")
        print("*Check for Select Text File Tab*")
        print("*Alt + Tab*")
        getTxt()

    #View Lexemes/Tokens
    elif ch == 2:
        viewLexemes()

    #View View Lexical Error
    elif ch == 3:
        viewLexicalError()

    #View View Syntax Error
    elif ch == 4:
        viewSyntaxError()

    elif ch == 5:
        viewSemanticError()

    #Exit
    elif ch == 6:
        print("=== Exiting ===")
        exit()

#MAIN CODE
tkinter.Tk().withdraw()
filepath = filedialog.askopenfilename(initialdir="N:\Schoolworks\Prog Languages\PL Final Proj",
                                        title="Select Text File",
                                        filetypes= (("text files","*.txt"), ("python files","*.py"),
                                        ("all files","*.*")))
global file
global fileName
file = open(filepath,'r+')
fileName = file.name

if file == "":
    print("\n==No File Uploaded==")
else:
    print("\n==File Uploaded==")
global keywords
global arithmetics
global assignments
global comparisons
global logicals
global identifiers
global memberships
global bitwise
global keyCharacters
global datatype
keywords = ["continue","finally","assert","lambda","return","global","except","import","class","break","raise","while","print","yield","pass","exec","else","with","elif","from","def","not","try","and","del","for","is","if","fire","reload","ei", "fixed"]
arithmetics = ["+", "-", "*", "/", "//"]
assignments = ["<<=", ">>=", "^=", "|=", "&=", "**=", "//=", "%=", "/=", "*=", "-=", "+=", "="]
comparisons = ["==", "!=", ">=", "<=", ">", "<"]
logicals = ["and", "or", "not"]
identifiers = ["is", "is not"]
memberships = ["in", "not in"]
bitwise = ["&", "|", "^", "~", "<<", ">>"]
keyCharacters = [".", ",", ":", ";", "'", '"', "{", "}", "[", "]", "(", ")"]
datatype = ["num", "dec", "let", "text", "cond"]
global keptFile

while True:
    keepTxt()
    reopenTxt()
    mainMenu()