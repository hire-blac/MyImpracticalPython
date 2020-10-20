'''day19 of 100DaysOfCode
A program using recursion to determine whether a word is a palindrome'''
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

def is_palindrome(word):

	palindrome = 0

	if len(word) <= 1:
		palindrome = 1
		return palindrome

	elif word[0] == word[len(word)-1]:
		palindrome = is_palindrome(word[1:len(word)-1])
		return palindrome

	else:
		palindrome = -1
		return palindrome

def find_palindrome():
	'''find palingrams in dictionary.'''
	pali_list = []
	words = set(word_list)

	for word in words:
		is_pali = is_palindrome(word)
		if is_pali == 1:
			pali_list.append(word)

	return pali_list
	
def main():
	find_palindrome()

	palindromes = find_palindrome()

	#sort palindrome on first word
	palindromes_sorted = sorted(palindromes)

	#display list of palindromes
	print('\nNumber of palindromes = {}\n'.format(len(palindromes_sorted)))
	for word in palindromes_sorted:
		print(word,'\n')


if __name__ == '__main__':
	main()