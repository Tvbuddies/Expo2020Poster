from tkinter import *
from tkinter.ttk import *
import webbrowser

#variables
root = Tk()
new = 100
url = "https://www.expo2020dubai.com/"
url2 = "https://www.youtube.com/watch?v=NGRPP57U4zo"

#commands and processes 
root.resizable(False, False)

def openweb():
    webbrowser.open(url,new=new)
def openvideo():
    webbrowser.open(url2,new=new)
Label(root, text="Hello, World... and welcome to the world expo", font=('Ariel', 15)).pack(side=TOP, pady=20)
photo = PhotoImage(file=r"C:\Users\s305126\Desktop\Expo app\expo logo up.png")


Button(root, text='', image=photo).pack(side=TOP)
Button(root, text='Check out the Expo 2020 website', command=openweb).pack(side=BOTTOM)
Button(root, text='Watch a video about expo 2020', command=openvideo).pack(side=BOTTOM)

mainloop()
