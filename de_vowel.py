#This function takes a string as an input and returns a copy of the string with the vowels removed
# user= raw_input("Type word: ")
def de_vowel(a_string):
    for n in a_string:
        if n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != 'u':
            print n
print de_vowel("laughing")
# no_vowels = de_vowel("This sentence has no vowels")
# print(no_vowels)

#how do I get it back into a sentence?
