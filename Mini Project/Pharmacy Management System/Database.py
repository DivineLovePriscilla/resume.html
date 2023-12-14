n=input("Enter the values")
result=""
for i in n:
    if i.isalpha():
        a=i
    else:
        result=result+ int(i)*a
print(result)