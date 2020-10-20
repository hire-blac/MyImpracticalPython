'''day6 of 100DaysOfCode
a program that embeds a null cipher within 
a list of dictionary wordsunder the deception of vocabulary training
'''
from random import randint
import string
import load_dictionary

#write a short message that doesnt contain punctuation or numbers
input_message = 'panel at east end of chapel slides open'

message = ''
for char in input_message:
	if char in string.ascii_letters:
		message += char
print(message, '\n')
message = ''.join(message.split())

#open dictionary file
word_list = load_dictionary.load('2of4brif.txt')

#build vocabulary word list with hidden message
vocab_list = []
for letter in message:
	size = randint(6, 15)
	for word in word_list:
		if len(word) == size and word[2].lower() == letter.lower()\
				and word not in vocab_list:
			vocab_list.append(word)
			break

if len(vocab_list) < len(message):
	print('Word list is too small. Try larger dictionary or shorter message')
else:
	print('vocabulary words for ujnit 1: \n', *vocab_list, sep='\n')