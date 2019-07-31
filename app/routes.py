
from app import app
from flask import render_template, request

from flask import render_template
from flask import request
@app.route('/')
@app.route('/index')
def index():
   # weight={"weight":"lbs"}
   # height={"height":"centimeters"}
   # age={"age":"years"}
   return render_template ("index.html")
@app.route('/cal_intake', methods=['GET','POST'])
def cal_intake():
   #if it's a GET request, send them back to fill out form
   #if it's a POST request, do the following:
   #save all user data from the form (line 24 in other file)
   #take each useful piece of info from form, save to variables (convert data types)
   #do calculation
   #send to results page with info
   if request.method=='GET':
       return render_template("index.html")
   else:
       userdata = request.form
       print (userdata)
       weight=userdata["weight"]
       height=userdata["height"]
       age=userdata["age"]
       female_intake = (10.0 * float(weight) * 0.4536) + (6.25 * float(height) * 2.54) - (5.0 * float(age)) - (161.0)
       male_intake = (10.0 * float(weight) * 0.4536) + (6.25 * float(height) * 2.54) - (5.0 * float(age)) + (5.0)
       gender=userdata["gender"]
       if gender== "female":
           intake = round(female_intake)
       else:
           intake = round(male_intake)
       return render_template("cal_intake.html", weight=weight, height=height, age=age, gender=gender, calories = intake )
   # if request.method=='GET':
   #     female_intake= (10 * weight * .4536) + (6.25 * height * 2.54) - (5 * age) - 161
   #     male_intake= (10 * weight * .4536) + (6.25 * height * 2.54) - (5 * age) + 5
   #     return render_template("cal_intake.html", female_intake=female_intake, male_intake=male_intake)