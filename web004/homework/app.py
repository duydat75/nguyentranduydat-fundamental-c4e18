from flask import *
import mlab
from models.service import Service
from models.user import User
from models.order import Order
import datetime

app = Flask(__name__)
mlab.connect()
app.secret_key = "Dat ultra super handsome"

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)


@app.route('/orderpage')
def orderpage():
    all_order = Order.objects()
    return render_template('orderpage.html', all_order=all_order)

@app.route('/accept/<order_id>')
def accept(order_id):
    order = Order.objects().with_id(order_id)
    order.update(set__is_accepted=True)
    return redirect(url_for('orderpage'))

@app.route('/delete/<service_id>')
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
    if "loggedin" in session:
        service = Service.objects().with_id(service_id)
        return render_template('detail.html', service = service)
    else :
        return redirect(url_for('login'))

@app.route('/order/<service_id>', methods = ["GET"])
def order(service_id):
    if request.method == "GET":
        service = Service.objects().with_id(service_id)
        new_order = Order(

            service_id = service_id,
            service_name = service.name,
            user_id =session['user_id'],
            user_name = User.objects().get(id =session['user_id']).fullname,
            time = str(datetime.datetime.now()),
            is_accepted = False
        )
        new_order.save()
        return "Đã gửi yêu cầu"


@app.route('/update/<service_id>', methods = ["GET","POST"])
def update(service_id):
    if request.method == "GET":
        id_to_get = Service.objects().get(id = service_id)
        return render_template('update-service.html',id_to_get = id_to_get)
    elif request.method == "POST":
        form = request.form
        id_to_get = Service.objects().get(id = service_id)
        id_to_get.update (
                            set__name=form['name'],
                            set__yob=form['yob'],
                            set__gender=form['gender'],
                            set__height=form['height'],
                            set__phone=form['phone'],
                            set__description=form['description'],
                            set__measurements=form['measurements'],
        )
        id_to_get.reload()
        return redirect(url_for('admin'))    

@app.route('/sign-in', methods=['GET','POST'])
def signin():
    if request.method =='GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['username']
        email = form['email']
        username = form['username']
        password = form['password']
        if fullname == '' or email == '' or username =='' or password =='':
            return render_template('signin.html') + "Đăng kí thất bại"
        else:
            new_user = User(
                fullname= fullname,
                email = email,
                username = username,
                password = password
            )
            new_user.save()
            return redirect('search')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        all_user=User.objects()
        for item in all_user:
            if username == item['username'] and password == item['password']:
                session['loggedin'] = True
                session['user_id'] = str(item.id)
                return redirect(url_for("search"))
            else:
                return "Đăng nhập thất bại"



@app.route('/logout')
def logout():
    if "loggedin" in session:
        del session['loggedin']
        del session['user_id']
        return redirect(url_for('search'))
    else :
        return "Mày đã đăng nhập đâu"


   


@app.route('/')
def index():
    return render_template('/index.html')

if __name__ == '__main__':
  app.run(debug=True)

