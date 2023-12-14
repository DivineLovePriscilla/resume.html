from Atm import ATM
import logging

FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename='./div.log',format=FORMAT,filemode='w',level=logging.INFO)
bank_users={"Divine":"Divine123","Priscilla":"Priscilla1234"}

my_obj=ATM()

while True:
    user_name=input("Enter user name: ")
    user_password=input("Enter user password: ")
    if user_name in bank_users and user_password==bank_users[user_name]:
        logging.info(f"User {user_name} Logged in")
        print(f"User {user_name} logged successfully")


        while True:
            print("type 1 for check balance")
            print("type 2 for  deposit")
            print("type 3 for  withdraw")
            print("type 4 for  exit")
            user_choice=int(input("enter the option"))
            if user_choice==1:
                my_obj.check_balance()
            elif user_choice==2:
                my_obj.deposit()
            elif user_choice==3:
                my_obj.withdraw()
            elif user_choice==4:
                logging.info("Logged out")
                my_obj.met_exit()
                break
            else:
                print("Invalid choice. Please select a valid option.")
                
        break
    elif user_name in bank_users.keys() and user_password!=bank_users[user_name]:
        print("Invalid password, please Enter correctly")
    else:
        print("Invalid user name")