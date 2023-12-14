# import csv

# with open('./data.csv','r') as file:
#     csv_reader=csv.reader(file)
#     data=[val for val in csv_reader]

# data[0][0]="user_name"

# with open('./data.csv','w',newline='') as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerows(data)

my_tuple=("r\n","a\n","m\n")
a="".join(my_tuple)
print(a)