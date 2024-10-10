from collections import defaultdict
def common_items(pair_list):
    user_items = defaultdict(list)
    for name, item in pair_list:
        user_items[name].append(item)
    
    result = []
    names = sorted(user_items.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            name1, name2 = names[i], names[j]
            common_count = len(set(user_items[name1]).intersection(set((user_items[name2]))))
            result.append((name1, name2, common_count))
    
    return result
