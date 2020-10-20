'''a simple 'Pig Latin' program
day15 of 100DaysOfCode'''

def main():
	'''main function to recieve input form user and
	convert to pig latin'''

	vowels = ['a', 'e', 'i', 'o', 'u']
	message = input('Enter a word or sentence to be translated to Pig Latin:\n')
	translation = ''

	for word in message.split():
		if len(word) <= 2:
			translation += word + ' '

		elif word[0].lower() in vowels:
			translation += word + 'way '

		else:
			new_word = word[1:]
			translation += new_word + word[0] + 'ay '

	print(translation)
	print('\n')

if __name__ == '__main__':
	main()