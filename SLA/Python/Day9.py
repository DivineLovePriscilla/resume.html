# #Task 1
# user_name=input("Enter the name of user")
# user_age=int(input("Enter the age of user"))
# if user_age>=18:
#         print("You are eligible for vote")
# else:
#         print("you are not eligible for vote")

# # Task 2
# a=int(input("Enter the number"))
# if a==0:
#     print("zero")
# elif a%2==0:
#     print(a, "is even number")
# elif a%2==1:
#     print(a, "is odd number")

# #Task 3

# print("Greetings! Welcome to Pizza order")
# size=input("Enter the size of pizza ")
# cost=0
# if size == "small":
#     cost=15
#     print("It costs 15$")
# if size == "medium":
#     cost=20
#     print("It costs 20$")
# if size == "large":
#     cost=25
#     print("It costs 25$")
# pepperoni=input("Do you need to add pepproni ")
# if pepperoni=="yes":
#     if size=="small":
#         cost+=2
#     if size=="medium":
#         cost+=3

#     if size=="large":
#         cost+=5
# extra_cheese=input("Would you like to add extra cheese ")
# if extra_cheese == "yes":
#     cost += 1

# print("Your total is $", cost)

# #Task 4 Roller coaster

# print("Welcome to blood freezing ride ")
# height=int(input("Enter the height of person in cm "))
# if height>120:
#     print("You are allowed to ride, Enjoy")
# else:
#     print("You are not allowed to ride, Sorry")
# age=int(input("Enter your age"))
# if age==12:
#     print("Costs 5$")
# if age>12:
#   if age==18:
#     print("Costs 7$")
# if age>18 :
#     print("Costs 12$")

# #Task 5 BMI
# weight=float(input("Enter your weight : "))
# height=float(input("Enter your height : "))
# bmi=weight/ (height**2)
# print(bmi)
# if bmi<18.5:
#     print("You are underweight")
# if bmi==18.5: 
#     if bmi<26:
#         print("You are normal weight")
# if bmi>25:
#     if bmi<31:
#         print("You are over weight")
# if bmi>30:
#     print("You are obese")

# #Task 6 Reverse name using for loop

name="Priscilla"
reversed_name=""
for i in range(len(name)):
    i=-i-1
print(reversed_name[i])





