# import re
# data=input("Enter the data to check the pattern\n")
# pattern=r'^[^\d]*$'  #\d is for alphabet
# result=re.match(pattern,data)
# if result:
#     print("Pattern matched")
# else:
#     print("Pattern not matched")


# url validation
# email validation

print('\n'.join(
    [''.join(
        [('Divinelove'[(x - y) % 8]  
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) * 3 - (x * 0.05) * 2 * (y * 0.1) ** 3 <= 0 else '')
            for x in range(-30, 30)])  
        for y in range(15, -15, -1)])) 



