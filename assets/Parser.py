import os, time

PureCode = {}
Count = 0

class Parser:
    def __init__(self):
        pass

    def NewLinesReplacer(self , PythonCode):
        return PythonCode.replace('\\n' , '\n')

    def BracketsRemove(self , vName):
        return vName.replace("<'" , '').replace("'>" , '')

    def DotCheck(self , name):
        return name.replace('-' , '.')

    def SpaceSet(self , Values):
        global Count
        
        if type(Values) == list:
            for Argument in Values:
                if "^" in Argument:
                    NewArgument = Argument.replace('^' , ' ')
                    Values[Count] = NewArgument
                Count += 1

            Count = 0
            return Values
        else:
            return Values.replace('^' , ' ')

    def FUNCTION(self , LineOfCode):
        Function = LineOfCode.split(' ')[1].replace(' ' , '')
        End = Function[-1:]

        if End == ".": Space = "    "; Function = Function[:-1]
        else: Space = ""

        if "," in Function:
            Values = Function.split(',')
            functionName = Values[0]
            del Values[0]

            for Arg in Values:
                if len(Values) == 1:
                    AddedCode = f"def {functionName}({Arg}):\n{Space}"
                else:
                    Arguments = ', '.join(Values)
                    AddedCode = f"def {functionName}({Arguments}):\n{Space}"
        else:
            AddedCode = f"def {Function}():\n{Space}"

        return AddedCode

    def CALL(self , LineOfCode):
        Function = LineOfCode.split(' ')[1].replace(' ' , '')
        End = Function[-1:]

        if End == ".": Space = "    "; Function = Function[:-1]
        else: Space = ""

        if "," in Function:
            Values = Function.split(",")
            functionName = Values[0]
            del Values[0]

            Values = self.SpaceSet(Values)
            functionName = self.DotCheck(functionName)

            for Arg in Values:
                if len(Values) == 1:
                    AddedCode = f"{functionName}({Arg})\n{Space}"
                else:
                    Arguments = ', '.join(Values)
                    AddedCode = f"{functionName}({Arguments})\n{Space}"
        else:
            AddedCode = f"{Function}()\n{Space}"

        return AddedCode


    def STORE(self , LineOfCode):
        Var = LineOfCode.split(' ')[1].replace(' ' , '')

        if "," in Var:
            Values = Var.split(",")

            if len(Values) == 1:
                AddedCode = f"{Var} = "
            else:
                Vars = ', '.join(Values)
                AddedCode = f"{Vars} = "
        else:
            AddedCode = f"{Var} = "

        return AddedCode

    def NEWLINE(self , LineOfCode):
        return '\n'

    def IMPORT(self , LineOfCode):
        Value = LineOfCode.split(' ')[1].replace(' ' , '')
        End = Value[-1:]

        if End == ".": Space = "    "; Value = Value[:-1]
        else: Space = ""

        Value = Value.replace('^' , ' ')

        AddedCode = f"import {Value}\n{Space}"
        return AddedCode

    def VAR(self , LineOfCode):
        Function = LineOfCode.split(' ')[1].replace(' ' , '')
        End = Function[-1:]

        if End == ".": Space = "    "; Function = Function[:-1]
        else: Space = ""

        if "," in Function:
            Values = Function.split(",")
            Values = self.SpaceSet(Values)
            
            for VarsStuff in Values:
                lastValue = VarsStuff

            Values.remove(lastValue)
            Arguments = ', '.join(Values)
            AddedCode = f"{Arguments} = {lastValue}\n{Space}"
        else:
            varValue = Function
            AddedCode = f'{varValue} = ""\n{Space}'

        return AddedCode

    def TAB(self , LineOfCode):
        return "    "

    def DEFINE(self , LineOfCode):
        global PureCode

        mainData = LineOfCode.split(' ')[1].replace(' ' , '')
        valueName = mainData.split('=')[0]; valueValue = mainData.split('=')[1]
        valueValue = self.BracketsRemove(vName=valueValue)

        valueValue = self.SpaceSet(valueValue)
        PureCode[valueName] = valueValue

        return ""

    def ADD(self , LineOfCode):
        global PureCode

        mainName = LineOfCode.split(' ')[1].replace(' ' , '')
        try:
            PythonCode = PureCode[mainName]
            PythonCode = self.NewLinesReplacer(PythonCode=PythonCode)

            return PythonCode
        except Exception:
            return "" # Creating error module for this. Errors.py. return is constant

def Main(File, Mode , Output):
    Content = open(File , 'r')
    Syntax = ['IMPORT' , 'FUNCTION' , 'CALL' , 'STORE' , 'VAR' , 'DEFINE' , 'ADD' , 'NEWLINE' , 'TAB']
    Comment = "#"
    Code = ""

    for CodeLine in Content:
        CodeLine = CodeLine.rstrip("\n")
        if ";" in CodeLine:
            if "<'" and "'>" in CodeLine: pass
            else: CodeLine = CodeLine.replace(';' , '\n')
        for SingleSyntax in Syntax:
            Limit = len(SingleSyntax)

            if '\n' not in CodeLine:
                if CodeLine[:Limit].upper() == SingleSyntax:
                    Call = globals()['Parser']()
                    Function = getattr(Call, SingleSyntax)
                    Code += Function(CodeLine)
                elif CodeLine.replace(' ' , '')[:1] == Comment:
                    pass
                else:
                    pass
            else:
                Codes = CodeLine.split('\n')
                for SomeCode in Codes:
                    if SomeCode[:Limit].upper() == SingleSyntax:
                        Call = globals()['Parser']()
                        Function = getattr(Call, SingleSyntax)
                        Code += Function(SomeCode)
                    elif SomeCode.replace(' ' , '')[:1] == Comment:
                        pass
                    else:
                        pass

    if Mode.lower().replace(' ' , '') == "show":
        print(Code)
    elif Mode.lower().replace(' ' , '') == "exec" or Mode.lower().replace(' ' , '') == "execute":
        startTime = time.process_time()
        exec(Code)
        endTime = time.process_time()
        print(f"Code Execution Done in {endTime - startTime} Seconds.")
    elif Mode.lower().replace(' ' , '') == "compile":
        CurrentPath = os.getcwd(); CurrentPath = CurrentPath.split('\\')
        FullPath = '/'.join(CurrentPath)
        FullPath += f"/compiled/{Output}"
        
        with open(FullPath , 'w') as OutputFile:
            OutputFile.write(Code)
            OutputFile.close()

        print(f"The Compiled Code Has Been Saved On: {FullPath}")
    else:
        print(f"The Mode You Selected Doesn't Exists: {Mode}\nModes: show, exec, execute, compile")
