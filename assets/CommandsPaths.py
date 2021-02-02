from os import getcwd , name

def Main():
    CurrentPath = getcwd()

    if name == "nt":
        Path = CurrentPath + r"\\data\\Commands.easy"
    else:
        Path = CurrentPath + "/data/Commands.easy"

    return Path