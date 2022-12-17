import string
from re import sub

# declare variables
# int coords
owX = 0 # overworld x coord
owY = 0 # overworld y coord
owZ = 0 # overworld z coord
nX = 0 # nether x coord
nY = 0 # nether y coord
nZ = 0 # nether z coord

# str coords
owXStr = "" # overworld x coord
owYStr = "" # overworld y coord
owZStr = "" # overworld z coord
nXStr = "" # nether x coord
nYStr = "" # nether y coord
nZStr = "" # nether z coord
owCoords = "" # full overworld coords
nCoords = "" # full nether coords

# lists
rawCoordsList = ""

# misc
rawCoords = ""
dimension = "ow"
rawCoordsListLen = 0
bGoto = ".b goto "

# resets variables to defaults
def resetVariables():
    global owX
    global owY
    global owZ
    global nX
    global nY
    global nZ
    global owXStr
    global owYStr
    global owZStr
    global nXStr
    global nYStr
    global nZStr
    global owCoords
    global nCoords

    # str coords
    owXStr = "" # overworld x coord
    owYStr = "" # overworld y coord
    owZStr = "" # overworld z coord
    nXStr = "" # nether x coord
    nYStr = "" # nether y coord
    nZStr = "" # nether z coord
    owCoords = "" # full overworld coords
    nCoords = "" # full nether coords

    # int coords
    owX = 0 # overworld x coord
    owY = 0 # overworld y coord
    owZ = 0 # overworld z coord
    nX = 0 # nether x coord
    nY = 0 # nether y coord
    nZ = 0 # nether z coord

    # lists
    rawCoordsList = ""
    rawCoords = ""
    dimension = "ow"
    rawCoordsListLen = 0

# adds a large divider
def divide():
    print("==============================")

# adds a small divider
def split():
    print("------------------------------")

# gets coords from user
def getCoords():
    global rawCoords
    global dimension
    dimension = "ow"
    print("Enter coords:")
    rawCoords = input(str())
    if "nether" in rawCoords or "Nether" in rawCoords or "n" in rawCoords:
        dimension = "n"
    else:
        dimension = "ow"

# removes non numeric characters from inputted coords
def cleanString(inStr):
    # variables
    strList = ""
    whitelist =  string.digits + ".-"
    blacklist0 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJK"
    blacklist00 ="LMNOPQRSTUVWXYZ!\"#$%&'()*+,/:;<=>?@[\]^_`{|}"
    blacklist = blacklist0 + blacklist00

    # removes non numeric characters (except for spaces) and ".-"
    for character in blacklist:
        inStr = inStr.replace(character, "")

    # removes spaces leaving only 0-9 and .-
    # stores data as a list
    strList = inStr.split(" ")
    while "" in strList:
        strList.remove("")

    return strList

# checks to see if the user inputted coords (smashed keyboard)
def validateCoords(rawCoordsList):
    # make global variables
    global owX
    global owY
    global owZ
    global owXStr
    global owYStr
    global owZStr
    global rawCoordsListLen

    # store the length of the list of coords
    rawCoordsListLen = len(rawCoordsList)

    # produce error messages
    if rawCoordsListLen == 0:
        print("////////////////////")
        print("Invalid input: list empty")
        print("////////////////////")
        split()
    elif rawCoordsListLen == 1:
        print("Invalid input: list too short")
    elif rawCoordsListLen == 3:
        print("//////////////////////////////////////////////////////////")
        print("Invalid input: list too long, attempting conversion anyway")
        print("//////////////////////////////////////////////////////////")
        split()
    elif rawCoordsListLen > 3:
        print("////////////////////////////////////////////")
        print("Invalid input: list too long, cannot convert")
        print("////////////////////////////////////////////")
        split()

    # make ow coords as int
    if rawCoordsListLen == 2:
        owXStr = rawCoordsList[0]
        owZStr = rawCoordsList[1]
        owX = int(owXStr)
        owZ = int(owZStr)
    if rawCoordsListLen == 3:
        owXStr = rawCoordsList[0]
        owYStr = rawCoordsList[1]
        owZStr = rawCoordsList[2]
        owX = int(owXStr)
        owY = int(owYStr)
        owZ = int(owZStr)

# makes coords for the opposite dimension
def convertNether():
    global owX
    global owY
    global owZ
    global nX
    global nY
    global nZ
    global owXStr
    global owYStr
    global owZStr
    global nXStr
    global nYStr
    global nZStr
    global owCoords
    global nCoords

    if dimension == "ow":
        nX = int(owX / 8)
        nZ = int(owZ / 8)
        nXStr = str(nX)
        nZStr = str(nZ)
        owCoords = owXStr + " " + owZStr
        nCoords = nXStr + " " + nZStr
    elif dimension == "n":
        nX = owX
        nZ = owZ
        nXStr = str(nX)
        nZStr = str(nZ)
        owX = int(nX * 8)
        owZ = int(nZ * 8)
        owXStr = str(owX)
        owZStr = str(owZ)
        owCoords = owXStr + " " + owZStr
        nCoords = nXStr + " " + nZStr

# prints out the results
def printCoords():
    print("Overworld coords: " + owCoords)
    print(bGoto + owCoords)
    split()
    print("Nether coords: " + nCoords)
    print(bGoto + nCoords)

# adds a bar at the top
divide()

# the actual program
while True:
    # get user coords
    getCoords()
    split()
    # make a list of the raw coords
    rawCoordsList = cleanString(rawCoords)
    # validate coords for user input errors
    validateCoords(rawCoordsList)
    # make nether coords
    convertNether()
    # printCoords
    printCoords()
    resetVariables()
    divide()
