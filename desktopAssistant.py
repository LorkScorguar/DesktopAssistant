import datetime
import platform
import re
import subprocess
import sys
import time
from tkinter import *

dapplicationsWin={"Chrome":"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
"Firefox":"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"}
dapplicationsLin={}

def notifyWin(text):
    root = Tk()
    label = Label(root, text=text, foreground="white", background="black", padx="10", pady="4")
    label.grid()
    wwidth=25
    wheight=26
    root.lift()
    root.attributes("-topmost",True)
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (wwidth,wheight,width-140,height-105))
    root.mainloop()

def notifyLin(text):
    import notify2
    notify2.init("Luchiana")
    notify2.Notification("Desktop Assistant",text)

def notify(text):
    if platform.system()=="Windows":
        notifyWin(text)
    else:
        notifyLin(text)

def analyse(data):
    res=""
    if re.search("[0-9+-\/\*]+",data):
        res=eval(data)
    elif data in dapplications.keys():
        subprocess.run(dapplications[data])
    if res!="":
        notify(res)

def run():
    root = Tk()
    text=StringVar()
    e = Entry(root, textvariable=text, foreground="white", background="black")
    e.grid()
    e.focus()
    e.bind("<Return>", lambda e: root.destroy())
    wwidth=100
    wheight=36
    root.lift()
    #root.overrideredirect(True) #to remove window decoration
    root.attributes("-topmost",True)
    root.attributes("-transparentcolor", "white")
    root.attributes("-alpha","0.8")
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (wwidth,wheight,width/2-wwidth,height/2-wheight))
    root.mainloop()
    data=text.get()
    analyse(data)

if __name__=="__main__":
    run()
