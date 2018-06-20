from flask import Flask,redirect
import os

app = Flask(__name__)


@app.route('/school')
def index():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
  app.run (debug=True)
 