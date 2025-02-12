class Time:
    def __init__(self,hour=0,min=0,sec=0):
        self.hours = hour
        self.minutes = min
        self.seconds = sec

    def get_time(self):
        return(f"{self.hours} hours,{self.minutes} minutes,{self.seconds}seconds")

    def add(self,other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds

        if total_seconds >= 60:
            total_seconds-=60
            total_minutes+=1
        if total_minutes >=60:
            total_minutes-=60
            total_hours+=1

        return Time(total_hours,total_minutes,total_seconds)
time1 = Time(2,40,14)
time2 =Time(1,30,50)
time3 = time1.add(time2)
print(f"Time 1 is {time1.get_time()}\nTime 2 is {time2.get_time()}\nTotal time {time3.get_time()}")