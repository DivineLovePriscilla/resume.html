a=[10,12,20,22]
# b=sum(a)
# print(b)

#Sum all items in the list
temp=0
for i in a:
    temp+=i
print("The sum of list is ", temp)

#Multiply all items in a list
a=[3,1,2,3]
result=1
for i in a:
    result=result*i
print(result)

# n=int(input("Enter the numbers"))
# reverse=int(str(n)[::-1])
# print("Reversed number is : ", reverse)

print("Twinkle, twinkle, little star,")
print("\t How I wonder what you are!")
print("\t \t Up above the world so high,")
print("\t \t Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\t How I wonder what you are")

#Get largest number from list
a=[8,-5,22,-3]
largest_num=a[0]
for i in a:
    if i>largest_num:
        largest_num=i
print("The largest number in the list is :", largest_num)
