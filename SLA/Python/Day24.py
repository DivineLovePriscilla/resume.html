
import datetime
class start_app():
    def __init__(self):
        self.start_time=datetime.datetime.now()
        self.start_hour=self.start_time.hour
        self.start_minute=self.start_time.minute
        self.start_seconds=self.start_time.second
        print(self.start_hour,self.start_minute)
        self.start()
    def start(self):
        self.data=[]
        while True:
            enter_data=input("Enter data to add")
            self.data.append(enter_data)
            again_data=input("If you want to add data again, type, else type s")
            if(again_data=="s"):
                end_time=datetime.datetime.now()
                end_hour=end_time.hour
                end_minute=end_time.minute
                end_seconds=end_time.second
                print(f"{end_hour-self.start_hour} hours, {end_minute-self.start_minute} minutes you stayed in function or loop")
                break
            else:
                continue
            

user_input=input("Enter the data start")
if user_input=="start":
    my_obj=start_app()
