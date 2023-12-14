#02-08-2023
#Task 1

# years=int(input("Enter the age of individual "))
# total_years=90
# Balance=total_years-years
# a=Balance*12
# b=Balance*52
# c=Balance*365
# print("Remaining months",a)
# print("Remaining weeks",b)
# print("Remaining days",c)

#Task 2
# user_name="Priscilla"
# user_password="Divine@1234"
# while True:
#     name=input("Enter the username ")
#     password=input("Enter the password  ")
#     if user_name==name and user_password==password:
#         print("login successful")
#         break
#     else:
#         print("login failed please try again")
# #Task 3
year=int(input("Enter any year "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year, "is a leap year ")
        else:
            print(year, "is not a leap year ")       
    else:
        print(year,"is leap year ")
else:
#     print(year, "is not a leap year")

# #Task 4
print("Love Calculator")

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
logic="True"
logic_2="Love"
combined_names = name1 + name2
love_score = 0

for i in logic:
    love_score += combined_names.count(i)
    print((logic+logic_2).count)

print("\nLove Score:", love_score, "%")

if love_score < 10 or love_score>90:
    print("Sorry it won't go good!")
elif love_score >40 and love_score<50:
    print("You are alright together ")
else:
    print("You are perfect match ")
