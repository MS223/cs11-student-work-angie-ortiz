my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print my_dictionary
print my_dictionary['dog']
print my_dictionary.get('dog')
print 'cat' in my_dictionary
print 'monkey' in my_dictionary
print my_dictionary['chair']
print my_dictionary['kittens']

# What prints? A list of the elements of my_dictionary prints. As well as the statement "a domestic canine" and true/false phrases
# What type1 is my_dictionary? A dictionary
# Add a line of code that will print the definition of chair, then run the code again.
# What happens if you use my_dictionary['kittens']? What do you think that error means? The error means that the key 'kitten' is not defined.
