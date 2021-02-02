from os import system , name

def Run(Input):
    if name == "nt":
        system('cls')
    else:
        system('clear')