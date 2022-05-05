from flask import Blueprint
from badges.streaks import streaks_bp
from badges.dday import dday_bp

badges_bp = Blueprint("badges_bp",__name__,
    static_url_path="badges")
# /badges/streaks/
badges_bp.register_blueprint(streaks_bp,
    url_prefix="/streaks")
# /badges/dday/
badges_bp.register_blueprint(dday_bp,
    url_prefix='/dday')

@badges_bp.route("/")
def main(): 
    return "badges"