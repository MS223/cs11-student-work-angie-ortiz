vowels= ['a','e', 'i', 'o', 'u']
sentence= raw_input("Give me a sentence:").lower() #won't have a problem with capitalized sentences
for x in sentence:
    if x in vowels:
        sentence=sentence.replace(x,'') #I made the mistake of printing sentence.replace(x,'') immediately
print sentence #
