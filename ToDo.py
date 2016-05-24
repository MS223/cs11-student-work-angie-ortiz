days_of_week= {
'Monday': [],
'Tuesday':[],
'Wednesday':[],
'Thursday':[],
'Friday':[],
'Saturday':[],
'Sunday':[],
}

def get(day):
    print days_of_week[day]


def add(action, day):
    days_of_week[day].append(action)


def choice():
    user_choice= "" #had to make them local variables
    action= ""
    day= ""
    while user_choice != "exit": #once I type exit it will stop
        user_choice= raw_input("How may I help you?" )
        if user_choice == "add":
            action= raw_input("What would you like to do? ")
            day= raw_input("What day? ").capitalize()
            add(action,day)
        elif user_choice == "get":
            day= raw_input("What day? ").capitalize()
            get(day)


choice()







