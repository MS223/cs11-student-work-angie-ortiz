integer= input("Give me an integer:") #this was easy
max_value= range(1,integer +1)
print max_value

list1 = [4,5,15,11,23,42]
list2 = [1,8,7,16,7,35]
def compare_lists(list1,list2): #there are two lists so I have to set both lists as the parameter
    for x in list1:
        if x> list2[list1.index(x)]: #.index finds an element at the index
            print x
        else:
            print list2[list1.index(x)]

compare_lists(list1,list2)


swapping_stars= input("How wide?")
height= input("How tall?")
for x in range(0,height):
    print swapping_stars * "* -"
