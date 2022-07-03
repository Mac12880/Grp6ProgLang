import re
import tkinter
from tkinter import *
from tkinter import filedialog
from turtle import clear
#header

def getTxt():
    tkinter.Tk().withdraw()
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Select Text File",
                                          filetypes= (("text files","*.txt"), ("python files","*.py"),
                                          ("all files","*.*")))
    global file
    file = open(filepath,'r')
    
    if file == "":
        print("\n==No File Uploaded==")
    else:
        print("\n==File Uploaded==")
    
def viewLexemes():
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
        for char in word: #read per character
            if strstatus == True and char != '"': #if an iteration of " is found this will not proceed
                temp.append(char)

            elif char == "\n": #proceed here if newline is encountered
                for item in temp: #list per character per word
                    tempString += item #combined characters to string
                temp.clear()
                if tempString == "": #so empty newlines dont get printed
                    continue
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
                            continue
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
                    continue
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
    

def mainMenu():
    print("\n===== Main Menu =====")
    print("[1] Upload Text File")
    print("[2] View Lexemes/Tokens")
    print("[3] View Lexical Error(Not Done)")
    print("[4] View Syntax Error(Not Done)")
    print("[5] View Semantic Error(Not Done)")
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

    #Exit
    elif ch == 6:
        print("=== Exiting ===")
        exit()

while True:
    mainMenu()
