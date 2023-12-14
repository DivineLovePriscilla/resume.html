#Spin box

import tkinter as tk
from PIL import Image,ImageTk
window=tk.Tk()
window.title("Spin box")
window.geometry("450x500")

# def getdata():
#     print(spin.get())

# spin=tk.Spinbox(window,bg="lightblue" ,from_=0,to=50)
# spin.pack()

# button=tk.Button(window,text="submit",command=getdata)
# button.pack()

# window.mainloop()

#image rendering
back_image=Image.open('divine.jpg')
bg_image=ImageTk.PhotoImage(back_image)
label=tk.Label(window,image=bg_image)
label.place(relwidth=1,relheight=1)
menu_bar=tk.Menu(window)
window.config(menu=menu_bar)

file_menu=tk.Menu(menu_bar)
menu_bar.add_cascade(label="file",menu_bar=file_menu)
window.mainloop()