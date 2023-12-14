import tkinter as tk


window=tk.Tk()
screen_width=window.winfo_screenwidth()
screen_heigth=window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_heigth}')
window.configure(bg="black")

def changeFrame():
    frame1.destroy()
    frame2.pack(fill='both', expand=True)
    

frame1=tk.Frame(window, bg="red")
frame1.pack(fill='both', expand=True)
label=tk.Label(frame1,text="Sign Up", fg="black",bg="white")
label.pack()

label1=tk.Label(frame1,text="frame1 1")
label1.grid(row=1,column=1)

entry1=tk.Entry(frame1, width=30)
entry1.grid(row=2,column=2)
frame2=tk.Frame(window, bg="blue")



btn=tk.Button(frame1,text="change frame1", command=changeFrame)
btn.pack()

window.mainloop()