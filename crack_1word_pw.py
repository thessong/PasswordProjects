import sys, time, itertools, getpass

# Brute force function
def tryPassword(passwordSet, stringTypeSet):
    chars = stringTypeSet
    attempts = 0
    for i in range(1, len(passwordSet)+1):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if letter == passwordSet:
                end = time.time()
                return attempts, end

symbols = "?!%"
#symbols = "!@#$%^&*()_-+=?/.,<>:;~`"

args = sys.argv[1:]
brute = False
silent = False
sym = False
if ("-c" in args):
        brute = True
        args.remove("-c")
if ("-v" in args):
        silent = True
        args.remove("-v")
if ("-s" in args):
        sym = True
        args.remove("-s")
try:
	password = args.pop(0)
except:
	password = getpass.getpass()
if len(args) > 0:
        raise TypeError("Argument not supported")
if brute == False:
        password = password.lower()

start = time.time()
guesses = 0

dictionary = open("dictionary.txt", "r")

guesed = False
for word in dictionary:
        word = word.strip()
        guesses += 1
        if word == password:
                if silent == True:
                        word = "*****"
                print("The password of \"%s\" was guessed in %s tries and %s seconds!") % (word, str(guesses), str(time.time() - start))
                guesed = True
        if sym == True:
                for char in symbols:
                        guesses += 1
                        if (word + char) == password:
                                if silent == True:
                                        word = "*****"
                                        char = ""
                                print("The password of \"%s\" was guessed in %s tries and %s seconds!") % (word+char, str(guesses), str(time.time() - start))
                                guesed = True
                                break
        if guesed == True:
                break
if (guesed != True) and (brute == True):
        stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~?!@#$%^&*()_-+=[{]}>"
        tries, timeAmount = tryPassword(password, stringType)
        guesses += tries
        if silent == True:
                password = "*****"
        print("Cracked the password \"%s\" in %s tries and %s seconds!") % (password, guesses, (timeAmount-start))
elif guesed != True:
        print("Your password was not guessed!")