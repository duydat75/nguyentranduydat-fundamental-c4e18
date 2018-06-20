from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
        'title': 'Thơ con cóc',
        'author': "Đạt handsome",
        'content': "Hôm nay trời mưa to. Em bị ngã gãy giò."
        },
        {
        'title':'Thơ con nhái',
        'author':'Vẫn là Đạt handsome',
        'content':'Hôm qua trời đô nắng. Em lại bị mẹ mắng'
        }
    ]
    
    return render_template("index.html", post = posts)


@app.route('/sayhi/<name>/<age>')
def sayhi(name, age):
    return "Hi {0}, you are {1} years old " .format(name,age)


@app.route('/sum/<int:a>/<int:b>')
def calc(a,b):
    sum = a + b
    return str(sum)


if __name__ == '__main__':
  app.run( debug=True)
 