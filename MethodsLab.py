class Time(object):
    def __init__(self, hour, minute, second):
     self.hour = hour
     self.minute = minute
     self.second = second

    def __str__ (self):
        return str(self.hour)+ ":" + str(self.minute) + ":" + str(self.second)



    def __add__(self,other):
        return Time(self.hour+other.hour ,self.minute+other.minute, self.second+other.second) #more efficient way to add

    # def __add__(self,other):
    #     return str(self.hour+other.hour)+ ":" + str(self.minute+other.minute) + ":" + str(self.second+other.second) #self refers to time 1 and other refers to time 2


time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)
time3 = Time(6,20,13)
print time1
print time2
print time1 + time2 + time3 #I can add as many things as I want
