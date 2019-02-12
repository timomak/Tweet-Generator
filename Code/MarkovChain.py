import string

def load(text):
   """
   Loads file as list of words
   Pulls all punctuation
   """
   file  = open(text)
   # Converts file to string of lower case words
   words = file.read()
   # Replaces punctuation with nothing
   words = words.replace(string.punctuation, "").replace(",", "").replace(".", "").replace("\"", "").replace("?", "").replace("!", "")

   # Creates list of words from string
   wordlist = [word for word in words.split()]
   file.close()
   return wordlist


markovSample = {"fish": {"two":3}, "red": {"fish":2}}


# for dict in markovSample: # Loop over all the dictionaries returns {"two":1} & {"fish":2}
    # for newDict in markovSample[dict]: # Loop over the contents of dictionaries. "two" & "fish"
        # print markovSample[dict][newDict] # Prints 3 & 2

def makeMarkovDict(text_file):
    markov = {}
    words_list = load(text_file)

    # for word in words_list:
    #     if word in markov.keys():
    #         # TODO: check next word and if it's already inside its dictionary.
    #         print "Item already in markov"
    #     else:
    #         # TODO: create a new dict inside markov
    #         markov[word] = {}

    """ Creating a markov first layer """
    for word in words_list:
        if word not in markov.keys():
            markov[word] = {}

    print markov # So far prints: {'fish': {}, 'two': {}, 'red': {}, 'one': {}}

    index = 0
    """ Fill up the markov dict second layer """
    for word in words_list:
        if len(words_list) == index + 1:
            print "done here"
        else:
            following_word = words_list[index + 1] # Get the word after the current one.
            if following_word in markov[word].keys():
                markov[word][following_word] += 1
            else:
                markov[word][following_word] = 1
            index += 1
    return markov

makeMarkovDict("txt.txt")
