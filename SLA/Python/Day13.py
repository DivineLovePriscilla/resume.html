# def data(user_name,user_country="India"):
#     print(f"user name is {user_name} and user country is {user_country}")
# data("Arun","Srilanka")

# def datas(*students):
#     print(students)
#     print(type(students))
# datas("Arun","Raja","Pravin","Priya")

#arbitrary keyword arguements

# def mul(a):
#     return lambda b:a*b
# num=mul(10)


# alpha = ['d','f','c']
# alpha += 'ka'
# print(list)

class Student:
    def __init__(self, user_name, user_password):
        self.name=user_name
        self.password=user_password
    def printdata(self):
        print(f"my name is {self.name} and my password is {self.password}")
my_obj=Student("Divine", "Divine@1234")
my_obj.printdata()
            