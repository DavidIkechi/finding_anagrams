# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # assumption ->  we assume the word might also be a compound word seperated by spaces
    # replace all spaces contained in the word with empty space
    word = word.replace(" ", "")
    anagram =  anagram.replace(" ", "")
    
    # sort both words in ascending order and check if they are same
    return sorted(word) == sorted(anagram)


print(find_anagram("mebelow ", "elbow me"))