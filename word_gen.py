from random import randrange
import sys

def file_to_list(filename, extension=".txt"):
    f = open((filename+extension), "r")
    data = (f.read()).split("\n")
    f.close
    return data

args = sys.argv[1:]
data = file_to_list("random_words")
length = len(data)
symbols = "!@#$%^&*+=?"

if ("-w" in args):
        find = True
        while find == True:
                if (raw_input("Do you want a random word? (y/n): ").lower() == "y"):
                        num = randrange(0, (length-1))
                        random_word = data[num]
                        print(random_word)
                else:
                        print("Bye!")
                        find = False
else:
        find = True
        while find == True:
                if (raw_input("Do you want a random password? (y/n): ").lower() == "y"):
                        word1 = randrange(0, (length-1))
                        word2 = randrange(0, (length-1))
                        number = randrange(0, 20)
                        symbol = randrange(0, (len(symbols)-1))
                        final = list(data[word1] + data[word2])
                        num_placement = randrange(0, (len(final)-1))
                        final.insert(num_placement, str(number))
                        symbol_placement = randrange(0, (len(final)-1))
                        final.insert(symbol_placement, symbols[symbol])
                        print("".join(final))
                else:
                        print("Bye!")
                        find = False
