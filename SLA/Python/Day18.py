class male:
    def __init__(self, *data):
        self.male = data
        print(data)
    def male_data(self):
        male_data = self.male
        print(male_data)
    
class female:
    def __init__(self,*data):
        self.female = data
        print(data)

    def female_data(self):
        female_data = self.female
        print(female_data)

class datas(male, female):
    def __init__(self,male_data,female_data):
        both=[male_data, female_data]
        print(both)

data=True
males=[]
females=[]
# both=males.extend(females)

while data:
    student={}
    name,age,gender=input("Enter the name, age and gender split by commas").split(",")
    data=input("enter the s to stop, c to continue")
    if data=="s":
        if gender=="male":
            student={"name":name,"age":age,"gender":gender}
            males.append(student)
        elif gender=="female":
            student={"name":name,"age":age,"gender":gender}
            females.append(student)
        else:
            print("please check the gender")
        data=False
    elif data=="c":
        if gender=="male":
            student={"name":name,"age":age,"gender":gender}
            males.append(student)
        elif gender=="female":
            student={"name":name,"age":age,"gender":gender}
            females.append(student)
        else:
            print("please check the gender")
    else:
        print("something went wrong")

data_choice=input("Enter the gender you want to see example male,female, or both.")
if data_choice=="male":
    male_data=male(males)
elif data_choice=="female":
    female_data=female(females)
elif data_choice=="both":
    both_data=datas(males,females)







# n=[19,19,5,5,5,78,76,90]
# if n.count(19) == 2 and n.count(5)== 3:
#     result = True
# else:
#     result = False

# print(result)


# def list(n):
#     nineteen=n.count(19)
#     five=n.count(5)
#     if nineteen==2 and five==3:
#         return True
#     else:
#         return False

# first_list=[19,5,19,5,5,4,6]
# n1=list(first_list)
# print(n1)
# second_list=[19,5,19,5,7,4,6]
# n2=list(second_list)
# print(n2)
# third_list=[19,5,4,5,8,4,6]
# n3=list(third_list)
# print(n3)