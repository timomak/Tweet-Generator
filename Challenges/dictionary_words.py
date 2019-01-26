import random, sys

wordList = [line.strip() for line in open('/usr/share/dict/words')]
sentence = []

if __name__ == '__main__':
    parameters = sys.argv[1:]
    counter = 0
    while counter != int(parameters[0]):
        sentence.append(wordList[random.randint(0, len(wordList) - 1)])
        counter += 1
    print(" ".join(sentence))
