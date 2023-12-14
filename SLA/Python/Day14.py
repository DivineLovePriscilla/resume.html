#Creating objects
#Blueprint
# class student:
#     a="Divine"
    
# data=student
# print(data.a)
class student():

    def __init__(self,user_name,user_password):
        self.name=user_name
        print(f"name is {user_name} and my password is {user_password}")
    def printdata(self):
        print(f"my user name is {self.user_name}")
my_obj=student("Divine","Divine@1234")
my_obj.printdata()