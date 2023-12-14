from tkinter import *
import pymysql
window=Tk()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()



class Database():
    def __init__(self):
        window.geometry(f"{screen_width}x{screen_height}")
        window.state("zoomed")
        window.title("My Window")
        self.connection=pymysql.connect(host="localhost",user="root",paasword="",database="signup_users")
        self.my_cursor