# import random
# H="Head"
# T="Tail"
# val=str(random.randin(H,T))
# print(val)

# num=random.random()
# print num

# name="Divine Love Priscilla"
# print(name[::-1])

#Task 1
for i in range(1,6):
    print()
    for j in range(0,i):
        print(j+1, end="")

# #Task 2
for i in range(1,6):
    print()
    for j in range(5):
        print(5,end=" ")
for i in range(1,5):
    print()
    for j in range(5):
        print(4,end=" ")
for i in range(1,4):
    print()
    for j in range(5):
        print(3,end=" ")

for i in range(1,3):
    print()
    for j in range(5):
        print(2,end=" ")

for i in range(1,2):
    print()
    for j in range(5):
        print(1,end=" ")


#Task 3

my_list=[8,5,45,65,95,745,5,551]
for i in range(5):
    print(max(my_list))
    my_list.remove(max(my_list))

# Task 4

a=[50,50,50,50,50]
avg=sum(a)/len(a)
print(avg)


