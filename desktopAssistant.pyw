# coding: utf-8
import datetime
import platform
import re
import subprocess
import sys
import time
from tkinter import *

dapplicationsWin={"chrome":r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
"firefox":r"C:\Program Files (x86)\Mozilla Firefox\\firefox.exe",
"notepad":r"C:\WINDOWS\system32\\notepad.exe",
"git":r"C:\Users\pied\AppData\Local\Programs\Git\\git-bash.exe --cd-to-home",
"ping":r"ping -n 1 %ARG%"}
dapplicationsLin={"chrome":"/usr/bin/google-chrome"}

wwidth=300
wheight=31

def notifyWin(text,title,fg,bg):
    root = Tk()
    label = Label(root, text=text, foreground=fg, background=bg, padx="10", pady="4")
    label.grid()
    wwidth=25
    wheight=26
    root.lift()
    root.attributes("-topmost",True)
    root.title(title)
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (wwidth,wheight,width-140,height-105))
    root.mainloop()

def notifyLin(text,title):
    import notify2
    notify2.init("Luchiana")
    notify2.Notification(title,text)

def notify(text,title="Desktop Assistant",fg="gray",bg="black"):
    if platform.system()=="Windows":
        notifyWin(text,title,fg,bg)
    else:
        notifyLin(text,title)

def analyse(data):
    res=""
    tmp=data.split(" ")
    if tmp[0].lower() in dapplicationsWin.keys() and platform.system()=='Windows':
        if not "%ARG%" in dapplicationsWin[tmp[0].lower()]:
            subprocess.run(dapplicationsWin[tmp[0].lower()])
        else:
            cmd=dapplicationsWin[tmp[0].lower()]
            del tmp[0]
            cmd=cmd.replace("%ARG%",' '.join(tmp))
            output=subprocess.run(cmd)
            if output.returncode==0:
                notify(cmd+" succeeded","Command","white","green")
            else:
                notify(cmd+" failed","Command","white","red")
    elif tmp[0].lower() in dapplicationsLin.keys() and platform.system()=='Linux':
        if not "%ARG%" in dapplicationsLin[tmp[0].lower()]:
            subprocess.run(dapplicationsLin[tmp[0].lower()])
        else:
            cmd=dapplicationsLin[tmp[0].lower()]
            del tmp[0]
            cmd=cmd.replace("%ARG%",' '.join(tmp))
            output=subprocess.run(cmd)
            if output.returncode==0:
                notify(cmd+" succeeded")
            else:
                notify(cmd+" failed")
    elif re.search("timer",data):
        if tmp[1][-1:]=="m":
            tsleep=int(tmp[1][:-1])*60
        else:
            tsleep=int(tmp[1])
        time.sleep(tsleep)
        del tmp[0]
        del tmp[0]
        notify(str(' '.join(tmp)),"Timer End")
    if res!="":
        notify(res)

def complete(data,label,root):
    res=""
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    wheight2=root.winfo_reqheight()
    if re.search("[0-9+-\/\*]+",data):
        try:
            res=eval(data)
            label.config(text=res)
            root.geometry('%dx%d+%d+%d' % (wwidth,wheight2,width/2-wwidth,height/2-wheight))
        except:
            pass
    elif data=="":
        label.config(text=res)
        root.geometry('%dx%d+%d+%d' % (wwidth,wheight,width/2-wwidth,height/2-wheight))

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
    text.trace("w", lambda name, index, mode, sv=text: complete(text.get(),label,root))
    root.lift()
    if platform.system()=="Windows":
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
