'''day3 of 100DaysOfCode
Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption begins at either the top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start from top and read down.

Example below is for a 4X4 matrix with key -1 2 -3 4.
Note '0' is not allowed.
Arrows show encryption route; for negative key values, read up.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_| 
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext'''

import sys

def validate_col_row(cipherlist):
	'''Check that input columns and rows are valid vs. message length'''
	factors = []
	len_cipher = len(cipherlist)
	for i in range(2, len_cipher): #range excludes 1-column ciphers
		if len_cipher % i == 0:
			factors.append(i)
	print('\nLength of cipher = {}'.format(len_cipher))
	print('Acceptable column/row values include: {}'.format(factors))
	print()

	#input rows and columns
	rows = int(input('Select a nuber of rows: '))
	cols = int(input('Select a nuber of columns: '))

	if rows * cols != len_cipher:
		print('\nError - Input columns & rows not factors of length ',
				'of cipher. Terminating program.', file=sys.stderr)
		sys.exit(1)
		
	return cols, rows

def generate_key(cols, i):
	'''generate possible key list based on number of columns'''
	key_list = [n for n in range(1, cols+1)]
	key = []

	if i > 1:
		for num in range(len(key_list)):
			key.append(key_list.pop())
		if i%2 == 0:
			for a in range(0, len(key), 2):
				key[a] = -key[a]
		else:
			for a in range(1, len(key), 2):
				key[a] = -key[a]
	else:
		key = key_list
		if i%2 == 0:
			for a in range(0, len(key), 2):
				key[a] = -key[a]
		else:
			for a in range(1, len(key), 2):
				key[a] = -key[a]

	return key

def build_matrix(key_int, cipherlist, cols, rows):
	'''Turn every n items in a list into a new item in a list of lists.'''
	translation_matrix = [None] * cols
	start = 0
	stop = rows
	for k in key_int:
		if k < 0: #read bottom-to-top of column
			col_items = cipherlist[start:stop]
		elif k > 0: #read top-to-bottom of column
			col_items = list((reversed(cipherlist[start:stop])))
		translation_matrix[abs(k) - 1] = col_items
		start += rows
		stop += rows

	return translation_matrix

def decrypt(translation_matrix, rows):
	'''Loop through nested lists popping off last items to a string.'''
	plaintext = ''
	for i in range(rows):
		for matrix_col in translation_matrix:
			word = str(matrix_col.pop())
			plaintext += word + ' '
	return plaintext

def main():
	'''Run program and print decrypted plaintext.'''
	ciphertext = input('\nEnter the ciphertext to be decrypted: ')

	#split elements into words, not letters
	cipherlist = list(ciphertext.split())
	while True:
		cols, rows = validate_col_row(cipherlist)
		print('\nTrying {} rows and {} columns'.format(rows, cols))

		for i in range(4):
			key_int = generate_key(cols, i)
			print('\nTrying key = {}'.format(key_int))

			translation_matrix = build_matrix(key_int, cipherlist, cols, rows)
			plaintext = decrypt(translation_matrix, rows)

			print('\nPlaintext = {}'.format(plaintext))

		try_again = input('\nPress "y" to try another Row/Column combination\nOr any other key to cancel: ')
		if try_again != 'y':
			break

if __name__ == '__main__':
	main()