# Solution 1 
def sum_alphabet(words):
    res = []
    for w in words:
        s = 0
        for ch in w:
            s+=ord(ch)-ord('a')+1
        res.append(s) 
    return res

# Solution 2 Using Hashmap 
def sum_alphabet(words):
    alphabet_map = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
    res = []
    for w in words:
        s = sum(alphabet_map[ch] for ch in w)
        res.append(s)
    return res

# Example usage
words = ["sport", "good", "bad"]
print(sum_alphabet(words))  # Output: [88, 41, 7]
