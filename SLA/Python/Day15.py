class Student:
    def __init__(self):
        print("Student constructor")
    def printdata(self):
        print("print data method is called")
class male(Student):
    def __init__(self):
        super().printdata()

my_obj=male()

# class Student:
#     def __init__(self, user_name, user_password):
#         self.user_name=user_name
#         self.user_password=user_password
#     def printdata(self):
#         print(f"my name is {self.user_name} and my password is {self.user_password}")
# my_obj=Student("Divine", "Divine@1234")
# my_obj.printdata()