import os, time

'''
import SyntaxGrabber
from ErrorHandler import classErrorHandler
'''

from assets import SyntaxGrabber
from assets.ErrorHandler import classErrorHandler
from assets.successHandler import classSuccessHandler
from assets.initParser import initParserClass

PureCode = {}
Count = 0
CurrentSyntax = ""
lineCount = 0
currentLineNumber = 0
filePath = ""
syntaxFound = False

class Parser:
    def __init__(self):
        pass

    def errorCaller(self , LineOfCode , charLength , Name , textMessage):
        global classErrorHandler , currentLineNumber, filePath

        functions = globals()['classErrorHandler']()
        errorMessage = getattr(functions , 'callErrorMessage')

        errorMessage(
            Code=LineOfCode,
            charLength=charLength,
            lineNumber=currentLineNumber,
            Path=filePath,
            Name=Name,
            textMessage=textMessage
        )

    def DotNewLine(self , Value):
        End = Value[-1:]
        if End == ".": Space = "    "; Value = Value[:-1]
        else: Space = ""

        return Space , Value

    def KeySpaceFilter(self , LineOfCode):
        LineOfCode = self.StartsSpaceDel(LineOfCode=LineOfCode)
        LineOfCode = self.EndsSpaceDel(LineOfCode=LineOfCode)

        return LineOfCode

    def StartsSpaceDel(self , LineOfCode):
        global CurrentSyntax

        CodeWithoutKey = LineOfCode.replace(CurrentSyntax , '' , 1)
        for Character in CodeWithoutKey:
            if Character == " ": CodeWithoutKey = CodeWithoutKey[1:]
            else: break

        return CodeWithoutKey

    def EndsSpaceDel(self , LineOfCode):
        global CurrentSyntax
        ReversedString = LineOfCode[::-1]

        for Character in ReversedString:
            if Character == " ": LineOfCode = LineOfCode[:-1]
            else: break

        return LineOfCode

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
        Function = self.KeySpaceFilter(LineOfCode=LineOfCode)
        Space , Function = self.DotNewLine(Value=Function)

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
        Function = self.KeySpaceFilter(LineOfCode=LineOfCode)
        Space , Function = self.DotNewLine(Value=Function)

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
        Var = self.KeySpaceFilter(LineOfCode=LineOfCode)
        _ , Var = self.DotNewLine(Value=Var)

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
        Value = self.KeySpaceFilter(LineOfCode=LineOfCode)
        Space , Value = self.DotNewLine(Value=Value)

        AddedCode = f"import {Value}\n{Space}"
        return AddedCode

    def VAR(self , LineOfCode):
        Function = self.KeySpaceFilter(LineOfCode=LineOfCode)
        Space , Function = self.DotNewLine(Value=Function)

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

        mainData = self.KeySpaceFilter(LineOfCode=LineOfCode)
        valueName = mainData.split('=')[0]; valueValue = mainData.split('=')[1]
        valueValue = self.BracketsRemove(vName=valueValue)

        valueValue = self.SpaceSet(valueValue)
        PureCode[valueName] = valueValue

        return ""

    def ADD(self , LineOfCode):
        global PureCode

        mainName = self.KeySpaceFilter(LineOfCode=LineOfCode)
        try:
            PythonCode = PureCode[mainName]
            PythonCode = self.NewLinesReplacer(PythonCode=PythonCode)

            return PythonCode
        except Exception:
            self.errorCaller(
                LineOfCode=LineOfCode,
                charLength=4,
                Name="Undefined Variable",
                textMessage="The Variable You're Trying To Add Isn't Defined."
            )

    def IF(self , LineOfCode):
        Condition = self.KeySpaceFilter(LineOfCode=LineOfCode)
        Space , Condition = self.DotNewLine(Value=Condition)

        if "," in Condition:
            Values = Condition.split(",")
            Values = self.SpaceSet(Values)

            if len(Values) < 3 or len(Values) > 3:
                self.errorCaller(
                    LineOfCode=LineOfCode,
                    charLength=len(Values) + 2,
                    Name="Max Arguments",
                    textMessage="You're Passing More Than Three Arguments Into The Condition."
                )
            else:
                firstValue = Values[0]
                secondValue = Values[1]
                thirdValue = Values[2]

            ConditionCode = f"if {firstValue} {secondValue} {thirdValue}:\n{Space}"
            AddedCode = ConditionCode
        else:
            AddedCode = f'if {Condition}:\n{Space}'

        return AddedCode

    def ELSE(self , LineOfCode):
        doAfter = self.KeySpaceFilter(LineOfCode=LineOfCode)
        Space , doAfter = self.DotNewLine(Value=doAfter)
        addedCode = "else:\n"

        if "," in doAfter:
            Values = doAfter.split(",")
            for doThing in Values:
                if doThing != '':
                    addedCode += f"    {doThing}\n{Space}"
        else:
            if doAfter != '':
                addedCode += f"    {doAfter}\n{Space}"

        return addedCode

    def TEST(self , LineOfCode):
        Code = self.KeySpaceFilter(LineOfCode=LineOfCode)
        print(f"Code: {Code}")

        return ""

    def INIT(self , LineOfCode):
        global CurrentSyntax

        initParserFunctions = globals()['initParserClass']()
        initParser = getattr(initParserFunctions , 'initParser')

        initVariables = initParser(CurrentSyntax=CurrentSyntax)
        for Key,Value in initVariables.items():
            PureCode[Key] = Value

        return ''

def Main(File, Mode , Output):
    global CurrentSyntax , currentLineNumber, filePath, syntaxFound

    errorHandler = globals()['classErrorHandler']()
    showErrorMessage = getattr(errorHandler , 'showErrorMessage')

    successHandler = globals()['classSuccessHandler']()
    showSuccessMessage = getattr(successHandler , 'showSuccessMessage')

    Content = open(File , 'r')
    Syntax = SyntaxGrabber.GrapSyntaxKeys()
    filePath = os.path.abspath(File)
    Comment = "#"
    Code = ""

    for CodeLine in Content:
        CodeLine = CodeLine.rstrip("\n")
        currentLineNumber += 1
        if ";" in CodeLine:
            if "<'" and "'>" in CodeLine: pass
            else: CodeLine = CodeLine.replace(';' , '\n')

        for SingleSyntax in Syntax:
            Limit = len(SingleSyntax)

            if '\n' not in CodeLine:
                if CodeLine.replace(' ' , '')[:Limit].upper() == SingleSyntax:
                    syntaxFound = True
                    CurrentSyntax = SingleSyntax
                    Call = globals()['Parser']()
                    Function = getattr(Call, SingleSyntax)
                    Code += Function(CodeLine)
                elif CodeLine.replace(' ' , '')[:1] == Comment:
                    syntaxFound = True
                else:
                    pass
            else:
                Codes = CodeLine.split('\n')
                for SomeCode in Codes:
                    if SomeCode.replace(' ' , '')[:Limit].upper() == SingleSyntax:
                        CurrentSyntax = SingleSyntax
                        syntaxFound = True
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

        try:
            exec(Code)
        except Exception as e:
            showErrorMessage(Message=f"[<[Python Error]>]: {str(e)}")
            return None

        endTime = time.process_time()
        realTime = endTime - startTime

        if int(realTime) < 1: print("Code Execution Done in Less Than 1 Second.")
        else: print(f"Code Execution Done in {int(realTime)} Second/s.")
    elif Mode.lower().replace(' ' , '') == "compile":
        CurrentPath = os.getcwd(); CurrentPath = CurrentPath.split('\\')
        FullPath = '/'.join(CurrentPath); FullPath += f"/compiled/{Output}"

        with open(FullPath , 'w') as OutputFile:
            OutputFile.write(Code); OutputFile.close()

        showSuccessMessage(Message=f"The Compiled Code Has Been Saved On: {FullPath}")
    else:
        showErrorMessage(Message=f"The Mode You Selected Doesn't Exists: {Mode}")
