a = [1, 2, 4]
b = a #It will not affect a because this is just saying that b is another way to name the list

input: a list of ints
output: an int
def update_list(a_list): #I predict that 4 will be replaced with "yo" and 5 will be replaced with 100
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list) #4 was replaced with "yo", index 4 was not replaced with 100
print my_list #variable b went from pointing to index 4 to then having it's value be equal to 100 so it won't change anything



var_1 = "kittens" #global
var_2 = "cookies" #global
# input: a string
# output: a string
def my_function(my_favorite_things): #global
    song_lyrics = "rain drops on roses," #local
    combined_song = song_lyrics + my_favorite_things #local
    return combined_song #local
# input: a string
# output: a string
def my_function_2(item, item2): #global
    full_lyrics = item + "on " + item2 #local
    full_song = my_function(full_lyrics) #local
    return full_song #local
my_song = my_function_2(var_1, var_2)

var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    elif favorite_pet == var_2: #I just changed the if to an elif
        print("My favorite pet is the dog.")
    var_2 = "cat"

print_out_my_favorite(var_1)
print(var_2)

my_num= 4
# add2= str(my_num) + 2
def multiply_num(multiplier):
    my_num= 
    print my_num
multiply_num(3)

