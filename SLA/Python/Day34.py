import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry("450x650")
window.resizable(False,False)
def getdata(event):
    selected_data=combo_box.get()
    print(selected_data)
    label2.configure(text=f"You selected {selected_data}")


label1=ttk.Label(window,text="Select your proof ")
label1.place(x=10,y=10)

proof=["driving license", "aadhar card", "PAN card"]
combo_box=ttk.Combobox(window,values=proof)
combo_box.set(proof[0])
combo_box.place(x=25,y=35)
label2=ttk.Label(window,text="")
label2.place(x=10,y=80)

combo_box.bind('<<ComboboxSelected>>',getdata)
window.mainloop()

