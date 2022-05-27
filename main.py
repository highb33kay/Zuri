# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
word = input("what is the word: ").lower()
anagram = input("what is the anagram: ").lower()


def find_anagram(word, anagram):
    # [assignment] Add your code here
    while len(anagram) == len(word):
        if sorted(word) == sorted(anagram):
            print("Could be an anagram")
            return True
        else:
            print("Definitely not an Anagram")
            return False
    else:
        print("Might not be an Anagram")

find_anagram(word, anagram)
