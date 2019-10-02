"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This is a tokenizer for the Jack Language
class JackTokenizer:
    
    def JackTokenizer():
        #Open Files
        outputFile="MainT.xml"
        filename= "Main.jack"
        oFile= open(outputFile, 'w')
        file= open(filename, 'r')
        #define Tokens
        symbols = ['}', '{', ')', '(', ']', '[', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
        keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                    'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
         
        #Temporary testing space
        with open(filename) as f:
            for line in f:
                for word in line.split():
                    if word == '//':
                        line++
 
                    print(word)
    

    """          
    def hasMoreTokens():
        
    def advance():
        
    def tokenType():
        
    def keyWord():
        
    def symbol():
        
    def identifier():
        
    def intVal():

    def stringVal():

"""