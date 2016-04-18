def is_even(x): #I tested with 6 and I got back true
    if x%2==0:
        return True
    else:
        return False
is_even(6)

def is_int(x): #I tested with 2.5 and I got back false
    if x== int(x):
        return True
    else:
        return False
is_int(2.5)
