from flask import Flask,render_template


app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bimcalc(weight,height):
    bmi = 10000*weight / (height*height)

    return render_template("bmi.html", bmi_value = bmi, bmi = bmi)

if __name__ == '__main__':
  app.run (debug=True)
 