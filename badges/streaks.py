from flask import Blueprint
from .gql import repoCommits

streaks_bp = Blueprint("streaks_bp",__name__,static_url_path="streaks")

@streaks_bp.route("/")
def _():
    return "badges/streaks"

@streaks_bp.route("/<user>/<repo>")
def streaks_repo(user, repo):
    max_streak = repoCommits(user,repo)
    return f"badges/streaks/user/repo: {user}/{repo} \n {len(max_streak),max_streak}"