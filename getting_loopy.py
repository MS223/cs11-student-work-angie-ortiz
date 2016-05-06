fruit= raw_input("Give me a fruit: ")
def fruit_pluralizer(list_of_strings):
    for x in fruit:
        if x[len(x)-1] + "ies":
            print x[:len(x)-1] + "ies"
    else:
        print x[:len(x)] + "s"

#I have to call it to check if it works
