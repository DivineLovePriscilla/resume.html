#id - inbuilt function
# a=5
# b=5
# print(id(a))
# print(id(b))

# def some_data(a,b):
#     '''
#     This function gets the two parameters and adds it and returns the value
#     '''
#     return a+b
# print(some_data(15,5))
# print(some_data.__doc__)

# a="Divine"
# print(id(a))

#Date time module
# import datetime
# get_current_time=datetime.datetime.now()
# print(get_current_time)

# current_time=datetime.date.today()
# print(current_time)

# current_day=datetime.date.today()
# print(current_day)

# initial_date=datetime.date(2023,6,30)
# end_date=datetime.date(2023,7,15)
# between_days=initial_date-end_date
# print(between_days)

# get_current_time=datetime.datetime.now().time()
# print(get_current_time)

import time
current_count = 0

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Login Time: {current_time}")
    a=2
    b=5
    print(a+b)
    current_count += 1
    time.sleep(3)
    break
Logout_time=time.strftime("%Y-%m-%d %H:%M:%S")
print("Logout time is",Logout_time)
