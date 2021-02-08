import sys , os
from colorama import init
from termcolor import colored
init()

class classErrorHandler:
    def __init__(self):
        pass

    def callErrorMessage(self , Code , charLength , lineNumber , Path , Name , textMessage):
        Message = f"{Name} Exception:"
        Message += f"\n\tPath: {Path}"
        Message += f"\n\t{Code} - Line: {str(lineNumber)}"
        Pointer = " " * int(charLength)
        Message += f"\n\t{Pointer}{str('^')}"
        Message += f"\n\t{textMessage}"
        print(colored(Message , 'red'))


'''
if __name__ == '__main__':
    init()

    Call = globals()['ErrorHandler']()
    Function = getattr(Call, 'CallErrorMessage')

    Function(
        Code="TEST file.com",
        charLength=0,
        lineNumber=4,
        Path="D:/Projects/EasyShell/dev.easy",
        Name="UndefinedVariable",
        textMessage="The Variable You Used Doesn't Exists"
    )
'''