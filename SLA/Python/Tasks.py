    # import tkinter as tk
    # user_passwords = {
    #     'David': 'password1',
    #     'Rahul': 'password2',
    #     'Banana': 'password3',
    #     'Apple': 'password4',
    #     'Divine': 'password5',
    # }
    # def check_password():
    #     username = username_entry.get()
    #     password = password_entry.get()

    #     if username in user_passwords and user_passwords[username] == password:
    #             print("Login Successful", "Welcome, " + username + "!")
    #     elif username in user_passwords and password!=user_passwords[username]:
    #             print("Login Failed, password is wrong!")
    #     elif username not in user_passwords:
    #         print("Login Failed, Enter valid user name")

    # root = tk.Tk()
    # root.title("Login")
    # root.geometry("560x650")

    # username_label = tk.Label(root, text="Username:")
    # username_label.pack()
    # username_entry = tk.Entry(root)
    # username_entry.pack()

    # password_label = tk.Label(root, text="Password:")
    # password_label.pack()
    # password_entry = tk.Entry(root, show="*")
    # password_entry.pack()


    # login_button = tk.Button(root, text="Login", command=check_password)
    # login_button.pack()
    # root.mainloop()



#Even number don't print task

# class myException(Exception):
#     def __init__(self,message):
#         super().__init__(message)
       
# def check_even(number):
#     if number%2==0:
#         raise myException("don't give a even number")
    
# try:
#     num=int(input("enter the number: "))
#     check_even(num)
# except Exception as error:
#     print("custom error generated: ", error)

import os
data=open('./demo.txt','r')
print(data.read())

data=open('./demo.txt','a')
while True:
   user_name=input("Enter the name: ")
   data.write(user_name)
   choice=input("Do you want to continue or stop: ")
   if choice=="c":
      continue
   else:
      data.close()
      break
user_choice=input("Do you want to read or delete: ")
if user_choice=="read":
   data=open('./demo.txt','r')
   print(data.read())
elif user_choice=="delete":
   os.remove("demo.txt")
else:
   print("something went wrong")


