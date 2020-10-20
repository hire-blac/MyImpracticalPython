'''day3 of 100DaysOfCode
a program to test a syllable counting program 
against random words in a dictionary file
'''
import sys
import random
import count_syllables
import load_dictionary

words = load_dictionary.load('2of4brif.txt')

def main():

	while True:
		
		missing = []

		num_of_words = input('\nNumber of words from dictionary to test\nor press Enter to exit: ')
		if num_of_words == '':
			sys.exit()
		if num_of_words.isdigit():
			for i in range(int(num_of_words)):
				test_word = words[random.randint(0, len(words))]
				try:
					num_syllables = count_syllables.count_syllables(test_word)
					print('{} : {}'.format(test_word, num_syllables))
				except KeyError:
					missing.append(test_word)
					print('"{}" not found!!!'.format(test_word), file=sys.stderr)
			
			print('\nwords not found:')
			for i in missing:
				print(i)
			print('number not found: {}'.format(len(missing)))

		else:
			print('NOT AN INTEGER!!!', file=sys.stderr)
			continue

if __name__ == '__main__':
	main()