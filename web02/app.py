from flask import *
import mlab
from models.service import Service


app = Flask(__name__)
mlab.connect()

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender = gender, yob__lte=2000 )
    return render_template('search.html', all_service = all_service)


@app.route ('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)


@app.route ('/delete/<service_id>')
def delete(service_id):
    xoa = Service.objects().get(id = service_id)
    if xoa is None:
        return ("Service not found")
    else:
        xoa.delete()
        return redirect(url_for('admin'))


@app.route ('/new_service', methods = ["GET","POST"])
def create():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        new_service = Service(
            name = name,
            yob = yob,
            address = address
        )
        new_service.save()
        return redirect(url_for('admin'))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 