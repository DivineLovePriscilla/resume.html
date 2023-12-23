#1. Print list of numbers in all possible combinations

# l=[1,2,3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if(i!=j and j!=k and i!=k):
#                 print(l[i],l[j],l[k])

# l=[1,2,3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(i,j,k)

#2. Print name in all possible combinations

# from itertools import permutations
# a="Priscilla"
# comb=permutations([i for i in a],len(a))
# print("The combination of name is: ")
# for j in comb:
#     print(j)

# from itertools import permutations
# name=input('enter name:')
# name_combinations=permutations([i for i in name],len(name))
# print('all possible combinations of',name,'is:')
# print('---------------------------------------')
# for j in name_combinations:
#     print(j)

# N=input("Enter the number ").split(" ")
# print(N)

# i/p=4 5 6 7 4 

#3.Write a Python function that takes an array of integers as input and removes all duplicates, returning a new array with unique elements. You should not use any built-in library functions or data structures like sets


# def remove_dup(arr_of_int):
#     store=[]
#     for i in arr_of_int:
#         if i not in store:
#             store.append(i)
#     return store
# arr_of_int=[2,2,5,6,7,9,9,2,5]
# print(remove_dup(arr_of_int))

#4.Write a Python function to shuffle the characters of a given string. The shuffling should be random and not follow any specific pattern. You can use Python's built-in random module for shuffling.
# import random
# def shuffled_string(input_string):
#     #char_list=input_string.split()
#     #print(char_list)
#     char_list=list(input_string)
#     #print(char_list)
#     random.shuffle(char_list)
#     shuffled_str=''.join(char_list)
#     print(shuffled_str)

# input_string="Priscilla"
# (shuffled_string(input_string))

#5.Write a Python function that counts the number of words in a given sentence.

# def num_of_words(sentence):
#     words=sentence.split()
#     cnt=len(words)
#     print(cnt)
# # sentence="I am a beautiful girl"
# num_of_words(sentence="I am a beautiful girl")


#6. Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing.

a=[1,2,3,6,7,8,9]
b=[]
for i in range(a[0],a[-1]+1):
    if i not in a:
        b.append(i)
        print(b)






    