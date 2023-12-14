import tkinter as tk
from tkinter import messagebox as msg

window=tk.Tk()
window.geometry("450x650")
window.title("My Appplication")
window.resizable(False,False)
window.configure(bg="beige")

def details():    #Frame 2
    Frame1.pack_forget()
    Frame2.pack(padx=40,pady=50)

def destroy():
    Frame2.pack_forget()
    Frame1.pack(padx=40,pady=50)

def getInfo(getinfo):
    if Entry1.get()=="Enter your mail address":
        Entry1.delete(0,"end")
        Entry1.config(fg="black")

def getoutInfo(getoutinfo):
    if Entry1.get()=="":
        Entry1.insert(0,"Enter your mail address") 
        Entry1.config(fg="grey")

def getInfo1(getinfo):
    if Entry2.get()=="Enter your name":
        Entry2.delete(0,"end")
        Entry2.config(fg="black")

def getoutInfo1(getoutinfo):
    if Entry2.get()=="":
        Entry2.insert(0,"Enter your name") 
        Entry2.config(fg="grey")

def getInfo2(getinfo):
    if Entry3.get()=="Enter your password":
        Entry3.delete(0,"end")
        Entry3.config(fg="black")

def getoutInfo2(getoutinfo):
    if Entry3.get()=="":
        Entry3.insert(0,"Enter your password") 
        Entry3.config(fg="grey")

Frame1=tk.Frame(window,bg="lightblue",width="300",height="300")
Frame1.pack(padx=40,pady=50)

Label1=tk.Label(Frame1,text="Signup",width="10",bg="salmon")
Label1.place(x=100,y=30)

Entry1=tk.Entry(Frame1,width="23")
Entry1.place(x=70,y=70)
Entry1.insert(0,"Enter your mail address")
Entry1.configure(fg="grey")
Entry1.bind('<FocusIn>',getInfo)
Entry1.bind('<FocusOut>',getoutInfo)

Entry2=tk.Entry(Frame1,width="23")
Entry2.place(x=70,y=110)
Entry2.insert(0,"Enter your name")
Entry2.configure(fg="grey")
Entry2.bind('<FocusIn>',getInfo1)
Entry2.bind('<FocusOut>',getoutInfo1)

Entry3=tk.Entry(Frame1,width="23")
Entry3.place(x=70,y=150)
Entry3.insert(0,"Enter your password")
Entry3.configure(fg="grey")
Entry3.bind('<FocusIn>',getInfo2)
Entry3.bind('<FocusOut>',getoutInfo2)

def alert():
    msg.showinfo(title="Info",message="You have registed successfully")

btn=tk.Button(Frame1,text="Create an account",bg="green",width="25",command=alert)

btn.place(x=50,y=200)

Label2=tk.Label(Frame1,text="Already have an account?",bg="white")
Label2.place(x=50,y=240)

btn=tk.Button(Frame1,text="Login",bg="blue",command=details)
btn.place(x=193,y=238)

#Frame 2 widgets

def destroy():
    Frame2.pack_forget()
    Frame1.pack(padx=40,pady=50)

def getInfo4(getinfo):
    if Entry4.get()=="Enter your mail or username":
        Entry4.delete(0,"end")
        Entry4.config(fg="black")

def getoutInfo4(getoutinfo):
    if Entry4.get()=="":
        Entry4.insert(0,"Enter your mail or username") 
        Entry4.config(fg="grey")

def getInfo5(getinfo):
    if Entry5.get()=="password":
        Entry5.delete(0,"end")
        Entry5.config(fg="black")

def getoutInfo5(getoutinfo):
    if Entry5.get()=="":
        Entry5.insert(0,"password") 
        Entry5.config(fg="grey")

Frame2=tk.Frame(window,bg="pink",width="300",height="300")

btn=tk.Button(Frame2,text="Login",bg="green",width="20")
btn.place(x=70,y=150)

Label2=tk.Label(Frame2,text="Don't have an account?",bg="white")
Label2.place(x=70,y=220)

btn=tk.Button(Frame2,text="signup",bg="lightgreen",command=destroy)
btn.place(x=201,y=217)

Entry4=tk.Entry(Frame2,width="25")
Entry4.place(x=70,y=70)
Entry4.insert(0,"Enter your mail or username")
Entry4.configure(fg="grey")
Entry4.bind('<FocusIn>',getInfo4)
Entry4.bind('<FocusOut>',getoutInfo4)

Entry5=tk.Entry(Frame2,width="25")
Entry5.place(x=70,y=110)
Entry5.insert(0,"password")
Entry5.configure(fg="grey")
Entry5.bind('<FocusIn>',getInfo5)
Entry5.bind('<FocusOut>',getoutInfo5)

window.mainloop()
