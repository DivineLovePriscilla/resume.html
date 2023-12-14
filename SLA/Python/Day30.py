import tkinter as tk
window=tk.Tk()
window.title("my tkinter window")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.configure(bg="black")

def data():
    
   user_name_label=tk.Label(text="user name", fg="Red",bg="white")
   user_name_label.pack(side="top")

label2=tk.Label(window,text="user name",bg="red",fg="white")
label2.grid(row=1,column=0)

entry1=tk.Entry(window)
entry1.grid(row=1,column=1)

btn=tk.Button(window,text="submit",bg="red",fg="white",command=data)
btn.grid(row=2,column=1)
window.mainloop()


# list of dictionaries, if user name wrong or password wrong





