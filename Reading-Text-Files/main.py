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
    text = str(read_file_content("./story.txt"))
    # [assignment] Add your code here
    words = {}
    for f in text.split(" "):
        count = 0
        words[f] = f.count("f")
    print(words)
    return words

count_words()
