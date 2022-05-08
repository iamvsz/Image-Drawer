# Import module
from tkinter import *
from sketchpy import library as lib


# Create object
root = Tk()
root.title('Image Drawer')

# Adjust size
root.geometry( "550x100" )

# Dropdown menu options
options = [
	"Iron Man",
	"BTS",
	"Vijay",
    "Indian Flag",
    "Tom Holland",
    "Gojo"
]


def draww():
    text = clicked.get()
    if text == "Iron Man":
        obj = lib.rdj()
    elif text == "BTS":
        obj = lib.bts()
    elif text == "Vijay":
        obj = lib.vijay()
    elif text == "Indian Flag":
        obj = lib.flag()
    elif text == "Tom Holland":
        obj = lib.tom_holland()
    elif text == "Gojo":
        obj = lib.gojo()               
    else:
        obj = lib.rdj()                            
    obj.draw()

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Iron Man" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "Draw" , command = draww ).pack()

# Create Label
label = Label( root , text = "NOTE : After Completion of first Drawing, Please close the window and double click Draw button" )
label.pack()

# Execute tkinter
root.mainloop()
