from flask import (Blueprint, Response,
    jsonify, request)
import requests as pyrequest
import datetime

DOMAIN = "https://jhojin7ddaybadges.herokuapp.com"
dday_bp = Blueprint("dday_bp",__name__,static_url_path="dday")

@dday_bp.route("/schema")#,methods=['GET'])
def schema():
    """ /badges/dday/schema """
    # /badges/dday/schema?label=ADSP&dday=2022-05-21 
        # (using this makes url to become too long...)
    label = "ADsP"
    date = "2022-05-21"
    due_date = datetime.date.fromisoformat(date)
    today_date = datetime.date.today()
    due = (due_date - today_date).days

    if due > 0:
        message = "D-%d" % abs(due)
    elif due < 0:
        message = "D+%d" % abs(due)
    else: # elif due == 0:
        message = "D-DAY"

    obj = {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "style": "flat-square",
        "color": "informational"
    }
    return jsonify(obj)

@dday_bp.route("/adsp",methods=['GET'])
def adsp():
    """badges/dday/adsp"""
    name = request.args.get('name',type=str)
    base_url = "https://img.shields.io/endpoint?url="
    # url = base_url + DOMAIN + "/badges/dday/schema?label=ADSP&dday=2022-05-21"
    url = base_url + DOMAIN + "/badges/dday/schema"
    headers = {'content-type':'application/json'}
    resp = pyrequest.get(url,headers=headers)
    print(url, resp.url)
    return Response(resp.content, mimetype="image/svg+xml")