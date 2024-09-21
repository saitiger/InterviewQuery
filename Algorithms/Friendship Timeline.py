from collections import defaultdict

def friendship_timeline(friends_added, friends_removed):
    # Dictionary to track the start date for each pair of friends
    active_friendships = defaultdict(list)
    timeline = []
    
    # Process all friendships added
    for added in friends_added:
        user_ids = tuple(sorted(added['user_ids']))
        active_friendships[user_ids].append(added['created_at'])
    
    # Process all friendships removed
    for removed in friends_removed:
        user_ids = tuple(sorted(removed['user_ids']))
        if user_ids in active_friendships and active_friendships[user_ids]:
            # Pop the earliest added friendship start date
            start_date = active_friendships[user_ids].pop(0)
            timeline.append({
                'user_ids': list(user_ids),
                'start_date': start_date,
                'end_date': removed['created_at']
            })
    
    return timeline
