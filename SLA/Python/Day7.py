# temp=2
# for i in range(0,10):
#     print(i+temp)
#     temp+=1

# temp=1
# for i in range(0,10):

#     print(i+temp)
#     temp+=1
#Multiple values
# a,b,c=2,3,4

my_list=["apple", "mango", "banana", "dragon fruit"]
my_list.append("kiwi")
print(my_list)

my_list.remove("kiwi")
print(my_list)

my_list.insert(1,"kiwi")
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

my_tuple=("apple", "mango", "banana", "dragon fruit")
my_list=list(my_tuple)
my_list.append("kiwi")
my_tuple=tuple(my_list)
print(my_tuple)


    