from flask import Flask, render_template
import mlab
from models.customer import Customer

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    all_customer=Customer.objects(gender = 1, contracted = False)
    return render_template('index.html', all_customer = all_customer)

if __name__ == '__main__':
  app.run(debug=True)
 