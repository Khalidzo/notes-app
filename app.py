from flask import Flask

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return '<script>alert("bad")</script>'