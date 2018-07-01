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


@app.route('/update/<service_id>', methods = ["GET","POST"])
def update(service_id):
    if request.method == "GET":
        id_to_get = Service.objects().get(id = service_id)
        return render_template('update-service.html',id_to_get = id_to_get)
    elif request.method == "POST":
        form = request.form
        id_to_get = Service.objects().get(id = service_id)
        id_to_get.update (set__name=form['name'],
                            set__yob=form['yob'],
                            set__gender=form['gender'],
                            set__height=form['height'],
                            set__phone=form['phone'],
                            set__description=form['description'],
                            set__measurements=form['measurements'],
                            set_avatar=form['avatar']
        )
        id_to_get.reload()
        return redirect(url_for('admin'))    



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 