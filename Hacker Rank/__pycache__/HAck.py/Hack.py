#Palindrome
# n=int(input("Enter the number"))
# temp=n
# reversed_num=0
# while (n>0):
#     digit=n%10   #1  2
#     reversed_num=reversed_num*10+digit    #0*10+1=1  1*10+2=12
#     n=n//10   #n=12                       #
    
# print("The reversed number is", reversed_num)
# if reversed_num==temp:
#     print("It is a palindrome number ")
# else:
#     print("It is not a palindrome number ")

#String Palindrome

# n=input("Enter a word")
# rev=""
# for i in n:
#     rev=i+rev           #Concatenation #It stores as E  n  (.........nE)
# print(rev)
# if rev==n:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

#Using slicing method

#Slicing is only applicable for string

#Reverse String

# n=int(input("Enter a number "))
# s=(str(n)[::-1])
# print(s)

# n=input("Enter a number or string ")
# s=n[::-1]
# print(s)

#Palindrome  using function

# def is_palindrome(string):
#     string=string.lower()

#     reversed_string=string[::-1]
#     return reversed_string==string

# string=input("enter a string")

# if is_palindrome(string):
#     print("The given string is a palindrome")
# else:
#     print("The given string is not a palindrome ")

#2. Factorial of a given number

# n=int(input("Enter a number "))
# f=1
# if n<0:
#     print("Factorial doesn't exist for negative number ")
# elif n==0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         f=f*i
        
#     print(f)

#3. Fibonacci Series named after Italian mathematician, Leonardo 

# n=5
# n1=0
# n2=1
# for i in range(n):
#     print(n1)
#     temp=n1
#     n1=n2
#     n2=temp+n2

#Using function

# def fib(n):
#     a=0
#     b=1
#     print(a)
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(10)

#4. Prime numbers

# n=int(input("Enter the number"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print(f"{n} is not a prime number")
#             break
#     else:
#             print(f"{n} is a prime number")
# else:
#      print(f"{n} is a unique number")

#Using function- block of codes

# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print(f"{n} is not a prime number")
#                 break
#         else:
#              print(f"{n} is a prime number")
#     else:
#       print(f"{n} is a unique number")

# prime(5)
#Aptitude format

# n=int(input("Enter a number "))
# a=[]
# for i in range(2,n+1):
#     if i**2>=n:
#         break
#     a.append(i)
# print(a)    
# for i in a:
#     if n%i==0:
#         print(n, "is not a prime number")
#         break
# else:
#     print(n, "is a prime number")


# n = int(input("Enter a number "))
# a = []
# for i in range(2, n):
#     if n % i == 0:
#         a.append(i)
# if not a:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")

#Checks 1 also

# n = int(input("Enter a number "))
# a = []

# for i in range(2, n):
#     if i**2 > n:
#         break
#     a.append(i)

# for i in a:
#     if n % i == 0:
#         print(n, "is not a prime number")
#         break
# else:
#     if n > 1:
#         print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n=5
for i in n:
    for j in i+1:
        print("*",end=" ")
    print()





