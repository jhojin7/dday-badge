from datetime import date, timedelta

def find_streak(df):
    """ WORK IN PROGRESS """
    # extract date and counts
    commits_count = df['committedDate'].value_counts()
    # commits_count = commits_count.to_string()
    print(commits_count)
    # print(commits_count.to_json())

    # for dddd in df['committedDate']:
        # print(date.fromisoformat(dddd))
    # for key,val in commits_count:
    for i in range(1,len(commits_count)):
        # yyyy = date.fromisoformat(key).year
        # mm = date.fromisoformat(key).month
        # dd = date.fromisoformat(key).day
        print(commits_count[i])
        prev = date.fromisoformat(commits_count[i-1])
        curr = date.fromisoformat(commits_count[i])
        print(prev, curr)

        # print(date.fromisoformat(key),commits_count[key])