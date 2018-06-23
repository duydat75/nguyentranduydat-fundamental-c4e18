from flask import Flask, render_template
import mlab
from models.service import Service

app = Flask(__name__)
mlab.connect()

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender = gender, yob__lte=2000,address__exact = "Ha Noi" )
    return render_template('search.html', all_service = all_service)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 