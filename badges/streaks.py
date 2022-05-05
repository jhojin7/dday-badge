from flask import Blueprint, Response
import requests as pyrequest
from badges.queries import repoCommits

streaks_bp = Blueprint("streaks_bp",__name__,static_url_path="streaks")

# badges/streaks
@streaks_bp.route("/")
def _():
    return "badges/streaks"

# badges/streaks/user/repo
@streaks_bp.route("/<user>/<repo>")
def streaks_repo(user, repo):
    max_streak = repoCommits(user,repo)
    # return f"badges/streaks/user/repo: {user}/{repo} \n {len(max_streak),max_streak}"

    label = f"longest streak"
    if max_streak == TypeError:
        message = "Error fetching commit data"
    else:
        message = f"{len(max_streak)}"
    color= "success"
    url = f"https://img.shields.io/static/v1?label={label}&message={message}&style=flat-square&color=informational"
    headers = {'content-type':'image/*'}
    resp = pyrequest.post(url,headers=headers)
    return Response(resp.content, mimetype="image/svg+xml")

# badges/streaks/user/repo/longest
# badges/streaks/user/repo/current