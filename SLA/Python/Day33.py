#Frame 
import tkinter as tk 
window=tk.Tk()
window.title("my tkinter window")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.configure(bg="black")

def check():
    frame1.destroy()
    frame2.pack(fill="both",expand=True)
frame1=tk.Frame(window,bg="red")
frame1.pack(fill="both",expand=True)

label1=tk.Label(frame1,text="username")
label1.place(x=0,y=0)

entry1=tk.Entry(frame1)
entry1.place(x=0,y=50)

frame2=tk.Frame(window, bg="black")
frame2.pack()

label2=tk.Label(frame2,text="username")
label2.pack()

entry2=tk.Entry(frame2)
entry2.pack()
label3=tk.Label(frame2,text="user password")
label3.pack()

entry3=tk.Entry(frame2)
entry3.pack()

btn=tk.Button(frame1,text="Login", command=check)
btn.pack()

window.mainloop()
