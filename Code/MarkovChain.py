import string
import random

def load(text):
   """
   Loads file as list of words
   Pulls all punctuation
   """
   file  = open(text)
   # Converts file to string of lower case words
   words = file.read()
   # Replaces punctuation with nothing
   # words = words.replace(string.punctuation, "").replace(",", "").replace(".", "").replace("\"", "").replace("?", "").replace("!", "")
   wordlist = []
   # Creates list of words from string

   # wordlist = [word for word in words.split()]
   for word in words.split():
       if len(wordlist) < 50001: # 50001
           wordlist.append(word)
   file.close()
   print "the lenght of list is:", len(wordlist)
   return wordlist


# markovSample = {"fish": {"two":3}, "red": {"fish":2}}

# for dict in markovSample: # Loop over all the dictionaries returns {"two":1} & {"fish":2}
    # for newDict in markovSample[dict]: # Loop over the contents of dictionaries. "two" & "fish"
        # print markovSample[dict][newDict] # Prints 3 & 2

def makeMarkovDict(text_file):
    markov = {}
    words_list = load(text_file)

    """ Creating a markov first layer """
    for word in words_list:
        if word not in markov.keys():
            markov[word] = {}

    # print markov # So far prints: {'fish': {}, 'two': {}, 'red': {}, 'one': {}}

    index = 0
    """ Fill up the markov dict second layer """
    for word in words_list:
        if len(words_list) == index + 1:
            print "Done sorting"
        else:
            following_word = words_list[index + 1] # Get the word after the current one.
            if following_word in markov[word].keys():
                markov[word][following_word] += 1
            else:
                markov[word][following_word] = 1
            index += 1
    return markov # Returns {'fish': {'two': 1, 'red': 1}, 'two': {'fish': 1}, 'red': {'fish': 1}, 'one': {'fish': 1}}

def makeSecondOrderMarkovDict(text_file):
    markov = {}
    words_list = load(text_file)

    count = 0
    """ Creating a markov first layer """
    for word in words_list:
        if len(words_list) > count + 2:
            count += 1
            tempTuple = (word, words_list[count])
            if tempTuple not in markov.keys():
                markov[tempTuple] = {}
    # print "finished first layer"

    # print markov # So far prints: {'fish': {}, 'two': {}, 'red': {}, 'one': {}}

    index = 0 # Needs to always be 1 ahead of where word is in list
    """ Creating a markov first layer """
    for word in words_list:
        # print index
        if len(words_list) > index + 3:
            index += 1
            tempTuple = (word, words_list[index])
            next_word = words_list[index + 1]
            # print next_word
            if next_word in markov[tempTuple].keys():
                markov[tempTuple][next_word] += 1
                # print "Adding ", word, "to", markov[tempTuple],"\n"
            else:
                markov[tempTuple][next_word] = 1
                # print "Creating ", word, "to", markov[tempTuple],"\n"


    return markov
    """ Returns
    {('dogs.', 'You'): {'like': 1}, ('I', 'hate'): {}, ('dogs', 'and'): {'I': 1}, ('like', 'cats'): {'but': 1}, ('You', 'like'):
    {'cats': 1, 'dogs': 1}, ('cats', 'but'): {'I': 1}, ('like', 'dogs.'): {'You': 1}, ('but', 'I'): {'hate': 1}, ('and', 'I'):
    {'like': 1}, ('I', 'like'): {'dogs.': 1}, ('like', 'dogs'): {'and': 1}}
    """

def generate_sentence():
    """
    Start with a random word, based on that word, see the probability of the next one.
    Return a sentence generated with the Makov chain.
    """
    markov_chain = makeMarkovDict("text.txt")

    # Pick a random word to begin with.
    first_word = random.choice(markov_chain.keys()) # Illegall

    # print first_word
    # random_choice = random.randint(0, len(markov_chain.keys()))
    # index = 0
    # first_word = ""
    # for word in markov_chain:
    #     print word
    #     if index == random_choice:
    #         first_word = word
    #         break
    #     index += 1

    # Based on that word, call function to chose the next word.
    # print markov_chain[first_word]
    # print word_selection(markov_chain[first_word])

    lenght_of_sentence = 10
    sentence = [first_word] # First word already in there
    for i in range(lenght_of_sentence):
        sentence.append(word_selection(markov_chain[sentence[i]]))
    # Sentence after loop: ['fish', 'red', 'fish', 'two', 'fish', 'red', 'fish', 'red', 'fish', 'two', 'fish']

    # Cap with letter and add period at the end.
    final_sentece = " ".join(sentence) + "."
    return final_sentece.capitalize()

def word_selection(dictionary):
    """
    Pick the next word from the dictionary it recieves.
    """
    total_sum = 0 # {'two': 4, 'red': 4} total_sum == 8
    cumulative_prob = 0.0

    for item in dictionary:
        total_sum += dictionary[item]

    random_num = random.uniform(0, 1)
    for value in dictionary:
        cumulative_prob += float(dictionary[value]) / float(total_sum)
        if cumulative_prob >= random_num:
            return value




# def word_selection_2nd(dictionary):
#     """
#     Pick the next word from the dictionary it recieves.
#     """
#     print dictionary
#     total_sum = 0 # {'two': 4, 'red': 4} total_sum == 8
#     cumulative_prob = 0.0
#
#     for item in dictionary:
#         for dict in dictionary[item]:
#             total_sum += dictionary[item][dict]
#
#     # print total_sum
#     random_num = random.uniform(0, 1)
#     for key_value in dictionary:
#         for value in dictionary[key_value]:
#             cumulative_prob += float(dictionary[key_value][value]) / float(total_sum)
#             if cumulative_prob >= random_num:
#                 return value

# print generate_sentence()
# print word_selection()
print makeSecondOrderMarkovDict("txt.txt")
