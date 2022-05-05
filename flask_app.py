from flask import Flask
from badges.badges_bp import badges_bp

app = Flask(__name__)
app.register_blueprint(badges_bp,url_prefix='/badges')

@app.route("/")
def hello():
    return str(app.url_map)

if __name__=='__main__':
    app.run(host='localhost', port = 5000, debug=True)