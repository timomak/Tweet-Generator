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

def tuple_histogram(array):
    list = []
    for word in array:
        found = False
        for inner_tuple in list:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                list.remove(inner_tuple)
                list.append((word, count))
                found = True
                break
        if not found:
            list.append((word, 1))
    return list


def histogram(array):
    list = []
    for word in array:
        found = False
        for inner_list in list:
            if word == inner_list[0]:
                inner_list[1] += 1
                found = True
                break
        if not found:
            list.append([word, 1])
    return list


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


# print open_file('text.txt')
# print histogram(open_file('text.txt'))
# print tuple_histogram(open_file('text.txt'))
