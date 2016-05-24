class Color(object):
    """Represents a color"""

first_color= Color() #tomato
first_color.red= 255
first_color.green= 99
first_color.blue= 71

second_color= Color() #olive drab
second_color.red= 107
second_color.green= 142
second_color.blue= 35

third_color= Color() #orchid
third_color.red= 218
third_color.green= 112
third_color.blue= 214

def add_color(first_color,second_color):
    print sum(first_color.red/2, second_color.red/2)

add_color(first_color,second_color)
