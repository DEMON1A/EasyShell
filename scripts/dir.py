from os import system , name

def Run(Input):
    if name == "nt":
        # Windows Machine
        system('dir')
    else:
        # Linux/Unix Machine
        system('ls')