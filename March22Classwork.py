#write a for loop to print only odd numbers
list = [3,4,7,13,54,32,653,256,1,41,65,83,92,31]
def odd_sum(input): #adding odd numbers
    odd_list=[]
    for x in list:
        if x % 2 == 1:
            odd_list.append(x)
    print sum(odd_list)

odd_sum(list)


def even_sum(input): #adding even numbers
    even_list=[]
    for x in list:
        if x % 2 == 0:
            even_list.append(x)
    print sum(even_list)
even_sum(list)
