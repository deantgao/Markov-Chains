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

    counter = 1
    for word in words: # iterate over each word in the list of words
        if word != words[-1]: # if the word does not equal the last word in the list
            key = (word, words[counter]) # create a tuple that is the word and the word following
            if word != words[-2]: # if the word does not equal the last two words
                
                if key not in chains: # if the tuple does not exist in the dict chains:
                    chains[key] = [words[counter + 1]] # add the tuple as the key and the word following the bigram as the value
                elif key in chains: # else if tuple is in dict:
                    (chains[key]).append(words[counter + 1]) # append the word following the bigram to the list that chains[key] is equal to
                
        counter += 1

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

for key, value in chains.items(): # iterate over each key in the list of keys:
    print key, value

# Produce random text
random_text = make_text(chains)

print random_text
