For each example below, predict what will be printed. Then, run the code and confirm your prediction.

a = 0
while a< 100:
	print a
"""
Prediction: It will print out infinity
Observation: It printed out 0's infinity amount of times and it crashed.
 """
a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: It will add one to every number being printed until 100.
Observation: I was correct.
 """

a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction: The statement "Would you like to quit" will eventually pop up.
Observation: It printed "Would you like to quit:" and whether you typed in yes or no it will continue to say "Would you like to quit:"
 """


