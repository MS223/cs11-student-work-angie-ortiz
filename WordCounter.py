text_input= raw_input("Paste your text here: ")
text_input= text_input.lower()
text_input= text_input.replace(".", " ")
text_input = text_input.split()
print text_input
words = raw_input("Paste the word(s) you are looking for: ")
my_dictionary= {

}
my_dictionary['word count'] = text_input.count(words)
print my_dictionary
 
 #still not done
 #have to chage the key
 #search more than one word
