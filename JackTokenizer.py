"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This is a tokenizer for the Jack Language
class JackTokenizer:
    
    def __init__(self, filename):
        #Open File and fix it for tokenizing
        filename= filename + ".jack"
        rawList= self.__openFile__(filename)
        self.toTokenize = self.__arrangeFile__(rawList)
        self.Tokens = self.__compileTokens__(self.toTokenize)
        
        
        #outputFile =  + "T.xml"
        #self.oFile= open(self.outputFile, 'w')
        #define Tokens-- Tokens are checked in this order for a particular reason, particularly the ';' being at the end of array
        self.keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                    'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
        #self.string= self.file.readlines()
        #self.tokens = []
        #self.index = 0
        #comment = False
        #self.sym = False
        
####### Loading and preparing files  ########
        
    def __openFile__ (self, filename):
        """ Opens a file and places it into a list """
        fileList = []
        file = open(filename, 'r')
        for line in file:
            fileList.append(line)    
        file.close()
        return fileList
    
    def __arrangeFile__(self, unchangedList):
        """Removes Comments, blanks, and whitespace from the list"""
        finishedList=[]
        
        for line in unchangedList:
            #remove blank spaces on sides
            line = line.strip()
            
            #remove comments
            line = self.__removeLineComments__(line)
            if line == '':
                continue
            line = self.__removeBlockComments__(line)
            if line == '':
                continue
                
            ##separate symbols from words/strings
            line = self.__addSpaces__(line)
                
            if len(line) > 0:
                finishedList.append(line)
    
        return finishedList
    
    def __removeBlockComments__(self, line):  
        output = ''
        #finds start of comment
        if line[0] == "/" and line[1]== "*":
            if len(line) > 3:
                #finds the end of the comment
                for i in range(3, len(line)):
                    if line[i] == "*" and line[i + 1] == "/":
                        output += (line[i+2:])
            return output
        #removes lines from comment
        elif line[0] == "*":
            return output
        #no comment found
        else:
            output = line
            return output
    
    def __removeLineComments__(self, line):
        i = line.find('//')
        if i >0:
            line = line[0:i]
        elif i == 0:
            line = ''
        return line
    
    def __addSpaces__(self, line):
        symbols = [ '.', ',', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~',\
                   '{', '(', '[', ']', ')', '}', ';']
        #selects symbol to check for
        for i in symbols:
            searched = False
            j = line.find(i)
            if j < 0:
                searched = True
            else:
                # Insert space before and after symbol
                temp = list(line)
                temp.insert(j+1, " ")
                temp.insert(j, " ")
                line = ''.join(temp)
            while searched == False:
                j = line.find(i, j + 2) #finds index of symbol in line
                if j < 0:
                    break
                else:
                    temp = list(line)
                    temp.insert(j+1, " ")
                    temp.insert(j, " ")
                    line = ''.join(temp)
        return line
    
    def __compileTokens__(self, toTokenize):
        tokens = []
        switch = False
        for line in toTokenize:
            j = line.find('"')
            if j > 0:
                k = line.find('"', j + 1)
                temp = line[j+1:k]
            for word in line.split():
                if switch == False and '"' not in word:
                    tokens.append(word)
                if '"' in word and switch == True:
                    switch = False
                    continue
                if '"' in word:
                    tokens.append(temp)
                    switch = True
                    continue
        return tokens
                    
        
        """
        #Preparing Tokens
        with open(self.filename) as f:
            for line in f:
                lineArr = line.split()
                index = 0
                ### 'word' is the same as 'i'
                for word in lineArr: #.split() by default separates string pieces by white space
                    ### Check for comment status and ignore lines if True
                    if comment == True:
                        if '*/' not in line:
                            break
                        if '*/' in line:
                            comment = False
                            break
                    #More Comment Checking   
                    elif '//' in word:
                        self.sym = True
                        break
                    #More Comment Checking
                    elif '/*' in word:
                        comment = True
                        if '*/' not in line:
                            self.sym = True
                            break
                    if comment == False:
                        #Checks for Symbols in the file and attmepts to separate them from other words. i.e. call.function()
                        for i in self.symbols:
                            self.sym = False
                            if i == word:
                                self.sym = True
                                self.Tokens.append(word)
                                break
                            if i in word:
                                ### Attempt to separate chains. See example above
                                elem = word.split(i, 1)
                                self.Tokens.append(elem[0]) #adds token to array
                                self.Tokens.append(i) #adds symbol to array
                                word = elem[1] #replaces word with remainder of word
                                if word == '':
                                    self.sym = True
                                    break
                    if '"' in word:
                        qInd= index
                        qInd + 1
                        while lineArr[qInd] != '"':
                            word = word + ' ' + lineArr[qInd]
                        qInd + 1
                        word = word + lineArr[qInd]
                        self.Tokens.append(word)
                        self.sym = True
                            
                    #if all else fails, it's a token :)
                    if self.sym == False:                        
                        self.Tokens.append(word)
                    index + 1
        """
    

"""
    def hasMoreTokens(self, i):
        if '}' in self.string[i, len(self.string)]:
            return True
        else:
            return False                                 
    
    def advance(self, line):
        index = i
        if '/' in self.line[index] and self.line[index+1] == '/':
           return None
        if '/' in self.line[index]:
            if self.line[index+1] == '*':
                    if self.words[index+1] == '/':
                        index + 1
                    else:
                        i + 1
        i + 1
        
        return token

    def tokenType(self, token):
    
          
        
        
    def keyWord(self, token):
        
    def symbol(self, token):
        
    def identifier(self, token):
        
    def intVal(self, token):

    def stringVal(self, token):

"""
    


a = JackTokenizer('Main')
print(a.toTokenize)
print(a.Tokens)