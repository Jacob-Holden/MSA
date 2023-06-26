import flask
from flask import request, jsonify
import student_generator_v2

#create an app
app = flask.Flask(__name__)

#use student generator program as a base
#write a function to create and return a list of student dictionaries
#create 2 routes
# - route returns all students
# - route returns student by id

#auto reload server when changes made
app.config["DEBUG"] = True

#load student dictionaries
student_dictionaries = student_generator_v2.get_student_dictionaries()

@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Jacob Nicholas Holden</h1>"

#Create route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    return jsonify(student_dictionaries)

app.run()

