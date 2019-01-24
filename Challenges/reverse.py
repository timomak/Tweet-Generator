import random, sys

def reverse(word):
    counter = 0
    newWord = ""
    while counter != len(word):
        temp_word = word[counter] + newWord
        newWord = temp_word
        counter += 1
    print(newWord)

if __name__ == '__main__':
    parameters = sys.argv[1:]
    for word in parameters:
        reverse(word)
