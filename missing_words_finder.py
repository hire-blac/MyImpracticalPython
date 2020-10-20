'''day2 of 100DaysOfCode
a program that counts the number of syllables in an English word or phrase

Find missing words from CMUdict and prepare a dictionary of the word 
with their syllable count as the the dictionary values

'''
import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()	#Carnegie Mellon University Pronouncing Dictionary

def main():
	haiku = load_haiku('train.txt')
	exceptions = cmudict_missing(haiku)

	build_dict = input('\nManually build an exceptions dictionary (y/n)? \n')
	if build_dict.lower() == 'n':
		sys.exit()
	else:
		missing_words_dict = make_exceptions_dict(exceptions)
		save_exceptions(missing_words_dict)

def load_haiku(filename):
	'''open and return training corpus of haiku as a set'''
	with open(filename) as in_file:
		haiku = set(in_file.read().replace('-', ' ').split())
		return haiku

def cmudict_missing(word_set):
	'''find and return words in word set missing from cmudict'''
	exceptions = set()
	for word in word_set:
		word = word.lower().strip(punctuation)
		if word.endswith("'s") or word.endswith("'s"):
			word = word[:-2]
		if word not in cmudict:
			exceptions.add(word)
	print('\nexceptions:')
	print(*exceptions, sep='\n')
	print('\nNumber of unique words in haiku corpus = {}'
				.format(len(word_set)))
	print('Number of words in corpus not in cmudict = {}'
				.format(len(exceptions)))
	membership = (1 - (len(exceptions) / len(word_set))) * 100
	print('cmudict membership = {:.1f}{}'.format(membership, '%'))
	return exceptions

def make_exceptions_dict(exceptions_set):
	'''Return dictionary of words and syllable counts from a set of words'''
	missing_words = {}
	print('Input # syllables in word. Mistakes can be corrected at end. \n')
	for word in exceptions_set:
		while True:
			num_sylls = input('Enter number syllables in {}: '.format(word))
			if num_sylls.isdigit():
				break
			else:
				print('			Not a valid answer!', file=sys.stderr)
		missing_words[word] = int(num_sylls)
	print()
	pprint.pprint(missing_words, width=1)

	print('\nMake changes to dictionary before saving?')
	print('''
		0 - Exit and Save
		1 - Add a word or change a syllable count
		2 - Remove a word
		''')

	while True:
		choice = input('\nEnter choice: ')
		if choice == '0':
			break
		elif choice == '1':
			word = input('\nWord to add or change: ')
			missing_words[word] = int(input('Enter number of syllables in {}:'
										.format(word)))
		elif choice == '2':
			word = input('\nEnter word to delete: ')
			missing_words.pop(word, None)

	print('\nNew words or syllable changes:')
	pprint.pprint(missing_words, width=1)

	return missing_words

def save_exceptions(missing_words):
	'''save exceptions dictionary as json file'''
	json_string = json.dumps(missing_words)
	f = open('missing_words.json', 'w')
	f.write(json_string)
	f.close()
	print('\nFile saved as missing_words.json')

if __name__ == '__main__':
	main()