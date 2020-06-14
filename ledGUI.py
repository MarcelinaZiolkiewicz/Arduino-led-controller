from tkinter import *
from tkinter import font
import os
import test

userName = 'username' #input("Please tell, how do they call you?  ")
userName = "Hello " + userName
usrLen = len(userName)


time = "00:00:00"
connectionStatus = ''
darkMode = True #do poprawy
dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = 'colorsStrip.txt'

wdth = 250

bttBcg = '#686de0'
actvBtt = '#4834d4'
bcgColor = '#c8d6e5'


root = Tk()
Arial = font.Font(family="Arial Rounded MT", size=22, weight='bold')
sArial = font.Font(family="Arial Rounded MT", size=20, weight='bold')


def loadColors(event):

    f = open(dir_path + '/' + filePath, "r", encoding="utf-8")
    listBx = Listbox(root, font=sArial, selectmode=SINGLE)

    count = len(open(dir_path + '/' + filePath, "r").readlines())
    print(f'\nColors found: {count} \n')


    for line in f:

        underTab = line.split("_")
        dotTab = underTab[0].split(".")
        col = dotTab[0] + "." + dotTab[1][0].capitalize() + dotTab[1][1:len(dotTab[1])]
        
        listBx.insert(int(dotTab[0]), col)
        print(col)

    # for x in range(count):
    #     listBx.insert(x, "text")
    

    f.close()

    #colorToSet = input("\nChose color to set: ")
    listBx.place(x=wdth, y=0, width=300, height=525, anchor='nw')
    print("Done")
    


def onClosing():
    print("Kill leds")
    root.destroy()


def darkMode():
    pass

def graphicMenu():

    canvas = Canvas(root, height=720, width=1280)
    canvas.pack()

    name = Label(root, text=userName,bg=bttBcg,bd=3, relief='solid', font=Arial, fg='black', underline=usrLen)
    name.place(x=0, y=0, width=wdth, height=75, anchor='nw')

    colors = Button(root, text='Colors',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
    colors.place(x=0, y=75, width=wdth, height=75, anchor='nw')
    colors.bind("<Button-1>", loadColors)
    addColor = Button(root, text='Add color',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
    addColor.place(x=0, y=150, width=wdth, height=75, anchor='nw')

    loadLast = Button(root, text='Load last',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
    loadLast.place(x=0, y=225, width=wdth, height=75, anchor='nw')

    ledEff = Button(root, text='Led effects',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
    ledEff.place(x=0, y=300, width=wdth, height=75, anchor='nw')

    manage = Button(root, text='Manage sections',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
    manage.place(x=0, y=375, width=wdth, height=75, anchor='nw')

    options = Button(root, text='Options',bg=bttBcg,bd=3, relief='solid', font=Arial, activebackground=actvBtt)
    options.place(x=0, y=450, width=wdth, height=75, anchor='nw')

    # newColorInpt = Entry(root, bd=3, relief='solid', font=sArial)
    # newColorInpt.place(x=0, y=525, width=wdth, height=50, anchor='nw')

    root.mainloop()


graphicMenu()