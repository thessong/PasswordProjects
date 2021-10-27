import sys, time, getpass

dictionary = open('common_passwords.txt', 'r')
args=sys.argv

try:
	passw = args[1]
except:
	passw = getpass.getpass()

x = 0
start = time.time()

for word in dictionary:
	password = word.strip()
	if (passw == password):
		print("Your password was found!")
		print('Time taken: {} seconds'.format(time.time() - start))
		x = 1
		break

if x != 1:
	print("Your password was NOT found!")
