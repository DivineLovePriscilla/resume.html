class Person:
    Person=[]
    def __init__(self, name, age):
        while True:
            name=input("Enter the name: \n")
            age=int(input("Enter the number: \n"))
            gender=input("Enter the gender")
            
            self.name=name
            self.age=age
    def data():
        pass  

class Male(Person):
    
    def data(self):
        print(f"my user name is {self.name} and age is {self.age}")

class Female(Person):
    def data(self):
        print(f"my user name is {self.name} and age is {self.age}")

male_person=Male
female_person=Female
# both_person=Person()

male_person.data()
female_person.data()
# both_person.data()






