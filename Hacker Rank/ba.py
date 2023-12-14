from bank import Atm
my_obj=Atm()
while True:
    print("Type 1 for check balance")
    print("")


    user_choice=int(input("Enter the option"))
    if user_choice==1:
        my_obj.check_balance()
    elif user_choice==2:
        my_obj.deposit()
    elif user_choice==3:
        my_obj.withdraw()
    elif user_choice==4:
        my_obj.met_exit()
    else:
        print("Something went wrong")
        