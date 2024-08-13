from collections import defaultdict

def most_tips(user_ids, tips):
    mpp = defaultdict(int)

    for i in range(len(tips)):
        mpp[user_ids[i]] += tips[i]
    
    return max(mpp, key=mpp.get)
