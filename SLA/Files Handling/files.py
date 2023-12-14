# data=open('./demo.text','r')
# print(data.read())
# print(data.readline())
# a=data.readlines()
# print(a[1])
# for i in range(len(a)):

#     if i==1:
#         print(a[1])
    # if i==0:
    #     pass
    # elif i==1:
    #     print(a[1])
    # else:
    #     pass

# data.close()

# data=open('./demo.text','a')
# data.write("\n")

#get data from user, get all names using while loop, if reading file, if yes---->read, if no---->exit
# import os

# e=open('./demo.text','r')
# print(e.read())
# e.close()
# while True:
#     name = input("Enter a name (or type 'exit' to quit): ")
#     if name =='exit':
#         break
#     else:
#         e= open('demo.text', 'a')
#         e.write(name +"\n ")

# b=input("Do you want to read the file or delete")
# if b=="read":
#     e= open('./demo.text', 'r')
#     names = e.readlines()
#     for name in names:
#         print(name) 
# elif b=="delete":
#     os.remove('./demo.text')


# e.close()


# data=open('./demo.text','w')
# data.write("This is writer mode line")
# data.close()

# datas=["single line \n","second line \n", "Third line"]
# data=open('./demo.text','w')
# data.writelines(datas)
# data.close()

data_to_write=[["kumar"]]