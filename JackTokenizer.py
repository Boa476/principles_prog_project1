"""PRINCIPLES OF PROGRAMMING LANGUAGES PROJECT 1"""
#This is a tokenizer for the Jack Language
class JackTokenizer:
    
    def __init__(self, filename):
        self.root = filename
        self.keywords = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', \
                    'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']                         
        self.symbols = [ '.', ',', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~',\
                   '{', '(', '[', ']', ')', '}', ';']
        self.ctr= 0
        filename= filename + ".jack"
        self.rawList= self.__openFile__(filename) #file prep
        self.toTokenize = self.__arrangeFile__(self.rawList)#file prep
        self.tokens = self.__compileTokens__(self.toTokenize)#file prep done!
        
######### class methods ###########        
    def hasMoreTokens(self):
        """ Checks to see if the current token is the last one in the array"""
        if self.ctr + 1 >= len(self.tokens):
            return False
        else:
            return True
        
    def advance(self):
        """self.ctr += 1"""
        self.ctr += 1
    
    def tokenType(self):
        """ Determines type of given token"""
        if self.tokens[self.ctr] in self.symbols:
            return 'symbol'
        elif self.tokens[self.ctr].isdigit():
            return 'integerConstant'
        elif self.tokens[self.ctr] in self.keywords:
            return 'keyword'
        elif self.tokens[self.ctr] not in self.keywords:
            for line in self.rawList:
                if line.find('"' + self.tokens[self.ctr] + '"') > 0:
                    return 'stringConstant'
            return 'identifier'
        
    def getToken(self):
        """returns the current token"""
        return self.token[self.ctr]   
        
####### Loading and preparing files  ########
        
    def __openFile__ (self, filename):
        """ Opens a file and places it into a list """
        fileList = []
        #open. the. file.
        file = open(filename, 'r')
        for line in file: #inserts all lines into a list
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
        """ Removes single line block comment """
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
        """Removes single line comments"""
        i = line.find('//') #find comment 
        if i >0:
            line = line[0:i]
        elif i == 0:
            line = ''
        return line
    
    def __addSpaces__(self, line):
        """ Adds a space before and after all symbols in the string"""
        #selects symbol to check for
        for i in self.symbols:
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
        """Formats all tokens into a single array"""
        tokens = []
        switch = False
        for line in toTokenize:
            j = line.find('"')#if line has a string literal
            if j > 0:
                k = line.find('"', j + 1)#find end of literal
                temp = line[j+1:k]
            for word in line.split():
                #ignore string literals and append tokens
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
#### End Class JackTokenizer ####
        
    
def main():
    name = input('Enter the name of the Jack file to be tokenized (omit ".jack" ext): ')
    
    a = JackTokenizer(name)
    check = True
    output = []
    #create output file and initialize it
    outputFile = a.root + "T.xml"
    file = open(outputFile, 'w')
    output.append('<tokens>\n')
    
    while check == True:
        ## insert Token into .xml
        if a.ctr == 0: #condition for first Token
            tType = a.tokenType()
            output.append('<' + tType + '> ' + a.tokens[a.ctr] + ' </' + tType + '>\n')
            a.advance()
            print(a.tokens[a.ctr])
        else: #all other "not first" Tokens
            tType = a.tokenType()
            output.append('<' + tType + '> ' + a.tokens[a.ctr] + ' </' + tType + '>\n')
            if a.hasMoreTokens():
                a.advance()
                print(a.tokens[a.ctr])
            else:
                check = False
        
    output.append('</tokens>')
    for i in output:
        file.write(i)
    file.close()

main()                    