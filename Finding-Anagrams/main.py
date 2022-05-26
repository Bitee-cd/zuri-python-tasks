# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def anagram_checker(word, second_word):
    new_word = word.replace(" ", "")
    new_second_word = second_word.replace(" ", " ")
    if len(new_word) != len(new_second_word):
        return False

    if sorted(new_word) != sorted(new_second_word):
        return False

    return True
