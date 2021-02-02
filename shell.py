import optparse , concurrent.futures
from assets import CommandsParser , ScriptsRunner , CommandsPaths , Parser
from os import path

def Shell(Options):
    Path = CommandsPaths.Main()
    Commands = CommandsParser.Main(Path)
    
    while (1):
        Input = input("root@Command: ")

        try:
            if "-" in Input:
                Command = Input.split('-')[0].replace(' ' , '')
                Arguments = Input.split('-')[1].replace(' ' , '')

                Script = Commands[Command]
                ScriptsRunner.Main(Script=Script , Input=Arguments)
            else:
                Script = Commands[Input]
                ScriptsRunner.Main(Script=Script , Input="")
        except Exception as e:
            if "No module named" in str(e):
                print("Command Has Found But The Script Doesn't Exists.")
            else:
                print("Can't Reconize This Command: '{0}'".format(Input))
                print(str(e))

def OptionsCollector():
    Parser = optparse.OptionParser()
    Parser.add_option("-f" , "--file" , dest="file" , help="The File You Want To Tranlate.")
    Parser.add_option("-m" , "--mode" , dest="mode" , help="The Compalier Mode.")
    Parser.add_option("-o" , "--output" , dest="output" , help="The Compiled Output File")
    Parser.add_option("--folder" , dest="folder" , help="Compile a Hall Folder That Contains Easy Code.")

    Options,_ = Parser.parse_args()
    return Options

def Validator(File , Mode , Output):
    if File:
        if Mode: pass
        else: print("You Didn't Pick Up a Mode.\nModes: show, exec, execute, compile"); exit()

        if not Output: Output = File.replace('.easy' , '.py')
        else: pass

        if path.exists(Options.file): Parser.Main(File=File , Mode=Mode , Output=Output); exit()
        else: print(f"The File You Selected Doesn't Exists: {Options.file}"); exit()
    else: pass

def Main(Options):
    Validator(Options.file , Options.mode , Options.output)

    try:
        Shell(Options=Options)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as Collector:
        Options = Collector.submit(OptionsCollector)
        Options = Options.result()

    with concurrent.futures.ThreadPoolExecutor() as Threader:
        _ = Threader.submit(Main , Options)