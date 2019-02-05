import random, sys
import histogram

# I didn't like my own implementation.
# Code based on what I learned from Jackson Ho's code: https://github.com/Mintri1199/Tweet_Generator
# python Stochastic-sampling.py text.txt 10000

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

def create_probability_dict(histogram, loop=10000):
    prob_dict = {}

    for item in histogram:
        prob_dict[item[0]] = 0

    for _ in range(0, loop):
        prob_dict[word_selection(histogram)] += 1

    return prob_dict

if __name__ == '__main__':
    parameters = sys.argv[1:]

    # List of lists
    temp_histogram = histogram.histogram(histogram.open_file(parameters[0]))

    loops = int(parameters[1])
    # Return a dict with words and the number of times it was called
    print create_probability_dict(temp_histogram, loops)
