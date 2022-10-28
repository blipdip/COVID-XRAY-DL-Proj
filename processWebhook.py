import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/icon.ico')
def icon():
     return send_from_directory(os.path.join(app.root_path, 'static'),'icon.ico',mimetype='image/icon.ico')

@app.route('/')
@app.route('/home')
def home():
     os.system("code_decider.py")

if __name__ == "__main__":
     app.secret_key = 'key'
     app.debug = True
     app.run()