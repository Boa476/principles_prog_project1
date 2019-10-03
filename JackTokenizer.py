"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This is a tokenizer for the Jack Language
class JackTokenizer:
    
    def __init__(self, filename):
        #Open Files
        self.outputFile = filename + "T.xml"
        self.filename= filename + ".jack"
        self.oFile= open(self.outputFile, 'w')
        self.file= open(self.filename, 'r')
        #define Tokens
        self.symbols = [ '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '{', '(', '[', ']', ')', '}']
        self.keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                    'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
        self.Tokens =[]
        
        #Preparing Tokens
        comment = False
        with open(self.filename) as f:
            for line in f:
                for word in line.split():
                    if comment == True:
                        if '*/' not in line:
                            break
                        if '*/' in line:
                            comment = False
                            break
                    if '//' in word:
                        break
                    if '/*' in word:
                        comment = True
                        if '*/' not in line:
                            break
                    if comment == False:
                        done = False
                        while(done == False):
                            for i in self.symbols:
                                if i in word:
                                    elem = word.split(i, 1)
                                    self.Tokens.append(elem[0])
                                    self.Tokens.append(i)
                                    word = elem[1]
                                    if elem[1] == '':
                                        done = True
                            self.Tokens.append(word)
        
    

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
a =JackTokenizer('Main')
for i in a.Tokens:
    print(a.Tokens[i])
