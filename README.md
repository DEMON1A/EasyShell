# EasyShell
- Cool Shell Written In Python3 Allows You To Write Your Own Commands And Execute It. That Includes It's Own Scripting Language.
- See The Wiki On The Github Repo For More Information About The Usage.

## Usage:
- If You Run EasyShell Without Arguments. It Will Just Open You The Shell That Will Take Your Inputs. Otherwise If You Want To Translate Or Execute Your Easy Code You Will Have To Use One Of These Examples Below

- Modes: `show, exec, execute, compile`

```
python3 shell.py --file /path/to/your/easy/code.easy --mode show # That Will Show You The Code
python3 shell.py --file /path/to/your/easy/code.easy --mode exec # That Will Execute Your Easy Code
python3 shell.py --file /path/to/your/easy/code.easy --mode compile --output code.py # That Will Translate Your Easy Code To Python Code And Put The File On compiled Folder.
```

## What The Hell Is EasyShell?
- EasyShell Is a Simple Project I Created That Allows You To Make Your Own Shell Where You Control The Commands And Code You're Executing. And It's Not Just That. EasyShell Comes With It's Own Scripting Language. That Allows You To Write *Easy* Code Then Translate It To Python Code. Then Do Whatever You Want With It. Most Of The Scripting Languages

## How To Add a New Command Into The Shell?
- It's Kinda Easy, You Have Two Folders. `scripts` And `data`. Adding Command Isn't That Hard. You Just Need To Write Your Own Code On `scripts` Folder That's Using `Run()` as a Main Function With `Input` as The Only Input It Takes. In Case You Want To Pass a User Controlled Input Into The Shell The User Should Pass It Next To The Command With `-` Sepacting Them. See The Examples Below For More Information:

- Before Using The Command You Have To Update The Commands Data On `data` Folder, Open The File `Commands.easy` Then You Should Add This Content On a Separated Line

```
command="script-without-dot-py"
```

### Examples:
##### Script Example:
```python
# filenme = "sample.py"

def Run(Input):
    print("Cool, Your Input is: {0}".format(Input))
```

##### Data Example:
```
testcommand="sample"
```

##### Shell Example:
```
testcommand - someinputhere
```

##### Output:
```
Cool, Your Input is: someinputhere
```

## To-Do:
- [X] Adding Local Variable Assignment
- [X] Allowing Using `;` For Multi Code In One Line
- [X] Using Pure Strings On The Code With `ADD` Option
- [X] Adding If Conditions Support
- [X] Adding Else Support
- [ ] Adding While Loops Support
- [ ] Adding For Loops Support
- [X] Making Easy Less Sensitive To Spaces
- [X] Appending __INIT__ Support
- [ ] Creating Some Useful Scripts For The Shell.
- [ ] Adding Folder Option Compile
- [X] Creating an Errors Handler For The Parser.
- [ ] Creating Some Cool And Easy ShortCuts. To Make Easy Really Easy.
- [ ] Creating a PIP Package For It.
- [ ] Creating a VSCode Language Support For It.
- [X] Perform Some Tests On a Linux Machine. Or Ask Someone To-Do So.

### Changelog [Year/Month/Day] :
- [2021/2/2] EasyShell beta version released 0.0.1
- [2021/2/8] EasyShell beta version updated with more features 0.0.2
- [2021/2/16] EasyShell is still on beta but updated. but for now it's ready for production 0.0.3
- [2021/2/18] New EasyShell Version With Play Music Support Via Shell Using `playmusic` Command 0.0.4

## Notes:
- Easy is Ready For Real Usage Now, You Can Use Multi Spaces And Even Use Spaces Before The Syntax. And You Don't Need To Use `^` Instead Of Space. The Space Split Funcions Has Been Replacted With Characters Loop That Removes Spaces at The First And The End Of The File.

## Something Isn't Working Or You Have Suggestions?
- Oh, I Would Love To Hear People Suggestions Specially For This Case. If You See That Something Isn't Working Or You Want To Improve Something. Then Please Open a Github Issue Or Fork The Repo Then Create a Pull Request. Also, You Can DM Me On Twitter: [DemoniaSlash](https://twitter.com/DemoniaSlash).
