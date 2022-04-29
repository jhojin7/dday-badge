from datetime import date

def find_max_streak(dates:list):
    """ finds the longest streak in a chronologically sorted list.
    Returns max_steak list """
    cur_streak = [dates[0]]
    max_streak = []
    for i in range(1,len(dates)):
        # if date diff = 1, append to cur_streak
        prev = date.fromisoformat(dates[i-1])
        cur = date.fromisoformat(dates[i])
        if (cur - prev).days == 1:# if dates[i-1]+1 == dates[i]:
            cur_streak.append(dates[i])
        else:
            # if current streak is the longest streak, let it be max_streak
            if len(cur_streak) > len(max_streak):
                max_streak[:] = cur_streak[:]
                # reset cur_streak to 1
                cur_streak = [dates[i]]
            else: # else just clean cur_streak only
                cur_streak = [dates[i]]
    # check before returning if max_streak is the longest
    if len(cur_streak) > len(max_streak): 
        max_streak[:] = cur_streak[:]
    return max_streak

# def test_find_max_streak():
#     # chronologically sorted dates
#     dates = [1,2,4,5,6,7,8,9,10,11,13,14,20,21,22,23,24,25,26,27,28,29]
#     expected = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
#     max_streak = find_max_streak(dates)
#     print(max_streak, len(max_streak))
#     print("expected:", expected, (max_streak==expected))

# if __name__=='__main__':
#     # test_find_max_streak()