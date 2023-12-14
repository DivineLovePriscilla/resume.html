#1. Number even or odd without using modulo operator

# n=int(input("Enter the number "))
# x=int(n//2)*2    #We use floor division here because it truncates(or roundoff) it
# if(x==n):
#     print("This is an even number")
# else:
#     print("This is an odd number")

#2.Square root of given number without using built-in functions
# n=int(input("Enter the number "))
# x=n**0.5
# print("The square root of given number is",x)

#3.Concatenate into a single string

# a=["I","am","a","good","girl"]
# b=" "
# for i in a:
#     b=b +" "+ i
# print(b)

# a=["I","am","a","good","girl"]
# for i in a:
#     print(i,end=" ")

#4. Reverse order of words in given sentence
# a="I am Divine Love Priscilla"
# b=a.split(" ")
# b.reverse()
# print(b)
# for i in b:
#     print(i,end=" ")

#5.Check if given number is power of 2

# n=int(input("Enter the number "))
# if n<=0:
#     print("It is not power of 2")
# elif (n&n-1)==0:
#     print("It is power of 2")
# else:
#     print("It is not power of 2")

#6.Remove all vowels from a given string

# str="priscilla"
# vowels="aeiou"
# # new=str
# for i in str:
#     if i in vowels:
#         str=str.replace(i,"")

# print(str)

#7.Given a list of numbers, find the sum of all positive numbers and the sum of all negative numbers.

# a=[2,-3,5,-6,23,-5,6,-8,9]
# positive=0
# negative=0
# for num in a:
#     if num>0:
#         positive+=num
#     else:
#         negative+=num
    
# print("Sum of positive numbers is",positive)
# print("Sum of negative numbers is",negative)

#8. Find the length of the longest word in a sentence.
# a=input("Enter the sentence")
# b=a.split()
# c=0
# for i in b:
#     if len(i)>c:
#         c=len(i)
#         word=i
# print("Longest word is",word)
# print(f"Length of {word} is {len(word)}" )

#9. Given a list of integers, find the sum of all even numbers and the sum of all odd numbers.
# a=[2,3,4,12,34,56,9,8]
# s=0
# o=0
# for num in a:
#     if num%2==0:
#         s=s+num
#     else:
#         o=o+num
# print("Sum of even numbers is ",s)
# print("Sum of odd numbers is ",o)

#10. Check if a given number is a perfect number

# n=int(input("Enter the number"))
# s=0
# for i in range(1,n):
#     if (n%i==0):
#         s+=i
# if s==n:
#     print(n,"is  a perfect number")
# else:
#     print(n, "is not a perfect number")

#11. Swap two variables without using a third variable.
# a=5
# b=10
# print("Numbers before swapping",a,b)
# a,b=b,a
# print("Numbers after swapping",a,b)

#12. Print the ASCII value of a given character.
# a="A"
# print(ord(a))

#13.Find the largest number in a list of floating-point numbers.
a=[2.3,4.3,2.1,4.5,2.1,2.2]
a.sort(reverse=True)
print(a[0])







    


