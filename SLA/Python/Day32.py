import tkinter as tk
window=tk.Tk()
window.title("My window")
window.geometry("450x650")

def getInfo(event):
    if entry1.get()=="Enter your username":
        entry1.delete(0,"end")
        entry1.config(fg='black')

def getOutInfo(event):
    if entry1.get()=="":
        entry1.insert(0,"enter your user name")
        entry1.config(fg='grey')


label1=tk.Label(window,text="user name",bg="violet")
label1.grid(row=0,column=0,padx=0,pady=0)

entry1=tk.Entry(window,width=30)
entry1.grid(row=1,column=0,columnspan=3,padx=10,pady=10)

entry1.insert(0,"Enter the user name")
entry1.config(fg='grey')
entry1.bind('<FocusIn>',getInfo)
entry1.bind('<FocusOut>',getOutInfo)
label2=tk.Label(window,text="user password",bg="violet")
label2.grid(row=2,column=0,padx=0,pady=10)

entry2=tk.Entry(window,width=30)
entry2.grid(row=3,column=0,columnspan=3,padx=0,pady=10)

window.mainloop()