import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image,ImageTk

class WIN():
    def __init__(self, window):
        self.database()
        self.window=window
        self.screen_width=self.window.winfo_screenwidth()
        self.screen_height=self.window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.state("zoomed")
        
        self.bg_image=Image.open("Pharmacy-Management-System.jpg")
        self.new_size=(self.screen_width,self.screen_height)
        self.resized_image=self.bg_image.resize(self.new_size)
        self.back_image=ImageTk.PhotoImage(self.resized_image)
        self.label=tk.Label(self.window,image=self.back_image)
        self.label.place(relwidth=1,relheight=1)
        window.title("Tkinter window")
        self.Signup_frame()
        self.login_frame()
        
    def Signup_frame(self):
       
        self.frame1=tk.Frame(self.window,bg="#B2BEB5",width="450",height="450")
        self.frame1.place(x=500,y=200)
        self.register=Label(self.frame1,text="Registration form",bg="#B2BEB5",font=("Times New Roman",20,"bold"))
        self.register.place(x=80,y=10)

        self.label1=tk.Label(self.frame1, text="User name",fg="black",bg="#00FF00",width="10")
        self.label1.place(x=30,y=70)  

        self.label2=tk.Label(self.frame1, text="Password",bg="#00FF00",fg="black",width="10")
        self.label2.place(x=30,y=100)

        self.label3=tk.Label(self.frame1, text="Email",bg="#00FF00",fg="black",width="10")
        self.label3.place(x=30,y=130)
        
        self.entry1=tk.Entry(self.frame1)
        self.entry1.place(x=100,y=70,height="25",width="220")

        self.entry2=tk.Entry(self.frame1)
        self.entry2.place(x=100,y=100,height="25",width="220")
        
        self.entry3=tk.Entry(self.frame1)
        self.entry3.place(x=100,y=130,height="25",width="220")

        self.Button=tk.Button(self.frame1,text="Register",bg="#00FF00",width="30",relief="raised",command=self.insertData)
        self.Button.place(x=60,y=190)
        
        self.label2=tk.Label(self.frame1, text="Already have an account?",bg="orange",fg="black")
        self.label2.place(x=60,y=240)
        
        self.Button1=tk.Button(self.frame1,text="Login",bg="White",relief="groove" ,command=self.changeframe)
        self.Button1.place(x=200,y=240)

    def database(self):
        self.connection=mysql.connector.connect(host="localhost",user="root",password="",database="signup_users")
        self.my_cursor=self.connection.cursor()
    
    def insertData(self):

        try:

            name=self.entry1.get()
            password=self.entry2.get()
            email=self.entry3.get()
            if not name and not password and not email:
                msg.showerror("Error","All fields are required")
            else:
                sql=f"INSERT INTO users(user_name,user_password,user_email) VALUES ('{name}','{password}','{email}')"
                self.my_cursor.execute(sql)
                self.connection.commit()
                self.my_cursor.close()
                self.connection.close()
                msg.showinfo("Form submitted", "Registered Successfully" )
                self.frame1.place_forget()
                self.frame2.place(x=500,y=200)
            
                self.entry1.delete(0,"end")
                self.entry2.delete(0,"end")
        except:
            msg.showerror("Warning","Username already exists")
        


    def login_frame(self):
        self.frame2=tk.Frame(self.window,bg="#B2BEB5",width="450",height="450")
  
        self.Label4=tk.Label(self.frame2,text="Login page",bg="lightgreen",fg="black")
        self.Label4.place(x=200,y=10)

        self.Label5=tk.Label(self.frame2,text="User_name",bg="#ADD8E6",fg="black")
        self.Label5.place(x=50,y=50)

        self.Label6=tk.Label(self.frame2,text="Password",bg="#ADD8E6",fg="black",width="10")
        self.Label6.place(x=50,y=90)

        self.Entry5=tk.Entry(self.frame2)
        self.Entry5.place(x=115,y=50,height="23",width="220")

        self.Entry6=tk.Entry(self.frame2)
        self.Entry6.place(x=115,y=90,height="23",width="220")

        self.Button2=tk.Button(self.frame2,text="Login",bg="#00FF00",width="28",command=self.getdata)
        self.Button2.place(x=60,y=160)

        self.Label3=tk.Label(self.frame2,text="Don't have an account?",bg="white",width="20")
        self.Label3.place(x=50,y=200)

        self.Button3=tk.Button(self.frame2,text="Signup",bg="yellow",command=self.change)
        self.Button3.place(x=187,y=198)

    

    def getdata(self):
        self.database()
        user_name=self.Entry5.get()
        user_password=self.Entry6.get()
        sql=f"select * from users where user_name='{user_name}' and user_password='{user_password}'"
        self.my_cursor.execute(sql)
        data=self.my_cursor.fetchone()
        self.my_cursor.close()
        self.connection.close()
        

        if user_name=="admin" and user_password=="admin@1234":
            msg.showinfo("Admin Verified staus","Logged in successfully")
            self.frame2.place_forget()


            self.frame3=tk.Frame(self.window,bg="White",width="650",height="650")
            self.frame3.place(x=200,y=200)
          
            self.Bg_image= Image.open('Pharm2.jpg') 
            self.new_size=(self.screen_width,self.screen_height)
            self.resized_image1=self.Bg_image.resize(self.new_size)
            self.back_image1=ImageTk.PhotoImage(self.resized_image1)
            self.label7=tk.Label(self.window,image=self.back_image1)
            self.label7.place(relwidth=1,relheight=1)

            self.frame3=tk.Frame(self.window,bg="White",width="650",height="650")
            self.frame3.place(x=200,y=120)

            self.label=tk.Label(self.frame3,text="Welcome Admin",bg="White",fg="Red",font=("times new roman",20,"bold"))
            self.label.place(x=30,y=4)

            self.Button4=tk.Button(self.frame3,text="Admin profile",bg="#0000FF",width="20",fg="white",font=("times new roman",20,"bold"))
            self.Button4.place(x=4,y=80,height="30",width="230")

            self.Button5=tk.Button(self.frame3,text="Total Users",bg="#0000FF",width="20",fg="white",font=("times new roman",20,"bold"))
            self.Button5.place(x=4,y=150,height="30",width="230")

            self.Button6=tk.Button(self.frame3,text="Live Users Count",bg="#0000FF",width="20",fg="white",font=("times new roman",20,"bold"))
            self.Button6.place(x=4,y=220,height="30",width="230")

            self.Button7=tk.Button(self.frame3,text="View Updates",bg="#0000FF",width="20",fg="white",font=("times new roman",20,"bold"))
            self.Button7.place(x=4,y=290,height="30",width="230")

            self.Button8=tk.Button(self.frame3,text="Help",bg="#0000FF",width="20",fg="white",font=("times new roman",20,"bold"))
            self.Button8.place(x=4,y=310,height="30",width="230")

            self.Button9=tk.Button(self.frame3,text="Deactivate Account",bg="#0000FF",fg="white",width="20",font=("times new roman",20,"bold"))
            self.Button8.place(x=4,y=330,height="30",width="230")

            self.Button10=tk.Button(self.frame3,text="Logout",bg="#0000FF",fg="white",width="20",font=("times new roman",20,"bold"))
            self.Button8.place(x=4,y=350,height="30",width="230")

        elif not(data==None):

            msg.showinfo("User verified status","Logged in successfully")
            self.frame2.place_forget()

            self.frame4=tk.Frame(self.window,bg="White",width="1650",height="1650")
            self.frame4.place(x=0,y=0)
            
            self.label7=tk.Label(self.frame4,text="Welcome to Pharmacy Management System",bg="Red",fg="White",font=("Times New Roman",36,"bold"))
            self.label7.place(x=0,y=10,width="1600",height="70")

            self.frame5=tk.Frame(self.frame4,bg="#0000FF",width="250",height="950")
            self.frame5.place(x=0,y=80)

            self.label8=tk.Label(self.frame5,text="Pharmacist",bg="#0000FF",fg="White",font=("Times New Roman",25,"bold"))
            self.label8.place(x=4,y=50,height="60",width="220") 

            self.Button11=tk.Button(self.frame5,text="Medicine Info",bg="#0000FF",fg="White",font=("Times New Roman",20,"bold"))
            self.Button11.place(x=4,y=170,height="60",width="220")

            self.Button12=tk.Button(self.frame5,text="Add medicines",bg="#0000FF",fg="White",font=("Times New Roman",20,"bold"))
            self.Button12.place(x=4,y=240,height="60",width="220")

            self.Button13=tk.Button(self.frame5,text="Stock Updates",bg="#0000FF",fg="White",font=("Times New Roman",20,"bold"))
            self.Button13.place(x=4,y=310,height="60",width="220")

            self.Button14=tk.Button(self.frame5,text="Delete Updates",bg="#0000FF",fg="White",font=("Times New Roman",20,"bold"))
            self.Button14.place(x=4,y=380,height="60",width="220")

            self.Button15=tk.Button(self.frame5,text="Invoice Collection",bg="#0000FF",fg="White",font=("Times New Roman",20,"bold"))
            self.Button15.place(x=4,y=450,height="60",width="220")

            self.Button16=tk.Button(self.frame5,text="Logout",bg="#0000FF",fg="white",font=("Times New Roman",25,"bold"))
            self.Button16.place(x=4,y=520,height="60",width="220")

            self.Button17=tk.Button(self.frame5,text="Exit",bg="#0000FF",fg="White",font=("Times New Roman",20,"bold"),command=self.need)
            self.Button17.place(x=4,y=590,height="60",width="220")

            

        # def med_add(self):

            self.frame5=tk.Frame(self.frame4,bg="White",width="1250",height="950")
            self.frame5.place(x=250,y=80)

            self.label9=tk.Label(self.frame5,text="Medicine add department",bg="White",fg="black",font=("Times New Roman",25,"bold"))
            self.label9.place(x=3,y=20,height="50")       

       
            self.label10=tk.Label(self.frame5,text="Reference No",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label10.place(x=20,y=100)

            self.label11=tk.Label(self.frame5,text="Company Name",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label11.place(x=20,y=150)

            self.label12=tk.Label(self.frame5,text="Type of medicine",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label12.place(x=20,y=200)

            self.label13=tk.Label(self.frame5,text="Issue Date",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label13.place(x=20,y=250)

            self.label14=tk.Label(self.frame5,text="Exp Date",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label14.place(x=20,y=300)

            self.label15=tk.Label(self.frame5,text="Uses",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label15.place(x=20,y=350)

            self.label16=tk.Label(self.frame5,text="Side effect",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label16.place(x=20,y=400)

            self.label17=tk.Label(self.frame5,text="Prec&Warning",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label17.place(x=20,y=450)

            self.label18=tk.Label(self.frame5,text="Dosage",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label18.place(x=20,y=500)

            self.label19=tk.Label(self.frame5,text="Tablets Price",bg="White",fg="Black",font=("Times New ROman",14,"bold"))
            self.label19.place(x=20,y=550)

            self.Entry7=tk.Entry(self.frame5)
            self.Entry7.place(x=225,y=100,height="23",width="220")

            self.Entry8=tk.Entry(self.frame5)
            self.Entry8.place(x=225,y=150,height="23",width="220")

            self.Entry9=tk.Entry(self.frame5)
            self.Entry9.place(x=225,y=200,height="23",width="220")

            self.Entry10=tk.Entry(self.frame5)
            self.Entry10.place(x=225,y=250,height="23",width="220")

            self.Entry11=tk.Entry(self.frame5)
            self.Entry11.place(x=225,y=300,height="23",width="220")

            self.Entry12=tk.Entry(self.frame5)
            self.Entry12.place(x=225,y=350,height="23",width="220")

            self.Entry13=tk.Entry(self.frame5)
            self.Entry13.place(x=225,y=400,height="23",width="220")

            self.Entry14=tk.Entry(self.frame5)
            self.Entry14.place(x=225,y=450,height="23",width="220")

            self.Entry15=tk.Entry(self.frame5)
            self.Entry15.place(x=225,y=500,height="23",width="220")

            self.Entry16=tk.Entry(self.frame5)
            self.Entry16.place(x=225,y=550,height="23",width="220")

            self.Button18=tk.Button(self.frame5,text="Submit",bg="#0000FF",fg="Black",font=("Times New Roman",25,"bold"),command=self.submit)
            self.Button18.place(x=335,y=600,height="60")


    def changeframe(self):
        self.frame1.place_forget()
        self.frame2.place(x=500,y=200)

    def change(self):
        self.frame2.place_forget()
        self.frame1.place(x=500,y=200) 

    def need(self):
         if msg.askyesno("yes or no","Do you really want to exit")==True:
            self.window.destroy()
    

    def submit(self):

            self.database()
            ref_no=self.Entry7.get()
            comp_name=self.Entry8.get()
            type_of_med=self.Entry9.get()
            issue_date=self.Entry10.get()
            exp_date=self.Entry11.get()
            uses=self.Entry12.get()
            side_effect=self.Entry13.get()
            prec_Warn=self.Entry14.get()
            dosage=self.Entry13.get()
            tablets_price=self.Entry14.get()
            
            sql=f"INSERT INTO add_medicine(reference_no,company_name,type_of_medicine,issue_date,exp_date,uses,side_effects,Prec_Warning,dosage,tablets_price) VALUES ('{ref_no}','{comp_name}','{type_of_med}','{issue_date}','{exp_date}','{uses}','{side_effect}','{prec_Warn}','{dosage}','{tablets_price}')"
            self.my_cursor.execute(sql)
            self.connection.commit()
            self.my_cursor.close()
            self.connection.close()

    # def stock_update():

    


if __name__=='__main__':
    window=tk.Tk()
    my_obj=WIN(window)
    window.mainloop()
        

        
