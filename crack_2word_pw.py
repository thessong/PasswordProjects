import time, sys, getpass

args = sys.argv[1:]
silent = False
sym = False
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

symbols = "?!%"
#symbols = "!@#$%^&*()_-+=?/.,<>:;~`"

start = time.time()
guesses = 0

dictionary = open("dictionary.txt", "r")
dictionary2 = open("dictionary.txt", "r")
guesed = False 
i = 0
for word in dictionary:
    dictionary2.seek(0,0)
    for other in dictionary2:
        word = word.strip()
        other = other.strip()
        guesses += 1
        if (word + other) == password:
            if silent == True:
                word = "*****"
                other = ""
            print("The password of \"%s\" was guessed in %s tries and %s seconds!") % (word + other, str(guesses), str(time.time() - start))
            guesed = True
        if sym == True:
            for char in symbols:
                guesses += 1
                if (word + other + char) == password:
                    if silent == True:
                        word = "*****"
                        other = ""
                        char = ""
                    print("The password of \"%s\" was guessed in %s tries and %s seconds!") % (word+other+char, str(guesses), str(time.time() - start))
                    guesed = True
                    break
        if guesed == True:
            break
    if guesed == True:
        break
if guesed != True:
        print("Your password was not guessed!")
dictionary.close()
dictionary2.close()