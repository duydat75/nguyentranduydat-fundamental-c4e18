from flask import Flask


app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bimcalc(weight,height):
    bmi = 10000*weight / (height*height)
    condition = ''
    if bmi < 16:
        condition = "Severely underweight"
    elif bmi < 18.5:
        condition = "Underweight"
    elif bmi < 25:
        condition = "Normal"
    elif bmi <= 30:
        condition = "Overweight"
    else: 
        condition = "Obese"
    return "Hi your BMI is {0} and your condition is {1}".format(bmi,condition)

if __name__ == '__main__':
  app.run (debug=True)
 