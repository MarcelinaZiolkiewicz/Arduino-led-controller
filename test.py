import serial.tools.list_ports
import serial
import time
import os

red = '' 
green = ''
blue = ''
rgbValue = ''

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = 'colors.txt'


def getPorts():
    comPorts = serial.tools.list_ports.comports()
    return comPorts

def findArdu(portsFound):

    commPort = 'None'
    numConnection = len(portsFound)

    for i in range(0, numConnection):
        port = foundPorts[i]
        strPort = str(port)

        if 'Arduino' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])

    return commPort

foundPorts = getPorts()
connectPort = findArdu(foundPorts)

if connectPort != 'None':
    ser = serial.Serial (connectPort, baudrate = 9600, timeout=1)
    print("Connected to: " + connectPort)
    time.sleep(2)
    print("Ready")
    
else:
    print("Connection error!")


def dataRequest(): 
    arduinoData = ser.readline()
    decode('ascii')
    print(arduinoData)

def sendColor(colorValue): 

    colorInBytes = str.encode(colorValue)
    ser.write(colorInBytes)
    print(f'\nSend: {colorValue}') 


def findInFile(colorToFind):
    print("Searching...")
    #ścieżka jako zmienna i będzie można wysłać na który pasek led wysłać jakie kolory
    with open(dir_path + '/' + filePath) as f:
        txtFile = f.readlines()

    for line in txtFile:
        
        lineTab = line.split(".")
        rgbValue = line.split("_")

        if colorToFind in lineTab:
            print("Color found ", end="")
            sendColor(rgbValue[1])
            return True

    return False
    print("Color does not exist")


def loadColors():

    f = open(dir_path + '/' + filePath, "r")

    count = len(open(dir_path + '/' + filePath, "r").readlines())
    print(f'\nColors found: {count} \n')


    for line in f:

        underTab = line.split("_")
        dotTab = underTab[0].split(".")
        print(dotTab[0] + "." + dotTab[1][0].capitalize() + dotTab[1][1:len(dotTab[1])])

    f.close()

    colorToSet = input("\nChose color to set: ")
    findInFile(colorToSet)

def setNewColor(numToSet):
    
    colSet = input("Do You want to set this color?\ny/n: ")
    
    if colSet == 'y':
        findInFile(str(numToSet))
        print("Color added and set up")
    elif colSet == 'n':
        print("Color added")
    else:
        print("Incorrect value")

def writeToFile(lineToAdd):
    with open(dir_path + '/' + 'colorsStrip.txt', "a") as f:
        f.write(lineToAdd)

def addZero(toEdit):    #autocompleating when the value don't have 3 chars
    if len(toEdit) == 1: 
        toEdit = "00" + toEdit
        return toEdit
    elif len(toEdit) == 2:
        toEdit = "0" + toEdit
        return toEdit
    elif len(toEdit) == 0:
        toEdit = "000" + toEdit
        return toEdit
    else:
        return toEdit

def addNewColor():
    count = len(open(dir_path + '/' + 'colors.txt', "r").readlines())+1
    #print("-!- Write '#info' for more info -!-")

    name = input("\nAdd color name: ")

    if name == "#info":
        print("\n -!- NOTE -!-")
        print("You can add color value in rgb or hex")
        print("- HEX -\n When you add color by hex use '#' at first position")
        print("Example value in hex: #00FA9A \nIn RGB this color looks like: r0 g250 b154")

    else:
        valOpt = input("\n1)RGB\n2)HEX\nChose color value type:")

        if valOpt == "1":
            print("-- Add RGB value --")

            red = input("Red: ")
            red = addZero(red)

            green = input("Green: ")
            green = addZero(green)

            blue = input("Blue: ")
            blue = addZero(blue)

            print()

            writable = str(count) + "." + name + "_" + str(red) + str(green) + str(blue) + "\n"
            writeToFile(writable)

            setNewColor(count)


        elif valOpt == "2":
            print("-- Add HEX value --")
            hexVal = input("Color: ") #trzeba z dekodować hex na rgb

            if hexVal[0] == '#':
                if len(hexVal)-1 == 6:
                    
                    redH = str(int(hexVal[1:3],16))
                    redH = addZero(redH)

                    greenH = str(int(hexVal[3:5],16))
                    greenH = addZero(greenH)

                    blueH = str(int(hexVal[5:7],16))
                    blueH = addZero(blueH)

                    writable = str(count) + "." + name + "_" + redH + greenH + blueH + "\n"
                    writeToFile(writable)

                    setNewColor(count)
                    
                else:
                    print("Value incorrect")
            else:
                print("Add #")


        else:
            print("Incorrect value")

def showAllColors():
    pass

def loadLastColor():
    pass

def ledType():
    pass

def menu():
    while 1:
        print("-- MENU --")
        print("1) Show color list")
        print("2) Add color to list") 
        # print("x) Load last color")
        # print("x) Show available color effects")
        # print("x) Manage section ")
        # print("x) Options")
        print("9) Turn off color ")

        wyb = int(input("Chose option: "))

        if wyb == 1:
            print("Reading colors list...")
            loadColors()
        
        elif wyb == 2:
            addNewColor()

        elif wyb == 9:
            sendColor("000000000")
            print("Turning off")

        else:
            print('Incorrect value')

menu() 