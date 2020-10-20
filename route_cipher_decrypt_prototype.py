'''day1 of 100DaysOfCode
a simple route cipher decryption program'''

ciphertext = '16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'

#split elements into words, not letters

cipherlist = list(ciphertext.split())

#initialise varibles
COLS = 4
ROWS = 5
key = '-1 2 -3 4' #neg number means read up column vs down
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

#turn key into list of integers
key_int = [int(i) for i in key.split()]

#turn columns ito items in list of lists:
for k in key_int:
	if k < 0: #reading from bottom-to-top
		col_items = cipherlist[start:stop]
	elif k > 0: #reading from top-to-bottom
		col_items = list((reversed(cipherlist[start:stop])))
	translation_matrix[abs(k) - 1] = col_items
	start += ROWS
	stop += ROWS

print('\nciphertext = {}'.format(ciphertext))
print('\ntranslation matrix =', *translation_matrix, sep='\n')
print('\nkey kength = {}'.format(len(key_int)))

#loop through nested list popping off last item to new list
for i in range(ROWS):
	for col_items in translation_matrix:
		word = str(col_items.pop())
		plaintext += word + ' '

print('\nplaintext = {}'.format(plaintext))