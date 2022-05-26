# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def anagram_checker(word, second_word):
    if len(word) != len(second_word):
        return False

    if sorted(word) != sorted(second_word):
        return False

    return True
