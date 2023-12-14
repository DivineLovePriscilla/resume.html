import tkinter as tk
window=tk.Tk()
window.title("my tkinter window")
window.geometry("450x650")
head_label=tk.Label(window,text="Login form")
head_label.grid(row=0,column=0,columnspan=2)
user_name=tk.Label(window,text="Username")
user_name.grid(row=1,column=1)
user_password=tk.Label(text="User Password")
user_password.grid(row=2,column=1)

entry1=tk.Entry(window)
entry1.grid(row=1,column=2)


user_name.grid(row=1,column=1)
window.mainloop()
