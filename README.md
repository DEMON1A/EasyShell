# EasyShell
Cool Shell Written In Python3 Allows You To Write Your Own Commands And Execute It. That Includes It's Own Scripting Language.

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

# How To Write Your Own Easy Code?
- I'm Not Really Sure If Easy Code Is Easy. But You Can Decide. Easy Code Is Based On Python So Every Easy Code You're Writing Is Getting Genrated Into a Python Code. You Can See `examples` Folder Or Follow The Documentation Below.

### Variable Assignment And Usage:
- Let's Start With The Most Basic Thing Here. In Easy You Can Store Local Variables Using `DEFINE` Key, When The Parser Adds That Variable Into The Dicc. You Will Be Able To Call It From Anywhere Outside Of This Of Code Using `ADD` Key. See The Example Below For More Information

```
DEFINE githubHandler=<'"DEMON1A"'>

STORE handler
ADD githubHandler;NEWLINE
CALL print,handler
```

- After Translating The Code With EasyShell, The Output Code Will Be Something Like This:

```python
handler = "DEMON1A"
print(handler)
```

- I Usally Use This Method To Add a Pure Python Code Into My Easy Code To Work With It Until I Implement a Key For The Thing I Need In Python
- You Can Define Multi Variables On a Line Using `,` Between Everyone. For Example: `STORE test,something,hi`. You Can Use This For Functions That Returns More Than One Variable

### Defining a Function:
- You Can Define Your Own Function With `FUNCTION` Key On The Code. That Will Create a Python Function For You But You Will Need To Use `.` at The End Of Every Syntax You Code. The Dot at The End Of The Code Adds a TAB Into **The Next Line Of Code**. So When You Define a Function You Should Use `.` At The End Of It. See The Example Below

```

FUNCTION Main.
CALL print,"Hello^World!"

NEWLINE
CALL Main
```

- After Translating The Code It Will Be Something Like This:

```python
def Main():
    print("Hello World!")

Main()
```

### Import Python Modules.
- No Python Code Can Work Without Imports. To Import a Python Library You Need To Use `IMPORT` Key. For Example If You Used `IMPORT os,time` After Tranlating The Code It Will Be `import os,time` LOL.

### Call a Function And Store Python Variables
- To Call a Function In Easy, You Should Use `CALL` Key. That Allows You To Call a Python Function With Arguments By Sperating The Values With `,`. For Example: `CALL print,"Hello^World!"`

- To Store Python Variables You Can Use `STORE` Key. That Will Set The Variable Name. And The Next Line Of Code Will Be It's Value.

### TAB and NEWLINE:
- It's Just a Basic Keys On Easy To Add NewLines And Tabs On The Code. So When You Want To Add a NewLine On Your Code You Just Need To Add `NEWLINE` And When You're Coding On a Function And You Hate Using Dots. Then Use `TAB` Key. I Know It's Not Pretty To Have `NEWLINE` and `TAB` On a Single Line. So I Allowed Using `;` On The Code. So You Can Just Do Whatever Code You Want Then Add `;TAB` Or `;NEWLINE` To Add a NewLine/Tab at The End

## To-Do:
- [X] Adding Local Variable Assignment
- [X] Allowing Using `;` For Multi Code In One Line
- [X] Using Pure Strings On The Code With `ADD` Option
- [ ] Adding If Conditions Support
- [ ] Adding While Loops Support
- [ ] Adding For Loops Support
- [ ] Creating Some Useful Scripts For The Shell.
- [ ] Adding Folder Option Compile
- [ ] Creating an Errors Handler For The Parser.
- [ ] Perform Some Tests On a Linux Machine. Or Ask Someone To-Do So.

### Changelog:
- EasyShell Beta Version Released

## Notes:
- Easy Is Sensitive To Spaces More Than Python. I Did Build The Parser From Zero Using Split Methods And Other Things On The Code. One Wrong Space Can Make an Error On The Code And Your LineOfCode Won't Be Applied. It's Only One Space Between The Key And It's Value. So `CALL something` Is Right. But `CALL  something` Will Kill The Code. And That's The Same For `;` You Can't Include Spaces On It. `NEWLINE;CALL something` Is Right, But `NEWLINE; CALL something` Is Really Wrong.

- I Didn't Implement The Error Handler Yet *( it's on the to-do list )* So Invalid Code Won't Be Applied On The Translated Code. You Won't Get an Error. If You Can't See Your Code On The Translation Then Check Your Code Again Specially For Spaces.

## Somethng Isn't Working Or You Have Suggestions?
- Oh, I Would Love To Hear People Suggestions Specially For This Case. If You See That Something Isn't Working Or You Want To Improve Something. Then Please Open a Github Issue Or Fork The Repo Then Create a Pull Request. Also, You Can DM Me On Twitter: [DemoniaSlash](https://twitter.com/DemoniaSlash).
