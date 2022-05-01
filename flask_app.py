# flask related
from flask import (Flask, jsonify, 
    redirect, request, url_for)
from badges.badges_bp import badges_bp
# misc
import datetime
import requests as pyrequest

app = Flask(__name__)
app.register_blueprint(badges_bp,url_prefix='/badges')

@app.route("/")
def hello():
    return "main"

@app.route("/schema",methods=['GET'])
def schema():
    label = "ADsP"
    date = "2022-05-21"
    # label = request.args.get('label')
    # date = request.args.get('due')
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

@app.route("/shield")
def shield():
    base_url = "https://img.shields.io/endpoint?url={}"
    # schema_url = "https://jhojin.pythonanywhere.com/schema?label=adsp&due=2022-05-21"
    schema_url = "https://jhojin.pythonanywhere.com/schema"
    url = base_url.format(schema_url)
    print(url_for('schema'))
    # print(pyrequest.get(url_for('schema')).text)
    return pyrequest.post(url).content
    # return redirect(url)

@app.route("/imgtest")
def imgtest():
    label = "aa"
    message = "test"
    obj = {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "style": "flat-square",
        "color": "informational"
    }
    aurl = """https://img.shields.io/badge/downloads-120%2Fweek-green"""
    headers = {'content-type':'image/*'}
    resp = pyrequest.post(aurl,json=obj,headers=headers)
    return resp.content

if __name__=='__main__':
    print(app.url_map)
    app.run(host='localhost', port = 5000, debug=True)