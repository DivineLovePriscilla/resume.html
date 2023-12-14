import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

class WIN():
    def __init__(self, window):
        self.window=window
        self.window.geometry("650x650")
        window.title("Tkinter window")
        self.window.configure(bg="#90EE90")
        self.window.resizable(True,True)
        self.window.state("zoomed")
        self.Signup_frame()
        self.login_frame()
        self.dashboard()

    
    def Signup_frame(self):
        self.frame1=tk.Frame(self.window,bg="#F4C2C2",width="450",height="450")
        self.frame1.place(x=100,y=100)

        self.label1=tk.Label(self.frame1, text="User name",fg="black",bg="lightblue",width="10")
        self.label1.place(x=20,y=30)  

        self.label2=tk.Label(self.frame1, text="Password",bg="lightblue",fg="black",width="10")
        self.label2.place(x=20,y=80)

        self.label3=tk.Label(self.frame1, text="Email",bg="lightblue",fg="black",width="10")
        self.label3.place(x=20,y=130)

        self.entry1=tk.Entry(self.frame1)
        self.entry1.place(x=90,y=29,height="22",width="222")
        
        self.entry2=tk.Entry(self.frame1)
        self.entry2.place(x=90,y=80,height="22",width="222")
        
        self.entry3=tk.Entry(self.frame1)
        self.entry3.place(x=90,y=130,height="22",width="222")

        
        self.Button=tk.Button(self.frame1,text="Create an account",bg="lightblue",width="30",command=self.Infomsg)
        self.Button.place(x=60,y=170)
        
        self.label2=tk.Label(self.frame1, text="Already have an account?",bg="orange",fg="black")
        self.label2.place(x=60,y=200)
        
        self.Button1=tk.Button(self.frame1,text="Login",bg="White",command=self.changeframe)
        self.Button1.place(x=200,y=198)


    def login_frame(self):
        self.frame2=tk.Frame(self.window,bg="#ffcccb",width="450",height="450")
  
        self.Label4=tk.Label(self.frame2,text="Login page",bg="lightgreen",fg="black")
        self.Label4.place(x=200,y=10)

        self.Label5=tk.Label(self.frame2,text="User_name",bg="#ADD8E6",fg="black")
        self.Label5.place(x=50,y=50)

        self.Label6=tk.Label(self.frame2,text="Password",bg="#ADD8E6",fg="black",width="10")
        self.Label6.place(x=50,y=90)

        self.Entry5=tk.Entry(self.frame2)
        self.Entry5.place(x=115,y=50,height="23")

        self.Entry6=tk.Entry(self.frame2)
        self.Entry6.place(x=115,y=90,height="23")

        self.Button2=tk.Button(self.frame2,text="Login",bg="green",width="28")
        self.Button2.place(x=35,y=140)

        self.Label3=tk.Label(self.frame2,text="Don't have an account?",bg="white",width="20")
        self.Label3.place(x=40,y=200)

        self.Button3=tk.Button(self.frame2,text="Signup",bg="yellow",command=self.changeframe1)
        self.Button3.place(x=187,y=198)

    def dashboard(self):
        self.frame3=tk.Frame(self.window,bg="#ffcccb",width="450",height="450")
        
        self.label7=tk.Label(self.frame3,text="Welcome to Pharmacy Management System",fg="black")
        self.label7.place(x=70,y=10)

        self.label7=tk.Label(self.frame3,text="DASHBOARD",fg="black",width="20")
        self.label7.place(x=40,y=50)

        self.button4=tk.Button(self.frame3,text="Home",bg="Green",fg="Black")
        self.button4.place(x=20,y=50)
    
    
    def Infomsg(self):
        msg.showinfo(title="Info",message="You have registed successfully")

    def changeframe(self):
        self.frame1.place_forget()
        self.frame2.place(x=100,y=100)

    def changeframe1(self):
        self.frame2.place_forget()
        self.frame3.place(x=250,y=100)  

if __name__=='__main__':
    app=tk.Tk()
    window=WIN(app)
    app.mainloop()
        

        
