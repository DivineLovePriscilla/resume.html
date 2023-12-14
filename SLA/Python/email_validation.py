# import re
# data=input("Enter the data to check the pattern\n")
# pattern=r'^[\w\.-]+@[\w-]+\.[\w]+$'
# result=re.match(pattern,data)
# if result:
#     print("Pattern matched")
# else:
#     print("Pattern not matched")

import tkinter as tk
from tkinter import messagebox as msg
def alert():
    msg.showinfo(title="success alert",message="u clicked me")

window=tk.Tk()
window.title("alert message")

button=tk.Button(window,text="click me", command=alert)
button.place(x=50,y=50)
window.mainloop()