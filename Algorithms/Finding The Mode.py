# Solution 1 : Single Mode
from collections import defaultdict
def mode (nums : list):
    if not nums:  
        return []
    
    mpp = defaultdict(int)
    for n in nums:
        mpp[n]+=1
    
    return max(mpp, key=mpp.get)

# Solution 2 : For multiple modes 
def mode(nums : list):
    if not nums:  
        return []
    
    mpp = defaultdict(int)
    for n in nums:
        mpp[n]+=1
    
    max_freq = max(count.values())
    
    modes = [num for num, freq in count.items() if freq == max_freq]
    
    # Sort modes in ascending order and return
    return sorted(modes) if max_freq > 1 else []
