from flask import *
import mlab
from models.service import Service


app = Flask(__name__)
mlab.connect()


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


@app.route('/new_service',methods=["GET","POST"])
def new_service():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form 
        new_service = Service(
            name = form['name'],
            yob = form['yob'],
            gender = form['gender'],
            height = form['height'],
            address = form['address'],
            phone = form['phone'],
            description = form['description'],
            measurements = form['measurements']
        )
    
        new_service.save()
        return redirect(url_for('admin'))


@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template('search.html',all_service = all_service)
    

@app.route('/detail/<service_id>')
def detail(service_id):
    all_service = Service.objects()
    id_to_get = Service.objects().get(id = service_id)
    return render_template('detail.html',id_to_get = id_to_get)

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
                            set__measurements=form['measurements']
        )
        id_to_get.reload()
        return redirect(url_for('admin'))    


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 