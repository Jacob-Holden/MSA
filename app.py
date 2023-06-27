from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)
app.config['DEBUG'] = True

#set secret key.
app.config['SECRET_KEY'] = 'your secret key'

#Function to get student data from the api
#input: url
#output: JSON student data
def get_student_data(url):
    #make a reuest
    response = requests.get(url)

    #convert to JSON
    response_json = response.json()
    return response_json

#create route for site index. Will display all student data
@app.route('/', methods=['GET'])
def index():

    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data = student_data)

#run the flask appplication
app.run(port=5007)