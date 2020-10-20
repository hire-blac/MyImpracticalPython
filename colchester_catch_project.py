'''day6 of 100DaysOfCode
a program that takes an input n and checks and 
displays a null cipher based on the nth letter 
after the start of every nth word'''
import string

def solve_cipher(n, message):
	'''solve a null cipher based on the nth letter after the start of every nth word'''
	plaintext = ''
	for i in range(n - 1, len(message) + 1, n):
		trauncated_message = ''.join(message.split()[i:])
		if len(trauncated_message) >= n:
			plaintext += trauncated_message[n - 1]

	print('\nPlaintext using {} as key = {}'.format(n, plaintext))

def main():
	'''request message from user and solve null cipher'''
	message = input('\nType the message to be decrypted: ')

	while True:
		key = input('\nInput a key to use (MUST BE AN INTEGER AND > 0): ')
		if key in string.ascii_letters:
			print('IVALID KEY!!!(MUST BE AN INTEGER)')
			continue
		else:
			key = int(key)
			if key < 1:
				print('INVALID KEY!!! (MUST BE > 0)')
				continue
			else:
				solve_cipher(key, message)

		try_again = input('\nPress Enter to try another key or press any other key to cancel: ')
		if try_again != '':
			break

if __name__ == '__main__':
	main()