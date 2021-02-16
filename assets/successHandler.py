from colorama import init
from termcolor import colored
init()

class classSuccessHandler:
    def __init__(self):
        pass

    def showSuccessMessage(self , Message):
        Message = colored(f"Operation is done:\n    {Message}" , 'green' , attrs=['bold'])
        print(Message)
