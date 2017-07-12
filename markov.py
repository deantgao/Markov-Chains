"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_file = open(file_path)
    full_text = text_file.read()

    return full_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    # loop over range of length of words - 2
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1]) # create a tuple that is the word and the word following
        if key not in chains: # if the tuple does not exist in the dict chains:
            chains[key] = [words[i + 2]] # add the tuple as the key and the word following the bigram as the value
        elif key in chains: # else if tuple is in dict:
            (chains[key]).append(words[i + 2]) # append the word following the bigram to the list that chains[key] is equal to

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    # random_key = choice(chains.keys())

    # words.append(random_key[0])
    # words.append(random_key[1])

    # while random_key in chains.keys():

    #     values_list = chains[random_key]

    #     chosen_word = choice(values_list)

    #     words.append(chosen_word)

    #     new_key = (random_key[1], chosen_word)

    #     random_key = new_key

    list_of_keys = chains.keys()

    random_key = choice(list_of_keys)

    words.append(random_key[0])
    words.append(random_key[1])

    while random_key in chains.keys():
        random_value = choice(chains.get(random_key, None))

        words.append(random_value)
        new_key = (random_key[1], random_value)
        random_key = new_key


    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# for key, value in chains.items():
#     print key, value



# Produce random text
random_text = make_text(chains)

print random_text























