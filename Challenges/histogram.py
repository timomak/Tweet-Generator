def open_file(file):
    array = []
    with open(file, 'r') as f:
	       file_content = f.read()
	       array = [line.replace(",", "").replace(".", "") for line in file_content.lower().split()]
    for string in array:
        if string == '':
            array.remove(string)
    return array

def dict_histogram(array):
    histogram = {}

    for word in array:
		if word in histogram.keys():
			histogram[word] += 1
		else:
			histogram[word] = 1
    return histogram

def tuple_histogram(histogram):
    tuple_histogram = []
    for array in histogram:
        tuple_histogram.append(tuple(array))
    return tuple_histogram




# Works properly
def histogram(array):
    histogram = []
    for index in range(len(array)):
        found_word = False
        if histogram:
            for counter in range(len(histogram)):
                if histogram[counter][0] == array[index]:
                    histogram[counter][1] += 1
                    found_word = True
                    break
            if found_word == False:
                histogram.append([array[index], 1])
        else:
            histogram.append([array[index], 1])
    return histogram

def unique_words(histogram):
    array = []
    for i in range(len(histogram)):
        if histogram[i][1] == 1:
             array.append(histogram[i][0])
    return array

def frequency(word, histogram):
    frequency = 0
    found = False
    for i in range(len(histogram)):
        if histogram[i][0] == word:
            found = True
            return histogram[i][1]
    if found == False:
        return 0

print tuple_histogram(histogram(open_file('hello')))
# print (open_file('hello'))
# print histogram(array)
# print unique_words(histogram(array))
# print frequency("one", histogram(array))
# print frequency("four", histogram(array))
