from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
        return create_sentence(histogram(open_file("text.txt")))

def open_file(file):
    array = []
    with open(file, 'r') as f:
	       file_content = f.read()
	       array = [line.replace(",", "").replace(".", "").replace("\"", "").replace("?", "").replace("!", "") for line in file_content.lower().split()]
    for string in array:
        if string == '':
            array.remove(string)
    return array


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

def word_selection(histogram):
    total_sum = 0
    cumulative_prob = 0.0

    for item in histogram:
        total_sum += item[1]

    random_num = random.uniform(0, 1)
    for value in histogram:
        cumulative_prob += float(value[1]) / float(total_sum)
        if cumulative_prob >= random_num:
            return value[0]

def create_sentence(histogram):
    newSentenceArray = []
    for _ in range(random.randint(10, 30)):
        newSentenceArray.append(word_selection(histogram))
    return " ".join(newSentenceArray) + "."
