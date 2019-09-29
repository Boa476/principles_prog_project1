"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This program is a parse tree for .JACK files
main()

def ParseTree(categories):
    #Start XML 
    outputFile.write("<token> \n")
    for char in file:
        
    outputFile.write("</token> \n")
        
    
def main():
    #define Tokens
    categories = ['()[]{},;=.+=*/&|~<>', 'class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                  'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this', \
                 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '_']
    #Open File(s)
    outputFile= "MainT.xml"
    filename= "example.JACK"
    oFile= open(outputFile, 'a')
    file= open(filename, 'r')
    
    #Parse it up!
    ParseTree(categories)


        
