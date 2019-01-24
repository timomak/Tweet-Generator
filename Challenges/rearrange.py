import random, sys

def rearrange(array):
    array2 = []
    counter = 0
    while counter != len(array):
        temporary_num = random.randint(0, len(array) - 1)
        array2.append(array[temporary_num])
        array.pop(temporary_num)
    print (array2)


if __name__ == '__main__':
    parameters = sys.argv[1:]
    rearrange(parameters)
