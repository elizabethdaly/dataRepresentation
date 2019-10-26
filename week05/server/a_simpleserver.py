#!flask/bin/python

from flask import Flask

# NameError: name 'app' is not defined at line @app.route('/')
# https://stackoverflow.com/questions/29277581/flask-nameerror-name-app-is-not-defined
# You need to use following line [app Flask(__name__]
app = Flask(__name__, static_url_path='', static_folder='../')

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
