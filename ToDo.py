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


def choice():
    user_choice= raw_input("How may I help you?" )
    if user_choice == "add":
action= raw_input("What would you like to do? ")
day= raw_input("What day? ").capitalize()
print add(action,day)
else:
print get(day)

def add(action, day):
    days_of_week[day].append(action)
#i need an option to call choice
add(action, day)

# print days_of_week

def get(day):
    print days_of_week[day]

get(day)

print days_of_week
#i need an option to call choice


def choice():
    user_choice= raw_input("How may I help you?" )
    if user_choice == add:
        print days_of_week
    else:
        print get(day)
    # if they chose add call add
    #if the choose get call get
#not adding anything

    #days_of_week[day]=action


    #should get our action variable and add it to our dictionary with the key day


