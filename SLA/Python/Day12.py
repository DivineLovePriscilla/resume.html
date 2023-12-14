# To do a specific task- function
# We can reuse code
#To avoid space error or to leave space empty, use pass

# def printdata(name, password):
#     print(f"my name is {name} and my password is {password}")
# user_name=input("Enter the user name ")
# user_password=input("Enter the password ")
# printdata(user_name,user_password)


#Task 1
# n="python"
# length=len(n)
# for i in range(length): 
#     for j in range(i+1):
#         print(n[j],end="")
#     print()

# for i in range(length-1):
#     for j in range(length-1-i):
#         print(n[j],end="")
#     print()

#Task 2

name=input("Enter the name ")
password=input("Enter the password ")
n=int(input("Enter the number of times "))
a=[]
for i in range(n):
    a.append({name:password})
print(a)
    
    