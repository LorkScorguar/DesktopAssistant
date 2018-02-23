import datetime
import platform
import re
import subprocess
import sys
import time
from tkinter import *

dapplicationsWin={"Chrome":"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
"Firefox":"C:\Program Files (x86)\Mozilla Firefox\\firefox.exe",
"Notepad":"C:\WINDOWS\system32\\notepad.exe"}
dapplicationsLin={"Chrome":"/usr/bin/google-chrome"}

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
    if data in dapplicationsWin.keys() and platform.system()=='Windows':
        subprocess.run(dapplicationsWin[data])
    elif data in dapplicationsLin.keys() and platform.system()=='Linux':
        subprocess.run(dapplicationsLin[data])
    if res!="":
        notify(res)

def complete(data,label):
    res=""
    if re.search("[0-9+-\/\*]+",data):
        try:
            res=eval(data)
            label.config(text=res)
        except:
            pass
    elif data=="":
        label.config(text=res)

def run():
    root = Tk()
    text=StringVar()
    e = Entry(root, textvariable=text, foreground="white", background="black", font=("Courier",20))
    e.grid()
    e.focus()
    e.bind("<Return>", lambda e: root.destroy())
    e.bind("<Escape>", lambda e: root.destroy())
    label = Label(root, text=text.get(), foreground="white", background="black", font=("Courier",20))
    label.grid()
    text.trace("w", lambda name, index, mode, sv=text: complete(text.get(),label))
    wwidth=300
    wheight=70
    root.lift()
    root.overrideredirect(True) #to remove window decoration
    root.attributes("-topmost",True)
    root.attributes("-alpha","0.8")
    root.configure(background="black")
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (wwidth,wheight,width/2-wwidth,height/2-wheight))
    root.mainloop()
    data=text.get()
    analyse(data)

if __name__=="__main__":
    run()
