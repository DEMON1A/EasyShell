from os import system

def Run(Input):
    while (1):
        Input = input("root@Shell: ")
        if Input == "exit":
            exit()
        else:
            system(Input)