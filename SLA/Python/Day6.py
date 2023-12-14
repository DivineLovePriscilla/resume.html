# text="gaghgsa"
# print(text.isalpha())
# my_list=["apple", "orange","mango","grapes"]
# for i in range(1,4,2):
#     print(my_list[i])

#Even and odd numbers
# for i in range(0,21,2):
#    print(i) 

# for i in range(1,20,2):
#    print(i)   

n=int(input("Enter the number "))
if n==n[::-1]:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")


