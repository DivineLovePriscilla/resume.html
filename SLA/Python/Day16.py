# class female:
#     def data(self):
#         print("Data method inside the female class")
# class male:
#     def printdata(self):
#         print("Call function inside male class")
# class Students(male,female):
#     def __init__(self):
#         super().data()
#         super().printdata()
# my_obj=Students()

class female:
    def data(self):
        print("Grandparent class")
class male(female):
    def datas(self):
        print("Parent class")

class student(male):
    def __init__(self):
        super().data()
myobj=student()


