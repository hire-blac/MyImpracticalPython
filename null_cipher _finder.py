'''day6 of 100DaysOfCode
a simple program using thr trevanion cipher 
to find hidden message in a text file'''
import sys
import string

def load_text_file(file):
	'''load a text file as a string'''
	with open(file) as f:
		return f.read().strip()

def solve_null_cipher(message, lookahead):
	'''solve a null cipher based on number of letters after a punctuation mark

	message = null ciphertext as string stripped of whitespaces
	lookahead = endpoint of range of letters after punctuation mark to examine
	'''
	for i in range(1, lookahead + 1):
		plaintext = ''
		count = 0
		found_first = False
		for char in message:
			if char in string.punctuation:
				count = 0
				found_first = True
			elif found_first is True:
				count += 1
			if count == i:
				plaintext += char

		print('Using offset of {} after punctuation = {}'.format(i, plaintext))
	print()

def main():
	'''load text, solve null cipher'''
	#load and process message
	filename = input('\nEnter full filename for message to translate: ')
	try:
		loaded_message = load_text_file(filename)
	except IOError as e:
		print('{}. Terminating program.'.format(e), file=sys.stderr)
		sys.exit(1)
	print('\nOriginal message =')
	print('{}'.format(loaded_message), '\n')
	print('\nList of puctuation marks to check = {}'.format(string.puctuation), '\n')

	#remove whitespaces
	message = ''.join(loaded_message.split())

	#get range of possible cipher keys from user
	while True:
		lookahead = input('\nNumber of letters to check after punctuation mark: ')
		if lookahead.isdigit():
			lookahead = int(lookahead)
			break
		else:
			print('Please input a number: ', file=sys.stderr)
	print()

	#run function to decode cipher
	solve_null_cipher(message, lookahead)

if __name__=='__main__':
	main()