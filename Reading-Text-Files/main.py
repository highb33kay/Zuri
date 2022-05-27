# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
filename = "./story.txt"
def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        content = f.read()
        print(content)
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # convert text to lower case
    text = text.lower()
    # split the text into individual words 
    text = text.split()
    
    # declare a dictionary and count to keep track of words 
    words = {}
    word_count = 0
    
    # loop through each word
    for f in text:
        if f in words:
            # for each word found in words increment word_count by one
            word_count += 1
            # assign value of word_count to words dictionary
            words[f] = word_count
        
        
        else:
            words[f] = 1

    print(words)
    return words

count_words()
