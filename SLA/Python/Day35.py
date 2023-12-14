#Radio button

import tkinter as tk
window=tk.Tk()
window.geometry("450x560")
#_______________________________________________________Radio button_________________________________________________________________________

# def getdata():
#     print(gender.get())
# gender=tk.StringVar()         #To get value from variable
# radio1=tk.Radiobutton(window,text="male",variable=gender,value="male")
# radio1.pack()

# radio2=tk.Radiobutton(window,text="female",variable=gender,value="female")
# radio2.pack()


#_______________________________________Checkbox_________________________________________________________________---
# def getdata():
#     if check1_var.get()==1:
#         print("Tamil selected")
#     if check2_var.get()==1:
#         print("English selected")

# label=tk.Label(window, text="How many languages do you know?")
# label.pack()
# check1_var=tk.IntVar()
# check2_var=tk.IntVar()
# check1=tk.Checkbutton(window,text="Tamil",variable=check1_var)
# check1.pack()
# check2=tk.Checkbutton(window,text="English",variable=check2_var)
# check2.pack()
# submit=tk.Button(window,text="submit",command=getdata)
# submit.pack()

# window.mainloop()

#__________________________________________________________Progress  Bar_________________________________________________________________



from tkinter import ttk
def increase_progress():
    current_value=progress_bar["value"]
    
    if current_value<100:
        progress_bar["value"]=current_value+10  
    else:
        progress_bar["value"]=0
        # progress_bar.start(10)
        
progress_bar=ttk.Progressbar(window,mode="determinate",length=200)
progress_bar.pack()

submit=tk.Button(window,text="submit",command=increase_progress)
submit.pack()

window.mainloop()