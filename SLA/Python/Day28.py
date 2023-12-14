import re
user_id=input("Enter your Email Id \n")
pattern =r"^[a-zA-Z0-9]{8,10}$"
result=re.match(pattern,user_password)

if result:
    print("pattern matched")
else:
    print("pattern not matched")
