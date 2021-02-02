def Main(CommandsPath):
    CommandsList = {}
    
    Data = open(CommandsPath , 'r')
    for Line in Data:
        Line = Line.rstrip("\n")
        Striped = Line.split('=')
        Command = Striped[0]; Script = Striped[1].replace('"' , '')
        CommandsList[Command] = Script

    return CommandsList