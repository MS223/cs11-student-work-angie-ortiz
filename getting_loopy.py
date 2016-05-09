fruit= raw_input("Give me a fruit: ")
def fruit_pluralizer(x): #removed the for loop and replaced the initial parameter in fruit_pluralizer to x
    # for x in fruit:
        if x[len(x)-1] == "y":
            print x[:len(x)-1] + "ies"
        else:
            print x[:len(x)] + "s"
fruit_pluralizer(fruit)
#I have to call it to check if it works
