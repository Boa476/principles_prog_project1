"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This is a tokenizer for the Jack Language

   
def JackTokenizer():
    #Open Files
    outputFile="MainT.xml"
    filename= "Main.JACK"
    oFile= open(outputFile, 'w')
    file= open(filename, 'r')
    file.read()
    #define Tokens
    symbols = ['}', '{', ')', '(', ']', '[', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                  'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']

def hasMoreTokens():
    
def advance():
    
def tokenType():

def keyWord():

def symbol():
    
def identifier():
    
def intVal():

def stringVal():
    