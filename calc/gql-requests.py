import os
import requests
import json
import pandas as pd
from copy import copy
import dotenv
import calculate

query_str = """
query repoCommits($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    id
    nameWithOwner
    object(expression: "main") {
      ... on Commit {
        history(first: 100) {
          edges {
            node {
              shortOid:abbreviatedOid #oid
              url
              message
              changedFiles
              committedDate
            }
          }
        }
      }
    }
  }
}
"""

if __name__ == '__main__':
    """ WORK IN PROGRESS """
    # env variables
    dotenv.load_dotenv()
    GQL_TOKEN = os.getenv("GQL_TOKEN")
    # graphql variables
    user = 'jhojin7'
    repo = 'problem-solving'
    gql_vars = {
        "owner": user,
        "name": repo
    }
    gql_url = "https://api.github.com/graphql"
    gql_header = {"Authorization": 'bearer ' + GQL_TOKEN}
    gql_body = {'query': query_str, 'variables': gql_vars}
    # POST request
    response = json.loads(requests.post(
        gql_url, headers=gql_header, json=gql_body).text)

    # if gql sript error, print response
    if ('errors' or 'message') in response.keys():
        print(response)

    # get commits list
    commits = response['data']['repository']['object']['history']['edges']

    # process json object for df
    for i in range(len(commits)):
        # obj <- {'node':obj}
        commits[i] = copy(commits[i]['node'])
    # remove time from timestamp for groupby(date)
    for i in range(len(commits)):
        commits[i]['committedDate'] = copy(commits[i]['committedDate'][:10])

    # make pandas df
    df = pd.DataFrame(commits)
    # drop duplicate dates, cast it to list, reverse list order
    dates = df['committedDate'].drop_duplicates().to_list()[::-1]
    print(dates)
    max_streak = calculate.find_max_streak(dates)
    print(len(max_streak), max_streak)
    # ['2022-04-21', '2022-04-26', '2022-04-27', '2022-04-28']
    # 3 ['2022-04-26', '2022-04-27', '2022-04-28']

    # # export
    # df.to_html('temp.html')
    # df.to_markdown('temp.md','w')