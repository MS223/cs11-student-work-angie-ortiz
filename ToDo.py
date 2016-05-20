action= raw_input("What would you like to do? ")
day= raw_input("What day? ").capitalize()
days_of_week= {
'Monday': [],
'Tuesday':[],
'Wednesday':[],
'Thursday':[],
'Friday':[],
'Saturday':[],
'Sunday':[],
}

def add():
    days_of_week[day].append(action)


print days_of_week

#not adding anything

    #days_of_week[day]=action


    #should get our action variable and add it to our dictionary with the key day


