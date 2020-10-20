'''day15 of 100DaysOfCode
a simple program to print a poor man's bar chart showing
the frequency of letters in a sentence'''

def main():
	'''main function'''
	frequency = {'a' : [], 'b' : [], 'c' : [], 'd' : [], 'e' : [], 'f' : [],
		    'g' : [], 'h' : [], 'i' : [], 'j' : [], 'k' : [], 'l' : [], 'm' : [],
			'n' : [], 'o' : [], 'p' : [], 'q' : [], 'r' : [], 's' : [], 't' : [],
			'u' : [], 'v' : [], 'w' : [], 'x' : [], 'y' : [], 'z' : []}

	text = input('Please type in a text:\n')
	print()

	#loop through the text
	for word in text.split():
		for letter in word:
			frequency[letter.lower()].append(str(letter.lower()))

	for item in frequency.items():
		print(item)
	print()

if __name__ == '__main__':
	main()