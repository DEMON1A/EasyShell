import playsound
from os import path , listdir
from random import choice
from assets.ErrorHandler import classErrorHandler

# globals
musicPath = "music/"
musicCounter = 0

def Run(userInput):
    global musicPath , musicCounter

    try:
        errorHandlerFunctions = globals()['classErrorHandler']()
        showErrorMessage = getattr(errorHandlerFunctions , 'showErrorMessage')

        if userInput == '' or userInput == None:
            showErrorMessage(Message="You didn't add the music file path.")
        else:
            if userInput == "random":
                songsList = listdir(musicPath)

                while (1):
                    randomSong = choice(songsList)
                    musicCounter += 1

                    playsound.playsound(f"{musicPath}{randomSong}")

                    if musicCounter == len(songsList): return None
            elif userInput == "playlist":
                songsList = listdir(musicPath)

                for singleSong in songsList:
                    playsound.playsound(singleSong)

                return None
            else:
                if path.exists(userInput):
                    playsound.playsound(userInput)
                else:
                    showErrorMessage(Message="The path you added doesn't exists.")
    except Exception as e:
        showErrorMessage(Message=f"[<[Sound Error]>]: {str(e)}")
