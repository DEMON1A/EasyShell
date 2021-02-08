from os import getcwd

def GrapSyntaxKeys():
    Syntaxes = []
    CurrentPath = getcwd()
    DataPath = "/data/Syntax.easy"

    FullPath = CurrentPath + DataPath
    SyntaxKeys = open(FullPath , 'r')

    for Key in SyntaxKeys:
        Key = Key.rstrip('\n')
        Syntaxes.append(Key)

    return Syntaxes