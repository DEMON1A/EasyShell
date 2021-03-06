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
        print(colored(Message , 'red' , attrs=['bold']))

    def shellCommandsErrorHandler(self):
        pass

    def showErrorMessage(self , Message):
        Message = colored(f"Error Detected:\n    {Message}" , 'red' , attrs=['bold'])
        print(Message)
