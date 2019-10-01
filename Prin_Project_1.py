"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This program is a parse tree for .JACK files
main()

def ParseTree(categories, symbols):
    #Start XML 
    outputFile.write("<token> \n")
    for i in file:
        for j in symbols:
            if file[i] == symbols[j]:
                parseSymbol(file[i])
            
                
            
            
    outputFile.write("</token> \n")
    
    
    
    def parseSymbol(symbol):
        
        
    
def main():
    #define Tokens
    symbols = ['}', '{', ')', '(', ']', '[', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                  'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
    #Open File(s)
    outputFile= "MainT.xml"
    filename= "example.JACK"
    oFile= open(outputFile, 'a')
    file= open(filename, 'r')
    
    #Parse it up!
    ParseTree(categories, symbols)


        
