from tkinter import *
from tkinter import font
import os
import test


userName = "Hello!"
darkMode = True #do poprawy
dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = 'colorsStrip.txt'

wdth = 250
bttBcg = '#686de0'
actvBtt = '#4834d4'
bcgColor = '#c8d6e5'

conStat = test.conStat #connection status message

root = Tk()

#FONTS
Arial = font.Font(family="Arial Rounded MT", size=22, weight='bold')
sArial = font.Font(family="Arial Rounded MT", size=20, weight='bold')
smallArial = font.Font(family="Arial Rounded MT", size=16)


def loadColors(event):
    clearFrame()

    f = open(dir_path + '/' + filePath, "r", encoding="utf-8")

    count = len(open(dir_path + '/' + filePath, "r").readlines())
    val = "Colors found: " + str(count)


    for line in f:

        underTab = line.split("_")
        dotTab = underTab[0].split(".")
        col = dotTab[0] + "." + dotTab[1][0].capitalize() + dotTab[1][1:len(dotTab[1])]
        
        listBx.insert(int(dotTab[0]), col)
        print(col)


    f.close()

    #colorToSet = input("\nChose color to set: ")
    listBx.place(x=10, y=30, width=300, height=495, anchor='nw')
    

    colorsQuantity = Label(rightFrame,text=val, bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
    colorsQuantity.place(x=10, y=0, width=300, height=30, anchor='nw')
    print("Done")
    
def onClosing(event): #not working
    print("Kill leds")
    root.destroy()

def getIndex(event):
    value = listBx.get(listBx.curselection())
    dotTab = value.split(".")   
    colorToSet = dotTab[0]
    test.findInFile(colorToSet)

    comm = "Color set: " + dotTab[1]

    colSetLab = Label(rightFrame, text=comm, bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
    colSetLab.place(x=10, y=530, width=300, height=30, anchor='nw')

def lastColor(event):
    test.loadLastColor()

def Off(event):
    test.sendColor("000000000")

def clearFrame():
    list = rightFrame.place_slaves()
    for l in list:
        l.place_forget()

def getInptValue(event):
    count = len(open(dir_path + '/' + filePath, "r").readlines())+1

    addRed.delete(3,END)
    addGreen.delete(3,END)
    addBlue.delete(3,END)

    red = addRed.get()
    green = addGreen.get()
    blue = addBlue.get()
    hext = addHex.get() 
    name = addName.get()

    red = test.addZero(red)
    green = test.addZero(green)
    blue = test.addZero(blue)

    rgb = red+green+blue


    #check is digit and show info 
    if not red.isdigit() or int(red) > 255:
        err.place_forget()
        print('Incorrect - red')
        err.place(x=410, y=50, width=40, height=40, anchor='nw')
        rgbCorrect = False

    elif not green.isdigit() or int(green) > 255:
        err.place_forget()
        print('Incorrect - green')
        err.place(x=410, y=120, width=40, height=40, anchor='nw')
        rgbCorrect = False

    elif not blue.isdigit() or int(blue) > 255:
        err.place_forget()
        print('Incorrect - blue')
        err.place(x=410, y=190, width=40, height=40, anchor='nw')
        rgbCorrect = False

    else:
        err.place_forget()
        print("Value correct")
        rgbCorrect = True


    if len(hext) == 7 and len(name) > 0:
        print(f'HEX value ok {hext}')

    elif len(rgb) == 9 and rgb != "000000000" and rgbCorrect and len(name) > 0:
        print(f'RGB value ok: {rgb}')
        writable = str(count) + "." + name + "_" + rgb
        test.writeToFile(writable)
        #set new color checkbox
        print("Send: " + writable)

    else:
        print(f'Wrong value: rgb-{len(rgb)}; hex-{len(hext)}; RGB digit: {rgb.isdigit()}; Name len: {len(name)}')    





def addNewColor(event): #printing widgets
    clearFrame()

    colPre = 'white'

    colorPreview = Canvas(rightFrame, height=150, width=150, bg=colPre, bd=3, relief='solid')
    colorPreview.place(x=50, y=50, anchor='nw')
    addRed.place(x=330, y=50, width=80, height=40, anchor='nw')
    addGreen.place(x=330, y=120, width=80, height=40, anchor='nw')
    addBlue.place(x=330, y=190, width=80, height=40, anchor='nw')
    addHex.place(x=330, y=260, width=150, height=40, anchor='nw')
    addName.place(x=330, y=330, width=200, height=40, anchor='nw')

    redLab.place(x=230, y=50, width=100, height=40, anchor='nw')
    greenLab.place(x=230, y=120, width=100, height=40, anchor='nw')
    blueLab.place(x=230, y=190, width=100, height=40, anchor='nw')
    hexLab.place(x=230, y=260, width=100, height=40, anchor='nw')
    nameLab.place(x=230, y=330, width=100, height=40, anchor='nw')

    addColor.place(x=230, y=400, width=100, height=40, anchor='nw')


canvas = Canvas(root, height=720, width=1280)
canvas.pack()

#frames
leftFrame = Frame(canvas)
leftFrame.place(x=0, y=0, width=250, height=720, anchor='nw')
rightFrame = Frame(canvas)
rightFrame.place(x=250, y=0, width=1030, height=720, anchor='nw')

#MENU
name = Label(leftFrame, text=userName,bg=bttBcg,bd=3, relief='solid', font=Arial, fg='black')
name.place(x=0, y=0, width=wdth, height=75, anchor='nw')

colors = Button(leftFrame, text='Colors',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
colors.place(x=0, y=75, width=wdth, height=75, anchor='nw')
colors.bind("<Button-1>", loadColors)


addColor = Button(leftFrame, text='Add color',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
addColor.place(x=0, y=150, width=wdth, height=75, anchor='nw')
addColor.bind("<Button-1>", addNewColor)

loadLast = Button(leftFrame, text='Load last',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
loadLast.place(x=0, y=225, width=wdth, height=75, anchor='nw')
loadLast.bind("<Button-1>", test.loadLastColor)

ledEff = Button(leftFrame, text='Led effects',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
ledEff.place(x=0, y=300, width=wdth, height=75, anchor='nw')

turnOff = Button(leftFrame, text='Turn off',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
turnOff.place(x=0, y=375, width=wdth, height=75, anchor='nw')
turnOff.bind("<Button-1>", Off)

#CLEAR TEST
options = Button(leftFrame, text='Clear',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
options.place(x=0, y=450, width=wdth, height=75, anchor='nw')
# options.bind("<Button-1>", clearFrame)

connectionStatus = Label(leftFrame, text=conStat, bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
connectionStatus.place(x=0, y=530, width=wdth, height=30, anchor='nw')


#COLORS LIST
listBx = Listbox(rightFrame, font=sArial, selectmode=SINGLE, bd=3, relief='solid')
listBx.bind('<<ListboxSelect>>', getIndex)

#COLOR ADDING
addRed = Entry(rightFrame, bd=3, relief='solid', font=sArial)
addGreen = Entry(rightFrame, bd=3, relief='solid', font=sArial)
addBlue = Entry(rightFrame, bd=3, relief='solid', font=sArial)
addHex = Entry(rightFrame, bd=3, relief='solid', font=sArial)
addName = Entry(rightFrame, bd=3, relief='solid', font=sArial)

redLab = Label(rightFrame, text='Red: ', bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
greenLab = Label(rightFrame, text='Green: ', bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
blueLab = Label(rightFrame, text='Blue: ', bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
hexLab = Label(rightFrame, text='Hex: ', bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
nameLab = Label(rightFrame, text='Name: ', bg=bttBcg,bd=3 ,relief='solid', font=smallArial, fg="black")
err = Label(rightFrame, text='!', bg='red',bd=3 ,relief='solid', font=Arial, fg="black")

addColor = Button(rightFrame, text='Add', bd=3, relief='solid', font=smallArial ,fg='black')
addColor.bind("<Button-1>", getInptValue)


root.mainloop()
