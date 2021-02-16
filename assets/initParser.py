from os import path

'''
from Parser import Parser
from ErrorHandler import classErrorHandler
'''

'''
from assets.Parser import Parser
'''


from assets.ErrorHandler import classErrorHandler

'''
__INIT__ has been created for defining global variables only
it can't be used to write your own easy code into it

you can use it to store global static variables and use it from your easy code
to call __INIT__ from your easy code you can use `INIT` key on your code

any variables has been defined before with `DEFINE` key then defined again with __INIT__
will be overritten in some cases.

the error messages are getting handled using the pre-made error handler on the assets.
the error handler gonna be used for all functions.
'''

class initParserClass:
    def __init__(self):
        self.initPaths = ["__INIT__.easy" , "__INIT__"]
        self.initExist = False
        self.initFile = ""
        self.initCode = {}

    def StartsSpaceDel(self , LineOfCode):
        CurrentSyntax = self.CurrentSyntax

        CodeWithoutKey = LineOfCode.replace(CurrentSyntax , '' , 1)
        for Character in CodeWithoutKey:
            if Character == " ": CodeWithoutKey = CodeWithoutKey[1:]
            else: break

        return CodeWithoutKey

    def EndsSpaceDel(self , LineOfCode):
        CurrentSyntax = self.CurrentSyntax
        ReversedString = LineOfCode[::-1]

        for Character in ReversedString:
            if Character == " ": LineOfCode = LineOfCode[:-1]
            else: break

        return LineOfCode

    def externalSpaceFilter(self , codeList):
        errorHandler = globals()['classErrorHandler']()
        showErrorMessage = getattr(errorHandler , 'showErrorMessage')

        if len(codeList) != 2:
            showErrorMessage(Message="You're using multiple values on a single variable. only one `=` is allowed.")
            exit()
        else:
            # Start parsing the __INIT__ variables
            firstItem = self.StartsSpaceDel(LineOfCode=codeList[0])
            firstItem = self.EndsSpaceDel(LineOfCode=firstItem)

            secondItem = self.StartsSpaceDel(LineOfCode=codeList[1])
            secondItem = self.EndsSpaceDel(LineOfCode=secondItem)

        return firstItem , secondItem

    def initValidator(self):
        global classErrorHandler

        for singlePath in self.initPaths:
            if path.exists(singlePath):
                if not self.initExist:
                    self.initExist = True
                    self.initFile = singlePath
                else:
                    functions = globals()['classErrorHandler']()
                    errorMessage = getattr(functions , 'showErrorMessage')
                    errorMessage(Message="Multiple __INIT__ Files Has Been Detected. Only One __INIT__ is Allowed")
                    return False

        self.initExist = False
        return True

    def initParser(self , CurrentSyntax):
        self.CurrentSyntax = CurrentSyntax
        if self.initValidator():
            initContent = open(self.initFile , 'r')

            for singleLine in initContent:
                singleLine = singleLine.rstrip('\n')
                codeList = singleLine.split('=')
                Key , Value = self.externalSpaceFilter(codeList=codeList)
                self.initCode[Key] = Value

            return self.initCode
        else:
            exit()

'''
if __name__ == '__main__':
    functions = globals()['initParserClass']()
    initParser = getattr(functions , 'initParser')
    initParser()
'''
