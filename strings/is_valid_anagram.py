# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.


def is_valid_anagram(s, t):
    if len(s) != len(t):
        return False
    return "".join(sorted(s)) == "".join(sorted(t))
