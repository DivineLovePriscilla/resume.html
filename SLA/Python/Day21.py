#Polymorphism

# class boy:
#     def intro(self):
#         return "am 18 years old boy"
# class student(boy):
#     def intro(self):
#         return "am 18 years old student"
    
# class player(boy):
#     def intro(self):
#         return "am 18 years old player"
    
# class writer(boy):
#     def intro(self):
#         return "am 18 years old writer"
    
# my_obj=[boy(),student(),player(),writer()]

# for i in my_obj:
#     print(i.intro())

class data():
    def __init__(self,username,userpassword):
        self.username=