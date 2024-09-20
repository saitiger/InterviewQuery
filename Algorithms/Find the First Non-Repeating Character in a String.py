from collections import defaultdict
def first_uniq_char(s):
    mpp = defaultdict(int)

    # Count frequency of each character in the string
    for ch in s:
        mpp[ch] += 1

    # Need to traverse the array since we need to find the first occurrence of non-repeating array
      for i in range(len(s)):
        if mpp[s[i]] == 1:
            return i

    # If no non-repeating character exists, return -1
    return -1
