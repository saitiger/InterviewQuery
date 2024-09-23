from collections import Counter
def are_anagrams(str1, str2):
    # Check if the strings are identical (not allowed as an anagram)
    if str1 == str2:
        return False
    return Counter(str1) == Counter(str2)
