from flask import Blueprint
from .streaks import streaks_bp

badges_bp = Blueprint("badges_bp",__name__,
    static_url_path="badges")
badges_bp.register_blueprint(streaks_bp, url_prefix="/streaks")

@badges_bp.route("/")
def _(): 
    return "badges"