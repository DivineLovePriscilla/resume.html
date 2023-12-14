class both:
    def __init__(self,male_data,female_data):
        self.male_data=male_data
        self.female_data=female_data

    def print_both_data(self):
        print(self.male_data)
        print(self.female_data)

    def print_male_data(self):
        print(self.male_data)

    def print_female_data(self):
        print(self.female_data)

class male(both):
    def __init__(self,male_data,female_data):
        super().__init__(male_data,female_data)  
        super().print_male_data()
        # self.another_meth()

    # def another_meth():
    #     print("another method in male class")


class female(both):
    def __init__(self,male_data,female_data):
        super().__init__(male_data,female_data)
        super().print_female_data()

male_data=[]
female_data=[]
while True:
    student={}
    name,age,gender=input("Enter the name, age and gender split by commas").split(",")
    if gender=="male":
       student={"name":name,"age":age,"gender":gender}
       male_data.append(student)
    elif gender=="female":
        student={"name":name,"age":age,"gender":gender}
        female_data.append(student)
    else:
        print("Please check the gender")

    data=input("Enter s to stop and c to continue")
    if data=="c":
        continue
    elif data=="s":
        break
    else:
        print("Please enter a valid data")

user_data=input("Type male, female or both")
if user_data=="male":
    male_obj=male(male_data,female_data)
elif user_data=="female":
    female_obj=female(male_data,female_data)
elif user_data=="both":
    both_obj=both(male_data,female_data)
    both_obj.print_both_data()
