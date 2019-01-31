import random, sys

def rearrange(array):
    array2 = []
    counter = 0
    while counter != len(array):
        temporary_num = random.randint(0, len(array) - 1)
        array2.append(array[temporary_num])
        array.pop(temporary_num)
    return array2

def ultimate_rearrange():
    sentence = input("Your sentence to rearrange: ")
    array = sentence.split(" ")
    counter = 0
    rearranged = array
    while counter != random.randint(1, 10):
        rearranged = rearrange(rearranged)
        counter += 1
    rearranged3 = (" ").join(rearranged)
    rearranged2 = rearranged3.lower()
    newSentense = rearranged2.capitalize()
    newSentense += "."
    print(("\033[1;32;40m {0} \n").format(newSentense))

if __name__ == '__main__':
    # parameters = sys.argv[1:]
    # rearrange(parameters)
    ultimate_rearrange()
