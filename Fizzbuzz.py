for groot in range(1,101): #this will give me numbers from 1-100
    if groot % 3 == 0 + groot % 5==0: #this makes the computer check for multiples of 3 and 5
        print "fizzbuzz" #it will replace the multiple with "fizzbuzz"
    elif groot % 5 == 0: #it took me a while to realize that I needed an elif
        print "buzz"
    elif groot % 3 ==0: #this checks for a multiple of 3 only
        print "fizz"
    else:
        print groot #this calls the function

