from math import floor

# Functions

def thickBar(length):
    for i in range(length):
        print("=", end="")
    print()


def thinBar(length):
    for i in range(length):
        print("-", end="")
    print()


def cleanCoords(raw):
    output = ""  # Initialize the output to be returned

    # Add valid characters to the output String
    for i in range(len(raw)):  # iterate through the raw coords

        if raw[i] in list("1234567890- "):  # Determine if the current character is valid
            output += str(raw[i])  # Append valid characters to the output list

    if output == "":
        output = "0 0"

    output = list(filter(None, output.split(" ")))  # Create a list with the coordinates as Strings

    # Parse all list elements to integers
    for i in range(len(output)):
        output[i] = floor(int(output[i]))

    return output


def getNether(owc):
    output = owc

    for i in range(len(owc)):
        output[i] = floor(owc[i] / 8)

    return output


def getOverworld(nc):
    output = nc

    for i in range(len(nc)):
        output[i] = floor(nc[i] * 8)

    return output

def getCoords():
    global coords
    coords = ""
    print(enterCoordsMsg, end="")
    coords = cleanCoords(input())
    thinBar((len(enterCoordsMsg) + len(coords)))

# Strings

enterCoordsMsg = "Enter coords to convert: "

selectOption = "Select option: "

badOption = "That's not an option."

optionMenu = "1. Remove non numeric characters\n" \
             "2. Get Nether coords\n" \
             "3. Get Overworld coords\n" \
             "4. Generate Overworld goto\n" \
             "5. Generate Nether goto\n" \
             "6. Generate /tp\n" \
             "-----------------------\n" \
             "Select option: "

# Variables

choice = -1
coords = ""

# greet user

thickBar(57)
print("This program converts Minecraft coords for easier travel.")
thickBar(57)

# Main Loop

while True:
    choice = -1

    while choice not in list("123456"):
        print(optionMenu, end="")
        choice = input()
        thinBar(len(selectOption) + len(choice))
        if choice not in list("123456"):
            print(badOption)
            thinBar(len(badOption))

    if choice == "1":
        getCoords()
        nc = getNether(coords)
        if len(nc) == 2:
            output = "Nether Coords: " + str(nc[0]) + " " + str(nc[1])
        elif len(nc) == 3:
            output = "Nether Coords: " + str(nc[0]) + " " + str(nc[2])
        print(output)
        thinBar(len(output))

    if choice == "2":
        getCoords()
        nc = getNether(coords)
        if len(nc) == 2:
            output = "Nether Coords: " + str(nc[0]) + " " + str(nc[1])
        elif len(nc) == 3:
            output = "Nether Coords: " + str(nc[0]) + " " + str(nc[2])
        print(output)
        thinBar(len(output))

    if choice == "3":
        getCoords()
        owc = getOverworld(coords)
        if len(owc) == 2:
            output = "Overworld Coords: " + str(owc[0]) + " " + str(owc[1])
        elif len(owc) == 3:
            output = "Overworld Coords: " + str(owc[0]) + " " + str(owc[2])
        print(output)
        thinBar(len(output))

    if choice == "4":
        getCoords()
        if len(coords) == 2:
            output = ",goto " + str(coords[0]) + " " + str(coords[1])
        elif len(coords) == 3:
            output = ",goto " + str(coords[0]) + " " + str(coords[2])
        print(output)
        thinBar(len(output))

    if choice == "5":
        getCoords()
        nc = getNether(coords)
        if len(nc) == 2:
            output = ",goto " + str(nc[0]) + " " + str(nc[1])
        elif len(nc) == 3:
            output = ",goto " + str(coords[0]) + " " + str(coords[2])
        print(output)
        thinBar(len(output))

    if choice == "6":
        getCoords()
        if len(coords) == 2:
            output = "/tp @p " + str(coords[0]) + " ~ " + str(coords[1])
        elif len(coords) == 3:
            output = "/tp @p " + str(coords[0]) + " " + str(coords[1]) + " " + str(coords[2])
        print(output)
        thinBar(len(output))